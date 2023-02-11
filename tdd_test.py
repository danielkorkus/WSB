from functions import *


def test_multiply():
    assert multiply(5, 10) == 50
    assert multiply(100, 1.1) == 110
    assert multiply(1.5, 1.5) == 2.25
    assert multiply(0.0000001, 100) == 0.00001
    assert multiply('mama', 3) == 'mamamamamama'
    assert multiply(None,5) == None


def test_no_of_letter():
    assert no_of_letter("Hello World!")
    assert no_of_letter(f"Dog {115}")
    assert no_of_letter("Cat" + "Dog")
    assert no_of_letter("Dog {} Cat {}".format(15, 20))
    assert no_of_letter(115)
