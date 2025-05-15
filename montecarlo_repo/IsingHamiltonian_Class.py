import numpy as np
import math      
import copy as cp
from .BitString_Class import *

class IsingHamiltonian:
    def __init__(self, G):
        self.G = G
        self.N = G.number_of_nodes()
        self.mu = np.zeros(self.N, dtype=int)
    
    def energy(self, config: BitString):
        energy = 0
        weight = 0

        spin_vals = [-1 if val == 0 else 1 for val in config.config]
        for k in range(self.N):
            energy += spin_vals[k] * self.mu[k]
        for i, j in (self.G).edges:
            weight = (self.G).edges[(i, j)]['weight']
            energy += weight * spin_vals[i] * spin_vals[j]
        
        return energy
    
    def compute_average_values(self, T: int):
        E  = 0.0
        M  = 0.0
        Z  = 0.0
        EE = 0.0
        MM = 0.0
        beta = 1/T
        HC = 0.0
        MS = 0.0
        prob = 0.0
        E_sum = 0.0
        M_sum = 0.0
        E_2_sum = 0.0
        M_2_sum = 0.0
        bs = BitString(self.N)
    # Write your function here!
        for i in range(2**self.N):
            bs.set_integer_config(i)
            E = self.energy(bs)
            M = sum([-1 if val == 0 else 1 for val in bs.config])
            prob = np.exp(-beta * E)

            Z += prob
            E_sum += prob * E
            M_sum += prob * M
            E_2_sum += prob * (E**2)
            M_2_sum += prob * (M**2)

        E = E_sum / Z
        M = M_sum / Z
        E2 = E_2_sum / Z
        M2 = M_2_sum / Z

        HC = (E2 - (E**2)) / (T**2)
        MS = (M2 - (M**2)) / T


        return E, M, HC, MS
    
    def set_mu(self, mus: np.array):
        self.mu = mus;            