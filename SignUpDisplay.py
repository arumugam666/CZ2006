import streamlit as st
from User import User
from hashlib import sha256
import requests


class SignUpDisplay:

    def renderDisplay(self):
        st.markdown('# SIGN UP')
        userName = st.text_input("Username")
        loginEmail = st.text_input("Login Email")
        updateEmail = st.text_input("Update Email")
        password = st.text_input("Input Password",type = "password")
        passwordHash = sha256(password.encode('utf-8')).hexdigest()
        rePassword = st.text_input("Retype Password",type = "password")
        rePasswordHash = sha256(rePassword.encode('utf-8')).hexdigest()
        if passwordHash != rePasswordHash:
            st.write("Passwords don't match!")
        updateFrequency = st.slider('Update Frequency', min_value=0, max_value=10)
        updateConfidence = st.slider('Update Confidence Level', min_value=85, max_value=95)
        if st.button('Submit'):
            payload = {}
            headers= {}
            url = "https://us-central1-cz2006-9cd2d.cloudfunctions.net/app/checkUserName/"+userName
            response = requests.request("GET", url, headers=headers, data = payload)
            if not response.json()["present"] and passwordHash == rePasswordHash:
                user = User(userName,loginEmail,passwordHash,updateEmail,updateFrequency,updateConfidence)
                user.postUser()
            else:
                st.write("That username is taken.")
                return False
            return True
        else:
            return False


if __name__ == "__main__":
    SignUpDisplay().renderDisplay()