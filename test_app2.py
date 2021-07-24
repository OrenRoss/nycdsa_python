# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as 
import dash_design_kit as ddk
import dash_html_components as html
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


vg_df = pd.read_csv(r'Data/vg_complete_df.csv')


# .query("total_sales > 5")

fig = px.scatter(vg_df.query("total_sales > 5"), x="user_score", y="critic_score",
         size="total_sales", color="company",
                 hover_name="title", log_x=False, size_max=40)

app.layout = html.Div([
    dcc.Graph(
        id='Video Game Sales and Reviews',
        figure=fig
    )
    dcc.RangeSlider(
        id='rang_slid'
        count=1,
        min=0,
        max=100,
        step=0.5,
        value=[15, 40]
    ), 
   html.Div(id='output-container-range-slider')
])






@app.callback(
    dash.dependencies.Output('slider-output-container', 'children'),
    [dash.dependencies.Input('my-slider', 'value')])
def update_output(value):
    return 'You have selected "{}"'.format(value)

fig.show()



'''
https://dash.plotly.com/interactive-graphing



dcc.RangeSlider(
    count=1,
    min=0,
    max=100,
    step=0.5,
    value=[15, 40]
)   




from datetime import date

dcc.DatePickerRange(
    id='date-picker-range',
    start_date=date(1997, 5, 3),
    end_date_placeholder_text='Select a date!'
)

https://plotly.com/python/range-slider/

'''