import numpy as np
import math      
import copy as cp
from .BitString_Class import *
from .IsingHamiltonian_Class import *

class MonteCarlo:
    def __init__(self, ham):
        self.ham = ham
    
    def run(self, T: int, n_samples: int, n_burn: int):
        pass