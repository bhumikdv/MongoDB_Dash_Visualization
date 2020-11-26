# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 17:29:03 2020

@author: bhumik
"""

# Run this app with `main.py` and
# visit http://127.0.0.1:2000/ in your web browser

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas as pd
import plotly.express as px


import pymongo
from pymongo import MongoClient
import pprint
import time

client = MongoClient()
client = MongoClient('localhost', 27017)


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUMEN])  # https://bootswatch.com/default/

db = client.WorldHappinessReport
collection = db.data


# df = pd.read_csv('WholeCummulativeData.csv')

client = MongoClient()
client = MongoClient('localhost', 27017)
test = db.test
df = pd.DataFrame(list(test.find()))
client.close()

    

figure_scatter_matrix = px.scatter_matrix(df, color='Country',
                dimensions=['Economy (GDP per Capita)', 
                            'crime rate','Health (Life Expectancy)',
                            'literacy rate',],
                hover_data=['year'],
                title="Scatter matrix of World Happiness Report",
                symbol="Country",
                height=800)

app.layout = html.Div([
    
    html.Div(html.H1("CRUD operations using MongoDB & Data Visualization using DASH"), 
             style={"text-align":"center",
                    "background":"#bde0fe"}),
    html.Div(html.H2("Does a country's Happiness depend on country's GDP? Health? Crime? Literacy?"), 
             style={"text-align":"center",
                    "background":"#bde0fe"}),
    html.Div(html.H3("- Bhumik Dhirajlal Varu & Poorva Morvekar"), 
             style={"text-align":"center",
                    "background":"#bde0fe",
                    'font-weight': 'bold'}),
    html.Hr(),
    
    # -------------------
    dbc.CardHeader(
            dbc.Button(
                html.H3("Describing the columns, comparing various columns and see how our data looks like at a glimpse!"),
                color="link",
                id="button_question_3",
            )
    ),
    
    dbc.Collapse(
        dbc.CardBody(children=[
                       
            html.Div([dcc.Graph(id='example-scatter-matrix',
                figure=figure_scatter_matrix)
                      ])
            ]),
                     
        id="collapse_question_3", is_open=False
    ),
    # -------------------
    dbc.CardHeader(
            dbc.Button(
                html.H3("Let's see what data says about Economy, Health, Crime and Literacy..."),
                color="link",
                id="button_question_1",
            )
    ),
    
    dbc.Collapse(
        dbc.CardBody(children=[
            
            html.H2("Select from the dropdown menu:"),
                     
            dcc.Dropdown(id='demo-dropdown',
                          options=[
                              {'label': 'Literacy Rate', 'value': 'fig_1'},
                              {'label': 'Economy', 'value': "fig_2"},
                              {'label': 'Crime', 'value': "fig_3"},
                              {'label': 'Health', 'value': "fig_4"}
                              ],
                          value="Fig1"),
                     
                     html.Div(id='dd-output-container', children=''),
                     ]),
                     
        id="collapse_question_1", is_open=False
    ),

    dbc.CardHeader(
            dbc.Button(
                html.H3("Now, lets see whether GDP and health are related across years..."),
                color="link",
                id="button_question_2",
            )
    ),
    
    dbc.Collapse(
        dbc.CardBody(children=[
                     dcc.Dropdown(id='dropdown', value=['Germany','India'], multi=True,
                                  options=[
                                      {'label': x, 'value': x} for x in df['Country'].unique()
                                      ]),
                     
                     
                     html.Div([
                          dcc.Graph(id='pie-graph', figure={}, className='six columns'),
                              dcc.Graph(id='my-graph', figure={}, clickData=None, hoverData=None, 
                   config={
                       'staticPlot': False,     
                       'scrollZoom': True,      
                       'doubleClick': 'reset',  
                       'showTips': False,       
                       'displayModeBar': True,  
                       'watermark': True,
                         },
                   className='six columns'
                   )])
                     
                     
                     ]),
    
        id="collapse_question_2", is_open=False
    ),
    
        dbc.CardHeader(
            dbc.Button(
                html.H3("Now, lets see whether crime and Happiness score are related across years..."),
                color="link",
                id="button_question_4",
            )
    ),
    
    dbc.Collapse(
        dbc.CardBody(children=[
                     dcc.Dropdown(id='dropdown-crime', value=['Germany','India'], multi=True,
                 options=[{'label': x, 'value': x} for x in
                          df['Country'].unique()]),
    html.Div([
        dcc.Graph(id='sunburst-graph-crime', figure={}, className='six columns'),
        dcc.Graph(id='my-graph-crime', figure={}, clickData=None, hoverData=None, 
                  config={
                      'staticPlot': False,     
                      'scrollZoom': True,      
                      'doubleClick': 'reset',  
                      'showTips': False,       
                      'displayModeBar': True,  
                      'watermark': True,
                        },
                  className='six columns'
                  )])
                     
                     
                     ]),
    
        id="collapse_question_4", is_open=False
    ),
    
    dbc.CardHeader(
            dbc.Button(
                html.H3("Now, lets see how Literacy, GDP & Happiness score are related across years..."),
                color="link",
                id="button_question_5",
            )
    ),
    
    dbc.Collapse(
        dbc.CardBody(children=[
                     dcc.Dropdown(id='dropdown-literacy', value=['Germany','India'], multi=True,
                 options=[{'label': x, 'value': x} for x in
                          df['Country'].unique()]),
    html.Div([
        dcc.Graph(id='bar-graph-literacy', figure={}, className='six columns'),
        dcc.Graph(id='my-graph-literacy', figure={}, clickData=None, hoverData=None, 
                  config={
                      'staticPlot': False,     
                      'scrollZoom': True,      
                      'doubleClick': 'reset',  
                      'showTips': False,       
                      'displayModeBar': True,  
                      'watermark': True,
                        },
                  className='six columns'
                  )])
                     
                     
                     ]),
    
        id="collapse_question_5", is_open=False
    ),
    
    # Changes here..
    
    # ------------------- Creating here
    dbc.CardHeader(
            dbc.Button(
                html.H3("Create ----- Do you want to add more data??"),
                color="link",
                id="button_question_6",
            )
    ),
    
    dbc.Collapse(
        dbc.CardBody(children=[
                       
            html.Div([
                dcc.Input(id='Country', type='text',  placeholder="Country"),
                dcc.Input(id='Region', type='text',  placeholder="Region"),
                dcc.Input(id='Happiness-Rank', type='text',  placeholder="Happiness Rank"),
                dcc.Input(id='Happiness-Score', type='text',  placeholder="Happiness Score"),
                dcc.Input(id='Economy', type='text',  placeholder="Economy (GDP per Capita)"),
                dcc.Input(id='Health', type='text',  placeholder="Health (Life Expectancy)"),
                dcc.Input(id='year', type='text',  placeholder="year"),
                dcc.Input(id='literacy-rate', type='text',  placeholder="literacy rate"),
                dcc.Input(id='crime-rate', type='text',  placeholder="crime rate"),
                html.Button('Insert', id='submit-val', n_clicks=0),
                html.Div(id='container-button-basic',
                         children='Enter values and press Insert')
                      ])
            ]),
                     
        id="collapse_question_6", is_open=False
    ),
    # -------------------
    
    # ------------------- Updating here
    dbc.CardHeader(
            dbc.Button(
                html.H3("Update ----- Do you want to Update data??"),
                color="link",
                id="button_question_7",
            )
    ),
    
    dbc.Collapse(
        dbc.CardBody(children=[
                       
            html.Div([
                dcc.Input(id='update-Country', type='text',  placeholder="Country"),
                dcc.Input(id='update-Happiness-Score', type='text',  placeholder="Happiness Score"),
                html.Button('Update', id='submit-value', n_clicks=0),
                html.Div(id='update-container-button-basic',
                         children='Enter values and press Update')
                      ])
            ]),
                     
        id="collapse_question_7", is_open=False
    ),
    # -------------------
    
    # ------------------- Deleting here
    dbc.CardHeader(
            dbc.Button(
                html.H3("Delete ----- Do you want to Delete data??"),
                color="link",
                id="button_question_8",
            )
    ),
    
    dbc.Collapse(
        dbc.CardBody(children=[
                       
            html.Div([
                dcc.Input(id='delete-Country', type='text',  placeholder="Country"),
                html.Button('Delete', id='submit-value-delete', n_clicks=0),
                html.Div(id='delete-container-button-basic',
                         children='Enter value and press Delete')
                      ])
            ]),
                     
        id="collapse_question_8", is_open=False
    ),
    # -------------------

],
    # style={"background":"#bde0fe"}
    )

@app.callback(
    Output("collapse_question_1", "is_open"),
    [Input("button_question_1", "n_clicks")],
    [State("collapse_question_1", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


@app.callback(
    Output("collapse_question_2", "is_open"),
    [Input("button_question_2", "n_clicks")],
    [State("collapse_question_2", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("collapse_question_3", "is_open"),
    [Input("button_question_3", "n_clicks")],
    [State("collapse_question_3", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("collapse_question_4", "is_open"),
    [Input("button_question_4", "n_clicks")],
    [State("collapse_question_4", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("collapse_question_5", "is_open"),
    [Input("button_question_5", "n_clicks")],
    [State("collapse_question_5", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("collapse_question_6", "is_open"),
    [Input("button_question_6", "n_clicks")],
    [State("collapse_question_6", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("collapse_question_7", "is_open"),
    [Input("button_question_7", "n_clicks")],
    [State("collapse_question_7", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("collapse_question_8", "is_open"),
    [Input("button_question_8", "n_clicks")],
    [State("collapse_question_8", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


@app.callback(
    dash.dependencies.Output('container-button-basic', 'children'),
    [dash.dependencies.Input('submit-val', 'n_clicks')],
    [dash.dependencies.State('Country', 'value'),
     dash.dependencies.State('Region', 'value'),
     dash.dependencies.State('Happiness-Rank', 'value'),
     dash.dependencies.State('Happiness-Score', 'value'),
     dash.dependencies.State('Economy', 'value'),
     dash.dependencies.State('Health', 'value'),
     dash.dependencies.State('year', 'value'),
     dash.dependencies.State('literacy-rate', 'value'),
     dash.dependencies.State('crime-rate', 'value')])
def update_output(n_clicks, Country, Region, HappinessRank, HappinessScore,
                  Economy, Health, year, literacyrate, crimerate):
    
    insert = {"Country":Country,
                "Region": Region,
                "Happiness Rank": int(HappinessRank),
                "Happiness Score": float(HappinessScore),
                "Economy (GDP per Capita)": float(Economy),
                "Health (Life Expectancy)":float(Health),
                "year": int(year),
                "literacy rate": float(literacyrate),
                "crime rate": float(crimerate),
              }
    
    client = MongoClient()
    client = MongoClient('localhost', 27017)
    test = db.test
    test_id = test.insert_one(insert)
       
    global df
    df = pd.DataFrame(list(test.find()))
    
    client.close()
    
    if n_clicks != 0:
        return 'The input value "{}, {}, {}, {}, {}, {}, {}, {}, {}" is added to the db.'.format(
            Country,
            Region,
            HappinessRank,
            HappinessScore,
            Economy,
            Health,
            year,
            literacyrate,
            crimerate
        )

# ----
@app.callback(
    dash.dependencies.Output('update-container-button-basic', 'children'),
    [dash.dependencies.Input('submit-value', 'n_clicks')],
    [dash.dependencies.State('update-Country', 'value'),
     dash.dependencies.State('update-Happiness-Score', 'value')])
def update_output(n_clicks, Country, HappinessScore):
    
    myquery = {  "Country": Country
              }
    
    client = MongoClient()
    client = MongoClient('localhost', 27017)
    test = db.test
    
    newvalues = { "$set": { "Happiness Score": float(HappinessScore) } }
    test.update_one(myquery, newvalues)
       
    global df
    df = pd.DataFrame(list(test.find()))
    
    client.close()
    
    if n_clicks != 0:
        return 'The Happiness Score value {} for country {} is updated.'.format(
            HappinessScore,
            Country
        )

# ---
# @app.callback(
#     dash.dependencies.Output('update-container-button-basic', 'children'),
#     [dash.dependencies.Input('submit-value', 'n_clicks')])
# def update_output(n_clicks, Country, HappinessScore):
    
#     if n_clicks != 0:
#         time.sleep(2)
#         return ''


# ----

# ----
@app.callback(
    dash.dependencies.Output('delete-container-button-basic', 'children'),
    [dash.dependencies.Input('submit-value-delete', 'n_clicks')],
    [dash.dependencies.State('delete-Country', 'value')])
def update_output(n_clicks, Country):
    
    myquery = {  "Country": Country
              }
    
    client = MongoClient()
    client = MongoClient('localhost', 27017)
    test = db.test
    
    test.delete_one(myquery)
       
    global df
    df = pd.DataFrame(list(test.find()))
    
    client.close()
    
    if n_clicks != 0:
        return 'Country {} is deleted.'.format(
            Country
        )

# ----



@app.callback(
    dash.dependencies.Output('dd-output-container', 'children'),
    [dash.dependencies.Input('demo-dropdown', 'value')])
def update_output(value):
    if value == "fig_1":
        fig_11 = px.bar(df, x="Country", y="literacy rate",
                        color="Happiness Score", barmode="group",
                        hover_data=['year'],
                        labels={'crime rate':'crime rate (per 100,000)'},
                        title="Literacy rate of Countries")
        return dcc.Graph(children='We see that Countries which has high literacy rate have more happiness score',
                id='example-bar',
                figure=fig_11
                
            )
    elif value == "fig_2":
        df["country"] = "country"
        fig_22 = px.treemap(df, path=['country', 'Country'], values='Economy (GDP per Capita)',
                  color='Region',
                  title="Economy (GDP per Capita) of Countries"
                  )
        return dcc.Graph(children='We see that Countries which has high GDP',
                id='example-tree',
                figure=fig_22
                
            )
    
    elif value == "fig_3":
        fig_33 =px.scatter(df, x="Country", y="crime rate",
                            size="crime rate", color="Region",
                            hover_data=['year'],
                            title="Crime rate of Countries")
        return dcc.Graph(
                id='example-scatter-size',
                figure=fig_33
            )
    elif value == "fig_4":
        fig_44 = px.scatter(df, x="Region", y="Health (Life Expectancy)",
                            color="Country",
                            hover_data=['year'],
                            title="Health (Life Expectancy) of Countries")
        return dcc.Graph(children='We see that Countries with good Health Expectancy rate',
                id='example-scatter',
                figure=fig_44
            )

@app.callback(
    Output(component_id='my-graph', component_property='figure'),
    Input(component_id='dropdown', component_property='value'),
    
)
def update_graph(country_chosen):
    dff = df[df['Country'].isin(country_chosen)]
    fig = px.line(data_frame=dff, x='year', y='Health (Life Expectancy)', color='Country',
                  custom_data=['Country', 'Region', 'Happiness Rank'],
                  title=f'Health (Life Expectancy) for: {country_chosen}',
                  
                  # hover_data=['Economy (GDP per Capita)']
                  )
    fig.update_traces(mode='lines+markers')
    return fig

@app.callback(
    Output(component_id='pie-graph', component_property='figure'),
    Input(component_id='my-graph', component_property='hoverData'),
    Input(component_id='my-graph', component_property='clickData'),
    Input(component_id='my-graph', component_property='selectedData'),
    Input(component_id='dropdown', component_property='value')
)
def update_side_graph(hov_data, clk_data, slct_data, country_chosen):
    if hov_data is None:
        dff2 = df[df['Country'].isin(country_chosen)]
        dff2 = dff2[dff2.year == 2016]
        print(dff2)
        fig2 = px.pie(data_frame=dff2, values='Economy (GDP per Capita)', names='Country',
                      title='Population for 2016'
                      # hover_data=['year','Health (Life Expectancy)']
                      )
        return fig2
    else:
        print(f'hover data: {hov_data}')
        dff2 = df[df['Country'].isin(country_chosen)]
        hov_year = hov_data['points'][0]['x']
        dff2 = dff2[dff2.year == hov_year]
        fig2 = px.pie(data_frame=dff2, values='Economy (GDP per Capita)', names='Country',
                      title=f'Population for: {hov_year}'
                      # hover_data=['year','Health (Life Expectancy)']
                      )
        return fig2

@app.callback(
    Output(component_id='my-graph-crime', component_property='figure'),
    Input(component_id='dropdown-crime', component_property='value'),
)
def update_graph_crime(country_chosen):
    dff = df[df['Country'].isin(country_chosen)]
    fig = px.line(data_frame=dff, x='year', y='Happiness Score', color='Country',
                  custom_data=['Country', 'Region', 'Happiness Rank'],
                  title=f'Health (Life Expectancy) for: {country_chosen}')
    fig.update_traces(mode='lines+markers')
    return fig

@app.callback(
    Output(component_id='sunburst-graph-crime', component_property='figure'),
    Input(component_id='my-graph-crime', component_property='hoverData'),
    Input(component_id='my-graph-crime', component_property='clickData'),
    Input(component_id='my-graph-crime', component_property='selectedData'),
    Input(component_id='dropdown-crime', component_property='value')
)
def update_side_graph_crime(hov_data, clk_data, slct_data, country_chosen):
    if hov_data is None:
        dff2 = df[df['Country'].isin(country_chosen)]
        dff2 = dff2[dff2.year == 2016]
        print(dff2)
        # fig2 = px.pie(data_frame=dff2, values='crime rate', names='Country',
        #               title='Population for 2016')
        fig2 = px.sunburst(dff2, 
                             path=['Region', 'Country'], 
                             values='crime rate',
                             color='Happiness Score', 
                             # hover_data=['Economy (GDP per Capita)', 'year'],
                             title='Crime rate for 2016',
                             labels={'crime rate':'crime rate (per 100,000)'})
        return fig2
    else:
        print(f'hover data: {hov_data}')
        dff2 = df[df['Country'].isin(country_chosen)]
        hov_year = hov_data['points'][0]['x']
        dff2 = dff2[dff2.year == hov_year]
        # fig2 = px.pie(data_frame=dff2, values='crime rate', names='Country', title=f'Population for: {hov_year}')
        
        fig2 = px.sunburst(dff2, 
                             path=['Region', 'Country'], 
                             values='crime rate',
                             color='Happiness Score', 
                             labels={'crime rate':'crime rate (per 100,000)'},
                             # hover_data=['Economy (GDP per Capita)', 'year'],
                             title=f'Crime rate: {hov_year}')
        return fig2

@app.callback(
    Output(component_id='my-graph-literacy', component_property='figure'),
    Input(component_id='dropdown-literacy', component_property='value'),
)
def update_graph_literacy(country_chosen):
    dff = df[df['Country'].isin(country_chosen)]
    fig = px.line(data_frame=dff, x='year', y='Economy (GDP per Capita)', color='Country',
                  custom_data=['Country', 'Region', 'Happiness Rank'],
                  title=f'Happiness score for: {country_chosen}')
    fig.update_traces(mode='lines+markers')
    return fig


@app.callback(
    Output(component_id='bar-graph-literacy', component_property='figure'),
    Input(component_id='my-graph-literacy', component_property='hoverData'),
    Input(component_id='my-graph-literacy', component_property='clickData'),
    Input(component_id='my-graph-literacy', component_property='selectedData'),
    Input(component_id='dropdown-literacy', component_property='value')
)
def update_side_graph_literacy(hov_data, clk_data, slct_data, country_chosen):
    if hov_data is None:
        dff2 = df[df['Country'].isin(country_chosen)]
        dff2 = dff2[dff2.year == 2016]
        print(dff2)
        fig2=px.bar(dff2, x="Country", y="literacy rate",
                        color="Happiness Score", barmode="group",
                        # hover_data=['year'],
                        labels={'crime rate':'crime rate (per 100,000)'},
                        title="Literacy rate of Countries in 2016")
        return fig2
    else:
        print(f'hover data: {hov_data}')
        dff2 = df[df['Country'].isin(country_chosen)]
        hov_year = hov_data['points'][0]['x']
        dff2 = dff2[dff2.year == hov_year]
        fig2=px.bar(dff2, x="Country", y="literacy rate",
                        color="Happiness Score", barmode="group",
                        # hover_data=['year'],
                        labels={'crime rate':'crime rate (per 100,000)'},
                        title=f"Literacy rate: {hov_year}")
        return fig2


if __name__ == "__main__":
    app.run_server(debug=False, port=2000)