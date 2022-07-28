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
df_mat2ano2bi = pd.read_csv(DATA_PATH.joinpath("mat2ano2bi.csv"))
df_habs22bi= df_mat2ano2bi.drop(columns=['Escola','Estudante','Ano','Turma','Total','Unnamed: 0'])

layout = html.Div(children=[
    
    dbc.Row(dbc.Col(dcc.Dropdown(df_mat2ano2bi['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-down22bi',), width=2)),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("Domínio Geral das Habilidades"),dbc.CardBody( children=[], id='total22bi', style={'font-size':30, 'margin':'auto'})], id='cardtotal22bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF02MA07"),dbc.CardBody(children=[] , id='EF02MA072bi', style={'font-size':30, 'margin':'auto'})], id='cardEF02MA072bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF02MA13"),dbc.CardBody(children=[] , id='EF02MA132bi', style={'font-size':30, 'margin':'auto'})], id='cardEF02MA132bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF02MA16"),dbc.CardBody(children=[] , id='EF02MA162bi', style={'font-size':30, 'margin':'auto'})], id='cardEF02MA162bi')),
            ]
    ),

    dbc.Popover(
            totalgeral,
            target="total22bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF02MA07,
            target="EF02MA072bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF02MA13,
            target="EF02MA132bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF02MA16,
            target="EF02MA162bi",
            body=True,
            trigger="hover"),

    html.Br(),

dbc.Row(children=[

    dbc.Col(dcc.Dropdown(df_mat2ano2bi['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-turma22bi')),
    dbc.Col(dcc.Dropdown(df_habs22bi.columns, value="EF02MA16", style ={'margin-top':10, 'margin-left':5}, id='drop-hab22bi')),
    
]),

html.Br(),
dbc.Row(children=[

    dbc.Col( dbc.Card(dcc.Graph(id='fighabs22bi',config= {'displaylogo': False}))),
    dbc.Col( dbc.Card(dcc.Graph(id='figacerto22bi',config= {'displaylogo': False}))),


]),

])

@app.callback(
    Output('total22bi','children'),
    Output('cardtotal22bi', 'color'),
    Input('drop-down22bi','value')
)
def habtotal(turma):
    df = df_mat2ano2bi.loc[df_mat2ano2bi['Turma']==turma]
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
    Output('EF02MA072bi','children'),
    Output('cardEF02MA072bi', 'color'),
    Input('drop-down22bi','value')
)
def hab1(turma):
    df= df_mat2ano2bi.loc[df_mat2ano2bi['Turma']==turma]
    soma = df['EF02MA07'].values.sum()
    qtd = df['EF02MA07'].count()
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
    Output('EF02MA132bi','children'),
    Output('cardEF02MA132bi', 'color'),
    Input('drop-down22bi','value')
)
def hab2(turma):
    df= df_mat2ano2bi.loc[df_mat2ano2bi['Turma']==turma]
    soma = df['EF02MA13'].values.sum()
    qtd = df['EF02MA13'].count()
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
    Output('EF02MA162bi','children'),
    Output('cardEF02MA162bi', 'color'),
    Input('drop-down22bi','value')
)
def hab3(turma):
    df= df_mat2ano2bi.loc[df_mat2ano2bi['Turma']==turma]
    soma = df['EF02MA16'].values.sum()
    qtd = df['EF02MA16'].count()
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
@app.callback(
    Output('figacerto22bi','figure'),
    Input('drop-hab22bi','value'),
    Input('drop-turma22bi','value'),
)
def acertos(hab, turma):
    d = df_mat2ano2bi.loc[df_mat2ano2bi['Turma']==turma]
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
    Output('fighabs22bi','figure'),
    Input('drop-turma22bi','value'),
)
def habs( turma):
    df = df_mat2ano2bi.loc[df_mat2ano2bi['Turma']==turma]
    fig= px.histogram(df, x = 'Total', color='Total', labels= {'Total':'Percentual de Habilidades Desenvolvidas'}, title= 'Percentual de Habilidades Desenvolvidas <br> por Quantidade de Estudante'+' na turma '+str(turma).upper())
    fig.update_layout(showlegend=False)
    fig.update_yaxes( title= 'Quantidade de Estudantes')
    return fig

