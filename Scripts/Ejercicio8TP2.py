# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 00:02:34 2022

@author: Deste
"""

## Realizo comprobaciones y calculo ejercicio 8 del TP2 2022 

## Declaracion de variables basicas 
import numpy as np 
import scipy.signal as sig
import splane as sp 
import matplotlib as plt 
import math as m


att_min = 53.98 
att_max = 1.0

wp = 2*m.pi*45000
ws = 2*m.pi*12000

ws_n_hp = ws / wp 

Ws_n_lp = 1/ws_n_hp

ee = 10**(att_max/10) - 1

for nn in range(2,5):
    
    # Solo pongo formula de Cheby porque me dara el menor orden, a lo sumo igual. 
    att_min_chebyshev = 10*np.log10(1 + ee * np.cosh(nn * np.arccosh(Ws_n_lp))**2 )
    
    if att_min_chebyshev >= att_min:
        break
    
print( 'nn {:d} - att1 = {:f}'.format(nn,att_min_chebyshev) )

num_lp, den_lp = sig.cheby1(4,1,1,'high','true','sos')

# Chequeo pasa bajos 

# myFilter = sig.TransferFunction(num_lp, den_lp)

# sp.bodePlot(myFilter)

# sp.pzmap(myFilter)

# num_hp, den_hp = sig.lp2hp(num_lp, den_lp)


# Chequeo pasa altos 

myFilter = sig.TransferFunction([0.891, 0, 0, 0, 0], [1, 2.694, 5.275,3.457,3.62 ])

sp.bodePlot(myFilter)

sp.pzmap(myFilter)
