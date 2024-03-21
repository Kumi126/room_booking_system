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


