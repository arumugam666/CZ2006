import streamlit as st
from User import User
from hashlib import sha256

class EditProfileDisplay:

    def __init__(self,user):
        self.__user = user

    def renderDisplay(self):
        st.markdown('# EDIT PROFILE')
        st.write("Username:", self.__user.getUserName())
        st.write("Login Email", self.__user.getLoginEmail())
        st.markdown('## Interested Stocks')
        watchlist = self.__user.getWatchList()
        if watchlist:
            for stock in watchlist:
                st.markdown(stock.name)
        else:
            st.markdown("You don't seem to have any Stocks on your watchlist yet")
        st.markdown('## Latest news sent to')
        updateEmail = st.text_input("Update Email", value=self.__user.getUpdateEmail())
        updateFrequency = st.slider('Update Frequency', min_value=0, max_value=10, value=self.__user.getUpdateFrequency())
        updateConfidence = st.slider('Update Confidence Level', min_value=85, max_value=95, value=self.__user.getUpdateConfidence())
        if st.button('Submit'):
            self.__user.setUpdateEmail(updateEmail)
            self.__user.setUpdateFrequency(updateFrequency)
            self.__user.setUpdateConfidence(updateConfidence)
            self.__user.postUser()
            return True
        else:
            return False


if __name__ == "__main__":
    user = User('Aru','arumugam123456789@gmail.com',sha256('1'.encode('utf-8')).hexdigest(),'arumugam123456789@gmail.com',1,1)

    EditProfileDisplay(user).renderDisplay()