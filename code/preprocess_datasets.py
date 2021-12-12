#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 13:06:24 2021

@author: stoutjd
"""
import mne

# =============================================================================
# Poor coding style - All datasets processed inline
# =============================================================================
#Perform this in the data folder - 
fname = 'BALE_QEEG_Ext.Tired_8.21 01.000.02 AGE 29  EC.edf'
raw = mne.io.read_raw_edf(fname, preload=True)
ch_picks = [i for i in raw.ch_names if i!='EEG A2-A1']
raw.pick_channels(ch_picks)
raw.notch_filter([60,120])
raw.filter(1.0,None)
raw.plot()

raw.save('BALE_QEEG_Tired.fif')
raw.set_eeg_reference(ref_channels='average')
epochs = mne.make_fixed_length_epochs(raw, duration=10, reject_by_annotation=True)
epochs.drop_bad()
epochs.save('BALE_QEEG_Tired-epo.fif')


############# Normal Run 1

fname='BALE QEEG Good Night Sleep 7.19.21 06.000.02 AGE 29  EO.edf'
raw = mne.io.read_raw_edf(fname, preload=True)
ch_picks = [i for i in raw.ch_names if i!='EEG A2-A1']
raw.pick_channels(ch_picks)
raw.notch_filter([60,120])
raw.filter(1.0,None)
raw.plot()

raw.save('BALE_QEEG_GoodSleep.fif')
raw.set_eeg_reference(ref_channels='average')
epochs = mne.make_fixed_length_epochs(raw, duration=10, reject_by_annotation=True)
epochs.drop_bad()
epochs.save('BALE_QEEG_GoodSleep-epo.fif')


################ NOrmal Run 2
fname='BALE QEEG Good Night Sleep 7.19.21 07.000.02 AGE 29  EO.edf'
raw = mne.io.read_raw_edf(fname, preload=True)
ch_picks = [i for i in raw.ch_names if i!='EEG A2-A1']
raw.pick_channels(ch_picks)
raw.notch_filter([60,120])
raw.filter(1.0,None)
raw.plot()

raw.save('BALE_QEEG_GoodSleep2.fif')
raw.set_eeg_reference(ref_channels='average')
epochs = mne.make_fixed_length_epochs(raw, duration=10, reject_by_annotation=True)
epochs.drop_bad()
epochs.save('BALE_QEEG_GoodSleep2-epo.fif')


##########
# epochs1 = mne.read_epochs('BALE_QEEG_GoodSleep-epo.fif', preload=True)
# epochs2 = mne.read_epochs('BALE_QEEG_GoodSleep2-epo.fif', preload=True)






######### Sleep Deprived Dataset
fname = 'BALE_Sleep_depr.10.21 01.000.02 AGE 32  EO.edf'
raw = mne.io.read_raw_edf(fname, preload=True)
ch_picks = [i for i in raw.ch_names if i!='EEG A2-A1']
raw.pick_channels(ch_picks)
raw.notch_filter([60,120])
raw.filter(1.0,None)
raw.plot()

raw.save('BALE_QEEG_SleepDepr.fif')
raw.set_eeg_reference(ref_channels='average')
epochs = mne.make_fixed_length_epochs(raw, duration=10, reject_by_annotation=True)
epochs.drop_bad()
epochs.save('BALE_QEEG_SleepDepr-epo.fif')
