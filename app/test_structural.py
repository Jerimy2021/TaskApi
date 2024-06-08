# test_structural.py
import example
from fastapi.exceptions import HTTPException
import pytest


def similar(a, b):
    """
    Función que compara dos tuplas de floats y devuelve True si son similares
    
    :param a: tupla de floats

    :param b: tupla de floats

    :return: True si las tuplas son similares, False en caso contrario
    """
    a_res = (float(a['latitude']), float(a['longitude']))
    b_res = b
    epsilon = 0.1
    return abs(a_res[0] - b_res[0]) < epsilon and abs(a_res[1] - b_res[1]) < epsilon


def test_can_call_existing_endpoints_of_the_API():
    """
    
    Test que verifica que se pueden llamar a los endpoints de la API

    """
    try:
        res = example.get_coordinates('Lima,Peru')
        assert(res is not None)
    except:
        assert False,'exeption failed'

def test_the_result_is_correct_for_lima():
    """

    Test que verifica que el resultado de la función get_coordinates es correcto para Lima,Peru

    """
    detected = example.get_coordinates('Lima,Peru')
    expected = -12.0463731,-77.042754
    assert similar(detected, expected), "Unit test failed"
    
    
def test_the_result_is_correct_for_buenosaires():
    """

    Test que verifica que el resultado de la función get_coordinates es correcto para Buenos Aires,Argentina

    """
    detected = example.get_coordinates('Buenos Aires,Argentina')
    expected = -34.603722,-58.381592
    assert similar(detected, expected), "Unit test failed"


def test_the_result_is_correct_for_rio_de_janeiro():
    """

    Test que verifica que el resultado de la función get_coordinates es correcto para Rio de Janeiro,Brazil
    
    """
    detected = example.get_coordinates('Rio de Janeiro,Brazil')
    expected =-22.9068467,-43.1728965
    assert similar(detected, expected), "Unit test failed"

                            
def test_the_result_is_correct_for_quito():
    """
    
    Test que verifica que el resultado de la función get_coordinates es correcto para Quito,Ecuador

    """
    detected = example.get_coordinates('Quito,Ecuador')
    expected = -0.2201641,-78.5123274
    assert similar(detected, expected), "Unit test failed"

def test_the_result_is_failed_for_empty_city():
    """

    Test que verifica que la función get_coordinates devuelve un error 404 para una ciudad vacía

    """
    with pytest.raises(HTTPException) as excinfo:
        example.get_coordinates('')
    assert excinfo.value.status_code == 404
    assert excinfo.value.detail == "City not found"


def test_the_result_is_correct_for_distance_between_lima_and_buenosaires():
    """

    Test que verifica que el resultado de la función get_distance es correcto para la distancia entre Lima,Peru y Buenos Aires,Argentina

    """
    lima = example.get_coordinates('Lima,Peru')
    buenosaires = example.get_coordinates('Buenos Aires,Argentina')
    detected = example.get_distance(lima['latitude'], lima['longitude'], buenosaires['latitude'], buenosaires['longitude'])
    expected = 3129.65
    detected = round(detected, 2)
    assert abs(detected - expected) < 0.1, "Unit test failed"


def test_the_result_is_correct_for_distance_between_lima_and_rio_de_janeiro():
    """
    Test que verifica que el resultado de la función get_distance es correcto para la distancia entre Lima,Peru y Rio de Janeiro,Brazil

    """
    lima = example.get_coordinates('Lima,Peru')
    riodejaneiro = example.get_coordinates('Rio de Janeiro,Brazil')
    detected = example.get_distance(lima['latitude'], lima['longitude'], riodejaneiro['latitude'], riodejaneiro['longitude'])
    expected = 3776.82
    detected = round(detected, 2)
    assert abs(detected - expected) < 0.1, "Unit test failed"


