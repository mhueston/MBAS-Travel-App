class SouthAmericaSeasons:
    
    """
    A class to determine seasonal weather conditions in South American countries based on user-specified country and month.

    Attributes:
        hot_season (dict): Maps countries to months with hot weather.
        rainy_season (dict): Maps countries to months with rainy weather.
        cold_season (dict): Maps countries to months with cold weather.

    Methods:
        get_season(country, month): Determines the predominant season for a given country and month.
    """
    
    def __init__(self):
        
        """
        Initializes the SouthAmericaSeasons object, setting up the dictionaries for hot, rainy, and cold seasons for each South American country.
        """
        
        self.hot_season = {
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

        self.rainy_season = {
            'Brazil': ['January', 'February', 'March', 'April', 'May', 'September', 'October', 'November', 'December'],
            'Chile': ['May', 'June', 'July', 'August', 'September'],
            'Argentina': ['January', 'February', 'March', 'September', 'October', 'November', 'December'],
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

        self.cold_season = {
            'Brazil': ['June', 'July', 'August'],
            'Chile': ['March', 'April', 'June', 'July', 'August', 'September'],
            'Argentina': ['April', 'May', 'June', 'July', 'August'],
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

    def get_season(self, country, month):
        
        """
        Determines the predominant season for a given country and month.

        Args:
            country (str): The name of the country.
            month (str): The month of the year.

        Returns:
            list[str]: A list of seasons (e.g., ["hot", "rainy"]) that may be predominant for the given country and month.
        """
        
        country = country.strip().capitalize()
        
        month = month.strip().capitalize()

        if country not in self.hot_season and country not in self.rainy_season and country not in self.cold_season:
            
            raise ValueError(f"{country} is not a South American country.")

        if month not in self.hot_season.get(country, []) and month not in self.rainy_season.get(country, []) and month not in self.cold_season.get(country, []):
            
            raise ValueError(f"{month} is not valid. Please enter a valid month.")

        seasons = []
        
        if country in self.hot_season and month in self.hot_season[country]:
            
            seasons.append("hot")
        
        if country in self.rainy_season and month in self.rainy_season[country]:
            
            seasons.append("rainy")
        
        if country in self.cold_season and month in self.cold_season[country]:
            
            seasons.append("cold")
            
        if seasons:
            
            return f"In {country} during {month}, the weather is {', '.join(seasons)}.\n"
        
        else:
            
<<<<<<< Updated upstream
            return f"Season information for {country} in {month} is unknown."

    
=======
            return f"Season information for {country} in {month} is unknown."    
>>>>>>> Stashed changes
