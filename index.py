from turtle import width
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

# Connect to main app.py file
from app import app
from app import server

# Connect to your app pages
from apps import mat1ano, mat2ano, mat3ano, mat4ano, mat5ano, mat6ano, mat7ano, mat8ano, mat9ano, port1ano, port2ano, port3ano, port4ano, port5ano, port6ano, port7ano, port8ano, port9ano

button = html.Div(
    [
        dbc.Button('Matemática 1 Ano', href='/apps/mat1ano', outline=True, className="me-1",color="primary"),
        dbc.Button('Matemática 2 Ano', href='/apps/mat2ano', outline=True, className="me-1",color="primary"),
        dbc.Button('Matemática 3 Ano', href='/apps/mat3ano', outline=True,className="me-1",color="primary"),
        dbc.Button('Matemática 4 Ano', href='/apps/mat4ano', outline=True,className="me-1",color="primary"),
        dbc.Button('Matemática 5 Ano', href='/apps/mat5ano', outline=True,className="me-1",color="primary"),
        dbc.Button('Matemática 6 Ano', href='/apps/mat6ano', outline=True,className="me-1",color="primary"),
        dbc.Button('Matemática 7 Ano', href='/apps/mat7ano', outline=True,className="me-1",color="primary"),
        dbc.Button('Matemática 8 Ano', href='/apps/mat8ano', outline=True,className="me-1",color="primary"),
        dbc.Button('Matemática 9 Ano', href='/apps/mat9ano', outline=True,className="me-1",color="primary"),
        html.Br(),
        dbc.Button('Português 1 Ano', href='/apps/port1ano', outline=True,className="me-1",color="success"),
        dbc.Button('Português 2 Ano', href='/apps/port2ano', outline=True,className="me-1",color="success"),
        dbc.Button('Português 3 Ano', href='/apps/port3ano', outline=True,className="me-1",color="success"),
        dbc.Button('Português 4 Ano', href='/apps/port4ano', outline=True,className="me-1",color="success"),
        dbc.Button('Português 5 Ano', href='/apps/port5ano', outline=True,className="me-1",color="success"),
        dbc.Button('Português 6 Ano', href='/apps/port6ano', outline=True,className="me-1",color="success"),
        dbc.Button('Português 7 Ano', href='/apps/port7ano', outline=True,className="me-1",color="success"),
        dbc.Button('Português 8 Ano', href='/apps/port8ano', outline=True,className="me-1",color="success"),
        dbc.Button('Português 9 Ano', href='/apps/port9ano', outline=True,className="me-1",color="success"), 
    ],
    className="d-grid gap-2 col-12 mx-auto",
)
app.layout = html.Div([
    
dcc.Location(id='url', refresh=False),

dbc.NavbarSimple(
    children=[html.Img(src=app.get_asset_url('alian.png'), style ={'height': 150})],         
    brand="Mapa de Habilidades BNCC - Aliança do Tocantins",
    color="primary",
    dark=True,
    brand_style={'font-size':35},
    className="shadow p-3 mb-5"
),

html.Div(
    [
        dbc.Button("Séries", id="open-offcanvas", n_clicks=0, style={'margin-top':3,'margin-left':10, 'width':200}),
        dbc.Offcanvas(
            children=[

                button,
            ],

            id="offcanvas",
            title="Secretaria de Educação de Aliança do Do Tocantins",
            is_open=False,
        ),
    ]
),
     
  html.Div(id='page-content', children=[])

], style={'background-color': '#D6EAF8'})




@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])

def display_page(pathname):
    
    if pathname == '/apps/mat1ano':
        return mat1ano.layout
    if pathname == '/apps/mat2ano':
        return mat2ano.layout
    if pathname == '/apps/mat3ano':
        return mat3ano.layout
    if pathname == '/apps/mat4ano':
        return mat4ano.layout
    if pathname == '/apps/mat5ano':
        return mat5ano.layout
    if pathname == '/apps/mat6ano':
        return mat6ano.layout
    if pathname == '/apps/mat7ano':
        return mat7ano.layout
    if pathname == '/apps/mat8ano':
        return mat8ano.layout
    if pathname == '/apps/mat9ano':
        return mat9ano.layout
    if pathname == '/apps/port1ano':
        return port1ano.layout
    if pathname == '/apps/port2ano':
        return port2ano.layout
    if pathname == '/apps/port3ano':
        return port3ano.layout
    if pathname == '/apps/port4ano':
        return port4ano.layout
    if pathname == '/apps/port5ano':
        return port5ano.layout
    if pathname == '/apps/port6ano':
        return port6ano.layout
    if pathname == '/apps/port7ano':
        return port7ano.layout
    if pathname == '/apps/port8ano':
        return port8ano.layout
    if pathname == '/apps/port9ano':
        return port9ano.layout
    else:
        return mat1ano.layout


@app.callback(
    Output("offcanvas", "is_open"),
    Input("open-offcanvas", "n_clicks"),
    [State("offcanvas", "is_open")],
)
def toggle_offcanvas(n1, is_open):
    if n1:
        return not is_open
    return is_open

if __name__ == '__main__':
    app.run_server(debug=False)
