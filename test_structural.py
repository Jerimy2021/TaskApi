# test_structural.py
import pytest
import example

def test_can_call_existing_endpoints_of_the_API():
    try:
        res = example.get_coordinates('Lima,Peru')
        assert(res is not None)
    except:
        assert False,'exeption failed'

def test_cannot_call_not_existing_endpoints_of_the_API():
    try:
        res = example.get_coordinates('blah blah')
        assert False,'exeption not failed'
    except:
        pass

def similar(a, b):
    epsilon = 0.1
    return abs(a[0] - b[0]) < epsilon and abs(a[1] - b[1]) < epsilon

def test_the_result_is_correct_for_lima():
    detected = example.get_coordinates('Lima,Peru')
    # coordinates of Lima are -12.0463731,-77.042754
    expected = -12.0463731,-77.042754
    assert similar(detected, expected), "Unit test failed"

def test_the_result_is_correct_for_buenosaires():
    detected = example.get_coordinates('Buenos Aires,Argentina')
    # coordinates of Buenos Aires are -34.603722,-58.381592
    expected = -34.603722,-58.381592

    assert similar(detected, expected), "Unit test failed"

def test_the_result_is_correct_for_rio_de_janeiro():
    detected = example.get_coordinates('Rio de Janeiro,Brazil')
    # coordinates of Rio de Janeiro are -22.9068467,-43.1728965
    expected =-22.9068467,-43.1728965
    assert similar(detected, expected), "Unit test failed"
                                         
def test_the_result_is_correct_for_quito():
    detected = example.get_coordinates('Quito,Ecuador')
    # coordinates of Quito are -0.2201641,-78.5123274
    expected = -0.2201641,-78.5123274
    assert similar(detected, expected), "Unit test failed"


