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
df_mat2ano3bi = pd.read_csv(DATA_PATH.joinpath("mat2ano3bi.csv"))
df_habs23bi= df_mat2ano3bi.drop(columns=['Escola','Estudante','Ano','Turma','Total'])

layout = html.Div(children=[
    
    dbc.Row(dbc.Col(dcc.Dropdown(df_mat2ano3bi['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-down23bi',), width=2)),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("Domínio Geral das Habilidades"),dbc.CardBody( children=[], id='total23bi', style={'font-size':30, 'margin':'auto'})], id='cardtotal23bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF02MA04"),dbc.CardBody(children=[] , id='EF02MA043bi', style={'font-size':30, 'margin':'auto'})], id='cardEF02MA043bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF02MA08"),dbc.CardBody(children=[] , id='EF02MA083bi', style={'font-size':30, 'margin':'auto'})], id='cardEF02MA083bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF02MA10"),dbc.CardBody(children=[] , id='EF02MA103bi', style={'font-size':30, 'margin':'auto'})], id='cardEF02MA103bi')),
            ]
    ),

    dbc.Popover(
            totalgeral,
            target="total23bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF02MA04,
            target="EF02MA043bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF02MA08,
            target="EF02MA083bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF02MA10,
            target="EF02MA103bi",
            body=True,
            trigger="hover"),

    html.Br(),
     dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF02MA15"),dbc.CardBody(children=[] , id='EF02MA153bi', style={'font-size':30, 'margin':'auto'})], id='cardEF02MA153bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF02MA11"),dbc.CardBody(children=[] , id='EF02MA113bi', style={'font-size':30, 'margin':'auto'})], id='cardEF02MA113bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF02MA17"),dbc.CardBody(children=[] , id='EF02MA173bi', style={'font-size':30, 'margin':'auto'})], id='cardEF02MA173bi')),
            ]
    ),

    dbc.Popover(
            EF02MA15,
            target="EF02MA153bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF02MA11,
            target="EF02MA113bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF02MA17,
            target="EF02MA173bi",
            body=True,
            trigger="hover"),

dbc.Row(children=[

    dbc.Col(dcc.Dropdown(df_mat2ano3bi['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-turma23bi')),
    dbc.Col(dcc.Dropdown(df_habs23bi.columns, value="EF02MA10", style ={'margin-top':10, 'margin-left':5}, id='drop-hab23bi')),
    
]),

html.Br(),
dbc.Row(children=[

    dbc.Col( dbc.Card(dcc.Graph(id='fighabs23bi',config= {'displaylogo': False}))),
    dbc.Col( dbc.Card(dcc.Graph(id='figacerto23bi',config= {'displaylogo': False}))),


]),

])

@app.callback(
    Output('total23bi','children'),
    Output('cardtotal23bi', 'color'),
    Input('drop-down23bi','value')
)
def habtotal(turma):
    df = df_mat2ano3bi.loc[df_mat2ano3bi['Turma']==turma]
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
    Output('EF02MA043bi','children'),
    Output('cardEF02MA043bi', 'color'),
    Input('drop-down23bi','value')
)
def hab1(turma):
    df= df_mat2ano3bi.loc[df_mat2ano3bi['Turma']==turma]
    soma = df['EF02MA04'].values.sum()
    qtd = df['EF02MA04'].count()
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
    Output('EF02MA083bi','children'),
    Output('cardEF02MA083bi', 'color'),
    Input('drop-down23bi','value')
)
def hab2(turma):
    df= df_mat2ano3bi.loc[df_mat2ano3bi['Turma']==turma]
    soma = df['EF02MA08'].values.sum()
    qtd = df['EF02MA08'].count()
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
    Output('EF02MA103bi','children'),
    Output('cardEF02MA103bi', 'color'),
    Input('drop-down23bi','value')
)
def hab3(turma):
    df= df_mat2ano3bi.loc[df_mat2ano3bi['Turma']==turma]
    soma = df['EF02MA10'].values.sum()
    qtd = df['EF02MA10'].count()
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
    Output('EF02MA153bi','children'),
    Output('cardEF02MA153bi', 'color'),
    Input('drop-down23bi','value')
)
def hab3(turma):
    df= df_mat2ano3bi.loc[df_mat2ano3bi['Turma']==turma]
    soma = df['EF02MA15'].values.sum()
    qtd = df['EF02MA15'].count()
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
    Output('EF02MA113bi','children'),
    Output('cardEF02MA113bi', 'color'),
    Input('drop-down23bi','value')
)
def hab3(turma):
    df= df_mat2ano3bi.loc[df_mat2ano3bi['Turma']==turma]
    soma = df['EF02MA11'].values.sum()
    qtd = df['EF02MA11'].count()
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
    Output('EF02MA173bi','children'),
    Output('cardEF02MA173bi', 'color'),
    Input('drop-down23bi','value')
)
def hab3(turma):
    df= df_mat2ano3bi.loc[df_mat2ano3bi['Turma']==turma]
    soma = df['EF02MA17'].values.sum()
    qtd = df['EF02MA17'].count()
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
    Output('figacerto23bi','figure'),
    Input('drop-hab23bi','value'),
    Input('drop-turma23bi','value'),
)
def acertos(hab, turma):
    d = df_mat2ano3bi.loc[df_mat2ano3bi['Turma']==turma]
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
    Output('fighabs23bi','figure'),
    Input('drop-turma23bi','value'),
)
def habs( turma):
    df = df_mat2ano3bi.loc[df_mat2ano3bi['Turma']==turma]
    fig= px.histogram(df, x = 'Total', color='Total', labels= {'Total':'Percentual de Habilidades Desenvolvidas'}, title= 'Percentual de Habilidades Desenvolvidas <br> por Quantidade de Estudante'+' na turma '+str(turma).upper())
    fig.update_layout(showlegend=False)
    fig.update_yaxes( title= 'Quantidade de Estudantes')
    return fig

