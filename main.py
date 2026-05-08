from fastapi import FastAPI, HTTPException, Depends
import httpx
from models import WeatherRequest
from database import SessionLocal, WeatherLog
from sqlalchemy.orm import Session
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()

def get_ai_recommendation(temperature: float, description: str):
    if "rain" in description.lower():
        return f"It's {temperature}° and raining. Grab an umbrella and maybe a waterproof shell. "
    elif temperature < 60:
        return f"Chilly at {temperature}°. A heavy jacket is definitely recommended. "
    elif temperature > 80 and "clear" in description.lower():
        return "It's a hot, sunny day! Stay hydrated and wear sunscreen."
    else:
        return f"The weather is {description} at {temperature}°. Stay hydrated and wear sunscreen."
        

@app.post("/weather")
async def get_weather(request: WeatherRequest, db: Session = Depends(get_db)):
    async with httpx.AsyncClient() as client:
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

                recommendation = get_ai_recommendation(current_temp, weather_desc)

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