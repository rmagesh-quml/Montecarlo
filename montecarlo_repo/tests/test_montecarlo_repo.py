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