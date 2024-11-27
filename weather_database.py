
"""
This script provides information about the seasons in South American countries based on user input.

It defines three dictionaries:
- `hot_season`: Maps countries to months with hot weather.
- `rainy_season`: Maps countries to months with rainy weather.
- `cold_season`: Maps countries to months with cold weather.

The `get_season` function determines the season for a given country and month.

The `main` function prompts the user for a country and month, calls `get_season`, and prints an appropriate message.
"""

# Dictionaries with seasons for each country

hot_season = {
    'Brazil': ['December', 'February', 'March', 'May', 'September'],
    'Chile': ['December', 'January', 'February', 'October', 'November'],
    'Argentina': ['December', 'January', 'February'],
    'Bolivia': ['January', 'February', 'March', 'April', 'May', 'September', 'October', 'November', 'December'],
    'Colombia': ['January', 'February', 'March', 'June', 'July', 'August', 'September', 'November', 'December'],
    'Ecuador': ['January', 'February', 'March', 'April', 'August', 'September', 'October', 'November'],
    'Guyana': ['February', 'March', 'April', 'May', 'September', 'October', 'November'],
    'Peru': ['April', 'May', 'September', 'October', 'November', 'December', 'January', 'February', 'March'],
    'Paraguay': ['December', 'January', 'February', 'May', 'September'],
    'Suriname': ['September', 'October', 'November'],
    'Uruguay': ['December', 'January', 'February'],
    'Venezuela': ['March', 'April', 'May', 'June', 'July', 'August', 'September', 'November']
}

rainy_season = {
    'Brazil': ['January', 'February', 'March', 'April', 'May', 'September', 'October', 'November', 'December'],
    'Chile': ['May', 'June', 'July', 'August', 'September'],
    'Argentina': ['January', 'February', 'March', 'September','October', 'November', 'December'],
    'Bolivia': ['January', 'February', 'March', 'April', 'November', 'December'],
    'Colombia': ['April', 'May', 'June', 'July', 'August', 'September', 'October', 'November'],
    'Ecuador': ['January', 'February', 'March', 'April', 'May', 'October', 'November', 'December'],
    'Guyana': ['January', 'February', 'May', 'June', 'July', 'August', 'November', 'December'],
    'Peru': ['January', 'February', 'March', 'April', 'November', 'December'],
    'Paraguay': ['January', 'February', 'March', 'April', 'October', 'November', 'December'],
    'Suriname': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'December'],
    'Uruguay': ['January', 'February', 'March', 'April', 'October', 'November', 'December'],
    'Venezuela': ['May', 'June', 'July', 'August', 'September', 'October', 'November']
}

cold_season = {
    'Brazil': ['June', 'July', 'August'],
    'Chile': ['March', 'April', 'June', 'July', 'August', 'September'],
    'Argentina': ['April', 'May','June', 'July', 'August'],
    'Bolivia': ['June', 'July', 'August'],
    'Colombia': ['June', 'July', 'August'],
    'Ecuador': ['June', 'July', 'August', 'September'],
    'Guyana': ['June', 'July', 'August'],
    'Peru': ['June', 'July', 'August'],
    'Paraguay': ['June', 'July', 'August'],
    'Suriname': ['June', 'July', 'August'],
    'Uruguay': ['May', 'June', 'July', 'August', 'September'],
    'Venezuela': ['January', 'February', 'December']
}

# Function to get the season based on user input
def get_season(country, month):
    """
    Determines the predominant season for a given country and month.

    Args:
        country (str): The name of the country.
        month (str): The month of the year.

    Returns:
        str: The season ("hot", "rainy", "cold", or "unknown") for the given country and month.
    """
    
    # Normalize input (capitalize country and month)
    country = country.strip().capitalize()
    
    month = month.strip().capitalize()
    
    # Check if country exists in any of the season dictionaries
    if country not in hot_season and country not in rainy_season and country not in cold_season:
        
        raise ValueError(f"{country} is not a South American country.")
    
    # Check if the month is valid
    if month not in hot_season.get(country, []) and month not in rainy_season.get(country, []) and month not in cold_season.get(country, []):
        
        raise ValueError(f"{month} is not valid. Please enter a valid month.")
    
    # Initialize an empty list for seasons
    seasons = []

    # Check each season dictionary for a match
    if country in hot_season and month in hot_season[country]:
        
        seasons.append("hot")
        
    if country in rainy_season and month in rainy_season[country]:
        
        seasons.append("rainy")
        
    if country in cold_season and month in cold_season[country]:
        
        seasons.append("cold")

    # Return the list of seasons (or ["unknown"] if no matches are found)
    return seasons if seasons else ["unknown"]

# Main program to interact with the user
def main():
    """
    Prompts the user for a country and month, then determines the expected weather conditions.

    This function takes user input for the country and month of travel and uses the `get_season` function to determine the predominant season. 
    
    Returns:
        message:  A message informing the user about the expected weather conditions.
    """
    
    # Collect user input
    country = input("Enter a South American country: ").strip()
    
    month = input("Enter a month (ex. January): ").strip()

    # Determine the season
    seasons = get_season(country, month)

    # Display the result
    if seasons != "unknown":
        
        print(f"In {country} during {month}, the weather is {', '.join(seasons)}.")
        
    else:
        
        print(f"Spelling is incorrect, try again.")
    

if __name__ == "__main__":
    
    main()
    