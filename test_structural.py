import pytest
import example

def can_call_existing_endpoints_of_the_API():
    try:
        res = example.get_coordinate('Lima,Peru')
        assert(res is not None)
    except:
        assert False,'exeption failed'

def cannot_call_not_existing_endpoints_of_the_API():
    try:
        res = example.something_not_existent('blah blah')
        assert False,'exeption not failed'
    except:
        pass
