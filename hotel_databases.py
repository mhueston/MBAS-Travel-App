import requests
#print hotels based on price, put in link

class HotelDatabase: 
    
    def get_hotels(city, rating, check_in, check_out, adults, price): 
            api_url = "https://hotels.com/v1/search" #placeholder
            api_key = "api key here"  #placeholder
            parameters = {
                "City": city,
                "Rating": rating,
                "Check_in": check_in,
                "Check_out": check_out,
                "Adults": adults,
                "Price": price,
                "api_key": api_key
            }
            response = requests.get(api_url, parameters)
            if response.status_code == 200:
                hotels = response.json().get("results", [])
                return [hotel for hotel in hotels if hotel.get('rating', 0) >= rating]
            else:
                print(f"Error: Unable to get data (Status Code: {response.status_code})")
            return []


    def __init__(self, db_name="hotels.db"):
            """
            Initializes the database connection and creates the necessary tables 
            if they don't already exist.
            
            Args:
                db_name (str): The name of the database file.
            """
            self.connection = sqlite3.connect(db_name)
            self.create_tables()

    def create_tables(self):
            """
            Creates tables for hotels and bookings if they do not already exist.
            The hotels table stores hotel details, and the bookings table stores 
            booking information for each hotel.
            """
            cursor = self.connection.cursor()
            
            # Create hotels table
            cursor.execute('''CREATE TABLE IF NOT EXISTS hotels (
                                id INTEGER PRIMARY KEY,
                                name TEXT NOT NULL,
                                location TEXT,
                                rating REAL,
                                price_per_night REAL
                            )''')
            
            # Create bookings table
            cursor.execute('''CREATE TABLE IF NOT EXISTS bookings (
                                id INTEGER PRIMARY KEY,
                                hotel_id INTEGER,
                                customer_name TEXT,
                                check_in_date TEXT,
                                check_out_date TEXT,
                                FOREIGN KEY (hotel_id) REFERENCES hotels (id)
                            )''')
            
            self.connection.commit()

    def display_hotel(hotels):
            """
            Adds a new hotel to the database.
            
            Args:
                name (str): The name of the hotel.
                location (str): The location of the hotel.
                rating (float): The hotel's rating.
                price_per_night (float): Price per night at the hotel.
            
            Returns:
                int: The ID of the newly added hotel.
            """
            if hotels:
                print("\nAvailable Hotels:")
                for i, hotel in enumerate(hotels, start=1):
                    print(f"{i}. Name: {hotel['name']}, Price: {hotel['price']}, Rating: {hotel['rating']}")
                return True
            else:
                print("No hotels found.")
                return False
        

            #cursor = self.connection.cursor()
            #cursor.execute('''INSERT INTO hotels (name, location, rating, price_per_night)
                            #VALUES (?, ?, ?, ?)''', (name, location, rating, price_per_night))
            
            #self.connection.commit()
            #return cursor.lastrowid


    def display():
        print("\nHotel Details:")
        print(f"Name: {hotel['name']}")
        print(f"Price: ${hotel['price']}")
        print(f"Rating: {hotel['rating']}")
        
            
if __name__ == "__main__":
    print(f'Welcome!')
    price = float(input("Enter maximum price per night: "))
    city = input("What city are you visting? ")
    rating = float(input("What is the lowest hotel rating you would prefer? "))
    check_in = input("What day are you checking in? (Year, Month, Day)").strip()
    check_out = input("What day are you checking out? (Year, Month, Day)").strip()
    hotel = get_hotels(city, rating, price)  

    #database not used due to project expansion(pulling from website)
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

    #things to do: 
    #get api keys for using hotels.com
    #clean up code


