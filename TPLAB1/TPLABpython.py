# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 13:48:22 2022

@author: Deste
"""

import numpy as np 
import scipy.signal as sig 
import math as m
import splane as sp

alfa_max = 0.5
wc = 2*m.pi*1500
ws = 2*m.pi*4500

wp_n = 1 
ws_n = ws/wc

e = m.sqrt(10**(alfa_max/10)-1)

# Orden 3 

# Transferencia calculada a mano 

a = 1
b = 1.252
c = 1.531
d = 0.715

# myFilter_hand = sig.TransferFunction([d], [a, b, c, d])

# sp.bodePlot(myFilter_hand)

a_desn = a/(wc)**3
b_desn = b/(wc)**2
c_desn = c/(wc)
d_desn = d

myFilter_hand_desn = sig.TransferFunction([d_desn], [a_desn, b_desn, c_desn, d_desn])

sp.bodePlot(myFilter_hand_desn )

sp.pzmap(myFilter_hand_desn)

roots = np.roots([a_desn, b_desn, c_desn, d_desn])
 

a_sos2 = 1
c_sos2  = (2942.0681042647802**2+9619.1898467647**2)
b_sos2 = 2*2942.0681042647802

num = c_sos2 * 5915.685798353704 

num_v = d_desn / a_desn 

Rf1 = m.sqrt(1/(c_sos2 * (1000e-12)**2))

C = 1/5915.685798353704
