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
df_port8ano = pd.read_csv(DATA_PATH.joinpath("port8ano.csv")) 
df_habsport8 = df_port8ano.drop(columns=['Escola','Estudante','Ano','Turma','Total'])

layout = html.Div(children=[
    
    dbc.Row(dbc.Col(dcc.Dropdown(df_port8ano['Turma'].unique(), value='u', style ={'margin-top':10, 'margin-left':5}, id='drop-down18',), width=2)),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("Domínio Geral das Habilidades"),dbc.CardBody( children=[], id='total18', style={'font-size':30, 'margin':'auto'})], id='cardtotal18')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF89LP14"),dbc.CardBody(children=[] , id='EF89LP14', style={'font-size':30, 'margin':'auto'})], id='cardEF89LP14')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF89LP01"),dbc.CardBody(children=[] , id='EF89LP01', style={'font-size':30, 'margin':'auto'})], id='cardEF89LP01')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF89LP16"),dbc.CardBody(children=[] , id='EF89LP16', style={'font-size':30, 'margin':'auto'})], id='cardEF89LP16')),
            ]
    ),
    dbc.Popover(
            totalgeral,
            target="total18",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF89LP14,
            target="EF89LP14",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF89LP01,
            target="EF89LP01",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF89LP16,
            target="EF89LP16",
            body=True,
            trigger="hover"),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF89LP04"),dbc.CardBody(children=[] , id='EF89LP04', style={'font-size':30, 'margin':'auto'})], id='cardEF89LP04')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF69LP56"),dbc.CardBody(children=[] , id='EF69LP56', style={'font-size':30, 'margin':'auto'})], id='cardEF69LP56')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF89LP32"),dbc.CardBody(children=[] , id='EF89LP32', style={'font-size':30, 'margin':'auto'})], id='cardEF89LP32')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF89LP17"),dbc.CardBody(children=[] , id='EF89LP17', style={'font-size':30, 'margin':'auto'})], id='cardEF89LP17')),
            ]
    ),
    dbc.Popover(
            EF89LP04,
            target="EF89LP04",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF69LP56,
            target="EF69LP56",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF89LP32,
            target="EF89LP32",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF89LP17,
            target="EF89LP17",
            body=True,
            trigger="hover"),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF89LP23"),dbc.CardBody(children=[] , id='EF89LP23', style={'font-size':30, 'margin':'auto'})], id='cardEF89LP23'), width=3),
           
            
            ]
    ),
    dbc.Popover(
            EF89LP23,
            target="EF89LP23",
            body=True,
            trigger="hover"),

    html.Br(),
dbc.Row(children=[

    dbc.Col(dcc.Dropdown(df_port8ano['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-turma17')),
    dbc.Col(dcc.Dropdown(df_habsport8.columns, value="EF89LP23", style ={'margin-top':10, 'margin-left':5}, id='drop-hab17')),
    
]),

html.Br(),
dbc.Row(children=[

    dbc.Col( dbc.Card(dcc.Graph(id='fighabs17',config= {'displaylogo': False}))),
    dbc.Col( dbc.Card(dcc.Graph(id='figacerto17',config= {'displaylogo': False}))),


]),

])

@app.callback(
    Output('total18','children'),
    Output('cardtotal18', 'color'),
    Input('drop-down18','value')
)
def habtotal(turma):
    df = df_port8ano.loc[df_port8ano['Turma']==turma]
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
    Output('EF89LP14','children'),
    Output('cardEF89LP14', 'color'),
    Input('drop-down18','value')
)
def hab1(turma):
    df= df_port8ano.loc[df_port8ano['Turma']==turma]
    soma = df['EF89LP14'].values.sum()
    qtd = df['EF89LP14'].count()
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
    Output('EF89LP01','children'),
    Output('cardEF89LP01', 'color'),
    Input('drop-down18','value')
)
def hab2(turma):
    df= df_port8ano.loc[df_port8ano['Turma']==turma]
    soma = df['EF89LP01'].values.sum()
    qtd = df['EF89LP01'].count()
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
    Output('EF89LP16','children'),
    Output('cardEF89LP16', 'color'),
    Input('drop-down18','value')
)
def hab3(turma):
    df= df_port8ano.loc[df_port8ano['Turma']==turma]
    soma = df['EF89LP16'].values.sum()
    qtd = df['EF89LP16'].count()
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
    Output('EF89LP04','children'),
    Output('cardEF89LP04', 'color'),
    Input('drop-down18','value')
)
def hab4(turma):
    df= df_port8ano.loc[df_port8ano['Turma']==turma]
    soma = df['EF89LP04'].values.sum()
    qtd = df['EF89LP04'].count()
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
    Output('EF69LP56','children'),
    Output('cardEF69LP56', 'color'),
    Input('drop-down18','value')
)
def hab5(turma):
    df= df_port8ano.loc[df_port8ano['Turma']==turma]
    soma = df['EF69LP56'].values.sum()
    qtd = df['EF69LP56'].count()
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
    Output('EF89LP32','children'),
    Output('cardEF89LP32', 'color'),
    Input('drop-down18','value')
)
def hab6(turma):
    df= df_port8ano.loc[df_port8ano['Turma']==turma]
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


#-----------------------------------------------------------------

@app.callback(
    Output('EF89LP17','children'),
    Output('cardEF89LP17', 'color'),
    Input('drop-down18','value')
)
def hab7(turma):
    df= df_port8ano.loc[df_port8ano['Turma']==turma]
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
    Output('EF89LP23','children'),
    Output('cardEF89LP23', 'color'),
    Input('drop-down18','value')
)
def hab8(turma):
    df= df_port8ano.loc[df_port8ano['Turma']==turma]
    soma = df['EF89LP23'].values.sum()
    qtd = df['EF89LP23'].count()
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
    Output('figacerto17','figure'),
    Input('drop-hab17','value'),
    Input('drop-turma17','value'),
)
def acertos(hab, turma):
    d = df_port8ano.loc[df_port8ano['Turma']==turma]
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
    Output('fighabs17','figure'),
    Input('drop-turma17','value'),
)
def habs(turma):
    df = df_port8ano.loc[df_port8ano['Turma']==turma]
    fig= px.histogram(df, x = 'Total', color='Total', labels= {'Total':'Percentual de Habilidades Desenvolvidas'}, title= 'Percentual de Habilidades Desenvolvidas <br> por Quantidade de Estudante'+' na turma '+str(turma).upper())
    fig.update_layout(showlegend=False)
    fig.update_yaxes( title= 'Quantidade de Estudantes')
    return fig
