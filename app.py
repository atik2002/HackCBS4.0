import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from funct import *

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LITERA], 
                            meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}])

server = app.server

all_options = {
    'Assam': ['Sonitpur', 'Tinsukia'],
    'Bihar': ['Patna', 'Supaul'],
    'Chhattisgarh':['Surguja'],
    'Madhya Pradesh':['Tikamgarh'],
    'Rajasthan':['Sirohi'],
    'Uttar Pradesh':['Lucknow','Varanshi']
}

app.layout = dbc.Container([
    dbc.Button("Home", outline=True, color="primary", className="me-1", size='lg',href="https://atik2002.github.io/HackCBS4.0/"),

    dbc.Row([
        dbc.Col(html.H1("Data Dashboard", className='text-center text-success ', style={'textDecoration':'underline'}))
    ]),
    html.Br(),

    dbc.Row([
            dbc.Col(html.H3("Data Visualization: "))
        ]),

    dbc.Row([
        dbc.Col([
            html.Div([
            html.Label('State:',className='fw-bold'),
            dcc.Dropdown(
                options=[
                    {'label': k, 'value': k} for k in all_options.keys()
                ], id='vis_select',value='Assam'
        ),
            ]),
        ], width={'size':6} ),
        dbc.Col([
        html.Div([
            html.Label('City:',className='fw-bold'),
            dcc.Dropdown(id='vis_select2',value='Sonitpur')
        ]),
        html.Br(),
        
    ], width={'size':6}),

    dbc.Row([
        dbc.Col([
            html.Div([
            html.H6('Select Display Model: '),
            dcc.RadioItems(
                options=[
                    {'label': 'Scatter plot', 'value': 'SP'},
                    {'label': 'Line Plot Height', 'value': 'LPH'},
                    {'label': 'Line Plot Weight', 'value': 'LPW'},
                    {'label': 'Hide plot', 'value': 'NO'},
                ],
                id='radio',value='NO',labelClassName='me-3'
            ),
        ]),
        html.Br(),
        html.Div(id='plot',className='text-center'),
        html.Br(),
            ])
        ])
    ]),

    dbc.Row([
            dbc.Col(html.H3("Get Raw Data: "))
        ]),

    dbc.Row([
        dbc.Col([
            html.Div([
        html.Label('State:',className='fw-bold'),
        dcc.Dropdown(
            options=[
                {'label': k, 'value': k} for k in all_options.keys()
            ], id='select',value='Assam'
        )
    ]),
        ],width={'size':6}),

        dbc.Col([
            html.Div([
            html.Label('City:',className='fw-bold'),
            dcc.Dropdown(id='select2',value='')
        ]),
        html.Br(),
        html.Br()
            ], width={'size':6}),
    ]),

    dbc.Row([
            dbc.Col(html.Div(id='data', className='text-center'))
        ]),
])

@app.callback(
    Output(component_id='select2', component_property='options'),
    Input(component_id='select', component_property='value')
)

def set_cities(select_state):
    return [{'label': i, 'value': i} for i in all_options[select_state]]

@app.callback(
    Output(component_id='vis_select2', component_property='options'),
    Input(component_id='vis_select', component_property='value')
)

def set_cities(select_state):
    return [{'label': i, 'value': i} for i in all_options[select_state]]


@app.callback(
    Output(component_id='data', component_property='children'),
    [Input(component_id='select', component_property='value'),
    Input(component_id='select2', component_property='value')]
)

def showdata(option1, option2):

    if option1 == "Madhya Pradesh":
        return html.Table(generate_table("madhya_pradesh",option2))

    if option1 == "Uttar Pradesh":
        return html.Table(generate_table("uttar_pradesh",option2))

    if option2 == '':
        return '⚠️ Select City Show Data to show data ⚠️'
    else:
        return html.Table(generate_table(option1,option2))

@app.callback(
    Output(component_id='plot', component_property='children'),
    Input(component_id='radio', component_property='value'),
    Input(component_id='vis_select', component_property='value'),
    Input(component_id='vis_select2', component_property='value')
)

def show_plot(option,option1, option2):

    if option == 'NO':
        return '⚠️ Select Plot type ⚠️'
    
    if option1 == "Madhya Pradesh":
        if option == "SP":
            return dcc.Graph(
            id='life-exp-vs-gdp',
            figure=plot_data(get_df("madhya_pradesh",option2))
            )
        elif option == "LPH":
            return dcc.Graph(
                id='line_plot_h',
                figure=plot_line_height(get_df("madhya_pradesh",option2))
            )
        else:
            return dcc.Graph(
                id='line_plot_w',
                figure=plot_line_weight(get_df("madhya_pradesh",option2))
            )

    elif option1 == "Uttar Pradesh":

        if option == "SP":
            return dcc.Graph(
            id='life-exp-vs-gdp',
            figure=plot_data(get_df("uttar_pradesh",option2))
            )
        elif option == "LPH":
            return dcc.Graph(
                id='line_plot_h',
                figure=plot_line_height(get_df("uttar_pradesh",option2))
            )
        else:
            return dcc.Graph(
                id='line_plot_w',
                figure=plot_line_weight(get_df("uttar_pradesh",option2))
            )
        
    else:
        if option == 'SP':
            return dcc.Graph(
            id='life-exp-vs-gdp',
            figure=plot_data(get_df(option1,option2))
        )
        elif option == 'LPH':
            return dcc.Graph(
                id='line_plot_h',
                figure=plot_line_height(get_df(option1,option2))
            )
        else:
            return dcc.Graph(
                id='line_plot_w',
                figure=plot_line_weight(get_df(option1,option2))
            )

if __name__ == '__main__':
    app.run_server(debug=False,dev_tools_ui=False,dev_tools_props_check=False)