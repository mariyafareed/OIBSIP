#Project title: BASIC WEATHER APP
import requests

def get_weather(api_key, location): # funtn to fetch weather data from OpenWeatherMap API
   
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def display_weather(data): #functn to display weather data
   
    if data:
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']
        city = data['name']
        
        print(f"Weather in {city}:")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {description.capitalize()}")
    else:
        print("Error fetching weather data. Please check the location or try again later.")

def main(): #main funtn to run the weather data
    
    api_key = input("Enter your OpenWeatherMap API key: ") #enter the api key 
    location = input("Enter the city name: ") #enter city name
    weather_data = get_weather(api_key, location)
    display_weather(weather_data)

if __name__ == "__main__":
    main()
