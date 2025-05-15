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

