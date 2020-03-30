import streamlit as st
from SearchDisplay import SearchDisplay
from LoginDisplay import LoginDisplay
from User import User
from hashlib import sha256
import SessionState
from IndividualDisplay import IndividualDisplay
from st_rerun import rerun
from streamlit.ScriptRunner import StopException, RerunException
from streamlit.ScriptRequestQueue import RerunData
from EditProfileDisplay import EditProfileDisplay

def App():
    session_state = SessionState.get(loggedIn = False,selectedOption = "Home",user = None)

    if session_state.loggedIn:
        st.sidebar.markdown("Welcome, {}!".format(session_state.user.getUserName()))

    homeButton = st.sidebar.button("Home")
    if homeButton:
        session_state.selectedOption = "Home"

    if session_state.loggedIn:
        profileButton = st.sidebar.button("Profile")
        if profileButton:
            session_state.selectedOption = "Profile"
        logoutButton = st.sidebar.button("Logout")
        if logoutButton:
            session_state.selectedOption = "Login"
            session_state.loggedIn = False
            rerun()
        
    else:
        loginButton = st.sidebar.button("Login")
        if loginButton:
            session_state.selectedOption = "Login"
        signupButton = st.sidebar.button("Sign Up")
        if signupButton:
            session_state.selectedOption = "Sign Up"


    if session_state.selectedOption == "Login":
        loggedIn,user = LoginDisplay().renderDisplay()
        if loggedIn:
            session_state.loggedIn = loggedIn
            session_state.user = user
            session_state.selectedOption = "Profile"
            rerun()

    elif session_state.selectedOption == "Home":
        SearchDisplay().renderDisplay()

    elif session_state.selectedOption == "Profile":
        if IndividualDisplay(session_state.user).renderDisplay():
            session_state.selectedOption = "Edit Profile"
            rerun()

    elif session_state.selectedOption == "Sign up":
        pass

    elif session_state.selectedOption == "Edit Profile":
        if (EditProfileDisplay(session_state.user).renderDisplay()):
            session_state.selectedOption = "Profile"
            rerun()
App()