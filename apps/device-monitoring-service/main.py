from fastapi import FastAPI
from typing import List
from pydantic import BaseModel
import datetime
import random

app = FastAPI()

class Telemetry(BaseModel):
    id: int
    data: str
    receiveDate: datetime.date
    deviceID: int

@app.get("/ping")
def ping():
    return {"message": "device-monitoring-service: pong"}

@app.get("/devices/{device_id}/telemetry", response_model=List[Telemetry])
def get_telemetry(device_id: int):
    telemetry = []
    for i in range(3):
        telemetry.append(Telemetry(
            id=i,
            data=f"temperature:{random.uniform(20,25):.1f}°C",
            receiveDate=datetime.date.today(),
            deviceID=device_id
        ))
    return telemetry