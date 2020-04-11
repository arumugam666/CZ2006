import streamlit as st
from Model.User import User
from hashlib import sha256
from StreamlitExtras.st_rerun import rerun
class IndividualDisplay:

    def __init__(self,user):
        self.__user = user

    def renderDisplay(self):
        st.markdown('# PROFILE')
        st.write('## Hello {}!'.format(self.__user.getUserName()))
        st.write('Email Id: {}'.format(self.__user.getLoginEmail()))
        st.markdown('## Interested Stocks')
        watchlist = self.__user.getWatchList()
        buttons = []
        if watchlist:
            for stock in watchlist:
                st.markdown('### '+stock.upper())
                buttons.append(st.button('Remove '+stock.upper()))
            for ind,buttonBool in enumerate(buttons):
                if buttonBool:
                    self.__user.removeStockFromWatchList(ind)
                    self.__user.postUser()
                    rerun()
        else:
            st.markdown("You don't seem to have any Stocks on your watchlist yet")
        st.markdown('## Latest news sent to')
        st.write(self.__user.getUpdateEmail())
        st.write('Update Frequency','< {}'.format(self.__user.getUpdateFrequency()))
        st.write('Update Confidence Level','> {}'.format(self.__user.getUpdateConfidence()))
        if st.button('Edit Profile'):
            return True
        else:
            return False


if __name__ == "__main__":
    user = User('Aru','arumugam123456789@gmail.com',sha256('1'.encode('utf-8')).hexdigest(),'arumugam123456789@gmail.com',1,1)

    IndividualDisplay(user).renderDisplay()