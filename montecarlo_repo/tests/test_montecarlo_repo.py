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

    conf = montecarlo.BitString(N)
    ham = montecarlo.IsingHamiltonian(G)
    E, M, HC, MS = ham.compute_average_values(1)
    print(" E = %12.8f" %E)
    print(" M = %12.8f" %M)
    print(" HC = %12.8f" %HC)
    print(" MS = %12.8f" %MS)
    assert(np.isclose(E, -11.95991923))
    assert(np.isclose(M, -0.00000000))
    assert(np.isclose(HC, 0.31925472))
    assert(np.isclose(MS, 0.01202961))


def montecarlo_test():
    N = 6
    Jval = 2.0
    G = nx.Graph()
    G.add_nodes_from([i for i in range(N)])
    G.add_edges_from([(i,(i+1)% G.number_of_nodes() ) for i in range(N)])
    for e in G.edges:
        G.edges[e]['weight'] = Jval
    ham = montecarlo.IsingHamiltonian(G)
    ham.set_mu([0.1 for i in range(N)])
    T = 2
    Eref, Mref, HCref, MSref = ham.compute_average_values(T)
    mc = montecarlo.MonteCarlo(ham)
    E, M = mc.run(T=T, n_samples=100000, n_burn=100)
    Eavg = np.mean(E)
    Estd = np.std(E)
    Mavg = np.mean(M)
    Mstd = np.std(M)
    HC = (Estd**2)/(T**2)
    MS = (Mstd**2)/T
    print(" E: %12.8f E(ref): %12.8f error: %12.2e " %(Eavg, Eref, Eavg - Eref))
    print(" M: %12.8f M(ref): %12.8f error: %12.2e " %(Mavg, Mref, Mavg - Mref))
    print(" HC: %12.8f HC(ref): %12.8f error: %12.2e " %(HC, HCref, HC - HCref))
    print(" MS: %12.8f MS(ref): %12.8f error: %12.2e " %(MS, MSref, MS - MSref))


