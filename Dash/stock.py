import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import yfinance as yf
import datetime
import csv
import numpy as np
import math as ma
import pandas as pd

test = yf.Ticker('EA')
df = test.history(start= '1999-01-01', end = '2018-01-01')
df.reset_index(inplace=True)

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Dropdown(
        id="ticker",
        options=[{"label": x, "value": x} 
                 for x in df.columns[1:]],
        value=df.columns[1],
        clearable=False,
    ),
    dcc.Graph(id="time-series-chart"),
])

@app.callback(
    Output("time-series-chart", "figure"), 
    [Input("ticker", "value")])
def display_time_series(ticker):
    fig = px.line(df, x='Date', y=ticker)
    return fig

app.run_server(debug=True)