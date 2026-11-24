import requests
import json

api_key = "dfc92b069ec7442ad3f227aea7aa0d8d"

def get_weather():
    city_name = input("Enter city name: ").lower()
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
    
    response = requests.get(url, timeout=30)
    
    try:
        if response.status_code == 200:
            
            data = response.json()
            
            weather = data["weather"][0]["main"]
            weather_description = data["weather"][0]["description"]
            temperature = round((data["main"]["temp"] - 273.15), 2)
            
            print(f"City Name: {city_name}")
            print(f"Weather: {weather}, {weather_description}")
            print(f"Temperature: {temperature}℃")
            
            
            try:
                with open("weather_records/records.txt", "w", encoding="utf-8") as f:
                    f.write(f"City Name: {city_name}\n")
                    f.write(f"Weather: {weather}, {weather_description}\n")
                    f.write(f"Temperature: {temperature}℃\n")
                    
            except Exception as e:
                print(f"Error: {e}")
                
            else:
                print("Weather record fetched..")
            
            try:
                with open("weather_records/data.json", "w") as f:
                    r = json.dumps(data)
                    f.write(r)
                    
            except Exception as e:
                print(f"Error: {e}")
                
            else:
                print("Record Updated")
            
        else:
            print("Cannot fetch weather data")
            
    except requests.RequestException as exc:
        print("Error:", exc)

if __name__ == "__main__":
    get_weather()
