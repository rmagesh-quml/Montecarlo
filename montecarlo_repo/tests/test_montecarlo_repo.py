"""
Unit and regression test for the montecarlo_repo package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest
import numpy as np
import networkx as nx

import montecarlo_repo as montecarlo


def test_montecarlo_repo_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "montecarlo_repo" in sys.modules

def test_import():
    assert "montecarlo_repo" in sys.modules


def test_bitstring_initialization():
    b = montecarlo.BitString(5)
    assert len(b.config) == 5
    assert np.all(b.config == 0)


def test_flip_site():
    b = montecarlo.BitString(3)
    b.flip_site(1)
    assert b.config[1] == 1
    b.flip_site(1)
    assert b.config[1] == 0


def test_set_integer_config():
    b = montecarlo.BitString(3)
    b.set_integer_config(5)  # binary: 101
    assert list(b.config) == [1, 0, 1]


def test_energy_computation():
    G = nx.Graph()
    G.add_edge(0, 1, weight=1.0)
    ham = montecarlo.IsingHamiltonian(G)
    ham.set_mu(np.array([0.5, -0.5]))
    bs = montecarlo.BitString(2)
    bs.set_config([1, 0])  # spins: [+1, -1]
    energy = ham.energy(bs)
    expected = 1.0 * 1 * -1 + 0.5 * 1 + (-0.5) * -1  # -1 + 0.5 + 0.5 = 0
    assert np.isclose(energy, 0.0)


def test_montecarlo_run_output_shape():
    G = nx.path_graph(3)
    for i, j in G.edges:
        G.edges[i, j]["weight"] = 1.0
    ham = montecarlo.IsingHamiltonian(G)
    ham.set_mu(np.array([0.1, 0.2, 0.3]))

    mc = montecarlo.MonteCarlo(ham)
    E, M = mc.run(T=2, n_samples=50, n_burn=10)
    assert len(E) == 50
    assert len(M) == 50
