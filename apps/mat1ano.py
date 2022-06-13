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
df_mat1ano = pd.read_csv(DATA_PATH.joinpath("mat1ano.csv"))

layout = html.Div(children=[
    
    dbc.Row(children = [ 
        dbc.Col(dcc.Dropdown(df_mat1ano['Escola'].unique(), value='Duque de Caxias', style ={'margin-top':10, 'margin-left':5}, id='escola',), width=2), 
        dbc.Col(dcc.Dropdown(df_mat1ano['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-down',), width=2)
        ]),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("Domínio Geral das Habilidades"),dbc.CardBody( children=[], id='total', style={'font-size':30, 'margin':'auto'})], id='cardtotal')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF01MA01"),dbc.CardBody(children=[] , id='EF01MA01', style={'font-size':30, 'margin':'auto'})], id='cardEF01MA01')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF01MA02"),dbc.CardBody(children=[] , id='EF01MA02', style={'font-size':30, 'margin':'auto'})], id='cardEF01MA02')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF01MA06"),dbc.CardBody(children=[] , id='EF01MA06', style={'font-size':30, 'margin':'auto'})], id='cardEF01MA06')),
            ]
    ),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF01MA20"),dbc.CardBody(children=[] , id='EF01MA20', style={'font-size':30, 'margin':'auto'})], id='cardEF01MA20')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF01MA03"),dbc.CardBody(children=[] , id='EF01MA03', style={'font-size':30, 'margin':'auto'})], id='cardEF01MA03')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF01MA05"),dbc.CardBody(children=[] , id='EF01MA05', style={'font-size':30, 'margin':'auto'})], id='cardEF01MA05')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF01MA09"),dbc.CardBody(children=[] , id='EF01MA09', style={'font-size':30, 'margin':'auto'})], id='cardEF01MA09')),
            ]
    ),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF01MA11"),dbc.CardBody(children=[] , id='EF01MA11', style={'font-size':30, 'margin':'auto'})], id='cardEF01MA11'), width=3),
            dbc.Col( dbc.Card([dbc.CardHeader("EF01MA12"),dbc.CardBody(children=[] , id='EF01MA12', style={'font-size':30, 'margin':'auto'})], id='cardEF01MA12'), width=3),
            
            
            ]
    ),


])

@app.callback(
    Output('total','children'),
    Output('cardtotal', 'color'),
    Input('escola','value'),
    Input('drop-down','value')
)
def habtotal(escola,turma):

    dff = df_mat1ano.loc[df_mat1ano['Escola']==escola]
    df= dff.loc[dff['Turma']==turma]
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
    Output('EF01MA01','children'),
    Output('cardEF01MA01', 'color'),
    Input('escola','value'),
    Input('drop-down','value')
)
def hab1(escola,turma):
    dff = df_mat1ano.loc[df_mat1ano['Escola']==escola]
    df= dff.loc[dff['Turma']==turma]
    soma = df['EF01MA01'].values.sum()
    qtd = df['EF01MA01'].count()
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
    Output('EF01MA02','children'),
    Output('cardEF01MA02', 'color'),
    Input('escola','value'),
    Input('drop-down','value')
)
def hab2(escola,turma):
    dff = df_mat1ano.loc[df_mat1ano['Escola']==escola]
    df= dff.loc[dff['Turma']==turma]
    soma = df['EF01MA02'].values.sum()
    qtd = df['EF01MA02'].count()
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
    Output('EF01MA06','children'),
    Output('cardEF01MA06', 'color'),
    Input('escola','value'),
    Input('drop-down','value')
)
def hab3(escola,turma):
    dff = df_mat1ano.loc[df_mat1ano['Escola']==escola]
    df= dff.loc[dff['Turma']==turma]
    soma = df['EF01MA06'].values.sum()
    qtd = df['EF01MA06'].count()
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
    Output('EF01MA20','children'),
    Output('cardEF01MA20', 'color'),
    Input('escola','value'),
    Input('drop-down','value')
)
def hab4(escola,turma):
    dff = df_mat1ano.loc[df_mat1ano['Escola']==escola]
    df= dff.loc[dff['Turma']==turma]
    soma = df['EF01MA20'].values.sum()
    qtd = df['EF01MA20'].count()
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
    Output('EF01MA03','children'),
    Output('cardEF01MA03', 'color'),
    Input('escola','value'),
    Input('drop-down','value')
)
def hab5(escola,turma):
    dff = df_mat1ano.loc[df_mat1ano['Escola']==escola]
    df= dff.loc[dff['Turma']==turma]
    soma = df['EF01MA03'].values.sum()
    qtd = df['EF01MA03'].count()
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
    Output('EF01MA05','children'),
    Output('cardEF01MA05', 'color'),
    Input('escola','value'),
    Input('drop-down','value')
)
def hab6(escola,turma):
    dff = df_mat1ano.loc[df_mat1ano['Escola']==escola]
    df= dff.loc[dff['Turma']==turma]
    soma = df['EF01MA05'].values.sum()
    qtd = df['EF01MA05'].count()
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
    Output('EF01MA09','children'),
    Output('cardEF01MA09', 'color'),
    Input('escola','value'),
    Input('drop-down','value')
)
def hab7(escola,turma):
    dff = df_mat1ano.loc[df_mat1ano['Escola']==escola]
    df= dff.loc[dff['Turma']==turma]
    soma = df['EF01MA09'].values.sum()
    qtd = df['EF01MA09'].count()
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
    Output('EF01MA11','children'),
    Output('cardEF01MA11', 'color'),
    Input('escola','value'),
    Input('drop-down','value')
)
def hab8(escola,turma):
    dff = df_mat1ano.loc[df_mat1ano['Escola']==escola]
    df= dff.loc[dff['Turma']==turma]
    soma = df['EF01MA11'].values.sum()
    qtd = df['EF01MA11'].count()
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
    Output('EF01MA12','children'),
    Output('cardEF01MA12', 'color'),
    Input('escola','value'),
    Input('drop-down','value')
)
def hab10(escola,turma):
    dff = df_mat1ano.loc[df_mat1ano['Escola']==escola]
    df= dff.loc[dff['Turma']==turma]
    soma = df['EF01MA12'].values.sum()
    qtd = df['EF01MA12'].count()
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

