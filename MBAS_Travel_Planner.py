""" INST326 Final Project
    
    Madison Hueston, Samgwaa Lesiga, Brooke Davis, Areana Holder

    A travel package planner.
"""
import requests
import location_database

class Travel_Planner:
    """A class that generates a custom travel package based on user input.

    Attributes:
        user_input (dict): A dictionary to store user input data (origin, destination, start_date, end_date, flight price max, hotel price max)
    """
    
    def __init__(self):
        pass
    
    def get_user_input(self):
        pass 
    
    def retreive_flight_data(self, origin, destination, start_date, end_date, flight_price_max):
        """ Take destiniation origin, date range, and flight price range to find a flight that fits the criteria. Driven by Madison
        
        Attributes:
            origin (String): Airport of origin
            destination (String): The destination airport
            start_date (String): Start date of trip in format YYYY-MM-DD
            end date (String): End date of trip in format YYYY-MM-DD
            flight_price_max (String): Max price of flight
            
        Returns: 
            reccomended_flight (String): The flight the user should take
        
        """
        pass
    
    def retreive_hotel_data(self):
        pass
    
    def retreive_weather_data(self):
        pass
    
    def retreive_event_data(self):
        
        events = location_database()
        events.search_activities()
    
    def create_travel_package(self):
        pass
    
    def display_travel_package(self):
        """ Takes information retreived by other methods and formats it in a readable way and displays it to the user. Driven by Madison.
        
        Attributes:
            travel_package (dict): A dictionary to store the travel package information.
            
        Returns:
            travel_package_output (String): A string format of the travel package.
        
        """
        pass
    
    
if __name__ == "__main__":
    
    planner = Travel_Planner() 
    
    planner.get_user_input() 
    
    planner.display_travel_package()
    
    

