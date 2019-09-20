import pytest
import Particle

def test_one():
    dim = 3
    particles = Particle.Particle(dim, 1, 1, 1, 1)
    assert(len(particles.get_x()) == dim)
    assert(len(particles.get_v()) == dim)
    assert(len(particles.get_gbest() == dim))