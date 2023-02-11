from functions import *


# def test_multiply():
#     assert multiply(5, 10) == 50
#     assert multiply(100, 1.1) == 110
#     assert multiply(1.5, 1.5) == 2.25
#     assert multiply(0.0000001, 100) == 0.00001
#     assert multiply('mama', 3) == 'mamamamamama'
#     assert multiply(None, 5) == None
#
#
# def test_no_of_letter():
#     assert no_of_letter("Hello World!")
#     assert no_of_letter(f"Dog {115}")
#     assert no_of_letter("Cat" + "Dog")
#     assert no_of_letter("Dog {} Cat {}".format(15, 20))
#     assert no_of_letter(115)


def test_no_of_letter():
    assert fissbuzz(1.3) == 1
    assert fissbuzz(1.9) == 1
    assert fissbuzz(4) == 4
    assert fissbuzz(0) == None
    assert fissbuzz("1") == 1
    assert fissbuzz(3) == 'fiss'
    assert fissbuzz(15) == 'fissbuzz'
    assert fissbuzz(5) == 'buzz'
    assert fissbuzz(-5) == None