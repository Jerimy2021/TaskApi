from locust import HttpUser, task, between



class WebsiteTestUser(HttpUser):
    """
    A class that defines a user that will be simulated.

    This class inherits from HttpUser, which is a class that defines a user that will be simulated.

    This class has two tasks:
    
    - get_coordinates: This task sends a GET request to the /get_coordinates endpoint.

    - get_distance: This task sends a GET request to the /get_distance endpoint.

    The wait_time attribute is set to a random value between 1 and 5 seconds. This means that the simulated user will wait between 1 and 5 seconds between each task.

    """
    wait_time = between(1, 5) 
    @task
    def get_coordinates(self):
        self.client.get("/get_coordinates/?city_name=Lima")
    @task
    def get_distance(self):
        self.client.get("/get_distance/?lat1=51.5074&lon1=-0.1278&lat2=48.8566&lon2=2.3522")
