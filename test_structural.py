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

def test_the_resul_is_correct_for_all_inputs_API():
    try:
        res = example.get_coordinates('Lima,Peru')

        expected = -12.0463731,-77.042754
        assert res == expected, "nooo :("
    except:
        assert False,'exeption failed'
