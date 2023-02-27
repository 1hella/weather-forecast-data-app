import os

import requests
from dotenv import load_dotenv

load_dotenv()
def get_data(place, days):
    NUM_VALUES_PER_DAY = 8
    api_key = os.getenv("API_KEY")
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    forecasts = data['list']
    num_values = NUM_VALUES_PER_DAY * days
    forecasts = forecasts[:num_values]
    return forecasts

if __name__ == "__main__":
    print(get_data("Vancouver", 5, "Temperature"))