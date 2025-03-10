import numpy as np
import project_template


def test_version():
    assert project_template.__version__ == "0.1.0"


def test_adder():
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    result = project_template.adder(a, b)
    assert np.all(result == np.array([5, 7, 9]))
