# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 16:10:34 2022

@author: Deste
"""

## TS2

import numpy as np 
import scipy.signal as sig
import splane as sp 
import matplotlib as plt 
import math as m


R1 = 100
R2 = 3000 
R3 = 1000
R4 = 100
C = 1e-3 
K = -(R3/R1)

# Lowpass
# num_lp_hand = [K/(C**2*R3**2)]
# den_lp_hand = [1, 1/(C*R2), 1/(C**2*R3**2)]
# lp_filter = sig.TransferFunction(num_lp_hand, den_lp_hand)


# sp.bodePlot(lp_filter, 1)

# sp.pzmap(lp_filter, 2)  # S plane pole/zero plot

#Bandpass
num_bp_hand = [(-R2/R1)*1/(R2*C), 0]
den_bp_hand = [1, 1/(R2*C), 1/(C**2*R3**2)]
lp_filter = sig.TransferFunction(num_bp_hand, den_bp_hand)

    
sp.bodePlot(lp_filter, 1)
    
sp.pzmap(lp_filter, 2) #S plane pole/zero plot
    
