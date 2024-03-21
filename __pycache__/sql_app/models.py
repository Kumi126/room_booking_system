from sqlalchemy import Column, ForeignKey, String, Integer,DateTime
from .database import Base

class User(Base):
    __tablename__ = 'users' ##create table from Base
    user_id = Column(Integer, primary_key=True, index=True) ## type hint is specifc in sqlalchmey syntax
    username = Column(String, unique=True, index=True)
    
class Room(Base):
    __tablename__ =  'rooms' ##create table from Base
    room_id = Column(Integer, primary_key=True, index=True) ## type hint is specifc in sqlalchmey syntax
    room_name = Column(String, unique=True, index=True)
    capacity = Column(Integer)
    
class Booking(Base):
    __tablename__ =  'bookings' ##create table from Base
    booking_id = Column(Integer, primary_key=True, index=True) 
    user_id = Column(Integer, ForeignKey('users.user_id',ondelete='SET NULL'), nullable=False) ## ForeignKey is to link to column from user
    room_id = Column(Integer, ForeignKey('rooms.user_id',ondelete='SET NULL'), nullable=False) ## ForeignKey is to link to column from user
    booked_num = Column(Integer, nullable=False)
    start_datetime = Column(DateTime, nullable=False)
    end_datetime = Column(DateTime, nullable=False)