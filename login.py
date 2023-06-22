import pyrebase
import streamlit as st
import hashlib
from streamlit_extras.switch_page_button import switch_page


st.set_page_config(page_title='Budget',initial_sidebar_state='collapsed')
no_sidebar_style = """
    <style>
        div[data-testid="stSidebarNav"] {display: none;}
    </style>
"""
st.markdown(no_sidebar_style, unsafe_allow_html=True)


firebaseConfig = {
    "apiKey": "AIzaSyChbWNVaBa2PBUO9PI-Z3atqntALcyWFrU",
    "authDomain": "nawe-dubai.firebaseapp.com",
    "projectId": "nawe-dubai",
    "databaseURL": "https://nawe-dubai-default-rtdb.europe-west1.firebasedatabase.app/",
    "storageBucket": "nawe-dubai.appspot.com",
    "messagingSenderId": "486183160293",
    "appId": "1:486183160293:web:c5c9de99dd13d8a48d870c",
    "measurementId": "G-68JY17EMDF"
  }

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

db = firebase.database()
storage = firebase.storage()

st.title("Welcome to NAWE DUBAI Consultancy Intelligence Platform")

choice = st.radio('New to NAWE Dubai? Then please signup.', ['Login', 'Signup'])

email = st.text_input('Please provide the Email address')
password = st.text_input('Input Password', type='password')

if choice == 'Signup':
    switch_page('form')

if choice == 'Login':
    login = st.checkbox('login')
    if login:
        user = auth.sign_in_with_email_and_password(email, password)
        if user:
            st.success('Login successful!')
            st.success('Login successful!')
            # Store user session
            st.session_state.user = user
            switch_page('main')
        else:
            st.error('Invalid email or password. Please try again.')