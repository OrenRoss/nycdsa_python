import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import csv
import pandas as pd

df = pd.read_csv(r'vg_df_dash.csv')

app = dash.Dash(__name__)

app.layout = html.Div([
    html.P("x-axis:"),
    dcc.RadioItems(
        id='x-axis', 
        options=[
            {'label': 'Critic Scores (100 point scale)', 'value': 'critic_score'},
            {'label': 'User Scores (100 point scale)', 'value': 'user_score'},
            {'label': 'Total Sales (in millions)', 'value': 'total_sales'}
        ],
        value='total_sales', 
        labelStyle={'display': 'inline-block'}
    ),
    html.P("y-axis:"),
    dcc.RadioItems(
        id='y-axis', 
        options=[
            {'label': 'Company', 'value': 'company'},
            {'label': 'Genre', 'value': 'genre_x'}
        ],
        value='company', 
        labelStyle={'display': 'inline-block'}
    ),
    dcc.Graph(id="box-plot"),
])



@app.callback(
    Output("box-plot", "figure"), 
    [Input("x-axis", "value"), 
     Input("y-axis", "value")])
def generate_chart(x, y):
    fig = px.box(df, x=x, y=y)
    return fig


def update_graph(stock):
    msk = df.Stock.isin([stock])
    figure = px.bar(df[msk], x='Stock', y='Number', title=f"{stock} open price")

    return figure





app.run_server(debug=True)