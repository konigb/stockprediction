Stock Prediction App
This is a simple stock price prediction app built using Streamlit, Prophet, and Plotly. The app allows users to select a stock from a predefined list, view its historical data, and generate predictions for future stock prices.

Features
Stock Data: View historical stock data for the selected company.
Interactive Plots: Interactive plots showing the stock's Open and Close prices.
Forecasting: Generate and visualize future stock price predictions using the Prophet forecasting model.
Forecast Components: View individual components (trend, yearly seasonality, weekly seasonality) of the forecast.
Technologies Used
Streamlit: For creating the interactive web app.
yfinance: To fetch historical stock data.
Prophet: To make future predictions based on historical data.
Plotly: For interactive data visualization.
How to Run Locally
To run this app locally, follow these steps:

Clone the repository:

bash
Copy
Edit
git clone https://github.com/your-username/stock-prediction-app.git
cd stock-prediction-app
Install the required dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the Streamlit app:

bash
Copy
Edit
streamlit run app.py
The app will be available at http://localhost:8501 in your browser.

Deployment
This app is deployed on Streamlit Cloud. You can access the live version by visiting:

Stock Prediction App

Requirements
Python 3.7+
The following Python packages:
streamlit
yfinance
pandas
prophet
plotly
To install the dependencies, use the following command:

bash
Copy
Edit
pip install -r requirements.txt
App Overview
1. Stock Selection
The app starts by allowing you to select one of the following stocks for prediction:

AAPL (Apple)
GOOG (Google)
MSFT (Microsoft)
GME (GameStop)
2. Historical Data
The app will display the last 20 rows of historical stock data for the selected company.

3. Plotting Stock Data
You can visualize the stock's Open and Close prices on an interactive graph, which provides a time series view of stock movements.

4. Forecasting Future Prices
The app uses Prophet to predict future stock prices based on historical data. It will display the forecasted values for a selected period and plot them on an interactive graph.

5. Forecast Components
The app also provides a breakdown of the forecast into components such as trends, weekly seasonality, and yearly seasonality.

Feel free to update the repository details and other parts as necessary! Let me know if you need further assistance.
