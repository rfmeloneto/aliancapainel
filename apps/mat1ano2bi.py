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
df_mat1ano2bi = pd.read_csv(DATA_PATH.joinpath("mat1ano2bi.csv"))
df_habs12bi= df_mat1ano2bi.drop(columns=['Unnamed: 0','Escola','Estudante','Ano','Turma','Total'])

layout = html.Div(children=[
    
    dbc.Row(children = [ 
        dbc.Col(dcc.Dropdown(df_mat1ano2bi['Escola'].unique(), value='Duque de Caxias', style ={'margin-top':10, 'margin-left':5}, id='escola2b',), width=2), 
        dbc.Col(dcc.Dropdown(df_mat1ano2bi['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-down2b',), width=2),
        ]),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("Domínio Geral das Habilidades"),dbc.CardBody( children=[], id='total2b', style={'font-size':30, 'margin':'auto'})], id='cardtotal2b'),width=3),
            dbc.Col( dbc.Card([dbc.CardHeader("EF01MA08"),dbc.CardBody(children=[] , id='EF01MA082b', style={'font-size':30, 'margin':'auto'})], id='cardEF01MA082b'),width=3),
            dbc.Col( dbc.Card([dbc.CardHeader("EF01MA13"),dbc.CardBody(children=[] , id='EF01MA132b', style={'font-size':30, 'margin':'auto'})], id='cardEF01MA132b'),width=3),
            dbc.Col( dbc.Card([dbc.CardHeader("EF01MA16"),dbc.CardBody(children=[] , id='EF01MA162b', style={'font-size':30, 'margin':'auto'})], id='cardEF01MA162b'),width=3),
            ]
            
    ),
    dbc.Popover(
            totalgeral,
            target="total2b",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF01MA08,
            target="EF01MA082b",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF01MA13,
            target="EF01MA132b",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF01MA16,
            target="EF01MA162b",
            body=True,
            trigger="hover"),
    

    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF01MA21"),dbc.CardBody(children=[] , id='EF01MA212b', style={'font-size':30, 'margin':'auto'})], id='cardEF01MA212b'),width=3),
            dbc.Col( dbc.Card([dbc.CardHeader("EF01MA18"),dbc.CardBody(children=[] , id='EF01MA182b', style={'font-size':30, 'margin':'auto'})], id='cardEF01MA182b'),width=3),
            dbc.Col( dbc.Card([dbc.CardHeader("EF01MA06"),dbc.CardBody(children=[] , id='EF01MA062b', style={'font-size':30, 'margin':'auto'})], id='cardEF01MA062b'),width=3),
            dbc.Col( dbc.Card([dbc.CardHeader("EF01MA03"),dbc.CardBody(children=[] , id='EF01MA032b', style={'font-size':30, 'margin':'auto'})], id='cardEF01MA032b'),width=3),
            ],


    ),


    dbc.Popover(
            EF01MA21,
            target="EF01MA212b",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF01MA18,
            target="EF01MA182b",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF01MA06,
            target="EF01MA062b",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF01MA03,
            target="EF01MA032b",
            body=True,
            trigger="hover"),

    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF01MA05"),dbc.CardBody(children=[] , id='EF01MA052b', style={'font-size':30, 'margin':'auto'})], id='cardEF01MA052b'), width=3),
            ]
    ),

    dbc.Popover(
            EF01MA05,
            target="EF01MA052b",
            body=True,
            trigger="hover"),

    html.Br(),
    

dbc.Row(children=[

    dbc.Col(dcc.Dropdown(df_mat1ano2bi['Escola'].unique(), value="Duque de Caxias", style ={'margin-top':10, 'margin-left':5}, id='drop-escola12b')),
    dbc.Col(dcc.Dropdown(df_mat1ano2bi['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-turma12b')),
    dbc.Col(dcc.Dropdown(df_habs12bi.columns, value="EF01MA05", style ={'margin-top':10, 'margin-left':5}, id='drop-hab12b')),
    
]),

html.Br(),
dbc.Row(children=[

    dbc.Col( dbc.Card(dcc.Graph(id='fighabs12b',config= {'displaylogo': False}))),
    dbc.Col( dbc.Card(dcc.Graph(id='figacerto12b',config= {'displaylogo': False}))),


]),

])

@app.callback(
    Output('total','children'),
    Output('cardtotal', 'color'),
    Input('escola','value'),
    Input('drop-down','value')
)
def habtotal(escola,turma):

    dff = df_mat1ano2bi.loc[df_mat1ano2bi['Escola']==escola]
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
    Output('EF01MA082b','children'),
    Output('cardEF01MA082b', 'color'),
    Input('escola2b','value'),
    Input('drop-down2b','value')
)
def hab1(escola,turma):
    dff = df_mat1ano2bi.loc[df_mat1ano2bi['Escola']==escola]
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
    Output('EF01MA132b','children'),
    Output('cardEF01MA132b', 'color'),
    Input('escola2b','value'),
    Input('drop-down2b','value')
)
def hab2(escola,turma):
    dff = df_mat1ano2bi.loc[df_mat1ano2bi['Escola']==escola]
    df= dff.loc[dff['Turma']==turma]
    soma = df['EF01MA13'].values.sum()
    qtd = df['EF01MA13'].count()
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
    Output('EF01MA162b','children'),
    Output('cardEF01MA162b', 'color'),
    Input('escola2b','value'),
    Input('drop-down2b','value')
)
def hab3(escola,turma):
    dff = df_mat1ano2bi.loc[df_mat1ano2bi['Escola']==escola]
    df= dff.loc[dff['Turma']==turma]
    soma = df['EF01MA16'].values.sum()
    qtd = df['EF01MA16'].count()
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
    Output('EF01MA212b','children'),
    Output('cardEF01MA212b', 'color'),
    Input('escola2b','value'),
    Input('drop-down2b','value')
)
def hab4(escola,turma):
    dff = df_mat1ano2bi.loc[df_mat1ano2bi['Escola']==escola]
    df= dff.loc[dff['Turma']==turma]
    soma = df['EF01MA21'].values.sum()
    qtd = df['EF01MA21'].count()
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
    Output('EF01MA182b','children'),
    Output('cardEF01MA182b', 'color'),
    Input('escola2b','value'),
    Input('drop-down2b','value')
)
def hab5(escola,turma):
    dff = df_mat1ano2bi.loc[df_mat1ano2bi['Escola']==escola]
    df= dff.loc[dff['Turma']==turma]
    soma = df['EF01MA18'].values.sum()
    qtd = df['EF01MA18'].count()
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
    Output('EF01MA062b','children'),
    Output('cardEF01MA062b', 'color'),
    Input('escola2b','value'),
    Input('drop-down2b','value')
)
def hab6(escola,turma):
    dff = df_mat1ano2bi.loc[df_mat1ano2bi['Escola']==escola]
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
    Output('EF01MA032b','children'),
    Output('cardEF01MA032b', 'color'),
    Input('escola2b','value'),
    Input('drop-down2b','value')
)
def hab7(escola,turma):
    dff = df_mat1ano2bi.loc[df_mat1ano2bi['Escola']==escola]
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
    Output('EF01MA052b','children'),
    Output('cardEF01MA052b', 'color'),
    Input('escola2b','value'),
    Input('drop-down2b','value')
)
def hab8(escola,turma):
    dff = df_mat1ano2bi.loc[df_mat1ano2bi['Escola']==escola]
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


#-----------------------------------------------------------------
@app.callback(
    Output('figacerto12b','figure'),
    Input('drop-hab12b','value'),
    Input('drop-turma12b','value'),
    Input('drop-escola12b','value')
)
def acertos(hab, turma, escola):
    d = df_mat1ano2bi.loc[df_mat1ano2bi['Escola']==escola]
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
    Output('fighabs12b','figure'),
    Input('drop-turma12b','value'),
    Input('drop-escola12b','value')
)
def habs( turma,escola):
    d = df_mat1ano2bi.loc[df_mat1ano2bi['Escola']==escola]
    df = d[d['Turma']==turma]
    fig= px.histogram(df, x = 'Total', color='Total', labels= {'Total':'Percentual de Habilidades Desenvolvidas'}, title= 'Percentual de Habilidades Desenvolvidas <br> por Quantidade de Estudante'+' na turma '+str(turma).upper())
    fig.update_layout(showlegend=False)
    fig.update_yaxes( title= 'Quantidade de Estudantes')
    return fig

