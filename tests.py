import unittest
from unittest.mock import patch, MagicMock
from MBAS_Travel_Planner import Travel_Planner

class TestTravelPlanner(unittest.TestCase):
    def setUp(self):
        """Set up the Travel_Planner object for tests."""
        self.planner = Travel_Planner()

    @patch("MBAS_Travel_Planner.input", side_effect=[
        "Brazil", "Rio de Janeiro", "JFK", "2024-12-15", "2024-12-22", "500", "150"
    ])
    def test_get_user_input(self, mock_input):
        """Test if user inputs are correctly captured."""
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
        """Test flight data retrieval."""
        # Mock the flight database
        mock_outbound = MagicMock()
        mock_inbound = MagicMock()
        mock_outbound.get_flight_results.return_value = ["Flight A", "Flight B"]
        mock_inbound.get_flight_results.return_value = ["Flight C", "Flight D"]
        mock_flight_db.side_effect = [mock_outbound, mock_inbound]

        # Set necessary attributes for the method
        self.planner.origin = "JFK"
        self.planner.destination = "GRU"
        self.planner.start_date = "2024-12-15"
        self.planner.end_date = "2024-12-22"
        self.planner.country_name = "Brazil"  # This attribute was missing

        # Call the method under test
        self.planner.retreive_flight_data()

        # Assert the expected results
        self.assertIn("Your flights to Brazil:", self.planner.flight_results)
        self.assertIn("Flight A", self.planner.flight_results)
        self.assertIn("Flight D", self.planner.flight_results)

    @patch("MBAS_Travel_Planner.hotel_databases.HotelDatabase")
    def test_retreive_hotel_data(self, mock_hotel_db):
        """Test hotel data retrieval."""
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
        """Test weather data retrieval."""
        mock_season_checker = MagicMock()
        mock_season_checker.get_season.return_value = "Sunny weather in December"
        mock_weather_db.return_value = mock_season_checker

        self.planner.country_name = "Brazil"
        self.planner.start_date = "2024-12-15"

        result = self.planner.retreive_weather_data()
        self.assertEqual(result, "Sunny weather in December")

    @patch("MBAS_Travel_Planner.travel_locations.PlaceScraper")
    def test_retreive_event_data(self, mock_place_scraper):
        """Test event data retrieval."""
        mock_scraper = MagicMock()
        mock_scraper.get_places_for_country.return_value = ["Place A", "Place B"]
        mock_place_scraper.return_value = mock_scraper

        self.planner.country_name = "Brazil"

        result = self.planner.retreive_event_data()
        self.assertEqual(result, ["Place A", "Place B"])

if __name__ == "__main__":
    unittest.main()
