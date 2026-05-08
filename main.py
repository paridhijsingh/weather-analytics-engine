from fastapi import FastAPI, HTTPException, Depends
import httpx
from models import WeatherRequest
from database import SessionLocal, WeatherLog
from sqlalchemy.orm import Session

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Initialize the OpenAI client
# API Key is stored in the .env file

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()

def get_ai_recommendation(city: str, temperature: float, description: str):
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a sophisticated AI Weather Consultant. "
                        "Provide personalized, high-value advice based on current weather conditions. "
                        "Consider health, productivity, travel, and mood. "
                        "Tailor your tone to be helpful and insightful for a general audience."
                    ),
                },
                {
                    "role": "user",
                    "content": (
                        f"The weather in {city} is {temperature}°C and {description}. "
                        "Provide a brief, helpful recommendation for my day."
                    ),
                },
            ],
            temperature=0.7,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Currently unable to reach the AI brain, but stay safe! (Error: {e})"


@app.post("/weather")
async def get_weather(request: WeatherRequest, db: Session = Depends(get_db)):
    async with httpx.AsyncClient() as http_client:
        # API Key
        API_KEY = "56cf2ee354898fcc67db50143a5d3fec"

        async with httpx.AsyncClient() as client:
            try: 
                url = f"https://api.openweathermap.org/data/2.5/weather?q={request.city}&appid={API_KEY}&units={request.units}"
                response = await client.get(url)
                response.raise_for_status()
                data = response.json()

                current_temp = data['main']['temp']
                weather_desc = data['weather'][0]['description']

                new_log = WeatherLog(city=request.city, temperature=current_temp)
                db.add(new_log)
                db.commit()

                recommendation = get_ai_recommendation(request.city, current_temp, weather_desc)

                return {
                    "message": request.city,
                    "current_temp": current_temp,
                    "weather_desc": weather_desc,
                    "ai_advice": recommendation
                }
            except httpx.HTTPStatusError as e:
                raise HTTPException(status_code=e.response.status_code, detail="City not found or API error")
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))

@app.get("/")   
def hello_world():
    return {"message": "Hello World"}