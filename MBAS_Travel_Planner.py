""" INST326 Final Project
    
    Madison Hueston, Samgwaa Lesiga, Brooke Davis, Areana Holder

    A travel package planner.
"""
import requests
import travel_locations 
import flight_database 
import hotel_databases
import weather_database

class Travel_Planner:
    
    """
    A travel planning tool designed for organizing trips to South American destinations.

    This class handles user input, retrieves relevant travel data, and generates a customized travel package 
    that includes flights, hotels, weather information, and events.
    
    This class provides methods for gathering user input, retrieving flight and hotel data, 
    fetching weather information, and displaying a customized travel package.

    Attributes:
        airport_codes (dict): Maps country names to their corresponding airport codes.
        tourist_cities (dict): Maps country names to lists of popular tourist cities.
        country_codes (dict): Maps country names to their corresponding Google Maps country codes.
        origin (str): The departure airport code.
        city (str): The destination city selected by the user.
        destination (str): The airport code for the destination country.
        start_date (str): The start date of the trip in 'YYYY-MM-DD' format.
        end_date (str): The end date of the trip in 'YYYY-MM-DD' format.
        flight_price_max (float): The maximum amount the user is willing to spend on flights.
        hotel_price_max (float): The maximum cost per night for hotel accommodations.
        flight_results (str): Stores the results of flight searches.
        gl (str): The country code used for travel-related queries.

    Methods:
        __init__(): Initializes the Travel_Planner object with default attribute values.
        get_user_input(): Collects user input for trip planning, including destination, travel dates, and budget.
        retreive_flight_data(): Retrieves flight information based on user input.
        retreive_hotel_data(): Retrieves hotel information based on user input.
        retreive_weather_data(): Retrieves weather information for the destination.
        retreive_event_data(): Retrieves event data for the destination country.
        display_travel_package(): Displays a formatted summary of the travel package.
    """
    
    airport_codes = {
            'Brazil': 'GRU', 
            'Chile': 'SCL', 
            'Argentina': 'EZE', 
            'Bolivia': 'LPB',
            'Colombia': 'BOG',
            'Ecuador': 'UIO',
            'Guyana': 'GEO',
            'Peru': 'ASU',
            'Paraguay': 'LIM',
            'Suriname': 'PBM',
            'Uruguay': 'MVD',
            'Venezuela': 'CCS'}
    
    tourist_cities = {
            'Brazil': ["Rio de Janeiro", "São Paulo", "Salvador", "Brasília", "Foz do Iguaçu"], 
            'Chile': ["Santiago", "Valparaíso", "San Pedro de Atacama", "Punta Arenas", "Puerto Varas"], 
            'Argentina': ["Buenos Aires", "Mendoza", "Bariloche", "Cordoba", "Salta"], 
            'Bolivia': ["La Paz", "Sucre", "Uyuni", "Santa Cruz de la Sierra", "Copacabana"],
            'Colombia': ["Bogotá", "Medellín", "Cartagena", "Cali", "Santa Marta"],
            'Ecuador': ["Quito", "Guayaquil", "Cuenca", "Baños", "Puerto Ayora"],
            'Guyana': ["Georgetown", "Bartica", "Lethem", "Linden", "Kaieteur National Park"],
            'Peru': ["Lima", "Cusco", "Arequipa", "Puno", "Iquitos"],
            'Paraguay': ["Asunción", "Ciudad del Este", "Encarnación", "San Bernardino", "Filadelfia"],
            'Suriname': ["Paramaribo", "Brownsberg", "Nieuw Nickerie", "Albina", "Galibi Nature Reserve"],
            'Uruguay': ["Montevideo", "Punta del Este", "Colonia del Sacramento", "Salto", "Rocha"],
            'Venezuela': ["Caracas", "Mérida", "Isla Margarita", "Canaima", "Maracaibo"]}
    
    country_codes = {
            'Argentina': 'ar', 
            'Bolivia': 'bo', 
            'Brazil': 'br', 
            'Chile': 'cl', 
            'Colombia': 'co', 
            'Ecuador': 'ec', 
            'Guyana': 'gy', 
            'Paraguay': 'py', 
            'Peru': 'pe', 
            'Suriname': 'sr', 
            'Uruguay': 'uy', 
            'Venezuela': 've'
    }
    
    def __init__(self):
        
        """
    Initializes the travel planning class with default attributes.

    This constructor sets up the necessary variables for storing user input and travel data, 
    ensuring the object is ready to handle subsequent operations such as fetching flights and hotels.

    Attributes:
        self.origin (str): The departure airport code (e.g., "JFK").
        self.city (str): The destination city selected by the user.
        self.destination (str): The airport code for the destination country.
        self.start_date (str): The start date of the trip in 'YYYY-MM-DD' format.
        self.end_date (str): The end date of the trip in 'YYYY-MM-DD' format.
        self.flight_price_max (float): The maximum amount the user is willing to spend on flights.
        self.hotel_price_max (float): The maximum cost per night for hotel accommodations.
        self.flight_results (str): Stores the results of flight searches.
        self.gl (str): The country code used for travel-related queries.
    """
        
        self.origin = "" 
        
        self.city = ""
        
        self.destination = ""
        
        self.start_date = ""
        
        self.end_date = ""
        
        self.flight_price_max = 0
        
        self.hotel_price_max = 0
        
        self.flight_results = ""
        
        self.gl = ""
    
    def get_user_input(self):
        
        """
    Collects and stores user input for planning a trip to a South American destination.

    The method gathers various details from the user to customize their travel experience, including:
    - Destination country and city.
    - Origin airport.
    - Travel dates.
    - Maximum budget for flights and hotel accommodations.

    Attributes:
        self.country_name (str): The South American country selected by the user.
        self.tourist_cities (dict): A dictionary containing top tourist cities for each country.
        self.city (str): The specific city the user wants to visit.
        self.origin (str): The airport code for the user's departure location.
        self.start_date (str): The start date of the trip in 'YYYY-MM-DD' format.
        self.end_date (str): The end date of the trip in 'YYYY-MM-DD' format.
        self.flight_price_max (float): The maximum amount the user is willing to spend on flights.
        self.hotel_price_max (str): The maximum cost per night for hotel accommodations.
        self.destination (str): The airport code for the destination country.
        self.gl (str): The country code used for travel-related searches.

    """
        
        self.country_name = input("Enter the South American country you would like to go to: ").strip()
        
        print(f'Here are the top 5 tourist cities in {self.country_name}')
        
        print(f'{self.tourist_cities[self.country_name]}')
        
        self.city = input("Enter the  city you would like to go to: ") 
        
        self.origin = input("Enter the origin airport code (e.g., JFK): ") 
        
        self.start_date = input("Enter the start date of the trip (YYYY-MM-DD): ") 
        
        self.end_date = input("Enter the end date of the trip (YYYY-MM-DD): ") 
        
        self.flight_price_max = float(input("Enter the maximum flight price: ")) 
        
        self.hotel_price_max = (input("Enter the maximum hotel price per night: ")) 
        
        self.destination = self.airport_codes[self.country_name]
        
        self.gl = self.country_codes[self.country_name]
        
    def retreive_flight_data(self):
        
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
        
        outbound_flight = flight_database.FlightDatabase(self.origin, self.destination, self.start_date)
        
        inbound_flight = flight_database.FlightDatabase(self.destination, self.origin, self.end_date)
        
        outbound_results = outbound_flight.get_flight_results()
        
        self.flight_results += f"Your flights to {self.country_name}:\n"
        
        self.flight_results += "\n".join(outbound_results) + "\n"
        
        inbound_results = inbound_flight.get_flight_results()
        
        self.flight_results += "Your flights home:\n"
        
        self.flight_results += "\n".join(inbound_results) + "\n"
        
        return
        
    
    def retreive_hotel_data(self):
        
        """
    Retrieves hotel data from a hotel database.

    This method interacts with the `HotelDatabase` class to fetch hotel information 
    based on the city, guest limit, date range, and maximum price specified 
    in the current object's attributes.

    Returns:
        str: A formatted string displaying the retrieved hotel data.
    """
        
        hotel_data = hotel_databases.HotelDatabase(self.city, self.gl, self.start_date, self.end_date, self.hotel_price_max)
        
        hotel = hotel_data.get_hotels()
        
        return hotel_data.display(hotel)
        
    
    def retreive_weather_data(self):
        
        """
        Retrieves the weather data for the specified country and start date.
        
        The month is extracted from the start date and used to fetch the seasonal weather information.
        
        Returns:
            message (str): A message indicating the predominant weather for the specified country and month, or an error message.
        """
        
        # Parse the date and extract the month
        
        year, month, day = self.start_date.split("-")
        
        month_number = int(month)

        # Convert month number to name
        
        months = [
            "January", 
            "February", 
            "March", 
            "April", 
            "May", 
            "June",
            "July", 
            "August", 
            "September", 
            "October", 
            "November", 
            "December"
        ]
        
        if not 1 <= month_number <= 12:
            
            return "Invalid month number. Must be between 1 and 12."
        
        month_name = months[month_number - 1]

        # Retrieve weather information from weather_database
        
        seasons_checker = weather_database.SouthAmericaSeasons()
        
        return seasons_checker.get_season(self.country_name, month_name)
    
    def retreive_event_data(self):
        
        """
    Retrieves event data for the specified country from a travel website.

    This method uses the `PlaceScraper` class from the `travel_locations` module 
    to scrape event data from the provided URL. 

    Returns:
        list: A list of events found for the specified country.
    """

        
        events = travel_locations.PlaceScraper(url = "https://www.travelandleisure.com/best-places-to-visit-in-south-america-7974457")
        
        events.scrape_places()
        
        return events.get_places_for_country(self.country_name)
    
    def display_travel_package(self):
        """ Takes information retreived by other methods and formats it in a readable way and displays it to the user. Driven by Madison.
        
        Attributes:
            travel_package (dict): A dictionary to store the travel package information.
            
        Returns:
            travel_package_output (String): A string format of the travel package.
        
        """
        self.retreive_flight_data()
        
        hotel_data = self.retreive_hotel_data()
        
        print("Thank you for choosing MBAS. Below is your custom travel package.\n")
        
        print (f'\nHere is your flight information:\n{self.flight_results}')
        
        print("-----------------------------------")
        
        print(f'\nHere is your hotel information:\n{hotel_data}')
        
        print("-----------------------------------")
        
        print(f'\nHere is the weather in {self.country_name}:')
        
        print(planner.retreive_weather_data())
        
        print("-----------------------------------\n")
        
        print(f'Here are places to visit in {self.country_name}:')
        
        print(self.retreive_event_data())
        
        print("-----------------------------------")
        
    
if __name__ == "__main__":
    
    planner = Travel_Planner()  
    
    planner.get_user_input() 
    
    planner.display_travel_package()
    


    
