# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 23:03:56 2022

@author: Deste
"""

    
# -----  LOWPASS ------
# num1 = [1, 1]
# num2 = [1,1,1]
# k = 1/9
# myFilter_hand = sig.TransferFunction([k*1,0,k*3**2], np.polymul(num1,num2))




# w, mag, phase = sig.bode(myFilter_hand)
# plt.figure()
# plt.title('Magnitude response')
# plt.xlabel('Angular frecuency')
# plt.ylabel('Magnitude[dB]')
# plt.semilogx(w, mag)  # Fase
# plt.show()

# plt.figure()
# plt.title('Phase response')
# plt.xlabel('Angular frecuency')
# plt.ylabel('Phase[deg]')
# plt.semilogx(w, phase)  # Fase
# plt.show()

# ----- HIGHPASS ------
import numpy as np 
import scipy.signal as sig 
import math as m
import splane as sp
import matplotlib.pyplot as plt

k = 1/9
num_lp_hand = [k*9,0,k*1,0]
den_lp_hand = [1,2,2,1]


myFilter_hand = sig.TransferFunction(num_lp_hand, den_lp_hand)

# Graphics


sp.bodePlot(myFilter_hand,1)
sp.pzmap(myFilter_hand,2)

# w, mag, phase = sig.bode(myFilter_hand)
# plt.figure()
# plt.title('Magnitude response')
# plt.xlabel('Angular frecuency')
# plt.ylabel('Magnitude[dB]')
# plt.semilogx(w, mag)  # Fase
# plt.show()

# plt.figure()
# plt.title('Phase response')
# plt.xlabel('Angular frecuency')
# plt.ylabel('Phase[deg]')
# plt.semilogx(w, phase)  # Fase
# plt.show()
