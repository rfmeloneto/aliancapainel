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
df_port9ano3bi = pd.read_csv(DATA_PATH.joinpath("port9ano3bi.csv")) 
df_habsport93bi = df_port9ano3bi.drop(columns=['Escola','Estudante','Ano','Turma','Total'])

layout = html.Div(children=[
    
    dbc.Row(dbc.Col(dcc.Dropdown(df_port9ano3bi['Turma'].unique(), value='u', style ={'margin-top':10, 'margin-left':5}, id='drop-down193bi',), width=2)),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("Domínio Geral das Habilidades"),dbc.CardBody( children=[], id='total193bi', style={'font-size':30, 'margin':'auto'})], id='cardtotal193bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF89LP07"),dbc.CardBody(children=[] , id='EF89LP073bi', style={'font-size':30, 'margin':'auto'})], id='cardEF89LP073bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF69LP17"),dbc.CardBody(children=[] , id='EF69LP173bi', style={'font-size':30, 'margin':'auto'})], id='cardEF69LP173bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF69LP29"),dbc.CardBody(children=[] , id='EF69LP293bi', style={'font-size':30, 'margin':'auto'})], id='cardEF69LP293bi')),
            ]
    ),
    dbc.Popover(
            totalgeral,
            target="total193bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF89LP07,
            target="EF89LP073bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF69LP17,
            target="EF69LP173bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF69LP29,
            target="EF69LP293bi",
            body=True,
            trigger="hover"),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF09LP06"),dbc.CardBody(children=[] , id='EF09LP063bi', style={'font-size':30, 'margin':'auto'})], id='cardEF09LP063bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF89LP34"),dbc.CardBody(children=[] , id='EF89LP343bi', style={'font-size':30, 'margin':'auto'})], id='cardEF89LP343bi')),
            ]
    ),
    dbc.Popover(
            EF09LP06,
            target="EF09LP063bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF89LP34,
            target="EF89LP343bi",
            body=True,
            trigger="hover"),

    html.Br(),

    dbc.Row(children=[

    dbc.Col(dcc.Dropdown(df_port9ano3bi['Turma'].unique(), value='u', style ={'margin-top':10, 'margin-left':5}, id='drop-turma183bi')),
    dbc.Col(dcc.Dropdown(df_habsport93bi.columns, value="EF69LP34", style ={'margin-top':10, 'margin-left':5}, id='drop-hab183bi')),
    
]),

html.Br(),
dbc.Row(children=[

    dbc.Col( dbc.Card(dcc.Graph(id='fighabs183bi',config= {'displaylogo': False}))),
    dbc.Col( dbc.Card(dcc.Graph(id='figacerto183bi',config= {'displaylogo': False}))),


]),



])

@app.callback(
    Output('total193bi','children'),
    Output('cardtotal193bi', 'color'),
    Input('drop-down193bi','value')
)
def habtotal(turma):
    df = df_port9ano3bi.loc[df_port9ano3bi['Turma']==turma]
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
    Output('EF89LP073bi','children'),
    Output('cardEF89LP073bi', 'color'),
    Input('drop-down193bi','value')
)
def hab1(turma):
    df= df_port9ano3bi.loc[df_port9ano3bi['Turma']==turma]
    soma = df['EF89LP07'].values.sum()
    qtd = df['EF89LP07'].count()
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
    Output('EF69LP173bi','children'),
    Output('cardEF69LP173bi', 'color'),
    Input('drop-down193bi','value')
)
def hab2(turma):
    df= df_port9ano3bi.loc[df_port9ano3bi['Turma']==turma]
    soma = df['EF69LP17'].values.sum()
    qtd = df['EF69LP17'].count()
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
    Output('EF69LP293bi','children'),
    Output('cardEF69LP293bi', 'color'),
    Input('drop-down193bi','value')
)
def hab3(turma):
    df= df_port9ano3bi.loc[df_port9ano3bi['Turma']==turma] 
    soma = df['EF69LP29'].values.sum()
    qtd = df['EF69LP29'].count()
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
    Output('EF09LP063bi','children'),
    Output('cardEF09LP063bi', 'color'),
    Input('drop-down193bi','value')
)
def hab4(turma):
    df= df_port9ano3bi.loc[df_port9ano3bi['Turma']==turma]
    soma = df['EF09LP06'].values.sum()
    qtd = df['EF09LP06'].count()
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
    Output('EF89LP343bi','children'),
    Output('cardEF89LP343bi', 'color'),
    Input('drop-down193bi','value')
)
def hab5(turma):
    df= df_port9ano3bi.loc[df_port9ano3bi['Turma']==turma]
    soma = df['EF89LP34'].values.sum()
    qtd = df['EF89LP34'].count()
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
    Output('EF09LP1233bi','children'),
    Output('cardEF09LP1233bi', 'color'),
    Input('drop-down193bi','value')
)
def hab6(turma):
    df= df_port9ano3bi.loc[df_port9ano3bi['Turma']==turma]
    soma = df['EF09LP12'].values.sum()
    qtd = df['EF09LP12'].count()
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
    Output('EF69LP2733bi','children'),
    Output('cardEF69LP2733bi', 'color'),
    Input('drop-down193bi','value')
)
def hab7(turma):
    df= df_port9ano3bi.loc[df_port9ano3bi['Turma']==turma]
    soma = df['EF69LP27'].values.sum()
    qtd = df['EF69LP27'].count()
    media= soma/qtd
    media = media*100
    media = int(media)
    if media >= 50:
        return str(media), 'success'
    elif media >= 30 and media < 50 :
        return str(media) , 'warning'
    else:
        return str(media), 'danger'

#-----------------------------------------------------------------------

@app.callback(
    Output('figacerto183bi','figure'),
    Input('drop-hab183bi','value'),
    Input('drop-turma183bi','value'),
)
def acertos(hab, turma):
    d = df_port9ano3bi.loc[df_port9ano3bi['Turma']==turma]
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
    Output('fighabs183bi','figure'),
    Input('drop-turma183bi','value'),
)
def habs(turma):
    df = df_port9ano3bi.loc[df_port9ano3bi['Turma']==turma]
    fig= px.histogram(df, x = 'Total', color='Total', labels= {'Total':'Percentual de Habilidades Desenvolvidas'}, title= 'Percentual de Habilidades Desenvolvidas <br> por Quantidade de Estudante'+' na turma '+str(turma).upper())
    fig.update_layout(showlegend=False)
    fig.update_yaxes( title= 'Quantidade de Estudantes')
    return fig

