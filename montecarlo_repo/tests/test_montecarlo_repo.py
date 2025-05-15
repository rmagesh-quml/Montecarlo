"""
Unit and regression test for the montecarlo_repo package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest
import numpy as np
import networkx as nx

import montecarlo_repo as montecarlo
from montecarlo_repo.BitString_Class import BitString


def test_montecarlo_repo_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "montecarlo_repo" in sys.modules

def test_flip_site():
    b = BitString(3)
    b.set_config([0, 0, 0])
    b.flip_site(1)
    assert b.config.tolist() == [0,1,0]
    b.flip_site(1)
    assert b.config.tolist() == [0,0,0]

def test_Ising():
    N = 6
    Jval = 2.0
    G = nx.Graph()
    G.add_nodes_from([i for i in range(N)])
    G.add_edges_from([(i,(i+1)% G.number_of_nodes() ) for i in range(N)])
    for e in G.edges:
        G.edges[e]['weight'] = Jval
    
    conf = montecarlo.BitString(N)
    ham = montecarlo.IsingHamiltonian(G)
    ham.set_mu(np.array([.1 for i in range(N)]))
    conf.flip_site(2)
    conf.flip_site(3)
    print(conf)
    e = ham.energy(conf)
    print(e)
    assert(np.isclose(e, 3.8))

