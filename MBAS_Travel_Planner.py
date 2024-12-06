""" INST326 Final Project
    
    Madison Hueston, Samgwaa Lesiga, Brooke Davis, Areana Holder

    A travel package planner.
"""
import requests
import travel_locations 
import flight_database 
import hotel_databases

class Travel_Planner:
    """A class that generates a custom travel package based on user input.

    Attributes:
        user_input (dict): A dictionary to store user input data (origin, destination, start_date, end_date, flight price max, hotel price max)
    """
    
    def __init__(self):
        self.origin = "" 
        self.destination = ""
        self.start_date = ""
        self.end_date = ""
        self.flight_price_max = 0
        self.hotel_price_max = 0
        self.flight_results = ""
        self.country_name = ""
    
    def get_user_input(self):
        
        self.country_name = input("Enter the South American country you want to go to: ").strip
        self.origin = input("Enter the origin airport code (e.g., JFK): ") 
        self.destination = input("Enter the destination airport code (e.g., LAX): ") 
        self.start_date = input("Enter the start date of the trip (YYYY-MM-DD): ") 
        self.end_date = input("Enter the end date of the trip (YYYY-MM-DD): ") 
        self.flight_price_max = float(input("Enter the maximum flight price: ")) 
        self.hotel_price_max = float(input("Enter the maximum hotel price per night: ")) 
    
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
        
        outbound_flight = flight_database.FlightDatabase(origin, destination, start_date)
        inbound_flight = flight_database.FlightDatabase(origin, destination, start_date)
        
        self.flight_results += outbound_flight.get_flight_results()
        self.flight_results += "-----------------------------------"
        self.flight_results += inbound_flight.get_flight_results()
        
    
    def retreive_hotel_data(self):
        pass
    
    def retreive_weather_data(self):
        pass
    
    def retreive_event_data(self):
        
        events = travel_locations.PlaceScraper(url = "https://www.travelandleisure.com/best-places-to-visit-in-south-america-7974457")
        events.places_by_country.get(self.country_name)
    
    def create_travel_package(self):
        pass
    
    def display_travel_package(self):
        """ Takes information retreived by other methods and formats it in a readable way and displays it to the user. Driven by Madison.
        
        Attributes:
            travel_package (dict): A dictionary to store the travel package information.
            
        Returns:
            travel_package_output (String): A string format of the travel package.
        
        """
        print (f'Here is your flight information:\n{self.flight_results}')
    
    
if __name__ == "__main__":
    
    planner = Travel_Planner()  
    
    planner.get_user_input() 
    
    planner.display_travel_package()