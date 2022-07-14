# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 18:38:56 2022

@author: mdestefano
"""


import numpy as np 
import scipy
import splane as sp 
import matplotlib.pyplot as plt
import math as m

## Normalizaciones de frecuencia
w_p1 = 2*m.pi*1600000
w_p2 = 2*m.pi*2500000
w_s1 = 2*m.pi*1250000
w_s2 = 2*m.pi*3200000

w0 = m.sqrt(w_p1 * w_p2)

print(f'w0={w0}')

w0_n = 1
w_p1_n = w_p1 / w0
w_p2_n = w_p2 / w0
w_s1_n = w_s1 / w0
w_s2_n = w_s2 / w0

print(f'w0_n={w0_n}')
print(f'w_p1_n={w_p1_n}, w_p2_n={w_p2_n}')
print(f'w_s1_n={w_s1_n}, w_s2_n={w_s2_n}')

BW_n = w_p2_n - w_p1_n
Q = w0_n / BW_n
print(f'Q={Q}')

Omega_p1 = Q * (w_p1_n ** 2 - 1) / w_p1_n
Omega_p2 = Q * (w_p2_n ** 2 - 1) / w_p2_n
Omega_s1 = Q * (w_s1_n ** 2 - 1) / w_s1_n
Omega_s2 = Q * (w_s2_n ** 2 - 1) / w_s2_n

print(f'Omega_p1={Omega_p1}, Omega_p2={Omega_p2}')
print(f'Omega_s1={Omega_s1}, Omega_s2={Omega_s2}')


# w_s = 2*m.pi*2000
# w_p = 2*m.pi*1000
# Omega_s1 = w_s/w_p
# att_max = 0.5
# att_min = 20.0
# ws1 = Omega_s1



# ee = 10**(att_max/10) - 1

# for nn in range(2,6):
    
#     att_min_butterworth = 10*np.log10(1 + ee * ws1**(2*nn))
    
#     if att_min_butterworth >= att_min:
#         break
    


# print( 'nn {:d} - att1 = {:f}'.format(nn,att_min_butterworth) )
# z,p,k = scipy.signal.buttap(nn)

# num_LP, den_LP = scipy.signal.zpk2tf(z,p,k)
# num_BP, den_BP = scipy.signal.lp2bp(num_LP, den_LP, w0_n, BW_n)


# den_BP_hand_sos1 = [1, 1/Q, 1]
# den_BP_hand_sos2 = [1, 1/Q, 2+(1/Q**2), 1/Q, 1]
    
# num_BP_hand = [1/(Q**3), 0, 0, 0]
# poly_mul = np.polymul(den_BP_hand_sos1, den_BP_hand_sos2)
# raices = np.roots(poly_mul)
# raices_py = np.roots(den_BP)

# my_tf = scipy.signal.TransferFunction(num_BP_hand,poly_mul)

# sp.bodePlot(my_tf, 1)
    
# sp.pzmap(my_tf, 2) #S plane pole/zero plot



