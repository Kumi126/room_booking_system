import datetime
from pydantic import BaseModel, Field
from fastapi import FastAPI


class Booking(BaseModel):
    booking_id: int
    user_id: int
    room_id: int
    booked_num: int
    start_datetime: datetime.datetime
    end_datetime: datetime.datetime
    
    class Config:
        orm_mode = True ## or mapper data will be accepted

class User(BaseModel):
    user_id: int
    username: str = Field(max_length=12)
    
    class Config:
        orm_mode = True ## or mapper data will be accepted
        
class Room(BaseModel):
    room_id: int
    room_name: str = Field(max_length=12)
    capacity: int
    
    class Config:
        orm_mode = True ## or mapper data will be accepted