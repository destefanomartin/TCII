# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 19:30:01 2022

@author: Deste
"""



import numpy as np
import scipy.signal as signal
import matplotlib as mpl
import matplotlib.pyplot as plt
import math as m
import splane as sp


wc = 2*m.pi*1000 
Fs = 100000
num_a = [wc**2]
den_a = [1, m.sqrt(2)*wc, wc**2]

num = [wc**2, 2*wc**2, wc**2]
den =[4*Fs**2+wc*m.sqrt(2)*2*Fs+wc**2, -8*Fs**2+2*wc**2,  wc**2+Fs**2*4-2*m.sqrt(2)*Fs*wc]  


myDigitalFilter = signal.TransferFunction(num,den,dt=1/Fs)
myAnalogFilter = signal.TransferFunction(num_a, den_a)

wa, maga,phasea = myAnalogFilter.bode()
wd1, magd1,phased1 = signal.dbode(myDigitalFilter)

fig, ax = plt.subplots()
ax.semilogx(wd1/(2*m.pi), magd1, color='g', label='Digital')  # Magnitud digital
ax.semilogx(wa/(2*m.pi), maga, color='r', label='Analogico')  # Magnitud analogica
ax.set_xlabel('Frecuencia[Hz]')
ax.set_ylabel('Ganancia [dB]')
plt.legend()
ax2 = ax.twinx()
ax2.semilogx(wd1/(2*m.pi), phased1, color='g', label='Digital', linestyle='dashed')  # Fase digital
ax2.semilogx(wa/(2*m.pi), phasea, color='r', label='Analogico', linestyle='dashed')  # Fase analogica¿
ax2.set_ylabel('Fase[rad]')
plt.grid()





