import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input
from dash.dependencies import Output
import plotly_express as px
import subprocess

df = px.data.gapminder()

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1('コールバック'),
    dcc.Input(id='input', value='init', type='text'),
    html.Div(id='output')

])

@app.callback(
    Output('output', 'chir'),
    Input('input', 'value')
)

def update_output_div(input_value):
    return '入力は"{}"です'.format(input_value)

if __name__ == '__main__':
    app.run_server()