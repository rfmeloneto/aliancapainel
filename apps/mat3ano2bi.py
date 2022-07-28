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
df_mat3ano2bi = pd.read_csv(DATA_PATH.joinpath("mat3ano2bi.csv"))
df_habs32bi= df_mat3ano2bi.drop(columns=['Escola','Estudante','Ano','Turma','Total','Unnamed: 0'])

layout = html.Div(children=[
    
    dbc.Row(dbc.Col(dcc.Dropdown(df_mat3ano2bi['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-down32bi',), width=2)), 
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("Domínio Geral das Habilidades"),dbc.CardBody( children=[], id='total32bi', style={'font-size':30, 'margin':'auto'})], id='cardtotal32bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF03MA05"),dbc.CardBody(children=[] , id='EF03MA052bi', style={'font-size':30, 'margin':'auto'})], id='cardEF03MA052bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF03MA04"),dbc.CardBody(children=[] , id='EF03MA042bi', style={'font-size':30, 'margin':'auto'})], id='cardEF03MA042bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF03MA03"),dbc.CardBody(children=[] , id='EF03MA032bi', style={'font-size':30, 'margin':'auto'})], id='cardEF03MA032bi')),
            ]
    ),

    dbc.Popover(
            totalgeral,
            target="total32bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF03MA05,
            target="EF03MA052bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF03MA04,
            target="EF03MA042bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF03MA05,
            target="EF03MA03bi",
            body=True,
            trigger="hover"),


    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF03MA16"),dbc.CardBody(children=[] , id='EF03MA162bi', style={'font-size':30, 'margin':'auto'})], id='cardEF03MA162bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF03MA24"),dbc.CardBody(children=[] , id='EF03MA242bi', style={'font-size':30, 'margin':'auto'})], id='cardEF03MA242bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF03MA20"),dbc.CardBody(children=[] , id='EF03MA202bi', style={'font-size':30, 'margin':'auto'})], id='cardEF03MA202bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF03MA27"),dbc.CardBody(children=[] , id='EF03MA272bi', style={'font-size':30, 'margin':'auto'})], id='cardEF03MA272bi')),
            ]
    ),
    html.Br(),

    dbc.Popover(
            EF03MA16,
            target="EF03MA162bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF03MA24,
            target="EF03MA242bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF03MA20,
            target="EF03MA202bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF03MA27,
            target="EF03MA272bi",
            body=True,
            trigger="hover"),

    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF03MA27"),dbc.CardBody(children=[] , id='EF03MA272bi', style={'font-size':30, 'margin':'auto'})], id='cardEF03MA272bi'), width=3),
            dbc.Col( dbc.Card([dbc.CardHeader("EF03MA26"),dbc.CardBody(children=[] , id='EF03MA262bi', style={'font-size':30, 'margin':'auto'})], id='cardEF03MA262bi'), width=3),
            
            
            ]
    ),

    dbc.Popover(
            EF03MA27,
            target="EF03MA272bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF03MA26,
            target="EF03MA262bi",
            body=True,
            trigger="hover"),

    html.Br(),

    dbc.Row(children=[

    dbc.Col(dcc.Dropdown(df_mat3ano2bi['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='2b2b')),
    dbc.Col(dcc.Dropdown(df_habs32bi.columns, value="EF03MA27", style ={'margin-top':10, 'margin-left':5}, id='drop-hab32b')),
    
]),

html.Br(),
dbc.Row(children=[

    dbc.Col( dbc.Card(dcc.Graph(id='fighabs32b',config= {'displaylogo': False}))),
    dbc.Col( dbc.Card(dcc.Graph(id='figacerto32b',config= {'displaylogo': False}))),


]),


])

@app.callback(
    Output('total3','children'),
    Output('cardtotal3', 'color'),
    Input('drop-down3','value')
)
def habtotal(turma):
    df = df_mat3ano2bi.loc[df_mat3ano2bi['Turma']==turma]
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
    Output('EF03MA052bi','children'),
    Output('cardEF03MA052bi', 'color'),
    Input('drop-down32bi','value')
)
def hab1(turma):
    df= df_mat3ano2bi.loc[df_mat3ano2bi['Turma']==turma]
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
    Output('EF03MA042bi','children'),
    Output('cardEF03MA042bi', 'color'),
    Input('drop-down32bi','value')
)
def hab2(turma):
    df= df_mat3ano2bi.loc[df_mat3ano2bi['Turma']==turma]
    soma = df['EF03MA04'].values.sum()
    qtd = df['EF03MA04'].count()
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
    Output('EF03MA032bi','children'),
    Output('cardEF03MA032bi', 'color'),
    Input('drop-down32bi','value')
)
def hab3(turma):
    df= df_mat3ano2bi.loc[df_mat3ano2bi['Turma']==turma]
    soma = df['EF03MA03'].values.sum()
    qtd = df['EF03MA03'].count()
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
    Output('EF03MA162bi','children'),
    Output('cardEF03MA162bi', 'color'),
    Input('drop-down32bi','value')
)
def hab4(turma):
    df= df_mat3ano2bi.loc[df_mat3ano2bi['Turma']==turma]
    soma = df['EF03MA16'].values.sum()
    qtd = df['EF03MA16'].count()
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
    Output('EF03MA242bi','children'),
    Output('cardEF03MA242bi', 'color'),
    Input('drop-down32bi','value')
)
def hab5(turma):
    df= df_mat3ano2bi.loc[df_mat3ano2bi['Turma']==turma]
    soma = df['EF03MA24'].values.sum()
    qtd = df['EF03MA24'].count()
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
    Output('EF03MA202bi','children'),
    Output('cardEF03MA202bi', 'color'),
    Input('drop-down32bi','value')
)
def hab6(turma):
    df= df_mat3ano2bi.loc[df_mat3ano2bi['Turma']==turma]
    soma = df['EF03MA20'].values.sum()
    qtd = df['EF03MA20'].count()
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
    Output('EF03MA272bi','children'),
    Output('cardEF03MA272bi', 'color'),
    Input('drop-down32bi','value')
)
def hab7(turma):
    df= df_mat3ano2bi.loc[df_mat3ano2bi['Turma']==turma]
    soma = df['EF03MA27'].values.sum()
    qtd = df['EF03MA27'].count()
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
    Output('EF03MA262bi','children'),
    Output('cardEF03MA262bi', 'color'),
    Input('drop-down3','value')
)
def hab8(turma):
    df= df_mat3ano2bi.loc[df_mat3ano2bi['Turma']==turma]
    soma = df['EF03MA26'].values.sum()
    qtd = df['EF03MA26'].count()
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
    Output('figacerto32b','figure'),
    Input('drop-hab32b','value'),
    Input('drop-turma32b','value'),
)
def acertos(hab, turma):
    d = df_mat3ano2bi.loc[df_mat3ano2bi['Turma']==turma]
    dff= d[hab]
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
    Output('fighabs32b','figure'),
    Input('2b2b','value'),
)
def habs(turma):
    df = df_mat3ano2bi.loc[df_mat3ano2bi['Turma']==turma]
    fig= px.histogram(df, x = 'Total', color='Total', labels= {'Total':'Percentual de Habilidades Desenvolvidas'}, title= 'Percentual de Habilidades Desenvolvidas <br> por Quantidade de Estudante'+' na turma '+str(turma).upper())
    fig.update_layout(showlegend=False)
    fig.update_yaxes( title= 'Quantidade de Estudantes')
    return fig

