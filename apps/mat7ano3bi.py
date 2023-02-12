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
df_mat7ano3bi = pd.read_csv(DATA_PATH.joinpath("mat7ano3bi.csv")) 
df_habs73bi= df_mat7ano3bi.drop(columns=['Escola','Estudante','Ano','Turma','Total'])

layout = html.Div(children=[
    
    dbc.Row(dbc.Col(dcc.Dropdown(df_mat7ano3bi['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-down73bi',), width=2)),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("Domínio Geral das Habilidades"),dbc.CardBody( children=[], id='total73bi', style={'font-size':30, 'margin':'auto'})], id='cardtotal73bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF07MA10"),dbc.CardBody(children=[] , id='EF07MA103bi', style={'font-size':30, 'margin':'auto'})], id='cardEF07MA103bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF07MA12"),dbc.CardBody(children=[] , id='EF07MA123bi', style={'font-size':30, 'margin':'auto'})], id='cardEF07MA123bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF07MA31"),dbc.CardBody(children=[] , id='EF07MA313bi', style={'font-size':30, 'margin':'auto'})], id='cardEF07MA313bi')),
            ]
    ),
    dbc.Popover(
            totalgeral,
            target="total73bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF07MA10,
            target="EF07MA103bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF07MA12,
            target="EF07MA123bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF07MA31,
            target="EF07MA313bi",
            body=True,
            trigger="hover"),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF07MA18"),dbc.CardBody(children=[] , id='EF07MA183bi', style={'font-size':30, 'margin':'auto'})], id='cardEF07MA183bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF07MA27"),dbc.CardBody(children=[] , id='EF07MA273bi', style={'font-size':30, 'margin':'auto'})], id='cardEF07MA273bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF07MA32"),dbc.CardBody(children=[] , id='EF07MA323bi', style={'font-size':30, 'margin':'auto'})], id='cardEF07MA323bi')),
            ]
    ),
    dbc.Popover(
            EF07MA18,
            target="EF07MA183bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF07MA27,
            target="EF07MA273bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF07MA32,
            target="EF07MA323bi",
            body=True,
            trigger="hover"),
    
   
    
    html.Br(),

    dbc.Row(children=[

    dbc.Col(dcc.Dropdown(df_mat7ano3bi['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-turma73bi')),
    dbc.Col(dcc.Dropdown(df_habs73bi.columns, value="EF07MA32", style ={'margin-top':10, 'margin-left':5}, id='drop-hab73bi')),
    ]),

    html.Br(),
    dbc.Row(children=[

    dbc.Col( dbc.Card(dcc.Graph(id='fighabs73bi',config= {'displaylogo': False}))),
    dbc.Col( dbc.Card(dcc.Graph(id='figacerto73bi',config= {'displaylogo': False}))),
])

])

@app.callback(
    Output('total73bi','children'),
    Output('cardtotal73bi', 'color'),
    Input('drop-down73bi','value')
)
def habtotal(turma):
    df = df_mat7ano3bi.loc[df_mat7ano3bi['Turma']==turma]
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
    Output('EF07MA313bi','children'),
    Output('cardEF07MA313bi', 'color'),
    Input('drop-down73bi','value')
)
def hab3(turma):
    df= df_mat7ano3bi.loc[df_mat7ano3bi['Turma']==turma]
    soma = df['EF07MA31'].values.sum()
    qtd = df['EF07MA31'].count()
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
    Output('EF07MA183bi','children'),
    Output('cardEF07MA183bi', 'color'),
    Input('drop-down73bi','value')
)
def hab4(turma):
    df= df_mat7ano3bi.loc[df_mat7ano3bi['Turma']==turma]
    soma = df['EF07MA18'].values.sum()
    qtd = df['EF07MA18'].count()
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
    Output('EF07MA273bi','children'),
    Output('cardEF07MA273bi', 'color'),
    Input('drop-down73bi','value')
)
def hab5(turma):
    df= df_mat7ano3bi.loc[df_mat7ano3bi['Turma']==turma]
    soma = df['EF07MA27'].values.sum()
    qtd = df['EF07MA27'].count()
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
    Output('EF07MA103bi','children'),
    Output('cardEF07MA103bi', 'color'),
    Input('drop-down73bi','value')
)
def hab6(turma):
    df= df_mat7ano3bi.loc[df_mat7ano3bi['Turma']==turma]
    soma = df['EF07MA10'].values.sum()
    qtd = df['EF07MA10'].count()
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



#-----------------------------------------------------------------




#-----------------------------------------------------------------



#-----------------------------------------------------------------



#-----------------------------------------------------------------

@app.callback(
    Output('EF07MA323bi','children'),
    Output('cardEF07MA323bi', 'color'),
    Input('drop-down73bi','value')
)
def hab10(turma):
    df= df_mat7ano3bi.loc[df_mat7ano3bi['Turma']==turma]
    soma = df['EF07MA32'].values.sum()
    qtd = df['EF07MA32'].count()
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
    Output('EF07MA123bi','children'),
    Output('cardEF07MA123bi', 'color'),
    Input('drop-down73bi','value')
)
def hab10(turma):
    df= df_mat7ano3bi.loc[df_mat7ano3bi['Turma']==turma]
    soma = df['EF07MA12'].values.sum()
    qtd = df['EF07MA12'].count()
    media= soma/qtd
    media = media*100
    media = int(media)
    if media >= 50:
        return str(media), 'success'
    elif media >= 30 and media < 50 :
        return str(media) , 'warning'
    else:
        return str(media), 'danger'

@app.callback(
    Output('figacerto73bi','figure'),
    Input('drop-hab73bi','value'),
    Input('drop-turma73bi','value'),
)
def acertos(hab, turma):
    d = df_mat7ano3bi.loc[df_mat7ano3bi['Turma']==turma]
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
    Output('fighabs73bi','figure'),
    Input('drop-turma73bi','value'),
)
def habs(turma):
    df = df_mat7ano3bi.loc[df_mat7ano3bi['Turma']==turma]
    fig= px.histogram(df, x = 'Total', color='Total', labels= {'Total':'Percentual de Habilidades Desenvolvidas'}, title= 'Percentual de Habilidades Desenvolvidas <br> por Quantidade de Estudante'+' na turma '+str(turma).upper())
    fig.update_layout(showlegend=False)
    fig.update_yaxes( title= 'Quantidade de Estudantes')
    return fig
