# -*- coding: utf-8 -*-

import dash
import dash_html_components as html
import dash_core_components as dcc

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Div(dcc.Input(id='input-on-submit', type='text')),
    html.Div(dcc.Input(id='input-on-submit2', type='text')),
    html.Div(dcc.Input(id='input-on-submit3', type='text')),
    html.Div(dcc.Input(id='input-on-submit4', type='text')),
    html.Button('Submit', id='submit-val', n_clicks=0),
    html.Div(id='container-button-basic',
             children='Enter a value and press submit')
])


@app.callback(
    dash.dependencies.Output('container-button-basic', 'children'),
    [dash.dependencies.Input('submit-val', 'n_clicks')],
    [dash.dependencies.State('input-on-submit', 'value'),
     dash.dependencies.State('input-on-submit2', 'value'),
     dash.dependencies.State('input-on-submit3', 'value'),
     dash.dependencies.State('input-on-submit4', 'value')])
def update_output(n_clicks, value, value2, value3, value4):
    return 'The input value was "{} {} {} {}" and the button has been clicked {} times'.format(
        value,
        value2,
        value4,
        value3,
        n_clicks
    )


if __name__ == '__main__':
    app.run_server(debug=True)