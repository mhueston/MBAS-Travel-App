import sqlite3

def create_database(db_name):
    """
    Creates an SQLite database with tables for countries and activities.
    
    Args:
        db_name: The name of the database file.
    """
    # Connect to SQLite and set up tables for Countries and Activities


def populate_countries_data(db_name, countries_data):
    """
    Populates the Countries table with a list of country data.
    
    Args:
        db_name: The name of the database file.
        countries_data: List of dictionaries, each containing country information.
    """
    # Insert each country's data (name, region, description) into the Countries table


def populate_activities_data(db_name, activities_data):
    """
    Populates the Activities table with a list of activity data, linked to countries.
    
    Args:
        db_name: The name of the database file.
        activities_data: List of dictionaries, each containing activity information.
    """
    # Insert each activity's data (activity name, description, category) into Activities table


def get_countries(db_name, region):
    """
    Retrieves a list of country names in the specified region.
    
    Args:
        db_name: The name of the database file.
        region: The region to filter countries by.
    
    Returns:
        A list of country names in the specified region.
    """
    # Query the Countries table to get all countries in the specified region


def get_activities_by_country(db_name, country_name):
    """
    Retrieves a list of activities for a specified country.
    
    Args:
        db_name: The name of the database file.
        country_name: The name of the country to filter activities by.
    
    Returns:
        A list of activities for the specified country.
    """
    # Query the Activities table, joining with Countries table, to find activities for the specified country


def search_activities(db_name, category=None, keyword=None):
    """
    Searches for activities based on category or keyword in the description.
    
    Args:
        db_name: The name of the database file.
        category (optional): The category to filter activities by.
        keyword (optional): A keyword to search within activity descriptions.
    
    Returns:
        A list of activities matching the specified criteria.
    """
    # Query the Activities table based on category or keyword in description
