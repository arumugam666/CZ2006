import streamlit as st

class SearchDisplay:

    @staticmethod
    def search(stockName, t, numOfArticles):
        if stockName:
            results = {
                "stockName":"APPLE",
                "confidenceLevel":100,
                "description":"Just another article"
            }
            return results

    @staticmethod
    def displayResults(results):
        if results:
            st.markdown('# '+results["stockName"])
            st.write('## '+results["description"],results["confidenceLevel"])

    def renderDisplay(self):
        st.markdown('# HOME')
        timeRange = st.selectbox("Select Time Range",('Last Hour', 'Last Day', 'Last Week'))
        numOfArticles = st.slider("Select number of articles")
        stockName = st.text_input("Please enter the stock name here")
        searchResults = self.search(stockName,timeRange,numOfArticles)
        self.displayResults(searchResults)


if __name__ == "__main__":
    SearchDisplay().renderDisplay()