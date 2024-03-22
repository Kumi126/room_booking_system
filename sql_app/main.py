from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import List
from . import schemas, models, crud
from .database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close()

# @app.get('/')
# async def index():
#     return ({'message':'Success'})

@app.get('/users', response_model=List[schemas.User])
async def reaad_users(skip: int = 0, limit:int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return (users)

@app.get('/rooms', response_model=List[schemas.Room])
async def rooms(skip: int = 0, limit:int = 100, db:Session = Depends(get_db)):
    rooms = crud.get_rooms(db, skip=skip, limit=limit)
    return (rooms)

@app.get('/bookings', response_model=List[schemas.Booking])
async def bookings(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    bookings = crud.get_bookings(db, skip=skip, limit=limit)
    return (bookings)


@app.post('/users', response_model=schemas.User)
async def create_users(user: schemas.User, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

@app.post('/rooms', response_model=schemas.Room)
async def rooms(room: schemas.User, db: Session = Depends(get_db)):
    return crud.create_room(db, room)

@app.post('/bookings', response_model=schemas.Booking)
async def bookings(booking: schemas.User, db: Session = Depends(get_db)):
    return crud.create_booking(db, booking)

