import requests
from bs4 import BeautifulSoup

def scrape_places_to_visit(url, country_name):
    """
    Scrapes the places to visit in the specified country from the given URL.
    
    Args:
        url: The URL of the webpage to scrape.
        country_name: The name of the country to filter results for.
    
    Returns:
        A list of places to visit in the specified country.
    """
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to fetch the webpage")
        return {}

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # List to store places in the specified country
    places_in_country = []

    # Find all span elements with the class "mntl-sc-block-heading__text"
    headings = soup.find_all('span', class_='mntl-sc-block-heading__text')
    
    for heading in headings:
        text = heading.text.strip()
        
        # Split the text into place and country (e.g., "Jardín, Antioquia, Colombia")
        parts = text.split(",")
        if len(parts) >= 2:  # Ensure there are at least a place and a country
            place = parts[0].strip()  # Extract the place name
            country = parts[-1].strip()  # Extract the country name
            
            # If the country matches the given parameter, add the place to the list
            if country.lower() ==  country_name.lower():
                places_in_country.append(place)

    return places_in_country


#if __name__ == "__main__":
#    url = "https://www.travelandleisure.com/best-places-to-visit-in-south-america-7974457"
#    country_name = "Colombia" # Specify the country you want to filter by
#    places = scrape_places_to_visit(url, country_name)

    # Print the scraped data
#    print(f"Places to Visit in {country_name}:")
#    for place in places:
#        print(f"  - {place}")
