import requests 
from fastapi import FastAPI, HTTPException
from geopy.distance import geodesic

app = FastAPI()

def fetch_coordinates(city_name: str):
    """
    Get the coordinates of a city using the OpenStreetMap API
    
    Input:
    - city_name: str: The name of the city
    
    Output:
    
    - latitude: float: The latitude of the city
    - longitude: float: The longitude of the city

    Function:

    - Makes a request to the OpenStreetMap API
    
    Returns:
    
    - The latitude and longitude of the city

    """
    api_url = f"https://nominatim.openstreetmap.org/search?q={city_name}&format=json"
    headers = {
        'User-Agent': 'Testing App'
    }
    response = requests.get(api_url, headers=headers)
    response_data = response.json()
    if not response_data or city_name == '':
         raise HTTPException(status_code=404, detail="City not found") 
    return {
            "latitude": response_data[0]['lat'],
            "longitude": response_data[0]['lon']
    }

@app.get("/get_coordinates/")
def get_coordinates(city_name: str):
    '''
    API endpoint to get the coordinates of a given city.

    Parameters: city_name (str): The name of the city to find coordinates for.

    Returns: dict: A dictionary containing the latitude and longitude of the city.
    '''
    return fetch_coordinates(city_name)


def calculate_distance(lat1, lon1, lat2, lon2):
    """
    Calculate the distance between two points on the Earth's surface
    
    Input:
    
    - lat1: float: The latitude of the first point
    
    - lon1: float: The longitude of the first point
    """
    coordinates = (lat1, lon1)
    destination = (lat2, lon2)
    distance = geodesic(coordinates, destination).kilometers
    return distance

@app.get("/get_distance/")
def get_distance(lat1: float, lon1: float, lat2: float, lon2: float):
    """
    Get the distance between two points on the Earth's surface
    
    Input:
    
    - lat1: float: The latitude of the first point
    
    - lon1: float: The longitude of the first point
    
    - lat2: float: The latitude of the second point
    
    - lon2: float: The longitude of the second point
    
    """
    return calculate_distance(lat1, lon1, lat2, lon2)
