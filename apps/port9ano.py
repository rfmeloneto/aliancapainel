from dash import dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import pathlib
from app import app


PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()
df_port9ano = pd.read_csv(DATA_PATH.joinpath("port9ano.csv")) 

layout = html.Div(children=[
    
    dbc.Row(dbc.Col(dcc.Dropdown(df_port9ano['Turma'].unique(), value='u', style ={'margin-top':10, 'margin-left':5}, id='drop-down19',), width=2)),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("Domínio Geral das Habilidades"),dbc.CardBody( children=[], id='total19', style={'font-size':30, 'margin':'auto'})], id='cardtotal19')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF89LP05"),dbc.CardBody(children=[] , id='EF89LP05', style={'font-size':30, 'margin':'auto'})], id='cardEF89LP05')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF09LP12"),dbc.CardBody(children=[] , id='EF09LP12', style={'font-size':30, 'margin':'auto'})], id='cardEF09LP12')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF89LP02"),dbc.CardBody(children=[] , id='EF89LP02', style={'font-size':30, 'margin':'auto'})], id='cardEF89LP02')),
            ]
    ),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF09LP01"),dbc.CardBody(children=[] , id='EF09LP01', style={'font-size':30, 'margin':'auto'})], id='cardEF09LP01')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF89LP29"),dbc.CardBody(children=[] , id='EF89LP29', style={'font-size':30, 'margin':'auto'})], id='cardEF89LP29')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF89LP17"),dbc.CardBody(children=[] , id='EF89LP173', style={'font-size':30, 'margin':'auto'})], id='cardEF89LP173')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF89LP32"),dbc.CardBody(children=[] , id='EF89LP323', style={'font-size':30, 'margin':'auto'})], id='cardEF89LP323')),
            ]
    ),
    html.Br(),



])

@app.callback(
    Output('total19','children'),
    Output('cardtotal19', 'color'),
    Input('drop-down19','value')
)
def habtotal(turma):
    df = df_port9ano.loc[df_port9ano['Turma']==turma]
    soma = df['Total'].values.sum()
    qtd = df['Total'].count()
    soma=int(soma)
    qtd= int(qtd)
    media= soma//qtd
    if media >= 50:
        return str(media), 'success'
    elif media >= 30 and media < 50 :
        return str(media) , 'warning'
    else:
        return str(media), 'danger'
#----------------------------------------------------------------------
@app.callback(
    Output('EF89LP05','children'),
    Output('cardEF89LP05', 'color'),
    Input('drop-down19','value')
)
def hab1(turma):
    df= df_port9ano.loc[df_port9ano['Turma']==turma]
    soma = df['EF89LP05'].values.sum()
    qtd = df['EF89LP05'].count()
    media= soma/qtd
    media = media*100
    media = int(media)
    if media >= 50:
        return str(media), 'success'
    elif media >= 30 and media < 50 :
        return str(media) , 'warning'
    else:
        return str(media), 'danger'

#-----------------------------------------------------------------

@app.callback(
    Output('EF09LP12','children'),
    Output('cardEF09LP12', 'color'),
    Input('drop-down19','value')
)
def hab2(turma):
    df= df_port9ano.loc[df_port9ano['Turma']==turma]
    soma = df['EF09LP12'].values.sum()
    qtd = df['EF09LP12'].count()
    media= soma/qtd
    media = media*100
    media = int(media)
    if media >= 50:
        return str(media), 'success'
    elif media >= 30 and media < 50 :
        return str(media) , 'warning'
    else:
        return str(media), 'danger'

#-----------------------------------------------------------------

@app.callback(
    Output('EF89LP02','children'),
    Output('cardEF89LP02', 'color'),
    Input('drop-down19','value')
)
def hab3(turma):
    df= df_port9ano.loc[df_port9ano['Turma']==turma] 
    soma = df['EF89LP02'].values.sum()
    qtd = df['EF89LP02'].count()
    media= soma/qtd
    media = media*100
    media = int(media)
    if media >= 50:
        return str(media), 'success'
    elif media >= 30 and media < 50 :
        return str(media) , 'warning'
    else:
        return str(media), 'danger'

#-----------------------------------------------------------------

@app.callback(
    Output('EF09LP01','children'),
    Output('cardEF09LP01', 'color'),
    Input('drop-down19','value')
)
def hab4(turma):
    df= df_port9ano.loc[df_port9ano['Turma']==turma]
    soma = df['EF09LP01'].values.sum()
    qtd = df['EF09LP01'].count()
    media= soma/qtd
    media = media*100
    media = int(media)
    if media >= 50:
        return str(media), 'success'
    elif media >= 30 and media < 50 :
        return str(media) , 'warning'
    else:
        return str(media), 'danger'

#-----------------------------------------------------------------

@app.callback(
    Output('EF89LP29','children'),
    Output('cardEF89LP29', 'color'),
    Input('drop-down19','value')
)
def hab5(turma):
    df= df_port9ano.loc[df_port9ano['Turma']==turma]
    soma = df['EF89LP29'].values.sum()
    qtd = df['EF89LP29'].count()
    media= soma/qtd
    media = media*100
    media = int(media)
    if media >= 50:
        return str(media), 'success'
    elif media >= 30 and media < 50 :
        return str(media) , 'warning'
    else:
        return str(media), 'danger'


#-----------------------------------------------------------------

@app.callback(
    Output('EF89LP173','children'),
    Output('cardEF89LP173', 'color'),
    Input('drop-down19','value')
)
def hab6(turma):
    df= df_port9ano.loc[df_port9ano['Turma']==turma]
    soma = df['EF89LP17'].values.sum()
    qtd = df['EF89LP17'].count()
    media= soma/qtd
    media = media*100
    media = int(media)
    if media >= 50:
        return str(media), 'success'
    elif media >= 30 and media < 50 :
        return str(media) , 'warning'
    else:
        return str(media), 'danger'


#-----------------------------------------------------------------

@app.callback(
    Output('EF89LP323','children'),
    Output('cardEF89LP323', 'color'),
    Input('drop-down19','value')
)
def hab7(turma):
    df= df_port9ano.loc[df_port9ano['Turma']==turma]
    soma = df['EF89LP32'].values.sum()
    qtd = df['EF89LP32'].count()
    media= soma/qtd
    media = media*100
    media = int(media)
    if media >= 50:
        return str(media), 'success'
    elif media >= 30 and media < 50 :
        return str(media) , 'warning'
    else:
        return str(media), 'danger'

