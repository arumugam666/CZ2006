import streamlit as st
from User import User

class SidebarDisplay:
    def __init__(self):
        self.__loggedIn = False
        self.__user = None
        self.__selectedOption = "Home"
    
    def setUser(self,user):
        self.__loggedIn = True
        self.__user = user

    def getSelectedOption(self):
        return self.__selectedOption
    
    def setSelectedOption(self,option):
        self.__selectedOption = option

    def renderDisplay(self):
        if self.__loggedIn:
            st.sidebar.markdown("Welcome, {}!".foramt(self.__user.getUsername()))
            profileButton = st.sidebar.button("Profile")
            if profileButton:
                self.__selectedOption = "Profile"
        else:
            loginButton = st.sidebar.button("Login")
            if loginButton:
                self.__selectedOption = "Login"
        
        homeButton = st.sidebar.button("Home")
        if homeButton:
            self.__selectedOption = "Home"

if __name__ == '__main__':
    SidebarDisplay().renderDisplay()