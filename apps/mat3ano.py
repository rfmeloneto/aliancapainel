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
df_mat3ano = pd.read_csv(DATA_PATH.joinpath("mat3ano.csv"))

layout = html.Div(children=[
    
    dbc.Row(dbc.Col(dcc.Dropdown(df_mat3ano['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-down3',), width=2)), 
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("Domínio Geral das Habilidades"),dbc.CardBody( children=[], id='total3', style={'font-size':30, 'margin':'auto'})], id='cardtotal3')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF03MA01"),dbc.CardBody(children=[] , id='EF03MA01', style={'font-size':30, 'margin':'auto'})], id='cardEF03MA01')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF03MA02"),dbc.CardBody(children=[] , id='EF03MA02', style={'font-size':30, 'margin':'auto'})], id='cardEF03MA02')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF03MA05"),dbc.CardBody(children=[] , id='EF03MA05', style={'font-size':30, 'margin':'auto'})], id='cardEF03MA05')),
            ]
    ),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF03MA07"),dbc.CardBody(children=[] , id='EF03MA07', style={'font-size':30, 'margin':'auto'})], id='cardEF03MA07')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF03MA18"),dbc.CardBody(children=[] , id='EF03MA18', style={'font-size':30, 'margin':'auto'})], id='cardEF03MA18')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF03MA10"),dbc.CardBody(children=[] , id='EF03MA10', style={'font-size':30, 'margin':'auto'})], id='cardEF03MA10')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF03MA15"),dbc.CardBody(children=[] , id='EF03MA15', style={'font-size':30, 'margin':'auto'})], id='cardEF03MA15')),
            ]
    ),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF03MA17"),dbc.CardBody(children=[] , id='EF03MA17', style={'font-size':30, 'margin':'auto'})], id='cardEF03MA17'), width=3),
            
            
            
            ]
    ),


])

@app.callback(
    Output('total3','children'),
    Output('cardtotal3', 'color'),
    Input('drop-down3','value')
)
def habtotal(turma):
    df = df_mat3ano.loc[df_mat3ano['Turma']==turma]
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
    Output('EF03MA01','children'),
    Output('cardEF03MA01', 'color'),
    Input('drop-down3','value')
)
def hab1(turma):
    df= df_mat3ano.loc[df_mat3ano['Turma']==turma]
    soma = df['EF03MA01'].values.sum()
    qtd = df['EF03MA01'].count()
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
    Output('EF03MA02','children'),
    Output('cardEF03MA02', 'color'),
    Input('drop-down3','value')
)
def hab2(turma):
    df= df_mat3ano.loc[df_mat3ano['Turma']==turma]
    soma = df['EF03MA02'].values.sum()
    qtd = df['EF03MA02'].count()
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
    Output('EF03MA05','children'),
    Output('cardEF03MA05', 'color'),
    Input('drop-down3','value')
)
def hab3(turma):
    df= df_mat3ano.loc[df_mat3ano['Turma']==turma]
    soma = df['EF03MA05'].values.sum()
    qtd = df['EF03MA05'].count()
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
    Output('EF03MA07','children'),
    Output('cardEF03MA07', 'color'),
    Input('drop-down3','value')
)
def hab4(turma):
    df= df_mat3ano.loc[df_mat3ano['Turma']==turma]
    soma = df['EF03MA07'].values.sum()
    qtd = df['EF03MA07'].count()
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
    Output('EF03MA18','children'),
    Output('cardEF03MA18', 'color'),
    Input('drop-down3','value')
)
def hab5(turma):
    df= df_mat3ano.loc[df_mat3ano['Turma']==turma]
    soma = df['EF03MA18'].values.sum()
    qtd = df['EF03MA18'].count()
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
    Output('EF03MA10','children'),
    Output('cardEF03MA10', 'color'),
    Input('drop-down3','value')
)
def hab6(turma):
    df= df_mat3ano.loc[df_mat3ano['Turma']==turma]
    soma = df['EF03MA10'].values.sum()
    qtd = df['EF03MA10'].count()
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
    Output('EF03MA15','children'),
    Output('cardEF03MA15', 'color'),
    Input('drop-down3','value')
)
def hab7(turma):
    df= df_mat3ano.loc[df_mat3ano['Turma']==turma]
    soma = df['EF03MA15'].values.sum()
    qtd = df['EF03MA15'].count()
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
    Output('EF03MA17','children'),
    Output('cardEF03MA17', 'color'),
    Input('drop-down3','value')
)
def hab8(turma):
    df= df_mat3ano.loc[df_mat3ano['Turma']==turma]
    soma = df['EF03MA17'].values.sum()
    qtd = df['EF03MA17'].count()
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
