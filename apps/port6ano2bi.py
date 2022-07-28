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
df_port6ano2bi = pd.read_csv(DATA_PATH.joinpath("port6ano2bi.csv")) 
df_habsport62bi = df_port6ano2bi.drop(columns=['Escola','Estudante','Ano','Turma','Total'])

layout = html.Div(children=[
    
    dbc.Row(dbc.Col(dcc.Dropdown(df_port6ano2bi['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-down162bi',), width=2)),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("Domínio Geral das Habilidades"),dbc.CardBody( children=[], id='total162bi', style={'font-size':30, 'margin':'auto'})], id='cardtotal162bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF67LP04"),dbc.CardBody(children=[] , id='EF67LP042bi', style={'font-size':30, 'margin':'auto'})], id='cardEF67LP042bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF67LP03"),dbc.CardBody(children=[] , id='EF67LP032bi1', style={'font-size':30, 'margin':'auto'})], id='cardEF67LP032bi1')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF67LP06"),dbc.CardBody(children=[] , id='EF67LP0612bi', style={'font-size':30, 'margin':'auto'})], id='cardEF67LP0612bi')),
            ]
    ),
     dbc.Popover(
            totalgeral,
            target="total162bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF67LP04,
            target="EF67LP042bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF67LP03,
            target="EF67LP032bi1",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF67LP06,
            target="EF67LP0612bi",
            body=True,
            trigger="hover"),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF67LP05"),dbc.CardBody(children=[] , id='EF67LP052bi', style={'font-size':30, 'margin':'auto'})], id='cardEF67LP052bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF67LP28"),dbc.CardBody(children=[] , id='EF67LP2812bi1', style={'font-size':30, 'margin':'auto'})], id='cardEF67LP2812bi1')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF69LP54"),dbc.CardBody(children=[] , id='EF69LP542bi', style={'font-size':30, 'margin':'auto'})], id='cardEF69LP542bi')),
            ]
    ),
    dbc.Popover(
            EF67LP05,
            target="EF67LP052bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF67LP28,
            target="EF67LP2812bi1",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF69LP54,
            target="EF69LP542bi",
            body=True,
            trigger="hover"),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF67LP27"),dbc.CardBody(children=[] , id='EF67LP272bi1', style={'font-size':30, 'margin':'auto'})], id='cardEF67LP272bi1'), width=3),
           
            ]
    ),
    dbc.Popover(
            EF67LP27,
            target="EF67LP272bi1",
            body=True,
            trigger="hover"),
   
           
dbc.Row(children=[

    dbc.Col(dcc.Dropdown(df_port6ano2bi['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-turma152bi')),
    dbc.Col(dcc.Dropdown(df_habsport62bi.columns, value="EF67LP27", style ={'margin-top':10, 'margin-left':5}, id='drop-hab152bi')),
    
]),

html.Br(),
dbc.Row(children=[

    dbc.Col( dbc.Card(dcc.Graph(id='fighabs152bi',config= {'displaylogo': False}))),
    dbc.Col( dbc.Card(dcc.Graph(id='figacerto152bi',config= {'displaylogo': False}))),


]),


])

@app.callback(
    Output('total162bi','children'),
    Output('cardtotal162bi', 'color'),
    Input('drop-down162bi','value')
)
def habtotal(turma):
    df = df_port6ano2bi.loc[df_port6ano2bi['Turma']==turma]
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
    Output('EF67LP042bi','children'),
    Output('cardEF67LP042bi', 'color'),
    Input('drop-down162bi','value')
)
def hab1(turma):
    df= df_port6ano2bi.loc[df_port6ano2bi['Turma']==turma]
    soma = df['EF67LP04'].values.sum()
    qtd = df['EF67LP04'].count()
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
    Output('EF67LP032bi1','children'),
    Output('cardEF67LP032bi1', 'color'),
    Input('drop-down162bi','value')
)
def hab2(turma):
    df= df_port6ano2bi.loc[df_port6ano2bi['Turma']==turma]
    soma = df['EF67LP03'].values.sum()
    qtd = df['EF67LP03'].count()
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
    Output('EF67LP0612bi','children'),
    Output('cardEF67LP0612bi', 'color'),
    Input('drop-down162bi','value')
)
def hab3(turma):
    df= df_port6ano2bi.loc[df_port6ano2bi['Turma']==turma]
    soma = df['EF67LP06'].values.sum()
    qtd = df['EF67LP06'].count()
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
    Output('EF67LP052bi','children'),
    Output('cardEF67LP052bi', 'color'),
    Input('drop-down162bi','value')
)
def hab4(turma):
    df= df_port6ano2bi.loc[df_port6ano2bi['Turma']==turma]
    soma = df['EF67LP05'].values.sum()
    qtd = df['EF67LP05'].count()
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
    Output('EF67LP2812bi1','children'),
    Output('cardEF67LP2812bi1', 'color'),
    Input('drop-down162bi','value')
)
def hab6(turma):
    df= df_port6ano2bi.loc[df_port6ano2bi['Turma']==turma]
    soma = df['EF67LP28'].values.sum()
    qtd = df['EF67LP28'].count()
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
    Output('EF69LP542bi','children'),
    Output('cardEF69LP542bi', 'color'),
    Input('drop-down162bi','value')
)
def hab7(turma):
    df= df_port6ano2bi.loc[df_port6ano2bi['Turma']==turma]
    soma = df['EF69LP54'].values.sum()
    qtd = df['EF69LP54'].count()
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
    Output('EF67LP272bi1','children'),
    Output('cardEF67LP272bi1', 'color'),
    Input('drop-down162bi','value')
)
def hab8(turma):
    df= df_port6ano2bi.loc[df_port6ano2bi['Turma']==turma]
    soma = df['EF67LP27'].values.sum()
    qtd = df['EF67LP27'].count()
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


#-----------------------------------------------------------------------

@app.callback(
    Output('figacerto152bi','figure'),
    Input('drop-hab152bi','value'),
    Input('drop-turma152bi','value'),
)
def acertos(hab, turma):
    d = df_port6ano2bi.loc[df_port6ano2bi['Turma']==turma]
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
    Output('fighabs152bi','figure'),
    Input('drop-turma152bi','value'),
)
def habs(turma):
    df = df_port6ano2bi.loc[df_port6ano2bi['Turma']==turma]
    fig= px.histogram(df, x = 'Total', color='Total', labels= {'Total':'Percentual de Habilidades Desenvolvidas'}, title= 'Percentual de Habilidades Desenvolvidas <br> por Quantidade de Estudante'+' na turma '+str(turma).upper())
    fig.update_layout(showlegend=False)
    fig.update_yaxes( title= 'Quantidade de Estudantes')
    return fig
