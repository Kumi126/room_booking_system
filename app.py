import streamlit as st
import requests
import json
import random
import datetime

page = st.sidebar.selectbox('Choose your page',['users','rooms','bookings'])

def submit_request(endpoint, data):
    url = f'http://127.0.0.1:8000/{endpoint}/'
    res = requests.post(url, json.dumps(data))
    st.write(res.text)

if page == 'users':
    st.title('API test (users)')

    with st.form(key='user'):
        user_id: int = random.randint(0,10)
        username: str = st.text_input('username', max_chars=12)
        data = {
            'user_id': user_id,
            'username': username
        }
        
        submit_button = st.form_submit_button(label='submit to make a request')
        
    if submit_button:
        submit_request('users',data)
        

elif page == 'rooms':
    st.title('API test (rooms)')
    with st.form(key='rooms'):
        room_id: int = random.randint(0,1)
        room_name: str = st.text_input('room name', max_chars=12)
        capacity: int = st.number_input('max people',step=1)
        data = {
            'room_id': room_id,
            'room_name': room_name,
            'capacity': capacity,
        }
        submit_button = st.form_submit_button(label='submit to make a request')
        
    if submit_button:
        submit_request('rooms',data)
        
elif page == 'bookings':
    st.title('API test (bookings)')
    with st.form(key='bookings'):
        booking_id: int = random.randint(0,1)
        user_id: int = random.randint(0,1)
        room_id: int = random.randint(0,1)
        booked_num: int = st.number_input('no of members',step=1)
        date = st.date_input('Date to book',min_value=datetime.date.today())
        start_time = st.time_input('Start time', value=datetime.time(hour=9, minute=0)) 
        end_time =  st.time_input('End time', value=datetime.time(hour=17, minute=0))
        data = {
            'booking_id': booking_id, 
            'user_id': user_id, 
            'room_id': room_id,
            'booked_num': booked_num,
            'start_datetime': datetime.datetime(year=date.year,month=date.month,day=date.day,hour=start_time.hour,minute=start_time.minute).isoformat(),
            'end_datetime': datetime.datetime(year=date.year,month=date.month,day=date.day,hour=end_time.hour,minute=end_time.minute).isoformat(),
        }
        submit_button = st.form_submit_button(label='submit to make a request')
        
    if submit_button:
        submit_request('bookings',data)
    