import unittest
from unittest.mock import patch, MagicMock
from MBAS_Travel_Planner import Travel_Planner

class TestTravelPlanner(unittest.TestCase):
    
    """
    Unit tests for the Travel_Planner class.

    This test suite validates the functionality of the Travel_Planner class by mocking
    dependencies and ensuring methods behave as expected based on input and data retrieval logic.
    """
    
    def setUp(self):
        
        """
        Sets up the Travel_Planner instance for each test case.
        
        This method initializes a Travel_Planner object to ensure a consistent state for testing.
        """
        
        self.planner = Travel_Planner()

    @patch("MBAS_Travel_Planner.input", side_effect=[
        "Brazil", "Rio de Janeiro", "JFK", "2024-12-15", "2024-12-22", "500", "150"
    ])
    
    def test_get_user_input(self, mock_input):
        
        """
        Tests the get_user_input method for correctly capturing and storing user inputs.
        
        Mock input is used to simulate user responses, and assertions validate 
        that the attributes of the Travel_Planner instance are correctly set.
        """
        
        self.planner.get_user_input()
        
        self.assertEqual(self.planner.country_name, "Brazil")
        
        self.assertEqual(self.planner.city, "Rio de Janeiro")
        
        self.assertEqual(self.planner.origin, "JFK")
        
        self.assertEqual(self.planner.start_date, "2024-12-15")
        
        self.assertEqual(self.planner.end_date, "2024-12-22")
        
        self.assertEqual(self.planner.flight_price_max, 500)
        
        self.assertEqual(self.planner.hotel_price_max, "150")
        
        self.assertEqual(self.planner.destination, "GRU")
        
        self.assertEqual(self.planner.gl, "br")

    @patch("MBAS_Travel_Planner.flight_database.FlightDatabase")
    
    def test_retreive_flight_data(self, mock_flight_db):
        
        """
        Tests the retreive_flight_data method to ensure correct handling of flight data retrieval.

        Mock objects simulate the behavior of the FlightDatabase class, allowing
        validation of flight results formatting and inclusion in the planner's output.
        """
        
        # Mock the flight database
        mock_outbound = MagicMock()
        
        mock_inbound = MagicMock()
        
        mock_outbound.get_flight_results.return_value = ["Flight A", "Flight B"]
        
        mock_inbound.get_flight_results.return_value = ["Flight C", "Flight D"]
        
        mock_flight_db.side_effect = [mock_outbound, mock_inbound]

        self.planner.origin = "JFK"
        
        self.planner.destination = "GRU"
        
        self.planner.start_date = "2024-12-15"
        
        self.planner.end_date = "2024-12-22"
        
        self.planner.country_name = "Brazil" 

        self.planner.retreive_flight_data()

        self.assertIn("Your flights to Brazil:", self.planner.flight_results)
        
        self.assertIn("Flight A", self.planner.flight_results)
        
        self.assertIn("Flight D", self.planner.flight_results)

    @patch("MBAS_Travel_Planner.hotel_databases.HotelDatabase")
    
    def test_retreive_hotel_data(self, mock_hotel_db):
        
        """
        Tests the retreive_hotel_data method to validate hotel data retrieval.

        Mock objects simulate the behavior of the HotelDatabase class, testing that 
        the returned hotel data matches the expected formatted string.
        """
        
        mock_hotel_instance = MagicMock()
        
        mock_hotel_instance.get_hotels.return_value = {"Hotel1": "Details"}
        
        mock_hotel_instance.display.return_value = "Hotel Details"

        mock_hotel_db.return_value = mock_hotel_instance

        self.planner.city = "Rio de Janeiro"
        
        self.planner.gl = "br"
        
        self.planner.start_date = "2024-12-15"
        
        self.planner.end_date = "2024-12-22"
        
        self.planner.hotel_price_max = 150

        result = self.planner.retreive_hotel_data()
        
        self.assertEqual(result, "Hotel Details")

    @patch("MBAS_Travel_Planner.weather_database.SouthAmericaSeasons")
    
    def test_retreive_weather_data(self, mock_weather_db):
        
        """
        Tests the retreive_weather_data method for correct seasonal weather retrieval.

        Mock objects simulate the behavior of the SouthAmericaSeasons class,
        ensuring the returned weather matches expectations based on input parameters.
        """
        
        mock_season_checker = MagicMock()
        
        mock_season_checker.get_season.return_value = "Sunny weather in December"
        
        mock_weather_db.return_value = mock_season_checker

        self.planner.country_name = "Brazil"
        
        self.planner.start_date = "2024-12-15"

        result = self.planner.retreive_weather_data()
        
        self.assertEqual(result, "Sunny weather in December")

    @patch("MBAS_Travel_Planner.travel_locations.PlaceScraper")
    
    def test_retreive_event_data(self, mock_place_scraper):
        
        """
        Tests the retreive_event_data method to validate event data retrieval.

        Mock objects simulate the behavior of the PlaceScraper class, ensuring 
        the returned events match the expected list for the specified country.
        """
        
        mock_scraper = MagicMock()
        
        mock_scraper.get_places_for_country.return_value = ["Place A", "Place B"]
        
        mock_place_scraper.return_value = mock_scraper

        self.planner.country_name = "Brazil"

        result = self.planner.retreive_event_data()
        
        self.assertEqual(result, ["Place A", "Place B"])

if __name__ == "__main__":
    
    unittest.main()
