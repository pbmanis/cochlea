#!/usr/bin/env python

from __future__ import division, absolute_import, print_function

__author__ = "Marek Rudnicki"

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as dsp

import mrlib.thorns as th

import cochlea
from cochlea.external import run_matlab_auditory_periphery

def main():

    fs = 48e3

    ### Make sound
    t = np.arange(0, 0.1, 1/fs)
    s = dsp.chirp(t, 80, t[-1], 20000)
    s = cochlea.set_dbspl(s, 50)
    pad = np.zeros(10e-3 * fs)
    sound = np.concatenate( (s, pad) )



    ### Run model
    anf = run_matlab_auditory_periphery(
        sound,
        fs,
        anf_num=(100,100,100),
        cf=(125, 20000, 100),
        seed=0,
    )



    ### Accumulate spike trains
    anf_acc = th.accumulate(anf, keep=['cf', 'duration'])
    anf_acc.sort('cf', ascending=False, inplace=True)



    ### Plot auditory nerve response
    fig, ax = plt.subplots(2,1)
    th.plot_signal(
        signal=sound,
        fs=fs,
        ax=ax[0]
    )
    th.plot_neurogram(
        anf_acc,
        fs,
        ax=ax[1]
    )
    plt.show()



if __name__ == "__main__":
    main()