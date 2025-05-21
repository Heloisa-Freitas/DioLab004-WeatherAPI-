from fastapi import FastAPI
from datetime import datetime, timedelta
import random

app = FastAPI()

summaries = [
    "Freezing", "Bracing", "Chilly", "Cool", "Mild",
    "Warm", "Balmy", "Hot", "Sweltering", "Scorching"
]

@app.get("/weatherforecast")
def get_forecast():
    forecast = []
    for i in range(5):
        forecast.append({
            "date": (datetime.now() + timedelta(days=i)).strftime("%Y-%m-%d"),
            "temperatureC": random.randint(-20, 35),
            "summary": random.choice(summaries)
        })
    return forecast
