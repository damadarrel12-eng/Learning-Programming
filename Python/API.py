import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
def get_capital(country: str)-> str:
    data = {
        "cameroon": "Yaoundé",
        "nigeria": "Abuja"
    }
    return data.get(country.lower(), "Capital not found")

def get_weather(city: str)-> str:
    data = {
        "yaounde": "28°C, Kinda cloudy",
        "abuja": "32°C, Sunny"
    }
    city = city.lower().replace("é", "e").replace("è", "e").replace("ê", "e").replace("ë", "e")
    return data.get(city, "Weather not found")
response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents="What is the capital of CAMEROON  ? And its weather?",
    config={"tools": [get_capital, get_weather]}
)

print(response.candidates[0].content.parts)