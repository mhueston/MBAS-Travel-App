import requests

class HotelDatabase:
    
    """
    A class to interact with the Google Hotels API to search and retrieve hotel information 
    based on specified parameters, and display the results in a user-friendly format.
    """
    
    def __init__(self, city, gl, check_in, check_out, price):
        
        """
        Initializes the HotelDatabase instance with search parameters for hotel availability.
        
        Args:
            city (str): The city to search for hotels in.
            gl (str): Geolocation code (e.g., country code) for search localization.
            check_in (str): Check-in date in YYYY-MM-DD format.
            check_out (str): Check-out date in YYYY-MM-DD format.
            price (int): Maximum price filter for hotel search.
        """
        
        self.city = city
        
        self.gl = gl
        
        self.rating = 3.5
        
        self.check_in = check_in
        
        self.check_out = check_out
        
        self.price = price
        
        self.api_key = "5330664078a7d7f3e969ffaa48d3865c5ca16390f5e8441f4d4382c0b13a0866"

    def get_hotels(self):
        
        """
        Queries the Google Hotels API for hotel availability based on the initialized parameters.
        
        Returns:
            dict: Details of the top hotel found, or None if no hotels match the criteria.
        """
        
        # Set the Google Hotels API endpoint
        api_url = "https://serpapi.com/search?engine=google_hotels"

        # Construct the parameters for the API request
        params = {
            "engine": "google_hotels",
            "q": self.city,  # Search query: city name
            "gl": self.gl,
            "hl": "en",  # Language
            "currency": "USD",  # Currency
            "check_in_date": self.check_in,  # Check-in date
            "check_out_date": self.check_out,  # Check-out date
            "adults": 2,  # Number of adults
            "children": 0,  # Number of children
            "max_price": self.price,  # Maximum price filter
            "api_key": self.api_key  # API key for SerpAPI
        }

        # Make the GET request to the API
        response = requests.get(api_url, params=params)
        
        if response.status_code == 200:
            
            response_json = response.json()
            
            hotels = response_json.get("properties", [])
            
            if hotels:
                
                top_hotel = hotels[0]
                
                return top_hotel
            
            else:
                return None
        
        else:
            print("Error fetching data from API.")
            
            return None

    def display(self, hotel):
        
        """
        Formats and displays the details of a hotel in a user-friendly string format.
        
        Args:
            hotel (dict): A dictionary containing hotel details, as returned by the API.
        
        Returns:
            results (str): A formatted string with hotel information, or a message if no hotel is found.
        """
        
        results = ""
    
        # Always include the essential fields
        if hotel:
            results += (f"Name: {hotel['name']}\n")
            
            results += (f"Price: {hotel['rate_per_night']['lowest']}\n")
            
            results += (f"Rating: {hotel.get('rating', 'N/A')}\n")
            
            results += (f"City: {self.city}\n")
            
            results += (f"Check-in Date: {self.check_in}\n")
            
            results += (f"Check-out Date: {self.check_out}\n")
            
            description = hotel.get('description')
            
            if description:
                
                results += (f"Description: {description}\n")
            
            link = hotel.get('link')
            
            if link:
                
                results += (f"Link: {link}\n")
            
            results += ("Note: Additional availability details must be confirmed with the hotel.\n")
        
        else:
            
            results += ("No hotel found.\n")
        
        return results
