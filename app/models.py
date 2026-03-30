from pydantic import BaseModel

class IoTData(BaseModel):
    device_id: str
    activity: str
    duration: int
    heart_rate: int | None = None
    location: str | None = "home"
    role: str = "caregiver"
