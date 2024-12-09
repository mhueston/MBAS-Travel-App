import requests

class FlightDatabase:
    """
    Manages flight itinerary data by querying the SerpAPI for travel destinations.

    Attributes:
        departure_id (str): The departure airport code.
        arrival_id (str): The arrival airport code.
        outbound_date (str): The date of departure in 'YYYY-MM-DD' format.
    """

    def __init__(self, departure_id, arrival_id, outbound_date):
        """
        Initializes the FlightDatabase with user-provided details.

        Args:
            departure_id (str): The departure airport code.
            arrival_id (str): The arrival airport code.
            outbound_date (str): The date of departure in 'YYYY-MM-DD' format.
        """
        self.departure_id = departure_id
        
        self.arrival_id = arrival_id
        
        self.outbound_date = outbound_date

    def get_flight_results(self):
        
        """
        Queries the SerpAPI for flight data based on the initialized parameters.

        Returns:
            list: A formatted list of flight information strings.
        """
        api_endpoint = 'https://serpapi.com/search'

        params = {
            "engine": "google_flights",
            "departure_id": self.departure_id,
            "arrival_id": self.arrival_id,
            "outbound_date": self.outbound_date,
            "api_key": '323920de37a645c0b46ed65aa8287b7141d154e42f03944ec84ff05489fc6115',
            "type": "2"
        }

        response = requests.get(api_endpoint, params=params)
        
        if response.status_code != 200: 
            
            print(f"Error fetching flight data. Status code: {response.status_code}") 
            
            return []

        data = response.json()
        
        flights_data = data.get('best_flights', [])
        
        if not flights_data:
            
            print("No flights found.")
            
            return []

        flight = flights_data[0]
        
        formatted_flight = []
        
        flight_number = 1

        for segment in flight['flights']:
            
            departure_info = f"Flight {flight_number} departs from {segment['departure_airport']['name']} at {segment['departure_airport']['time']}."
            
            arrival_info = f"Flight arrives at {segment['arrival_airport']['name']} at {segment['arrival_airport']['time']}."
            
            extras = ', '.join(segment.get('extensions', []))
            
            flight_info = f"{departure_info}\n{arrival_info}\nThere is {extras}\n "
            
            flight_number += 1
            
            formatted_flight.append(flight_info)

        return ["\n".join(formatted_flight)]
