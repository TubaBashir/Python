import requests

def get_live_weather(lat, lon):
    # 1. Target URL for the free Open-Meteo API
    url = f"https://open-meteo.com{lat}&longitude={lon}&current_weather=True"
    
    try:
        # 2. Send HTTP request to download data
        response = requests.get(url)
        data = response.json()
        
        # 3. Parse JSON results
        if "current_weather" in data:
            current = data["current_weather"]
            temp = current["temperature"]
            windspeed = current["windspeed"]
            time_stamp = current["time"]
            
            print("\n☀️ Live Weather Prediction Report ☀️")
            print(f"Timestamp:   {time_stamp}")
            print(f"Temperature: {temp}°C")
            print(f"Wind Speed:  {windspeed} km/h")
        else:
            print("Could not retrieve data for those coordinates.")
            
    except requests.exceptions.RequestException as e:
        print(f"Connection Error: {e}")

# Example coordinates (Lat/Lon for Jammu: 32.7266, 74.8570)
get_live_weather(32.7266, 74.8570)
