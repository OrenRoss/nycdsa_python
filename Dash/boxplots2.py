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
    html.P("categ:"),
    dcc.RadioItems(
        id='categ', 
        options=[
            {'label': 'Company', 'value': 'company'},
            {'label': 'Genre', 'value': 'genre_x'}
        ],
        value='company', 
        labelStyle={'display': 'inline-block'}
    ),
    dcc.Graph(id="graph"),
])



@app.callback(
    Output("graph", "figure"), 
    [Input("categ", "value")])
def generate_chart(x, y):
    fig = px.box(df, x='release_date_x', y='count',
             color="company", marginal="rug")
    return fig


# fig = px.histogram(rls_dt_comp_ct, x="release_date_x", y='count', color="company", marginal="rug")
# fig.update_layout(
#     autosize=False,
#     width=1000,
#     height=750,
#     margin=dict(
#         l=35,
#         r=10,
#         b=30,
#         t=20,
#         pad=4
#     ),
#     paper_bgcolor="LightSteelBlue",
# )
# fig.show()






app.run_server(debug=True)