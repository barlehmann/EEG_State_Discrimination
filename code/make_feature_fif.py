#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 14:51:53 2021

@author: stoutjd
"""

import mne
import pandas as pd
import os.path as op
import glob

from mne.preprocessing import ICA

def get_subjid(fname):
    base_=op.basename(fname)
    return base_.split('_')[0]

def get_eye_condition(fname):
    base_=op.basename(fname)
    return op.splitext(fname)[0].split('restingPre')[-1].replace('_','')

def return_raw_ica(fname):
    if op.splitext(fname)[-1]=='.edf':
        raw=mne.io.read_raw_edf(fname, preload=True)
        ch_picks = [i for i in raw.ch_names if i!='EEG A2-A1']
        raw.pick_channels(ch_picks)
        raw.filter(1.0,None)
        ica = ICA(random_state=0)
    else:
        raw = mne.io.read_raw_fif(fname, preload=True)
        raw.pick_channels(ch_names[0:64])
        raw.filter(1.0,None)
        ica = ICA(n_components=20, random_state=0)
    ica.fit(raw, picks=raw.info['ch_names'])
    return raw, ica

def convert_to_common_ave_ref(fname):
    '''Subtract the average of all channels from each'''
    

#Perform this in the data folder
fname = 'BALE_QEEG_Ext.Tired_8.21 01.000.02 AGE 29  EC.edf'
raw = mne.io.read_raw_edf(fname, preload=True)
ch_picks = [i for i in raw.ch_names if i!='EEG A2-A1']
raw.pick_channels(ch_picks)
raw.notch_filter([60,120])
raw_avg_ref = raw.copy().set_eeg_reference(ref_channels='average')
raw_avg_ref.filter(1.0, None)
raw_avg_ref.plot()


# raw.annotations.description = ['bad_stuff']*len(raw.annotations)
epochs = mne.make_fixed_length_epochs(raw_avg_ref, duration=10, reject_by_annotation=True)
raw, ica = return_raw_ica(fname)


ica.apply(raw, exclude=ica.exclude)


def return_coherence_

