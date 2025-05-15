import numpy as np
import math      
import copy as cp
from .BitString_Class import *
from .IsingHamiltonian_Class import *
import random

class MonteCarlo:
    def __init__(self, ham):
        self.ham = ham
        self.N = ham.N
        self.config = BitString(self.N)
    
    def run(self, T: int, n_samples: int, n_burn: int):
        beta = 1.0/T
        E_vals = []
        M_vals = []

        for step in range(n_samples + n_burn):
            for site in range(self.N):
                trial = BitString(self.N)
                trial.set_config(self.config.config.copy())
                trial.flip_site(site)

                E_current = self.ham.energy(self.config)
                E_trial = self.ham.energy(trial)
                dE = E_trial - E_current

                if dE < 0 or np.random.rand() < np.exp(-beta * dE):
                    self.config = trial

            if step >= n_burn:
                E_vals.append(self.ham.energy(self.config))
                spin_vals = [-1 if x == 0 else 1 for x in self.config.config]
                M_vals.append(sum(spin_vals))

        return np.array(E_vals), np.array(M_vals)
