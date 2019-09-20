import pytest
import PSO
import numpy as np

np.random.seed(123)

def func(x):
        total=0
        for i in range(len(x)):
            total+=x[i]**2
        return total

def test_lengths():
    dim = 3
    parts = 2

    pso = PSO.PSO(parts, dim, 1, 1, 1, func)
    assert(len(pso.swarm) == parts)