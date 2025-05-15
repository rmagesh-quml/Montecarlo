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
        pass
