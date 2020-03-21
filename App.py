import streamlit as st
from SidebarDisplay import SidebarDisplay
from SearchDisplay import SearchDisplay
from LoginDisplay import LoginDisplay
from User import User
from hashlib import sha256

def myApp():
    sidebar = SidebarDisplay()
    sidebar.renderDisplay()
    currentPage = sidebar.getSelectedOption()
    if currentPage == "Home":
        SearchDisplay().renderDisplay()
    elif currentPage == "Login":
        user = User('Aru','arumugam123456789@gmail.com',sha256('1'.encode('utf-8')).hexdigest(),'',1,1)
        LoginDisplay(user).renderDisplay()

if __name__ == "__main__":
    myApp()