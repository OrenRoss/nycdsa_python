import pandas as pd 
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

df = pd.read_csv(r'Data/vg_complete_df.csv')

app = dash.Dash(__name__)

app.layout = html.Div([
    
    html.P("x-axis:"),
    html.Label('Dropdown'),
    dcc.Dropdown(
        options=[
            {'label': 'User Score', 'value': 'user_score'},
            {'label': 'User Count', 'value': 'user_count'},
            {'label': 'Critic Score', 'value': 'critic_score'},
            {'label': 'Critic Count', 'value': 'critic_count'},
            {'label': 'Total Sales', 'value': 'total_sales'}
            ],
        value='total_sales'
    ),
    
    html.P("y-axis:"),
    dcc.RadioItems(
        id='y-axis', 
        options=[{'value': x, 'label': x} 
                 for x in ['genre', 'company']],
        value='genre', 
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

app.run_server(debug=True)