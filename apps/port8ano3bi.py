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
df_port8ano3bi = pd.read_csv(DATA_PATH.joinpath("port8ano3bi.csv")) 
df_habsport83bi = df_port8ano3bi.drop(columns=['Escola','Estudante','Ano','Turma','Total'])

layout = html.Div(children=[
    
    dbc.Row(dbc.Col(dcc.Dropdown(df_port8ano3bi['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-down183bi',), width=2)),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("Domínio Geral das Habilidades"),dbc.CardBody(children=[], id='total183bi', style={'font-size':30, 'margin':'auto'})], id='cardtotal183bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF69LP02"),dbc.CardBody(children=[] , id='EF69LP023bi', style={'font-size':30, 'margin':'auto'})], id='cardEF69LP023bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF89LP07"),dbc.CardBody(children=[] , id='EF89LP073bi1', style={'font-size':30, 'margin':'auto'})], id='cardEF89LP073bi1')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF89LP20"),dbc.CardBody(children=[] , id='EF89LP203bi', style={'font-size':30, 'margin':'auto'})], id='cardEF89LP203bi')),
            ]
    ),
    dbc.Popover(
            totalgeral,
            target="total183bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF69LP02,
            target="EF69LP023bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF89LP07,
            target="EF89LP073bi1",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF89LP20,
            target="EF89LP203bi",
            body=True,
            trigger="hover"),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF08LP09"),dbc.CardBody(children=[] , id='EF08LP093bi', style={'font-size':30, 'margin':'auto'})], id='cardEF08LP093bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF08LP08"),dbc.CardBody(children=[] , id='EF08LP083bi', style={'font-size':30, 'margin':'auto'})], id='cardEF08LP083bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF08LP07"),dbc.CardBody(children=[] , id='EF08LP073bi', style={'font-size':30, 'margin':'auto'})], id='cardEF08LP073bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF69LP55"),dbc.CardBody(children=[] , id='EF69LP553bi', style={'font-size':30, 'margin':'auto'})], id='cardEF69LP553bi')),
            ]
    ),
    dbc.Popover(
            EF08LP09,
            target="EF08LP093bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF08LP08,
            target="EF08LP083bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF08LP07,
            target="EF08LP073bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF69LP55,
            target="EF69LP553bi",
            body=True,
            trigger="hover"),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF89LP33"),dbc.CardBody(children=[] , id='EF89LP333bi1', style={'font-size':30, 'margin':'auto'})], id='cardEF89LP333bi1'), width=3),
            dbc.Col( dbc.Card([dbc.CardHeader("EF69LP29"),dbc.CardBody(children=[] , id='EF69LP293bi1', style={'font-size':30, 'margin':'auto'})], id='cardEF69LP293bi1'), width=3),

            
            ]
    ),
    dbc.Popover(
            EF89LP33,
            target="EF89LP333bi1",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF69LP29,
            target="EF69LP293bi1",
            body=True,
            trigger="hover"),

    html.Br(),
dbc.Row(children=[

    dbc.Col(dcc.Dropdown(df_port8ano3bi['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-turma173bi')),
    dbc.Col(dcc.Dropdown(df_habsport83bi.columns, value="EF89LP33", style ={'margin-top':10, 'margin-left':5}, id='drop-hab173bi')),
    
]),

html.Br(),
dbc.Row(children=[

    dbc.Col( dbc.Card(dcc.Graph(id='fighabs173bi',config= {'displaylogo': False}))),
    dbc.Col( dbc.Card(dcc.Graph(id='figacerto173bi',config= {'displaylogo': False}))),


]),

])

@app.callback(
    Output('total183bi','children'),
    Output('cardtotal183bi', 'color'),
    Input('drop-down183bi','value')
)
def habtotal(turma):
    df = df_port8ano3bi.loc[df_port8ano3bi['Turma']==turma]
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
    Output('EF69LP023bi','children'),
    Output('cardEF69LP023bi', 'color'),
    Input('drop-down183bi','value')
)
def hab1(turma):
    df= df_port8ano3bi.loc[df_port8ano3bi['Turma']==turma]
    soma = df['EF69LP02'].values.sum()
    qtd = df['EF69LP02'].count()
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
    Output('EF89LP073bi1','children'),
    Output('cardEF89LP073bi1', 'color'),
    Input('drop-down183bi','value')
)
def hab2(turma):
    df= df_port8ano3bi.loc[df_port8ano3bi['Turma']==turma]
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
    Output('EF89LP203bi','children'),
    Output('cardEF89LP203bi', 'color'),
    Input('drop-down183bi','value')
)
def hab3(turma):
    df= df_port8ano3bi.loc[df_port8ano3bi['Turma']==turma]
    soma = df['EF89LP20'].values.sum()
    qtd = df['EF89LP20'].count()
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
    Output('EF08LP093bi','children'),
    Output('EF08LP093bi', 'color'),
    Input('drop-down183bi','value')
)
def hab4(turma):
    df= df_port8ano3bi.loc[df_port8ano3bi['Turma']==turma]
    soma = df['EF08LP09'].values.sum()
    qtd = df['EF08LP09'].count()
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
    Output('EF08LP083bi','children'),
    Output('cardEF08LP083bi', 'color'),
    Input('drop-down183bi','value')
)
def hab5(turma):
    df= df_port8ano3bi.loc[df_port8ano3bi['Turma']==turma]
    soma = df['EF08LP08'].values.sum()
    qtd = df['EF08LP08'].count()
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
    Output('EF08LP073bi','children'),
    Output('cardEF08LP073bi', 'color'),
    Input('drop-down183bi','value')
)
def hab6(turma):
    df= df_port8ano3bi.loc[df_port8ano3bi['Turma']==turma]
    soma = df['EF08LP07'].values.sum()
    qtd = df['EF08LP07'].count()
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
    Output('EF69LP553bi','children'),
    Output('cardEF69LP553bi', 'color'),
    Input('drop-down183bi','value')
)
def hab7(turma):
    df= df_port8ano3bi.loc[df_port8ano3bi['Turma']==turma]
    soma = df['EF69LP55'].values.sum()
    qtd = df['EF69LP55'].count()
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
    Output('EF89LP333bi1','children'),
    Output('cardEF89LP333bi1', 'color'),
    Input('drop-down183bi','value')
)
def hab8(turma):
    df= df_port8ano3bi.loc[df_port8ano3bi['Turma']==turma]
    soma = df['EF89LP33'].values.sum()
    qtd = df['EF89LP33'].count()
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
    Output('EF69LP293bi1','children'),
    Output('cardEF69LP293bi1', 'color'),
    Input('drop-down183bi','value')
)
def hab8(turma):
    df= df_port8ano3bi.loc[df_port8ano3bi['Turma']==turma]
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

#-----------------------------------------------------------------------

@app.callback(
    Output('figacerto173bi','figure'),
    Input('drop-hab173bi','value'),
    Input('drop-turma173bi','value'),
)
def acertos(hab, turma):
    d = df_port8ano3bi.loc[df_port8ano3bi['Turma']==turma]
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
    Output('fighabs173bi','figure'),
    Input('drop-turma173bi','value'),
)
def habs(turma):
    df = df_port8ano3bi.loc[df_port8ano3bi['Turma']==turma]
    fig= px.histogram(df, x = 'Total', color='Total', labels= {'Total':'Percentual de Habilidades Desenvolvidas'}, title= 'Percentual de Habilidades Desenvolvidas <br> por Quantidade de Estudante'+' na turma '+str(turma).upper())
    fig.update_layout(showlegend=False)
    fig.update_yaxes( title= 'Quantidade de Estudantes')
    return fig
