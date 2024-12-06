import requests
from bs4 import BeautifulSoup as bs

class PlaceScraper:
    def __init__(self, url):
        self.url = url
        self.places_by_country = {}

    def scrape_places(self):
        """
        Scrapes the places to visit from the given URL and organizes them by country.
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
        return self.places_by_country.get(country_name, [])
