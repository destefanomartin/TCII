# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 19:50:02 2022

@author: Deste
"""

import numpy as np 
import scipy.signal as sig 
import math as m
import splane as sp
import matplotlib.pyplot as plt

myFilter_hand = sig.TransferFunction([1,-0.517/(1/m.sqrt(2)),0.517**2], [1,0.517/(1/m.sqrt(2)),0.517**2])



w, mag, phase = sig.bode(myFilter_hand)
plt.figure()
plt.title('Magnitude response')
plt.xlabel('Angular frecuency')
plt.ylabel('Magnitude[dB]')
plt.semilogx(w, mag)  # Fase
plt.show()

plt.figure()
plt.title('Phase response')
plt.xlabel('Angular frecuency')
plt.ylabel('Phase[deg]')
plt.semilogx(w, phase)  # Fase
plt.show()
