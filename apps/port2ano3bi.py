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
df_port2ano2bi = pd.read_csv(DATA_PATH.joinpath("port2ano2bi.csv"))
df_habsport22bi = df_port2ano2bi.drop(columns=['Escola','Estudante','Ano','Turma','Total']) 

layout = html.Div(children=[
    
    dbc.Row(dbc.Col(dcc.Dropdown(df_port2ano2bi['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-down112bi',), width=2)),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("Domínio Geral das Habilidades"),dbc.CardBody( children=[], id='total112bi', style={'font-size':30, 'margin':'auto'})], id='cardtotal112bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF12LP04"),dbc.CardBody(children=[] , id='EF12LP042bi', style={'font-size':30, 'margin':'auto'})], id='cardEF12LP042bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF02LP09"),dbc.CardBody(children=[] , id='EF02LP092bi', style={'font-size':30, 'margin':'auto'})], id='cardEF02LP092bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF02LP11"),dbc.CardBody(children=[] , id='EF02LP112bi', style={'font-size':30, 'margin':'auto'})], id='cardEF02LP112bi')),
            ]
    ),
    dbc.Popover(
            totalgeral,
            target="total112bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF12LP04,
            target="EF12LP042bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF02LP09,
            target="EF02LP092bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF02LP11,
            target="EF02LP112bi",
            body=True,
            trigger="hover"),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF02LP03"),dbc.CardBody(children=[] , id='EF02LP032bi', style={'font-size':30, 'margin':'auto'})], id='cardEF02LP032bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF15LP14"),dbc.CardBody(children=[] , id='EF15LP142bi', style={'font-size':30, 'margin':'auto'})], id='cardEF15LP142bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF02LP04"),dbc.CardBody(children=[] , id='EF02LP042bi', style={'font-size':30, 'margin':'auto'})], id='cardEF02LP042bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF02LP01"),dbc.CardBody(children=[] , id='EF02LP012bi', style={'font-size':30, 'margin':'auto'})], id='cardEF02LP012bi')),
            ]
    ),
    dbc.Popover(
            EF02LP03,
            target="EF02LP032bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF15LP14,
            target="EF15LP142bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF02LP04,
            target="EF02LP042bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF02LP01,
            target="EF02LP012bi",
            body=True,
            trigger="hover"),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF12LP17"),dbc.CardBody(children=[] , id='EF12LP172bi', style={'font-size':30, 'margin':'auto'})], id='cardEF12LP172bi'), width=3),
            dbc.Col( dbc.Card([dbc.CardHeader("EF02LP28"),dbc.CardBody(children=[] , id='EF02LP282bi', style={'font-size':30, 'margin':'auto'})], id='cardEF02LP282bi'), width=3),
            dbc.Col( dbc.Card([dbc.CardHeader("EF02LP26"),dbc.CardBody(children=[] , id='EF02LP262bi', style={'font-size':30, 'margin':'auto'})], id='cardEF02LP262bi'), width=3),

            ]
    ),
    dbc.Popover(
            EF12LP17,
            target="EF12LP172bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF02LP26,
            target="EF02LP262bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF02LP28,
            target="EF02LP282bi",
            body=True,
            trigger="hover"),

    html.Br(),

    dbc.Row(children=[

    dbc.Col(dcc.Dropdown(df_port2ano2bi['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-turma112bi')),
    dbc.Col(dcc.Dropdown(df_habsport22bi.columns, value="EF02LP28", style ={'margin-top':10, 'margin-left':5}, id='drop-hab112bi')),
    
]),

html.Br(),
dbc.Row(children=[

    dbc.Col( dbc.Card(dcc.Graph(id='fighabs112bi',config= {'displaylogo': False}))),
    dbc.Col( dbc.Card(dcc.Graph(id='figacerto112bi',config= {'displaylogo': False}))),


]),
    

])

@app.callback(
    Output('total112bi','children'),
    Output('cardtotal112bi', 'color'),
    Input('drop-down112bi','value')
)
def habtotal(turma):
    df = df_port2ano2bi.loc[df_port2ano2bi['Turma']==turma]
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
    Output('EF12LP042bi','children'),
    Output('cardEF12LP042bi', 'color'),
    Input('drop-down112bi','value')
)
def hab1(turma):
    df= df_port2ano2bi.loc[df_port2ano2bi['Turma']==turma]
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
    Output('EF02LP092bi','children'),
    Output('cardEF02LP092bi', 'color'),
    Input('drop-down112bi','value')
)
def hab2(turma):
    df= df_port2ano2bi.loc[df_port2ano2bi['Turma']==turma]
    soma = df['EF02LP09'].values.sum()
    qtd = df['EF02LP09'].count()
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
    Output('EF02LP112bi','children'),
    Output('cardEF02LP112bi', 'color'),
    Input('drop-down112bi','value')
)
def hab3(turma):
    df= df_port2ano2bi.loc[df_port2ano2bi['Turma']==turma]
    soma = df['EF02LP11'].values.sum()
    qtd = df['EF02LP11'].count()
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
    Output('EF02LP032bi','children'),
    Output('cardEF02LP032bi', 'color'),
    Input('drop-down112bi','value')
)
def hab4(turma):
    df= df_port2ano2bi.loc[df_port2ano2bi['Turma']==turma]
    soma = df['EF02LP03'].values.sum()
    qtd = df['EF02LP03'].count()
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
    Output('EF15LP142bi','children'),
    Output('cardEF15LP142bi', 'color'),
    Input('drop-down112bi','value')
)
def hab5(turma):
    df= df_port2ano2bi.loc[df_port2ano2bi['Turma']==turma]
    soma = df['EF15LP14'].values.sum()
    qtd = df['EF15LP14'].count()
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
    Output('EF02LP042bi','children'),
    Output('cardEF02LP042bi', 'color'),
    Input('drop-down112bi','value')
)
def hab6(turma):
    df= df_port2ano2bi.loc[df_port2ano2bi['Turma']==turma]
    soma = df['EF02LP04'].values.sum()
    qtd = df['EF02LP04'].count()
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
    Output('EF02LP012bi','children'),
    Output('cardEF02LP012bi', 'color'),
    Input('drop-down112bi','value')
)
def hab7(turma):
    df= df_port2ano2bi.loc[df_port2ano2bi['Turma']==turma]
    soma = df['EF02LP01'].values.sum()
    qtd = df['EF02LP01'].count()
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
    Output('EF12LP172bi','children'),
    Output('cardEF12LP172bi', 'color'),
    Input('drop-down112bi','value')
)
def hab8(turma):
    df= df_port2ano2bi.loc[df_port2ano2bi['Turma']==turma]
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
    Output('EF02LP282bi','children'),
    Output('cardEF02LP282bi', 'color'),
    Input('drop-down112bi','value')
)
def hab10(turma):
    df= df_port2ano2bi.loc[df_port2ano2bi['Turma']==turma]
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

@app.callback(
    Output('EF02LP262bi','children'),
    Output('cardEF02LP262bi', 'color'),
    Input('drop-down112bi','value')
)
def hab11(turma):
    df= df_port2ano2bi.loc[df_port2ano2bi['Turma']==turma]
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
@app.callback(
    Output('figacerto112bi','figure'),
    Input('drop-hab112bi','value'),
    Input('drop-turma112bi','value'),
)
def acertos(hab, turma):
    d = df_port2ano2bi.loc[df_port2ano2bi['Turma']==turma]
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
    Output('fighabs112bi','figure'),
    Input('drop-turma112bi','value'),
)
def habs( turma):
    df = df_port2ano2bi.loc[df_port2ano2bi['Turma']==turma]
    fig= px.histogram(df, x = 'Total', color='Total', labels= {'Total':'Percentual de Habilidades Desenvolvidas'}, title= 'Percentual de Habilidades Desenvolvidas <br> por Quantidade de Estudante'+' na turma '+str(turma).upper())
    fig.update_layout(showlegend=False)
    fig.update_yaxes( title= 'Quantidade de Estudantes')
    return fig

