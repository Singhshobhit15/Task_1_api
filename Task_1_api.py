import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def get_weather_data(lat, lon, cnt, api_key):
    api_key = "056a9df7e29ff239aad589c254e564c2"  # Replace with the active API key

# Example API call with the new API key:
    url = f"https://api.openweathermap.org/data/2.5/forecast/daily?lat={lat}&lon={lon}&cnt={cnt}&appid={api_key}&units=metric"

    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None

def process_weather_data(data):
    """Processes weather data into a pandas DataFrame."""
    dates = []
    temperatures = []
    for entry in data['list']:
        dates.append(pd.to_datetime(entry['dt'], unit='s'))  # Convert timestamp to datetime
        temperatures.append(entry['temp']['day'])  # Extract the daytime temperature
    
    # Create DataFrame
    df = pd.DataFrame({'Date': dates, 'Temperature': temperatures})
    return df

def plot_weather_data_seaborn(df):
    """Creates a plot of the weather data using Seaborn."""
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='Date', y='Temperature', data=df, marker='o', color='b')
    plt.title("7-Day Weather Forecast")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Main Execution
if __name__ == "__main__":
    # Coordinates for London (you can change this to any location)
    lat = 51.5074  # Latitude for London
    lon = -0.1278  # Longitude for London
    cnt = 7  # Number of days in the forecast
    api_key = "your_api_key_here"  # Replace with your actual OpenWeatherMap API key
    
    # Fetch the weather data
    data = get_weather_data(lat, lon, cnt, api_key)

    if data:
        # Process the data into a DataFrame
        weather_df = process_weather_data(data)
        # Visualize the data
        plot_weather_data_seaborn(weather_df)
