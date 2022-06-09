# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 20:03:07 2022

@author: Deste
"""

# Ejercicio 5 TP2 

import numpy as np 
import scipy.signal as sig
import splane as sp 
import matplotlib as plt 
import math as m


att_min = 48
att_max = 0.4

wp = 9.6
ws = 3.2

ws_n_hp = ws / wp 

Ws_n_lp = 1/ws_n_hp

ee = 10**(att_max/10) - 1

for nn in range(2,6):
    
    # Solo pongo formula de Cheby porque me dara el menor orden, a lo sumo igual. 
    att_min_chebyshev = 10*np.log10(1 + ee * np.cosh(nn * np.arccosh(Ws_n_lp))**2 )
    
    if att_min_chebyshev >= att_min:
        break
    
print( 'nn {:d} - att1 = {:f}'.format(nn,att_min_chebyshev) )

num, den = sig.cheby1(5,0.4,1,'low',True, 'ba')


num_hp, den_hp = sig.lp2hp(num,den)

r = np.roots(den_hp)