import requests
from bs4 import BeautifulSoup as bs

class PlaceScraper:
    
    """
    A class to scrape and organize tourist destinations by country from a given webpage.
    """
    
    def __init__(self, url):
        
        """
        Initializes the PlaceScraper with a URL and an empty dictionary to store places by country.
        
        Args:
            url (str): The URL of the webpage to scrape.
        """
        
        self.url = url
        
        self.places_by_country = {}

    def scrape_places(self):
        
        """
        Scrapes the places to visit from the provided URL and organizes them by country.

        This method makes a GET request to the URL, parses the HTML content using BeautifulSoup, 
        and extracts the names of places and their corresponding countries. The results are stored 
        in the `places_by_country` dictionary.
        
        If the request fails, it prints an error message and does not attempt to parse the content.
        """
        
        response = requests.get(self.url)

        if response.status_code != 200:

            print("Failed to fetch the webpage")

            return

        soup = bs(response.content, 'html.parser')

        headings = soup.find_all('span', class_='mntl-sc-block-heading__text')

        for heading in headings:

            text = heading.text.strip()

            parts = text.split(",")

            if len(parts) >= 2:

                place = parts[0].strip()

                country = parts[-1].strip()
                
                if country not in self.places_by_country:
                    
                    self.places_by_country[country] = []

                self.places_by_country[country].append(place)

    def get_places_for_country(self, country_name):
        
        """
        Retrieves the list of places to visit for a specific country.
        
        Args:
            country_name: The name of the country to filter results for.
        
        Returns:
            A list of places to visit in the specified country.
        """
        
        if country_name in self.places_by_country:
            results = self.places_by_country[country_name]
            formatted_results = "\n"
            
            for i in range(len(results)):
                formatted_results += f'{i+1}. {results[i]}\n'
        
            return formatted_results
            
            return self.places_by_country[country_name]
        else:
            
            return f'There are limited tourist places in {country_name}'

