import requests
from bs4 import BeautifulSoup

def scrape_places_to_visit(url):
    """
    Scrapes the names of South American countries and the places to visit from the given URL.
    
    Args:
        url: The URL of the webpage to scrape.
    
    Returns:
        A dictionary where keys are country names and values are lists of places to visit.
    """
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to fetch the webpage")
        return {}

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Dictionary to store countries and their places
    travel_data = {}

    # Find all span elements with the class "mntl-sc-block-heading__text"
    headings = soup.find_all('span', class_='mntl-sc-block-heading__text')
    
    for heading in headings:
        text = heading.text.strip()
        
        # Split the text into place and country (e.g., "Jardín, Antioquia, Colombia")
        parts = text.split(",")
        if len(parts) >= 2:  # Ensure there are at least a place and a country
            place = parts[0].strip()  # Extract the place name
            country = parts[-1].strip()  # Extract the country name
            
            # Add the place to the corresponding country in the dictionary
            if country not in travel_data:
                travel_data[country] = []
            travel_data[country].append(place)

    return travel_data


if __name__ == "__main__":
    url = "https://www.travelandleisure.com/best-places-to-visit-in-south-america-7974457"
    travel_data = scrape_places_to_visit(url)

    # Print the scraped data
    for country, places in travel_data.items():
        print(f"{country}:")
        for place in places:
            print(f"  - {place}")
