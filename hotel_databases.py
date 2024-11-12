import sqlite3

class HotelDatabase:
    """
    A class to manage hotel information and bookings for a travel app.
    This class handles adding, retrieving, and updating hotel information 
    and booking records in a SQLite database.
    """

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

    def add_hotel(self, name, location, rating, price_per_night):
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
        cursor = self.connection.cursor()
        cursor.execute('''INSERT INTO hotels (name, location, rating, price_per_night)
                          VALUES (?, ?, ?, ?)''', (name, location, rating, price_per_night))
        
        self.connection.commit()
        return cursor.lastrowid

    def get_hotels_by_location(self, location):
        """
        Retrieves all hotels in a specific location.
        
        Args:
            location (str): The location to filter hotels by.
        
        Returns:
            list of dict: A list of dictionaries containing hotel details in the specified location.
        """
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM hotels WHERE location = ?", (location,))
        hotels = cursor.fetchall()
        
        return [{"id": h[0], "name": h[1], "location": h[2], "rating": h[3], "price_per_night": h[4]} for h in hotels]

    def get_hotel_info(self, hotel_id):
        """
        Retrieves information for a specific hotel based on its ID.
        
        Args:
            hotel_id (int): The ID of the hotel to retrieve.
        
        Returns:
            dict: A dictionary containing hotel details or None if hotel is not found.
        """
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM hotels WHERE id = ?", (hotel_id,))
        hotel = cursor.fetchone()
        
        if hotel:
            return {"id": hotel[0], "name": hotel[1], "location": hotel[2], "rating": hotel[3], "price_per_night": hotel[4]}
        else:
            return None

    # Other methods remain the same

    def close_connection(self):
        """
        Closes the database connection.
        """
        self.connection.close()

        
if __name__ == "__main__":
    db = HotelDatabase()
    
    # Example: User specifies a location
    user_location = input("Enter the location to search for hotels: ")
    hotels_in_area = db.get_hotels_by_location(user_location)
    
    # Display hotels
    if hotels_in_area:
        print("Hotels in", user_location)
        for hotel in hotels_in_area:
            print(f"{hotel['name']} - Rating: {hotel['rating']}, Price: {hotel['price_per_night']}")
    else:
        print(f"No hotels found in {user_location}.")
    
    db.close_connection()

