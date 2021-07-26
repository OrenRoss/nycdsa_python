import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import csv


df = pd.read_csv(r'vg_df_dash.csv')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

fig = px.scatter(df.query("total_sales > 5"), x="user_score", y="critic_score",
         size="total_sales", color="company",
                 hover_name="title", log_x=False, size_max=40)

app.layout = html.Div([
    dcc.Graph(
        id='User to Critic Score',
        figure=fig
    )
])


if __name__ == '__main__':
    app.run_server(debug=True)