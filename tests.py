import unittest
from unittest.mock import patch, MagicMock
from MBAS_Travel_Planner import Travel_Planner  # Adjust the import path as needed

class TestTravelPlanner(unittest.TestCase):
    
    def setUp(self):
        """Set up a Travel_Planner instance for testing."""
        self.planner = Travel_Planner()

    @patch("builtins.input", side_effect=["JFK", "LAX", "2024-12-01", "2024-12-10", "500", "150"])
    def test_get_user_input(self, mock_input):
        """Test that user input is correctly stored in attributes."""
        self.planner.get_user_input()
        self.assertEqual(self.planner.origin, "JFK")
        self.assertEqual(self.planner.destination, "LAX")
        self.assertEqual(self.planner.start_date, "2024-12-01")
        self.assertEqual(self.planner.end_date, "2024-12-10")
        self.assertEqual(self.planner.flight_price_max, 500.0)
        self.assertEqual(self.planner.hotel_price_max, 150.0)

    @patch("flight_database.FlightDatabase")
    def test_retreive_flight_data(self, MockFlightDatabase):
        """Test flight data retrieval with mock flight database."""
        mock_flight_instance = MagicMock()
        mock_flight_instance.get_flight_results.return_value = "Mock Flight Data"
        MockFlightDatabase.return_value = mock_flight_instance

        self.planner.retreive_flight_data("JFK", "LAX", "2024-12-01", "2024-12-10", 500)
        expected_output = "Mock Flight Data-----------------------------------Mock Flight Data"
        self.assertEqual(self.planner.flight_results, expected_output)

        # Verify the database class is called with correct parameters
        MockFlightDatabase.assert_called_with("JFK", "LAX", "2024-12-01")

    @patch("location_database")
    def test_retreive_event_data(self, MockLocationDatabase):
        """Test event data retrieval with mock location database."""
        mock_event_instance = MagicMock()
        mock_event_instance.search_activities.return_value = "Mock Events Data"
        MockLocationDatabase.return_value = mock_event_instance

        self.planner.retreive_event_data()

        # Verify the database method was called
        mock_event_instance.search_activities.assert_called_once()

    @patch("builtins.print")
    def test_display_travel_package(self, mock_print):
        """Test travel package display functionality."""
        self.planner.flight_results = "Sample Flight Results"
        self.planner.display_travel_package()

        mock_print.assert_called_once_with("Here is your flight information:\nSample Flight Results")

if __name__ == "__main__":
    unittest.main()
