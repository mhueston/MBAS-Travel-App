from flask import Flask

from flask import render_template

from flask import request

from flask import jsonify

from MBAS_Travel_Planner import Travel_Planner

app = Flask(__name__)

@app.route('/')

def index():
    
    """
    Renders the index page of the application.
    
    This function is called when the user accesses the root URL of the application.
    It renders the 'index.html' template for display to the user.

    Returns:
        Rendered HTML template for the index page.
    """
    return render_template('index.html')

@app.route('/create_package', methods=['POST'])

def create_package():
    
    """
    Creates a travel package based on user input and returns related details.

    This function accepts a POST request with JSON data, which includes the user's 
    country, city, origin, dates, and price preferences. It uses the Travel_Planner 
    class to gather information about flights, hotels, weather, and events, then returns 
    a JSON response with this data.

    Parameters:
        request.json (dict): A JSON object containing user inputs for country, city, 
                              origin, start date, end date, flight price max, 
                              and hotel price max.

    Returns:
        jsonify (dict): A JSON response containing the travel package details, including
                        country, flight information, hotel information, weather information,
                        and event information.
    """
    
    data = request.json
    
    planner = Travel_Planner()
    
    planner.country_name = data['country']
    
    planner.city = data['city']
    
    planner.origin = data['origin']
    
    planner.start_date = data['start_date']
    
    planner.end_date = data['end_date']
    
    planner.flight_price_max = float(data['flight_price_max'])
    
    planner.hotel_price_max = float(data['hotel_price_max'])
    
    planner.destination = planner.airport_codes[planner.country_name]
    
    planner.gl = planner.country_codes[planner.country_name]

    planner.retreive_flight_data()
    
    hotel_data = planner.retreive_hotel_data()
    
    weather_data = planner.retreive_weather_data()
    
    events = planner.retreive_event_data()
    
    response = {
        "country": planner.country_name,
        
        "flight_info": planner.flight_results,
        
        "hotel_info": hotel_data,
        
        "weather_info": weather_data,
        
        "events": events
    }
    
    return jsonify(response)

@app.route('/package')

def package():
    
    """
    Renders the travel package details page.

    This function is called when the user accesses the '/package' route. It renders
    the 'package.html' template for displaying the travel package information.

    Returns:
        Rendered HTML template for the package page.
    """
    return render_template('package.html')
