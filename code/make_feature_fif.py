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



# ica  = ICA()
# ica.fit(epochs)
# ica.plot_sources(raw)

# from pactools.dar_model import DAR, extract_driver
epochs_gs1 = mne.read_epochs('BALE_QEEG_GoodSleep-epo.fif', preload=True)
epochs_gs2 = mne.read_epochs('BALE_QEEG_GoodSleep2-epo.fif', preload=True)
epochs_t = mne.read_epochs('BALE_QEEG_Tired-epo.fif', preload=True)
epochs_sd = mne.read_epochs('BALE_QEEG_SleepDepr-epo.fif', preload=True)


import numpy as np
from mne.connectivity import spectral_connectivity

epochs = epochs_gs1

def return_epoch_conn(epoch, info):
    fmin, fmax = 4., 12.
    sfreq = info['sfreq']  # the sampling frequency
    tmin = 0.0 
    con = spectral_connectivity(
        epoch, method='coh', mode='multitaper', sfreq=sfreq, fmin=fmin, fmax=fmax,
        faverage=True, tmin=tmin, mt_adaptive=False, n_jobs=7, fskip=4) 
    return np.squeeze(con[0])

def return_conn_mat(epochs):
    tmp_ = []
    for idx in range(len(epochs)):
        # return_epoch_conn(epoch, epochs.info)
        tmp_.append(return_epoch_conn(epochs[idx], epochs.info))
    conn_mat = np.stack(tmp_)    
    return conn_mat

f_gs1=return_conn_mat(epochs_gs1)
f_gs2=return_conn_mat(epochs_gs2)
f_t=return_conn_mat(epochs_t)
f_sd=return_conn_mat(epochs_sd)






