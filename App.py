import streamlit as st
from SearchDisplay import SearchDisplay
from LoginDisplay import LoginDisplay
from User import User
from hashlib import sha256
import SessionState

def App():
    session_state = SessionState.get(loggedIn = False,selectedOption = "Home",user = None)

    user = User('Aru','arumugam123456789@gmail.com',sha256('1'.encode('utf-8')).hexdigest(),'',1,1)
    if session_state.loggedIn:
        st.sidebar.markdown("Welcome, {}!".foramt(user.getUsername()))
        profileButton = st.sidebar.button("Profile")
        if profileButton:
            session_state.selectedOption = "Profile"
    else:
        loginButton = st.sidebar.button("Login")
        if loginButton:
            session_state.selectedOption = "Login"
            user = User('Aru','arumugam123456789@gmail.com',sha256('1'.encode('utf-8')).hexdigest(),'',1,1)


    homeButton = st.sidebar.button("Home")
    if homeButton:
        session_state.selectedOption = "Home"

    if session_state.selectedOption == "Login":
        print(LoginDisplay(user).renderDisplay())
    elif session_state.selectedOption == "Home":
        SearchDisplay().renderDisplay()

App()