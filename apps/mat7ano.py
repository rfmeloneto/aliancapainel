from dash import dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import pathlib
from app import app
from dicionario import *


PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()
df_mat7ano = pd.read_csv(DATA_PATH.joinpath("mat7ano.csv")) 

layout = html.Div(children=[
    
    dbc.Row(dbc.Col(dcc.Dropdown(df_mat7ano['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-down7',), width=2)),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("Domínio Geral das Habilidades"),dbc.CardBody( children=[], id='total7', style={'font-size':30, 'margin':'auto'})], id='cardtotal7')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF07MA19"),dbc.CardBody(children=[] , id='EF07MA19', style={'font-size':30, 'margin':'auto'})], id='cardEF07MA19')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF07MA21"),dbc.CardBody(children=[] , id='EF07MA21', style={'font-size':30, 'margin':'auto'})], id='cardEF07MA21')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF07MA29"),dbc.CardBody(children=[] , id='EF07MA29', style={'font-size':30, 'margin':'auto'})], id='cardEF07MA29')),
            ]
    ),
    dbc.Popover(
            totalgeral,
            target="total7",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF07MA19,
            target="EF07MA19",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF07MA21,
            target="EF07MA21",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF07MA29,
            target="EF07MA29",
            body=True,
            trigger="hover"),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF07MA13"),dbc.CardBody(children=[] , id='EF07MA13', style={'font-size':30, 'margin':'auto'})], id='cardEF07MA13')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF07MA15"),dbc.CardBody(children=[] , id='EF07MA15', style={'font-size':30, 'margin':'auto'})], id='cardEF07MA15')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF07MA04"),dbc.CardBody(children=[] , id='EF07MA04', style={'font-size':30, 'margin':'auto'})], id='cardEF07MA04')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF07MA20"),dbc.CardBody(children=[] , id='EF07MA20', style={'font-size':30, 'margin':'auto'})], id='cardEF07MA20')),
            ]
    ),
    dbc.Popover(
            EF07MA13,
            target="EF07MA13",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF07MA15,
            target="EF07MA15",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF07MA04,
            target="EF07MA04",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF07MA20,
            target="EF07MA20",
            body=True,
            trigger="hover"),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF07MA03"),dbc.CardBody(children=[] , id='EF07MA03', style={'font-size':30, 'margin':'auto'})], id='cardEF07MA03'), width=3),
            dbc.Col( dbc.Card([dbc.CardHeader("EF07MA36"),dbc.CardBody(children=[] , id='EF07MA36', style={'font-size':30, 'margin':'auto'})], id='cardEF07MA36'), width=3),
            dbc.Col( dbc.Card([dbc.CardHeader("EF07MA01"),dbc.CardBody(children=[] , id='EF07MA01', style={'font-size':30, 'margin':'auto'})], id='cardEF07MA01'), width=3),
            
            ]
    ),

    dbc.Popover(
            EF07MA03,
            target="EF07MA03",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF07MA36,
            target="EF07MA36",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF07MA01,
            target="EF07MA01",
            body=True,
            trigger="hover"),
    html.Br(),

])

@app.callback(
    Output('total7','children'),
    Output('cardtotal7', 'color'),
    Input('drop-down7','value')
)
def habtotal(turma):
    df = df_mat7ano.loc[df_mat7ano['Turma']==turma]
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


#-----------------------------------------------------------------

@app.callback(
    Output('EF07MA29','children'),
    Output('cardEF07MA29', 'color'),
    Input('drop-down7','value')
)
def hab3(turma):
    df= df_mat7ano.loc[df_mat7ano['Turma']==turma]
    soma = df['EF07MA29'].values.sum()
    qtd = df['EF07MA29'].count()
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
    Output('EF07MA13','children'),
    Output('cardEF07MA13', 'color'),
    Input('drop-down7','value')
)
def hab4(turma):
    df= df_mat7ano.loc[df_mat7ano['Turma']==turma]
    soma = df['EF07MA13'].values.sum()
    qtd = df['EF07MA13'].count()
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
    Output('EF07MA15','children'),
    Output('cardEF07MA15', 'color'),
    Input('drop-down7','value')
)
def hab5(turma):
    df= df_mat7ano.loc[df_mat7ano['Turma']==turma]
    soma = df['EF07MA15'].values.sum()
    qtd = df['EF07MA15'].count()
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
    Output('EF07MA19','children'),
    Output('cardEF07MA19', 'color'),
    Input('drop-down7','value')
)
def hab6(turma):
    df= df_mat7ano.loc[df_mat7ano['Turma']==turma]
    soma = df['EF07MA19'].values.sum()
    qtd = df['EF07MA19'].count()
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




#-----------------------------------------------------------------

@app.callback(
    Output('EF07MA20','children'),
    Output('cardEF07MA20', 'color'),
    Input('drop-down7','value')
)
def hab8(turma):
    df= df_mat7ano.loc[df_mat7ano['Turma']==turma]
    soma = df['EF07MA20'].values.sum()
    qtd = df['EF07MA20'].count()
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
    Output('EF07MA03','children'),
    Output('cardEF07MA03', 'color'),
    Input('drop-down7','value')
)
def hab10(turma):
    df= df_mat7ano.loc[df_mat7ano['Turma']==turma]
    soma = df['EF07MA03'].values.sum()
    qtd = df['EF07MA03'].count()
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
    Output('EF07MA36','children'),
    Output('cardEF07MA36', 'color'),
    Input('drop-down7','value')
)
def hab10(turma):
    df= df_mat7ano.loc[df_mat7ano['Turma']==turma]
    soma = df['EF07MA36'].values.sum()
    qtd = df['EF07MA36'].count()
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
    Output('EF07MA01','children'),
    Output('cardEF07MA01', 'color'),
    Input('drop-down7','value')
)
def hab10(turma):
    df= df_mat7ano.loc[df_mat7ano['Turma']==turma]
    soma = df['EF07MA01'].values.sum()
    qtd = df['EF07MA01'].count()
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
    Output('EF07MA04','children'),
    Output('cardEF07MA04', 'color'),
    Input('drop-down7','value')
)
def hab10(turma):
    df= df_mat7ano.loc[df_mat7ano['Turma']==turma]
    soma = df['EF07MA04'].values.sum()
    qtd = df['EF07MA04'].count()
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
    Output('EF07MA21','children'),
    Output('cardEF07MA21', 'color'),
    Input('drop-down7','value')
)
def hab10(turma):
    df= df_mat7ano.loc[df_mat7ano['Turma']==turma]
    soma = df['EF07MA21'].values.sum()
    qtd = df['EF07MA21'].count()
    media= soma/qtd
    media = media*100
    media = int(media)
    if media >= 50:
        return str(media), 'success'
    elif media >= 30 and media < 50 :
        return str(media) , 'warning'
    else:
        return str(media), 'danger'