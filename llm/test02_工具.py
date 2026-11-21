import httpx

def get_weather(latitude, longitude):
    response = httpx.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code")
    data = response.json()
    return f"{data['current']['temperature_2m']}℃"
