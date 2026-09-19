import boseqx


def test_version():
    assert boseqx.__version__ == "0.1.0"

from boseqx import Vector
a = Vector([1, 2, 3])
print(a)