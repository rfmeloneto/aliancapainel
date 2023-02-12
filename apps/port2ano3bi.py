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
df_port2ano3bi = pd.read_csv(DATA_PATH.joinpath("port2ano3bi.csv"))
df_habsport23bi = df_port2ano3bi.drop(columns=['Escola','Estudante','Ano','Turma','Total']) 

layout = html.Div(children=[
    
    dbc.Row(dbc.Col(dcc.Dropdown(df_port2ano3bi['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-down113bi',), width=2)),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("Domínio Geral das Habilidades"),dbc.CardBody( children=[], id='total113bi', style={'font-size':30, 'margin':'auto'})], id='cardtotal113bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF12LP04"),dbc.CardBody(children=[] , id='EF12LP043bi', style={'font-size':30, 'margin':'auto'})], id='cardEF12LP043bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF12LP10"),dbc.CardBody(children=[] , id='EF12LP103bi', style={'font-size':30, 'margin':'auto'})], id='cardEF12LP103bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF02LP16"),dbc.CardBody(children=[] , id='EF02LP163bi', style={'font-size':30, 'margin':'auto'})], id='cardEF02LP163bi')),
            ]
    ),
    dbc.Popover(
            totalgeral,
            target="total113bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF12LP04,
            target="EF12LP043bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF12LP10,
            target="EF12LP103bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF02LP16,
            target="EF02LP163bi",
            body=True,
            trigger="hover"),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF12LP17"),dbc.CardBody(children=[] , id='EF12LP173bi2', style={'font-size':30, 'margin':'auto'})], id='cardEF12LP173bi2')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF02LP20"),dbc.CardBody(children=[] , id='EF02LP203bi', style={'font-size':30, 'margin':'auto'})], id='cardEF02LP203bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF02LP25"),dbc.CardBody(children=[] , id='EF02LP253bi', style={'font-size':30, 'margin':'auto'})], id='cardEF02LP253bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF02LP26"),dbc.CardBody(children=[] , id='EF02LP263bi', style={'font-size':30, 'margin':'auto'})], id='cardEF02LP263bi')),
            ]
    ),
    dbc.Popover(
            EF12LP17,
            target="EF12LP173bi2",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF02LP20,
            target="EF02LP203bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF02LP25,
            target="EF02LP253bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF02LP26,
            target="EF02LP263bi",
            body=True,
            trigger="hover"),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF02LP28"),dbc.CardBody(children=[] , id='EF02LP283bi', style={'font-size':30, 'margin':'auto'})], id='cardEF02LP283bi'), width=3),

            ]
    ),
   
  
    dbc.Popover(
            EF02LP28,
            target="EF02LP283bi",
            body=True,
            trigger="hover"),

    html.Br(),

    dbc.Row(children=[

    dbc.Col(dcc.Dropdown(df_port2ano3bi['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-turma113bi')),
    dbc.Col(dcc.Dropdown(df_habsport23bi.columns, value="EF02LP28", style ={'margin-top':10, 'margin-left':5}, id='drop-hab113bi')),
    
]),

html.Br(),
dbc.Row(children=[

    dbc.Col( dbc.Card(dcc.Graph(id='fighabs113bi',config= {'displaylogo': False}))),
    dbc.Col( dbc.Card(dcc.Graph(id='figacerto113bi',config= {'displaylogo': False}))),


]),
    

])

@app.callback(
    Output('total113bi','children'),
    Output('cardtotal113bi', 'color'),
    Input('drop-down113bi','value')
)
def habtotal(turma):
    df = df_port2ano3bi.loc[df_port2ano3bi['Turma']==turma]
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
    Output('EF12LP043bi','children'),
    Output('cardEF12LP043bi', 'color'),
    Input('drop-down113bi','value')
)
def hab1(turma):
    df= df_port2ano3bi.loc[df_port2ano3bi['Turma']==turma]
    soma = df['EF12LP04'].values.sum()
    qtd = df['EF12LP04'].count()
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
    Output('EF12LP103bi','children'),
    Output('cardEF12LP103bi', 'color'),
    Input('drop-down113bi','value')
)
def hab2(turma):
    df= df_port2ano3bi.loc[df_port2ano3bi['Turma']==turma]
    soma = df['EF12LP10'].values.sum()
    qtd = df['EF12LP10'].count()
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
    Output('EF02LP163bi','children'),
    Output('cardEF02LP163bi', 'color'),
    Input('drop-down113bi','value')
)
def hab3(turma):
    df= df_port2ano3bi.loc[df_port2ano3bi['Turma']==turma]
    soma = df['EF02LP16'].values.sum()
    qtd = df['EF02LP16'].count()
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
    Output('EF12LP173bi2','children'),
    Output('cardEF12LP173bi2', 'color'),
    Input('drop-down113bi','value')
)
def hab4(turma):
    df= df_port2ano3bi.loc[df_port2ano3bi['Turma']==turma]
    soma = df['EF12LP17'].values.sum()
    qtd = df['EF12LP17'].count()
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
    Output('EF02LP203bi','children'),
    Output('cardEF02LP203bi', 'color'),
    Input('drop-down113bi','value')
)
def hab5(turma):
    df= df_port2ano3bi.loc[df_port2ano3bi['Turma']==turma]
    soma = df['EF02LP20'].values.sum()
    qtd = df['EF02LP20'].count()
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
    Output('EF02LP253bi','children'),
    Output('cardEF02LP253bi', 'color'),
    Input('drop-down113bi','value')
)
def hab6(turma):
    df= df_port2ano3bi.loc[df_port2ano3bi['Turma']==turma]
    soma = df['EF02LP25'].values.sum()
    qtd = df['EF02LP25'].count()
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
    Output('EF02LP263bi','children'),
    Output('cardEF02LP263bi', 'color'),
    Input('drop-down113bi','value')
)
def hab7(turma):
    df= df_port2ano3bi.loc[df_port2ano3bi['Turma']==turma]
    soma = df['EF02LP26'].values.sum()
    qtd = df['EF02LP26'].count()
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
    Output('EF02LP283bi','children'),
    Output('cardEF02LP283bi', 'color'),
    Input('drop-down113bi','value')
)
def hab10(turma):
    df= df_port2ano3bi.loc[df_port2ano3bi['Turma']==turma]
    soma = df['EF02LP28'].values.sum()
    qtd = df['EF02LP28'].count()
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
    Output('figacerto113bi','figure'),
    Input('drop-hab113bi','value'),
    Input('drop-turma113bi','value'),
)
def acertos(hab, turma):
    d = df_port2ano3bi.loc[df_port2ano3bi['Turma']==turma]
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
    Output('fighabs113bi','figure'),
    Input('drop-turma113bi','value'),
)
def habs( turma):
    df = df_port2ano3bi.loc[df_port2ano3bi['Turma']==turma]
    fig= px.histogram(df, x = 'Total', color='Total', labels= {'Total':'Percentual de Habilidades Desenvolvidas'}, title= 'Percentual de Habilidades Desenvolvidas <br> por Quantidade de Estudante'+' na turma '+str(turma).upper())
    fig.update_layout(showlegend=False)
    fig.update_yaxes( title= 'Quantidade de Estudantes')
    return fig

