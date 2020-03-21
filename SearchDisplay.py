import streamlit as st

class SearchDisplay:

    @staticmethod
    def search(stockName, t, numOfArticles):
        return results

    @staticmethod
    def displayResults(results):
        print('gg')

    @staticmethod
    def renderDisplay():
        timeRange = st.selectbox("Select Time Range",('Last Hour', 'Last Day', 'Last Week'))
        numOfArticles = st.slider("Select number of articles")
        stockName = st.text_input("Please enter the stock name here")
        searchResults = self.search(stockName,timeRange,numOfArticles)
        self.displayResults(searchResults)

SearchDisplay().renderDisplay()