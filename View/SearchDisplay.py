import streamlit as st
from Controller.SearchController import SearchController
from Controller.PredictionController import PredictionController
from Model.User import User
class SearchDisplay:

    @staticmethod
    def getSearchResults(stockName, t, numOfArticles):
        searchResults = SearchController.search(stockName,t,numOfArticles)
        return PredictionController.predict(searchResults)

    @staticmethod
    def displayResults(stockName,results,user):
        st.write('# '+stockName.upper())
        if user:
            # print(user.getWatchList())
            if stockName in user.getWatchList():
                st.write('## Stock already in watchlist')
                addStock = False
            else:
                addStock = st.button("Add stock to watch list")
                if addStock:
                    user.addStockToWatchList(stockName)
                    print("!!",user.getWatchList())
        else:

            st.write('## Login to add stock to watch list')
            addStock = False
        average = results[1]
        st.write("Average Prediction Value: " + str(average))
        if average >= 0.75:
            st.write("Decision Result: Definitely Buy")
        elif average >= 0.65:
            st.write("Decision Result: Strong Buy")
        elif average >= 0.55:
            st.write("Decision Result: Week Buy")
        elif average > 0.45:
            st.write("Decision Result: Unknown")
        elif average > 0.35:
            st.write("Decision Result: Week Sell")
        elif average > 0.25:
            st.write("Decision Result: Strong Sell")
        else:
            st.write("Definitely Sell")
        st.write(results[0])
        return addStock
        # if results:
        #     st.markdown('# '+results["stockName"])
        #     st.write('## '+results["description"],results["confidenceLevel"])

    def renderDisplay(self,user = None):
        # print(user)
        st.markdown('# HOME')
        timeRange = st.selectbox("Select Time Range",('Last Hour', 'Last Day', 'Last Week', 'Last Year'))
        numOfArticles = st.slider("Select number of articles", value = 5)
        stockName = st.text_input("Please enter the stock name here")
        stockName = stockName.strip()
        stockName = stockName.lower()

        if stockName !="":
            searchResults = self.getSearchResults(stockName,timeRange,numOfArticles)
            return self.displayResults(stockName,searchResults,user)

        return False

if __name__ == "__main__":
    print(SearchDisplay().renderDisplay(u)) 