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
df_mat9ano = pd.read_csv(DATA_PATH.joinpath("mat9ano.csv")) 

layout = html.Div(children=[
    
    dbc.Row(dbc.Col(dcc.Dropdown(df_mat9ano['Turma'].unique(), value='u', style ={'margin-top':10, 'margin-left':5}, id='drop-down9',), width=2)),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("Domínio Geral das Habilidades"),dbc.CardBody( children=[], id='total9', style={'font-size':30, 'margin':'auto'})], id='cardtotal9')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF09MA03"),dbc.CardBody(children=[] , id='EF09MA03', style={'font-size':30, 'margin':'auto'})], id='cardEF09MA03')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF09MA03bTO"),dbc.CardBody(children=[] , id='EF09MA03bTO', style={'font-size':30, 'margin':'auto'})], id='cardEF09MA03bTO')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF09MA17"),dbc.CardBody(children=[] , id='EF09MA17', style={'font-size':30, 'margin':'auto'})], id='cardEF09MA17')),
            ]
    ),
    dbc.Popover(
            totalgeral,
            target="total9",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF09MA03,
            target="EF09MA03",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF09MA03bTO,
            target="EF09MA03bTO",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF09MA17,
            target="EF09MA17",
            body=True,
            trigger="hover"),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF09MA23aTO"),dbc.CardBody(children=[] , id='EF09MA23aTO', style={'font-size':30, 'margin':'auto'})], id='cardEF09MA23aTO')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF09MA03aTO"),dbc.CardBody(children=[] , id='EF09MA03aTO', style={'font-size':30, 'margin':'auto'})], id='cardEF09MA03aTO')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF09MA02"),dbc.CardBody(children=[] , id='EF09MA02', style={'font-size':30, 'margin':'auto'})], id='cardEF09MA02')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF09MA02aTO"),dbc.CardBody(children=[] , id='EF09MA02aTO', style={'font-size':30, 'margin':'auto'})], id='cardEF09MA02aTO')),
            ]
    ),
    dbc.Popover(
            EF09MA23aTO,
            target="EF09MA23aTO",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF09MA03aTO,
            target="EF09MA03aTO",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF09MA02,
            target="EF09MA02",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF09MA02aTO,
            target="EF09MA02aTO",
            body=True,
            trigger="hover"),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF09MA01bTO"),dbc.CardBody(children=[] , id='EF09MA01bTO', style={'font-size':30, 'margin':'auto'})], id='cardEF09MA01bTO'), width=3),
            dbc.Col( dbc.Card([dbc.CardHeader("EF09MA09aTO"),dbc.CardBody(children=[] , id='EF09MA09aTO', style={'font-size':30, 'margin':'auto'})], id='cardEF09MA09aTO'), width=3),
            dbc.Col( dbc.Card([dbc.CardHeader("EF09MA23bTO"),dbc.CardBody(children=[] , id='EF09MA23bTO', style={'font-size':30, 'margin':'auto'})], id='cardEF09MA23bTO'), width=3),
            dbc.Col( dbc.Card([dbc.CardHeader("EF09MA04"),dbc.CardBody(children=[] , id='EF09MA04', style={'font-size':30, 'margin':'auto'})], id='cardEF09MA04'), width=3),
            
            ]
    ),
    dbc.Popover(
            EF09MA01bTO,
            target="EF09MA01bTO",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF09MA09aTO,
            target="EF09MA09aTO",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF09MA23bTO,
            target="EF09MA23bTO",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF09MA04,
            target="EF09MA04",
            body=True,
            trigger="hover"),

    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF09MA09bTO"),dbc.CardBody(children=[] , id='EF09MA09bTO', style={'font-size':30, 'margin':'auto'})], id='cardEF09MA09bTO')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF09MA10"),dbc.CardBody(children=[] , id='EF09MA10', style={'font-size':30, 'margin':'auto'})], id='cardEF09MA10')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF09MA23"),dbc.CardBody(children=[] , id='EF09MA23', style={'font-size':30, 'margin':'auto'})], id='cardEF09MA23')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF09MA09"),dbc.CardBody(children=[] , id='EF09MA09', style={'font-size':30, 'margin':'auto'})], id='cardEF09MA09')),
            ]
    ),
    dbc.Popover(
            EF09MA09bTO,
            target="EF09MA09bTO",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF09MA10,
            target="EF09MA10",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF09MA23,
            target="EF09MA23",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF09MA09,
            target="EF09MA09",
            body=True,
            trigger="hover"),


    html.Br(),

])

@app.callback(
    Output('total9','children'),
    Output('cardtotal9', 'color'),
    Input('drop-down9','value')
)
def habtotal(turma):
    df = df_mat9ano.loc[df_mat9ano['Turma']==turma]
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
    Output('EF09MA03','children'),
    Output('cardEF09MA03', 'color'),
    Input('drop-down9','value')
)
def hab1(turma):
    df= df_mat9ano.loc[df_mat9ano['Turma']==turma]
    soma = df['EF09MA03'].values.sum()
    qtd = df['EF09MA03'].count()
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
    Output('EF09MA03bTO','children'),
    Output('cardEF09MA03bTO', 'color'),
    Input('drop-down9','value')
)
def hab2(turma):
    df= df_mat9ano.loc[df_mat9ano['Turma']==turma]
    soma = df['EF09MA03bTO'].values.sum()
    qtd = df['EF09MA03bTO'].count()
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
    Output('EF09MA17','children'),
    Output('cardEF09MA17', 'color'),
    Input('drop-down9','value')
)
def hab3(turma):
    df= df_mat9ano.loc[df_mat9ano['Turma']==turma]
    soma = df['EF09MA17'].values.sum()
    qtd = df['EF09MA17'].count()
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
    Output('EF09MA23aTO','children'),
    Output('cardEF09MA23aTO', 'color'),
    Input('drop-down9','value')
)
def hab4(turma):
    df= df_mat9ano.loc[df_mat9ano['Turma']==turma]
    soma = df['EF09MA23aTO'].values.sum()
    qtd = df['EF09MA23aTO'].count()
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
    Output('EF09MA03aTO','children'),
    Output('cardEF09MA03aTO', 'color'),
    Input('drop-down9','value')
)
def hab5(turma):
    df= df_mat9ano.loc[df_mat9ano['Turma']==turma]
    soma = df['EF09MA03aTO'].values.sum()
    qtd = df['EF09MA03aTO'].count()
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
    Output('EF09MA02','children'),
    Output('cardEF09MA02', 'color'),
    Input('drop-down9','value')
)
def hab6(turma):
    df= df_mat9ano.loc[df_mat9ano['Turma']==turma]
    soma = df['EF09MA02'].values.sum()
    qtd = df['EF09MA02'].count()
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
    Output('EF09MA02aTO','children'),
    Output('cardEF09MA02aTO', 'color'),
    Input('drop-down9','value')
)
def hab7(turma):
    df= df_mat9ano.loc[df_mat9ano['Turma']==turma]
    soma = df['EF09MA02aTO'].values.sum()
    qtd = df['EF09MA02aTO'].count()
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
    Output('EF09MA01bTO','children'),
    Output('cardEF09MA01bTO', 'color'),
    Input('drop-down9','value')
)
def hab8(turma):
    df= df_mat9ano.loc[df_mat9ano['Turma']==turma]
    soma = df['EF09MA01bTO'].values.sum()
    qtd = df['EF09MA01bTO'].count()
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
    Output('EF09MA09aTO','children'),
    Output('cardEF09MA09aTO', 'color'),
    Input('drop-down9','value')
)
def hab10(turma):
    df= df_mat9ano.loc[df_mat9ano['Turma']==turma]
    soma = df['EF09MA09aTO'].values.sum()
    qtd = df['EF09MA09aTO'].count()
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
    Output('EF09MA09bTO','children'),
    Output('cardEF09MA09bTO', 'color'),
    Input('drop-down9','value')
)
def hab10(turma):
    df= df_mat9ano.loc[df_mat9ano['Turma']==turma]
    soma = df['EF09MA09bTO'].values.sum()
    qtd = df['EF09MA09bTO'].count()
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
    Output('EF09MA10','children'),
    Output('cardEF09MA10', 'color'),
    Input('drop-down9','value')
)
def hab10(turma):
    df= df_mat9ano.loc[df_mat9ano['Turma']==turma]
    soma = df['EF09MA10'].values.sum()
    qtd = df['EF09MA10'].count()
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
    Output('EF09MA23','children'),
    Output('cardEF09MA23', 'color'),
    Input('drop-down9','value')
)
def hab10(turma):
    df= df_mat9ano.loc[df_mat9ano['Turma']==turma]
    soma = df['EF09MA23'].values.sum()
    qtd = df['EF09MA23'].count()
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
    Output('EF09MA09','children'),
    Output('cardEF09MA09', 'color'),
    Input('drop-down9','value')
)
def hab10(turma):
    df= df_mat9ano.loc[df_mat9ano['Turma']==turma]
    soma = df['EF09MA09'].values.sum()
    qtd = df['EF09MA09'].count()
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
    Output('EF09MA04','children'),
    Output('cardEF09MA04', 'color'),
    Input('drop-down9','value')
)
def hab10(turma):
    df= df_mat9ano.loc[df_mat9ano['Turma']==turma]
    soma = df['EF09MA04'].values.sum()
    qtd = df['EF09MA04'].count()
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
    Output('EF09MA23bTO','children'),
    Output('cardEF09MA23bTO', 'color'),
    Input('drop-down9','value')
)
def hab10(turma):
    df= df_mat9ano.loc[df_mat9ano['Turma']==turma]
    soma = df['EF09MA23bTO'].values.sum()
    qtd = df['EF09MA23bTO'].count()
    media= soma/qtd
    media = media*100
    media = int(media)
    if media >= 50:
        return str(media), 'success'
    elif media >= 30 and media < 50 :
        return str(media) , 'warning'
    else:
        return str(media), 'danger'