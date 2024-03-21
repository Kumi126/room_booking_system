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


@app.post('/users')
async def users(users: schemas.User):
    return ({'users': users})

@app.post('/rooms')
async def rooms(rooms: schemas.Room):
    return ({'rooms': rooms})

@app.post('/bookings')
async def bookings(bookings: schemas.Booking):
    return ({'bookings': bookings})
