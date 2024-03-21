import requests
from sqlalchemy.orm import Session
from . import models, schemas ## . means from the same directly

## get 100 data from each database table
def get_users(db: Session, skip:int = 0, limit: int = 100):
    ## offset skip means numbers of data to skip to refer
    return db.query(models.User).offset(skip).limit(limit).all()

def get_rooms(db: Session, skip:int = 0, limit: int = 100):
    return db.query(models.Room).offset(skip).limit(limit).all()

def get_bookings(db: Session, skip:int = 0, limit: int = 100):
    return db.query(models.Booking).offset(skip).limit(limit).all()


## resister a user
def create_user(db: Session, user:schemas.User):
    db_user = models.User(username=user.username) ## build instance
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

## resister a room
def create_room(db: Session, room:schemas.Room):
    db_room = models.Room(room_name=room.room_name, capacity=room.capacity) ## build instance
    db.add(db_room)
    db.commit()
    db.refresh(db_room)
    return db_room

## resister booking
def create_booking(db: Session, booking:schemas.Booking):
    db_booking = models.Booking(
        room_id = booking.room_id,
        user_id = booking.user_id,
        booked_num = booking.booked_num,
        start_datetime = booking.start_datetime,
        end_datetime = booking.end_datetime
    ) ## build instance
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking