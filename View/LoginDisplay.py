import streamlit as st
from Model.User import User
from hashlib import sha256
import requests

class LoginDisplay:
    def __init__(self):
        self.submit = False

    # consider using firebase to handle data
    @staticmethod
    def getUser(userName):
        url = "https://us-central1-cz2006-9cd2d.cloudfunctions.net/app/user/"+userName
        headers = {
        'Content-Type': 'application/json',
        'Content-Type': 'application/json'
        }
        response = requests.request("GET", url, headers=headers)
        user = response.json()
        print(user)
        user = User(user["userName"],user["loginEmail"],user["passwordHash"],user["updateEmail"],int(user["updateFrequency"]),int(user["updateConfidence"]),user["watchList"])
        return user

    @staticmethod
    def login(userName,passwordHash):
        url = "https://us-central1-cz2006-9cd2d.cloudfunctions.net/app/verifyPassword"

        payload = payload = "{\r\n\t\"userName\":\""+userName+"\",\r\n\t\"passwordHash\":\""+passwordHash+"\"\r\n}"
        headers = {
        'Content-Type': 'application/json',
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data = payload)
        if response.json()["Verified"]:
            return LoginDisplay.getUser(userName)
        else:
            return False

    def renderDisplay(self):
        st.markdown('# LOGIN')
        username = st.text_input("Username")
        password = st.text_input("Password",type = 'password')
        passwordHash = sha256(password.encode('utf-8')).hexdigest()
        if st.button('Login',key = "loginButton"):
            resultUser = LoginDisplay.login(username,passwordHash)
            if resultUser:
                loggedIn = True
            else:
                loggedIn = False
                resultUser = None
                st.write('## Login failed')
        else:
            return False,None
        return loggedIn,resultUser
        
if __name__ == "__main__":
    f = LoginDisplay()
    # print(f.renderDisplay())
    # st.markdown('# LOGIN')
    # username = st.text_input("Username")
    # password = st.text_input("Password",type = 'password')
    # print(f.login(username,password))
    print(f.renderDisplay())