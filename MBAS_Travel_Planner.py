""" INST326 Final Project
    
    Madison Hueston, Samgwaa Lesiga, Brooke Davis, Areana Holder

    A travel package planner.
"""
import requests
import travel_locations
import flight_database
import hotel_databases

<<<<<<< Updated upstream
class TravelPlanner:
    """A class that generates a custom travel package based on user input.
=======
class Travel_Planner:
    """A class that generates a custom travel package based on user input."""
>>>>>>> Stashed changes

    def __init__(self):
        self.origin = "" 
        self.destination = ""
        self.start_date = ""
        self.end_date = ""
        self.flight_price_max = 0
        self.hotel_price_max = 0
        self.flight_results = ""
<<<<<<< Updated upstream
        self.places_to_visit = []
=======
        self.hotel_results = ""
        self.event_results = ""
>>>>>>> Stashed changes
    
    def get_user_input(self):
        self.origin = input("Enter the origin airport code (e.g., JFK): ") 
        self.destination = input("Enter the destination airport code (e.g., LAX): ") 
        self.start_date = input("Enter the start date of the trip (YYYY-MM-DD): ") 
        self.end_date = input("Enter the end date of the trip (YYYY-MM-DD): ") 
        self.flight_price_max = float(input("Enter the maximum flight price: ")) 
        self.hotel_price_max = float(input("Enter the maximum hotel price per night: ")) 
    
    def retreive_flight_data(self):
        """Retrieve flight data based on user input."""
        outbound_flight = flight_database.FlightDatabase(self.origin, self.destination, self.start_date)
        inbound_flight = flight_database.FlightDatabase(self.destination, self.origin, self.end_date)
        
        of_results = outbound_flight.get_flight_results()
        if_results = inbound_flight.get_flight_results()
        
        self.flight_results = f"{of_results}\n{if_results}"

    def retreive_hotel_data(self):
        """Retrieve hotel data based on user input."""
        hotels = hotel_databases.HotelDatabase(self.destination, self.hotel_price_max)
        self.hotel_results = hotels.get_hotel_results()

    def retreive_event_data(self):
<<<<<<< Updated upstream
        """
        Retrieves a list of places to visit in the destination country using a web scraper.
        
        This method uses the `travel_locations.scrape_places_to_visit` function to fetch 
        a list of popular places to visit in the specified destination country. The results 
        are stored in the `places_to_visit` attribute of the class.
        
        Args:
            None
        
        Returns:
            None: The results are stored in the `places_to_visit` attribute.
        
        Raises:
            Exception: If the web scraping process encounters issues, appropriate error 
            messages will be printed.
        """  

        url = "https://www.travelandleisure.com/best-places-to-visit-in-south-america-7974457"
        self.places_to_visit = travel_locations.scrape_places_to_visit(url, self.destination)
    
=======
        """Retrieve local events based on the destination."""
        events = travel_locations.TravelLocations(self.destination)
        self.event_results = events.search_activities()

>>>>>>> Stashed changes
    def create_travel_package(self):
        """Combine all data into a travel package."""
      
        travel_package = {
            "flight": self.flight_results,
            "hotel": self.hotel_results,
            "events": self.event_results
        }
        return travel_package

    def display_travel_package(self):
        """Display the travel package."""
        travel_package = self.create_travel_package()

        print(f"Here is your travel package for {self.destination}:\n")
        print(f"Flights:\n{travel_package['flight']}")
        print(f"\nHotels:\n{travel_package['hotel']}")
        print(f"\nEvents:\n{travel_package['events']}")
    
if __name__ == "__main__":
    planner = Travel_Planner() 
    
    planner.get_user_input()  # Get user input
    
    # Retrieve data for the travel package
    planner.retreive_flight_data()
    planner.retreive_hotel_data()
    planner.retreive_event_data()
    
    # Display the complete travel package
    planner.display_travel_package()
    
if __name__ == "__main__":
    
<<<<<<< Updated upstream
    planner = TravelPlanner() 
    
    planner.get_user_input() 
    
    planner.display_travel_package()
    
    

=======
    travel_plan = Travel_Planner()
>>>>>>> Stashed changes
