import streamlit as st
from datetime import date
import pandas as pd

import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objects as go
import plotly.express as px

START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

st.title("Stock Prediction App")


stocks = ("AAPL", "GOOG", "MSFT", "GME")

selected_stock = st.selectbox("Select dataset for prediction", stocks)

n_years  = st.slider("Years of prediction:", 1, 5)
period = n_years*365

#cache data so it doesn't load everytime
@st.cache_data
def load_data(ticker):
    data = yf.download(ticker,START, TODAY)
    data.reset_index(inplace=True)
    return data

data_load_state = st.text("Load data...")
data = load_data(selected_stock)
data_load_state.text("Loading data...done!")


st.subheader("Raw data")
st.write(data.tail(20))

# Flatten the column names if they are multi-indexed
data.columns = [col[0] if isinstance(col, tuple) else col for col in data.columns]

def plot_raw_data(data):
     # Create a figure for the combined plot
    fig = go.Figure()

    # Add the 'Open' line to the figure
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], mode='lines', name='Open'))

    # Add the 'Close' line to the figure
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], mode='lines', name='Close', line=dict(color='red')))

    # Update layout with titles and axis labels
    fig.update_layout(
        title=f"Time Series Data for {selected_stock}",
        xaxis_title="Date",
        yaxis_title="Stock Price",
        xaxis_rangeslider_visible=True,
        legend_title="Stock Data"
    )
    st.plotly_chart(fig)

plot_raw_data(data)


#frocasting
df_train = data[['Date', 'Close']]
df_train = df_train.rename(columns={"Date":"ds","Close":"y"})

m = Prophet()
m.fit(df_train)
future = m.make_future_dataframe(periods=period)
forecast = m.predict(future)

st.subheader(f"Forecast Data")
st.write(forecast.tail(20))

st.write(f"Forecast Data for {selected_stock}")
fig1 = plot_plotly(m, forecast)
st.plotly_chart(fig1)

st.write("Forecast Components")
fig2 = m.plot_components(forecast)
st.write(fig2)