import requests


def get_coordinates(city_name):
    api_url = f"https://nominatim.openstreetmap.org/search?q={city_name}&format=json"
    headers = {
        'User-Agent': 'Testing App'
    }
    response = requests.get(api_url, headers=headers)
    response_data = response.json()
    
    return float(response_data[0]['lat']), float(response_data[0]['lon'])
    
