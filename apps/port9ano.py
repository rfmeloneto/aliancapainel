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
df_port9ano = pd.read_csv(DATA_PATH.joinpath("port9ano.csv")) 
df_habsport9 = df_port9ano.drop(columns=['Escola','Estudante','Ano','Turma','Total'])

layout = html.Div(children=[
    
    dbc.Row(dbc.Col(dcc.Dropdown(df_port9ano['Turma'].unique(), value='u', style ={'margin-top':10, 'margin-left':5}, id='drop-down19',), width=2)),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("Domínio Geral das Habilidades"),dbc.CardBody( children=[], id='total19', style={'font-size':30, 'margin':'auto'})], id='cardtotal19')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF89LP05"),dbc.CardBody(children=[] , id='EF89LP05', style={'font-size':30, 'margin':'auto'})], id='cardEF89LP05')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF09LP12"),dbc.CardBody(children=[] , id='EF09LP12', style={'font-size':30, 'margin':'auto'})], id='cardEF09LP12')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF89LP02"),dbc.CardBody(children=[] , id='EF89LP02', style={'font-size':30, 'margin':'auto'})], id='cardEF89LP02')),
            ]
    ),
    dbc.Popover(
            totalgeral,
            target="total19",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF89LP05,
            target="EF89LP05",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF09LP12,
            target="EF09LP12",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF89LP02,
            target="EF89LP02",
            body=True,
            trigger="hover"),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF09LP01"),dbc.CardBody(children=[] , id='EF09LP01', style={'font-size':30, 'margin':'auto'})], id='cardEF09LP01')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF89LP29"),dbc.CardBody(children=[] , id='EF89LP29', style={'font-size':30, 'margin':'auto'})], id='cardEF89LP29')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF89LP17"),dbc.CardBody(children=[] , id='EF89LP173', style={'font-size':30, 'margin':'auto'})], id='cardEF89LP173')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF89LP32"),dbc.CardBody(children=[] , id='EF89LP323', style={'font-size':30, 'margin':'auto'})], id='cardEF89LP323')),
            ]
    ),
    dbc.Popover(
            EF09LP01,
            target="EF09LP01",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF89LP29,
            target="EF89LP29",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF89LP17,
            target="EF89LP173",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF89LP32,
            target="EF89LP323",
            body=True,
            trigger="hover"),
    html.Br(),

    dbc.Row(children=[

    dbc.Col(dcc.Dropdown(df_port9ano['Turma'].unique(), value='u', style ={'margin-top':10, 'margin-left':5}, id='drop-turma18')),
    dbc.Col(dcc.Dropdown(df_habsport9.columns, value="EF89LP32", style ={'margin-top':10, 'margin-left':5}, id='drop-hab18')),
    
]),

html.Br(),
dbc.Row(children=[

    dbc.Col( dbc.Card(dcc.Graph(id='fighabs18',config= {'displaylogo': False}))),
    dbc.Col( dbc.Card(dcc.Graph(id='figacerto18',config= {'displaylogo': False}))),


]),



])

@app.callback(
    Output('total19','children'),
    Output('cardtotal19', 'color'),
    Input('drop-down19','value')
)
def habtotal(turma):
    df = df_port9ano.loc[df_port9ano['Turma']==turma]
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
    Output('EF89LP05','children'),
    Output('cardEF89LP05', 'color'),
    Input('drop-down19','value')
)
def hab1(turma):
    df= df_port9ano.loc[df_port9ano['Turma']==turma]
    soma = df['EF89LP05'].values.sum()
    qtd = df['EF89LP05'].count()
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
    Output('EF09LP12','children'),
    Output('cardEF09LP12', 'color'),
    Input('drop-down19','value')
)
def hab2(turma):
    df= df_port9ano.loc[df_port9ano['Turma']==turma]
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
    Output('EF89LP02','children'),
    Output('cardEF89LP02', 'color'),
    Input('drop-down19','value')
)
def hab3(turma):
    df= df_port9ano.loc[df_port9ano['Turma']==turma] 
    soma = df['EF89LP02'].values.sum()
    qtd = df['EF89LP02'].count()
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
    Output('EF09LP01','children'),
    Output('cardEF09LP01', 'color'),
    Input('drop-down19','value')
)
def hab4(turma):
    df= df_port9ano.loc[df_port9ano['Turma']==turma]
    soma = df['EF09LP01'].values.sum()
    qtd = df['EF09LP01'].count()
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
    Output('EF89LP29','children'),
    Output('cardEF89LP29', 'color'),
    Input('drop-down19','value')
)
def hab5(turma):
    df= df_port9ano.loc[df_port9ano['Turma']==turma]
    soma = df['EF89LP29'].values.sum()
    qtd = df['EF89LP29'].count()
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
    Output('EF89LP173','children'),
    Output('cardEF89LP173', 'color'),
    Input('drop-down19','value')
)
def hab6(turma):
    df= df_port9ano.loc[df_port9ano['Turma']==turma]
    soma = df['EF89LP17'].values.sum()
    qtd = df['EF89LP17'].count()
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
    Output('EF89LP323','children'),
    Output('cardEF89LP323', 'color'),
    Input('drop-down19','value')
)
def hab7(turma):
    df= df_port9ano.loc[df_port9ano['Turma']==turma]
    soma = df['EF89LP32'].values.sum()
    qtd = df['EF89LP32'].count()
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
    Output('figacerto18','figure'),
    Input('drop-hab18','value'),
    Input('drop-turma18','value'),
)
def acertos(hab, turma):
    d = df_port9ano.loc[df_port9ano['Turma']==turma]
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
    Output('fighabs18','figure'),
    Input('drop-turma18','value'),
)
def habs(turma):
    df = df_port9ano.loc[df_port9ano['Turma']==turma]
    fig= px.histogram(df, x = 'Total', color='Total', labels= {'Total':'Percentual de Habilidades Desenvolvidas'}, title= 'Percentual de Habilidades Desenvolvidas <br> por Quantidade de Estudante'+' na turma '+str(turma).upper())
    fig.update_layout(showlegend=False)
    fig.update_yaxes( title= 'Quantidade de Estudantes')
    return fig

