import pathlib

import dash_bootstrap_components as dbc
import dash_html_components as html
import pandas as pd
import plotly.express as px
from app import app
from dash import dcc
from dash.dependencies import Input, Output
from dicionario import *

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()
df_mat1ano3bi = pd.read_csv(DATA_PATH.joinpath("mat1ano3bi.csv"))
df_habs13bi = df_mat1ano3bi.drop(columns=['Escola','Estudante','Ano','Turma','Total'])

layout = html.Div(children=[
    
    dbc.Row(children = [ 
        dbc.Col(dcc.Dropdown(df_mat1ano3bi['Escola'].unique(), value='Duque de Caxias', style ={'margin-top':10, 'margin-left':5}, id='escola3b',), width=2), 
        dbc.Col(dcc.Dropdown(df_mat1ano3bi['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-down3b',), width=2),
        ]),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("Domínio Geral das Habilidades"),dbc.CardBody( children=[], id='total3b', style={'font-size':30, 'margin':'auto'})], id='cardtotal3b'),width=3),
            dbc.Col( dbc.Card([dbc.CardHeader("EF01MA04"),dbc.CardBody(children=[] , id='EF01MA043b', style={'font-size':30, 'margin':'auto'})], id='cardEF01MA043b'),width=3),
            dbc.Col( dbc.Card([dbc.CardHeader("EF01MA05"),dbc.CardBody(children=[] , id='EF01MA053b', style={'font-size':30, 'margin':'auto'})], id='cardEF01MA053b'),width=3),
            dbc.Col( dbc.Card([dbc.CardHeader("EF01MA06"),dbc.CardBody(children=[] , id='EF01MA063b', style={'font-size':30, 'margin':'auto'})], id='cardEF01MA063b'),width=3),
            ]
            
    ),
    dbc.Popover(
            totalgeral,
            target="total3b",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF01MA04,
            target="EF01MA043b",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF01MA05,
            target="EF01MA053b",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF01MA06,
            target="EF01MA063b",
            body=True,
            trigger="hover"),
    

    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF01MA07"),dbc.CardBody(children=[] , id='EF01MA073b', style={'font-size':30, 'margin':'auto'})], id='cardEF01MA073b'),width=3),
            dbc.Col( dbc.Card([dbc.CardHeader("EF01MA08"),dbc.CardBody(children=[] , id='EF01MA083b', style={'font-size':30, 'margin':'auto'})], id='cardEF01MA083b'),width=3),
            dbc.Col( dbc.Card([dbc.CardHeader("EF01MA15"),dbc.CardBody(children=[] , id='EF01MA153b', style={'font-size':30, 'margin':'auto'})], id='cardEF01MA153b'),width=3),
            dbc.Col( dbc.Card([dbc.CardHeader("EF01MA10"),dbc.CardBody(children=[] , id='EF01MA103b', style={'font-size':30, 'margin':'auto'})], id='cardEF01MA103b'),width=3),
            ],


    ),


    dbc.Popover(
            EF01MA07,
            target="EF01MA073b",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF01MA08,
            target="EF01MA083b",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF01MA15,
            target="EF01MA153b",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF01MA10,
            target="EF01MA103b",
            body=True,
            trigger="hover"),

    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF01MA22"),dbc.CardBody(children=[] , id='EF01MA223b', style={'font-size':30, 'margin':'auto'})], id='cardEF01MA223b'), width=3),
            ]
    ),

    dbc.Popover(
            EF01MA22,
            target="EF01MA223b",
            body=True,
            trigger="hover"),

    html.Br(),
    

dbc.Row(children=[

    dbc.Col(dcc.Dropdown(df_mat1ano3bi['Escola'].unique(), value="Duque de Caxias", style ={'margin-top':10, 'margin-left':5}, id='drop-escola13b')),
    dbc.Col(dcc.Dropdown(df_mat1ano3bi['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-turma13b')),
    dbc.Col(dcc.Dropdown(df_habs13bi.columns, value="EF01MA05", style ={'margin-top':10, 'margin-left':5}, id='drop-hab13b')),
    
]),

html.Br(),
dbc.Row(children=[

    dbc.Col( dbc.Card(dcc.Graph(id='fighabs13b',config= {'displaylogo': False}))),
    dbc.Col( dbc.Card(dcc.Graph(id='figacerto13b',config= {'displaylogo': False}))),


]),

])

@app.callback(
    Output('total3b','children'),
    Output('cardtotal3b', 'color'),
    Input('escola3b','value'),
    Input('drop-down3b','value')
)
def habtotal(escola,turma):

    dff = df_mat1ano3bi.loc[df_mat1ano3bi['Escola']==escola]
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
    Output('EF01MA043b','children'),
    Output('cardEF01MA043b', 'color'),
    Input('escola3b','value'),
    Input('drop-down3b','value')
)
def hab1(escola,turma):
    dff = df_mat1ano3bi.loc[df_mat1ano3bi['Escola']==escola]
    df= dff.loc[dff['Turma']==turma]
    soma = df['EF01MA04'].values.sum()
    qtd = df['EF01MA04'].count()
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
    Output('EF01MA053b','children'),
    Output('cardEF01MA053b', 'color'),
    Input('escola3b','value'),
    Input('drop-down3b','value')
)
def hab2(escola,turma):
    dff = df_mat1ano3bi.loc[df_mat1ano3bi['Escola']==escola]
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
    Output('EF01MA063b','children'),
    Output('cardEF01MA063b', 'color'),
    Input('escola3b','value'),
    Input('drop-down3b','value')
)
def hab3(escola,turma):
    dff = df_mat1ano3bi.loc[df_mat1ano3bi['Escola']==escola]
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
    Output('EF01MA073b','children'),
    Output('cardEF01MA073b', 'color'),
    Input('escola3b','value'),
    Input('drop-down3b','value')
)
def hab4(escola,turma):
    dff = df_mat1ano3bi.loc[df_mat1ano3bi['Escola']==escola]
    df= dff.loc[dff['Turma']==turma]
    soma = df['EF01MA07'].values.sum()
    qtd = df['EF01MA07'].count()
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
    Output('EF01MA083b','children'),
    Output('cardEF01MA083b', 'color'),
    Input('escola3b','value'),
    Input('drop-down3b','value')
)
def hab5(escola,turma):
    dff = df_mat1ano3bi.loc[df_mat1ano3bi['Escola']==escola]
    df= dff.loc[dff['Turma']==turma]
    soma = df['EF01MA08'].values.sum()
    qtd = df['EF01MA08'].count()
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
    Output('EF01MA153b','children'),
    Output('cardEF01MA153b', 'color'),
    Input('escola3b','value'),
    Input('drop-down3b','value')
)
def hab6(escola,turma):
    dff = df_mat1ano3bi.loc[df_mat1ano3bi['Escola']==escola]
    df= dff.loc[dff['Turma']==turma]
    soma = df['EF01MA15'].values.sum()
    qtd = df['EF01MA15'].count()
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
    Output('EF01MA103b','children'),
    Output('cardEF01MA103b', 'color'),
    Input('escola3b','value'),
    Input('drop-down3b','value')
)
def hab7(escola,turma):
    dff = df_mat1ano3bi.loc[df_mat1ano3bi['Escola']==escola]
    df= dff.loc[dff['Turma']==turma]
    soma = df['EF01MA10'].values.sum()
    qtd = df['EF01MA10'].count()
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
    Output('EF01MA223b','children'),
    Output('cardEF01MA223b', 'color'),
    Input('escola3b','value'),
    Input('drop-down3b','value')
)
def hab8(escola,turma):
    dff = df_mat1ano3bi.loc[df_mat1ano3bi['Escola']==escola]
    df= dff.loc[dff['Turma']==turma]
    soma = df['EF01MA22'].values.sum()
    qtd = df['EF01MA22'].count()
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
    Output('figacerto13b','figure'),
    Input('drop-hab13b','value'),
    Input('drop-turma13b','value'),
    Input('drop-escola13b','value')
)
def acertos(hab, turma, escola):
    d = df_mat1ano3bi.loc[df_mat1ano3bi['Escola']==escola]
    df = d[d['Turma']==turma]
    dff= df[hab]
    acerto = 0
    erro = 0
    for i in dff:
        if i > 0:
            acerto= acerto+1
        else:
            erro = erro +1
    fig= px.pie( values=[acerto, erro], names = {acerto:'Apresentaram Domínio Mínimo', erro:'Não Apresentaram Domínio Mínimo'}, color={'Apresentaram Domínio Mínimo':'#0000ff','Não Apresentaram Domínio Mínimo':'#ff0000'}, title='Percentual de estudantes que mostraram <br> pelo menos domínio mínimo na habilidade '+str(hab)+' na turma '+str(turma).upper())
    return fig

@app.callback(
    Output('fighabs13b','figure'),
    Input('drop-turma13b','value'),
    Input('drop-escola13b','value')
)
def habs( turma,escola):
    d = df_mat1ano3bi.loc[df_mat1ano3bi['Escola']==escola]
    df = d[d['Turma']==turma]
    fig= px.histogram(df, x = 'Total', color='Total', labels= {'Total':'Percentual de Habilidades Desenvolvidas'}, title= 'Percentual de Habilidades Desenvolvidas <br> por Quantidade de Estudante'+' na turma '+str(turma).upper())
    fig.update_layout(showlegend=False)
    fig.update_yaxes( title= 'Quantidade de Estudantes')
    return fig

