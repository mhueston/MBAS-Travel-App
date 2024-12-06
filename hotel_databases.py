import requests


def get_hotels(city, rating, check_in, check_out, price): 
        api_key = "5330664078a7d7f3e969ffaa48d3865c5ca16390f5e8441f4d4382c0b13a0866"
        geocode_url = "https://maps.googleapis.com/maps/api/geocode/json"
        geocode_params = {
        "address": city,
        "key": api_key
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
        "key": api_key
    }
        response = requests.get(places_url, params = places_params)        
        if response.status_code == 200:
            hotels = response.json().get("results", [])
            filter_hotels = [
                {
                    "Name": hotel["Name"],
                    "Rating": hotel.get("Rating", "N/A"),
                    "Price": hotel.get("Price_Level", "N/A"),
                    "City": hotel.get("City", "N/A"),
                    "Check-In": check_in,
                    "Check-Out": check_out

                }
                for hotel in hotels if hotel.get("Rating", 0) >= rating
            ]
            return filter_hotels
        else:
            print(f"Error: Unable to get data (Status Code: {response.status_code})")
            return []


def display_hotel(hotels):
        if hotels:
            print("\nAvailable Hotels:")
            for i, hotel in enumerate(hotels, start=1):
                print(f"{i}. Name: {hotel['name']}, Price: {hotel['price']}, Rating: {hotel['rating']}")
            return True
        else:
            print("No hotels found.")
            return False


def display():
    print("\nHotel Details:")
    print(f"Name: {hotel['name']}")
    print(f"Price: {hotel['price_level']}")
    print(f"Rating: {hotel['rating']}")
    print(f"Address: {hotel['address']}")
    print(f"Check-in Date: {hotel['check_in']}")
    print(f"Check-out Date: {hotel['check_out']}")
    print("Note: Additional availability details must be confirmed with the hotel.")
        
if __name__ == "__main__":
    print(f'Welcome!')
    price = int(input("Enter maximum price level(Lowest Rating: 1, Highest Rating: 4): "))
    city = input("What city are you visting? ")
    rating = float(input("What is the lowest hotel rating you would prefer? ex. 3.8: "))
    check_in = input("What day are you checking in? (YYYY-MM-DD)").strip()
    check_out = input("What day are you checking out? (YYYY-MM-DD)").strip()
    hotel = get_hotels(city, rating,check_in, check_out, price)  
   
    
    if display_hotel(hotel):
        try:
            # Ask user to select a hotel
            hotel_choice = int(input("\nEnter the number of the hotel to view details: ").strip())
            if 1 <= hotel_choice <= len(hotel):
                selected_hotel = hotel[hotel_choice - 1]
                display(selected_hotel)
            else:
                print("Invalid selection.")
        except ValueError:
            print("Invalid input. Please enter a number.")


