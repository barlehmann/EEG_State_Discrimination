#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 11:10:57 2021

@author: stoutjd
"""

import mne
import glob
import os
import os.path as op
import scipy
from scipy.io import loadmat

topdir=os.path.dirname('__file__')
extra_data_path = os.path.join(topdir, 'extra_data','Pre-SART EEG') 

mat_files = glob.glob(op.join(extra_data_path, '*.mat'))

#From dataset description
_ch_names="'Fp1';'AF7';'AF3';'F1';'F3';'F5';'F7';'FT7';'FC5';'FC3';'FC1';'C1';'C3';'C5';'T7';'TP7';'CP5';'CP3';'CP1';'P1';'P3';'P5';'P7';\
    'P9';'PO7';'PO3';'O1';'Iz';'Oz';'POz';'Pz';'CPz';'Fpz';\
    'Fp2';'AF8';'AF4';'Afz';'Fz';'F2';'F4';'F6';'F8';'FT8';'FC6';'FC4';'FC2';'FCz';'Cz';\
    'C2';'C4';'C6';'T8';'TP8';'CP6';'CP4';'CP2';'P2';'P4';'P6';'P8';'P10';'PO8';'PO4';'O2'"

ch_names=_ch_names.replace(';', ' ').replace("'","").split()


def convert_to_fif(fname):
    '''Load mat files and make an MNE RawArray'''
    mat = scipy.io.loadmat(fname)['dataRest']
    sampling_freq = 256 # in Hertz
    extra_chans = [str(i) for i in range(4)]
    info = mne.create_info(ch_names+extra_chans, sfreq=sampling_freq, 
                           ch_types=['eeg']*len(ch_names+extra_chans))
    raw = mne.io.RawArray(mat, info)
    return raw
    
for mat_fname in mat_files:
    raw = convert_to_fif(mat_fname)
    out_dir= op.dirname(mat_fname)
    _fname = op.basename(mat_fname)
    out_fname = op.join(out_dir, _fname.replace('.mat','_eeg.fif'))
    print(out_fname)
    raw.save(out_fname, overwrite=True)
    