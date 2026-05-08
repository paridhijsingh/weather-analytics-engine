from pydantic import BaseModel

class WeatherRequest(BaseModel):
    city: str
    units: str = "metric"
    user_id: int

