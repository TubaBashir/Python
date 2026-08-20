import requests

city = input("Enter city name: ")
# wttr.in format '?format=3' returns a simplified, text-based weather string
url = f"https://wttr.in{city}?format=3"

try:
    response = requests.get(url)
    print(response.text.strip())
except Exception as e:
    print("Could not retrieve weather information.")
