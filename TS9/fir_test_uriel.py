# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 22:14:09 2022

@author: Deste
"""
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 20:26:36 2022

@author: Deste
"""
# Inicialización e importación de módulos

# Módulos para Jupyter
import warnings
warnings.filterwarnings('ignore')



# Módulos importantantes
import scipy.signal as sig
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy.io as sio
from splane import plot_plantilla
import splane as sp
from pylab import *

# def impz(b,a=1):
#     l = len(b)
#     impulse = repeat(0.,l); impulse[0] =1.
#     x = arange(0,l)
#     response = signal.lfilter(b,a,impulse)
#     subplot(211)
#     stem(x, response)
#     ylabel('Amplitude')
#     xlabel(r'n (samples)')
#     title(r'Impulse response')

fig_sz_x = 10
fig_sz_y = 7
fig_dpi = 100 # dpi

fig_font_size = 16

mpl.rcParams['figure.figsize'] = (fig_sz_x,fig_sz_y)
plt.rcParams.update({'font.size':fig_font_size})

###
## Señal de ECG registrada a 1 kHz, con contaminación de diversos orígenes.
###

# para listar las variables que hay en el archivo
#io.whosmat('ecg.mat')
mat_struct = sio.loadmat('ecg.mat')

ecg_one_lead = mat_struct['ecg_lead']
ecg_one_lead = ecg_one_lead.flatten()
cant_muestras = len(ecg_one_lead)

fs = 1000 # Hz
nyq_frec = fs / 2
# Plantilla

# filter design
ripple = 0 # dB
atenuacion = 40 # dB

ws1 = 1.0 #Hz
wp1 = 3.0 #Hz
wp2 = 25.0 #Hz
ws2 = 35.0 #Hz
frecs = np.array([0.0,         ws1,         wp1,     wp2,  26, 28, 30, 32,   ws2,         nyq_frec   ]) / nyq_frec
gains = np.array([-atenuacion, -atenuacion, -ripple, -ripple,-10,-20,-30, -40, -atenuacion, -atenuacion])
gains = 10**(gains/20)
numtaps = 1501

#Diseño filtro FIR

# #################################### FIRWIN2 ########################################

# #Regulacion de las frecuncias criticas
# frecs_firwin2 = np.array([0.0, 1.8 ,ws1 + 1.3,         wp1 -.7 ,     wp2 +1,  ws2 - 1,         nyq_frec   ]) / nyq_frec
# gains_firwin2 = np.array([-atenuacion, -60,-atenuacion, -ripple, -ripple,  -atenuacion, -atenuacion])
# gains_firwin2 = 10**(gains_firwin2/20)

# cant_coeficientes = 2401

# num_win = sig.firwin2(cant_coeficientes, frecs_firwin2, gains_firwin2 , window='blackmanharris' )

# #######################################################################################

#################################### FIRLS ########################################

#Regulacion de las frecuncias criticas
frecs_firls = np.array([0.0,      ws1+.4,         wp1,     wp2,  28, 32,   ws2,         nyq_frec   ])  / nyq_frec
gains_firls = np.array([-atenuacion*2, -atenuacion, -ripple, -ripple,-25,-40, -atenuacion, -atenuacion])
gains_firls = 10**(gains_firls/20)  

cant_coeficientes = 1501

num_win = sig.firls(cant_coeficientes, frecs_firls, gains_firls)

#######################################################################################

den = 1.0



    
# muestreo el filtro donde me interesa verlo según la plantilla.
w  = np.append(np.logspace(-1, 0.8, 250), np.logspace(0.9, 1.6, 250) )
w  = np.append(w, np.linspace(110, nyq_frec, 100, endpoint=True) ) / nyq_frec * np.pi

_, hh_win = sig.freqz(num_win, den, w)

# renormalizo el eje de frecuencia
w = w / np.pi * nyq_frec


## Graficos 
plt.figure(1)
plt.plot(w, 20 * np.log10(abs(hh_win)), label='FIR-Win {:d}'.format(num_win.shape[0]))
plt.title('Filtros diseñados')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Módulo [dB]')
plt.grid()
plt.axis([0, 100, -60, 5 ]);
axes_hdl = plt.gca()
axes_hdl.legend()
plot_plantilla(filter_type = 'bandpass', fpass = frecs[[2, 3]]* nyq_frec, ripple = ripple , fstop = frecs_firls[ [1, 6] ]* nyq_frec, attenuation = atenuacion, fs = fs)


plt.figure(2)
h_Phase = np.unwrap(arctan2(imag(hh_win),real(hh_win)))
plot(w,h_Phase)
ylabel('Phase (radians)')
xlabel('Frecuencia [Hz]')
title(r'Phase response')
subplots_adjust(hspace=0.5)


plt.figure(3)

t,y = sig.dimpulse((num_win,1,1/fs))
plt.step(t, np.squeeze(y))
plt.grid()
plt.xlabel('n [samples]')
plt.ylabel('Amplitude')


