import requests

class HotelFinder:
    def __init__(self,city, country_name, rating, check_in, check_out, price):
        self.api_key = '5330664078a7d7f3e969ffaa48d3865c5ca16390f5e8441f4d4382c0b13a0866'
        self.city = city
        self.rating = 3.5
        self.check_in = check_in
        self.check_out = check_out
        self.price = price
        self.county_name = country_name
        self.rating = rating

    def get_hotels(self):
        geocode_url = "https://maps.googleapis.com/maps/api/geocode/json"
        geocode_params = {
            "address": self.city,
            "key": self.api_key
        }
        geocode_response = requests.get(geocode_url, params=geocode_params).json()

        if geocode_response.get("status") == "OK":
            location = geocode_response["results"][0]["geometry"]["location"]
            lat, lng = location["lat"], location["lng"]
        else:
            print("Error: Unable to determine the coordinates of the specified city.")
            return []

        places_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
        places_params = {
            "location": f"{lat},{lng}",
            "radius": 50000,  # 50 km radius
            "type": "lodging",
            "key": self.api_key
        }
        response = requests.get(places_url, params=places_params)
        if response.status_code == 200:
            hotels = response.json().get("results", [])
            self.hotels = [
                {
                    "Name": hotel["name"],
                    "Rating": hotel.get("rating", "N/A"),
                    "Price": hotel.get("price_level", "N/A"),
                    "City": self.city,
                    "Country": self.country_name,
                    "Check-In": self.check_in,
                    "Check-Out": self.check_out
                }
                for hotel in hotels if hotel.get("rating", 0) >= self.rating
            ]
            return self.hotels
        else:
            print(f"Error: Unable to get data (Status Code: {response.status_code})")
            return []

    def display_hotels(self):
        if self.hotels:
            print("\nAvailable Hotels:")
            for i, hotel in enumerate(self.hotels, start=1):
                print(f"{i}. Name: {hotel['Name']}, Price: {hotel['Price']}, Rating: {hotel['Rating']}")
            return True
        else:
            print("No hotels found.")
            return False

    def display_hotel_details(self, hotel_index):
        if 0 <= hotel_index < len(self.hotels):
            hotel = self.hotels[hotel_index]
            print("\nHotel Details:")
            print(f"Name: {hotel['Name']}")
            print(f"Price: {hotel['Price']}")
            print(f"Rating: {hotel['Rating']}")
            print(f"City: {hotel['City']}")
            print(f"Check-in Date: {hotel['Check-In']}")
            print(f"Check-out Date: {hotel['Check-Out']}")
            print("Note: Additional availability details must be confirmed with the hotel.")
        else:
            print("Invalid hotel index.")

if __name__ == "__main__":
    print('Welcome!')
    api = "group_api_key"
    price = int(input("Enter maximum price level(Lowest Rating: 1, Highest Rating: 4): "))
    country_name = input("What country are you visiting? ")
    city = input("What city are you visiting? ")
    rating = float(input("What is the lowest hotel rating you would prefer? ex. 3.8: "))
    check_in = input("What day are you checking in? (YYYY-MM-DD)").strip()
    check_out = input("What day are you checking out? (YYYY-MM-DD)").strip()


    hotel_finder = HotelFinder(city, country_name, rating, check_in, check_out, price)
    hotel_finder.get_hotels()


    if hotel_finder.display_hotels():
        try:
            hotel_choice = int(input("\nEnter the number of the hotel to view details: ").strip())
            hotel_finder.display_hotel_details(hotel_choice - 1)
        except ValueError:
            print("Invalid input. Please enter a number.")
