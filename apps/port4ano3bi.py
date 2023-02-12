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
df_port4ano3bi = pd.read_csv(DATA_PATH.joinpath("port4ano3bi.csv")) 
df_habsport43bi = df_port4ano3bi.drop(columns=['Escola','Estudante','Ano','Turma','Total'])

layout = html.Div(children=[
    
    dbc.Row(dbc.Col(dcc.Dropdown(df_port4ano3bi['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-down143bi',), width=2)),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("Domínio Geral das Habilidades"),dbc.CardBody( children=[], id='total143bi', style={'font-size':30, 'margin':'auto'})], id='cardtotal143bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF35LP14"),dbc.CardBody(children=[] , id='EF35LP143bi1', style={'font-size':30, 'margin':'auto'})], id='cardEF35LP143bi1')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF15LP15"),dbc.CardBody(children=[] , id='EF15LP153bi', style={'font-size':30, 'margin':'auto'})], id='cardEF15LP153bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF04LP19"),dbc.CardBody(children=[] , id='EF04LP1913bi', style={'font-size':30, 'margin':'auto'})], id='cardEF04LP1913bi')),
            ]
    ),
    dbc.Popover(
            totalgeral,
            target="total143bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF35LP14,
            target="EF35LP143bi1",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF15LP15,
            target="EF15LP153bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF04LP19,
            target="EF04LP1913bi",
            body=True,
            trigger="hover"),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF04LP24"),dbc.CardBody(children=[] , id='EF04LP243bi', style={'font-size':30, 'margin':'auto'})], id='cardEF04LP243bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF04LP27"),dbc.CardBody(children=[] , id='EF04LP2713bi', style={'font-size':30, 'margin':'auto'})], id='cardEF04LP2713bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF35LP24"),dbc.CardBody(children=[] , id='EF35LP2413bi', style={'font-size':30, 'margin':'auto'})], id='cardEF35LP2413bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF15LP18"),dbc.CardBody(children=[] , id='EF15LP183bi', style={'font-size':30, 'margin':'auto'})], id='cardEF15LP183bi')),
            ]
    ),
    dbc.Popover(
            EF04LP24,
            target="EF04LP243bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF04LP27,
            target="EF04LP2713bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF35LP24,
            target="EF35LP2413bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF15LP18,
            target="EF15LP183bi",
            body=True,
            trigger="hover"),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF35LP30"),dbc.CardBody(children=[] , id='EF35LP303bi', style={'font-size':30, 'margin':'auto'})], id='cardEF35LP303bi'), width=3),
           
            ]
    ),

    dbc.Popover(
            EF35LP30,
            target="EF35LP303bi",
            body=True,
            trigger="hover"),

   

dbc.Row(children=[

    dbc.Col(dcc.Dropdown(df_port4ano3bi['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-turma133bi')),
    dbc.Col(dcc.Dropdown(df_habsport43bi.columns, value="EF35LP30", style ={'margin-top':10, 'margin-left':5}, id='drop-hab133bi')),
    
]),

html.Br(),
dbc.Row(children=[

    dbc.Col( dbc.Card(dcc.Graph(id='fighabs133bi',config= {'displaylogo': False}))),
    dbc.Col( dbc.Card(dcc.Graph(id='figacerto133bi',config= {'displaylogo': False}))),


]),


])

@app.callback(
    Output('total143bi','children'),
    Output('cardtotal143bi', 'color'),
    Input('drop-down143bi','value')
)
def habtotal(turma):
    df = df_port4ano3bi.loc[df_port4ano3bi['Turma']==turma]
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
    Output('EF35LP143bi1','children'),
    Output('cardEF35LP143bi1', 'color'),
    Input('drop-down143bi','value')
)
def hab1(turma):
    df= df_port4ano3bi.loc[df_port4ano3bi['Turma']==turma]
    soma = df['EF35LP14'].values.sum()
    qtd = df['EF35LP14'].count()
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
    Output('EF15LP153bi','children'),
    Output('cardEF15LP153bi', 'color'),
    Input('drop-down143bi','value')
)
def hab2(turma):
    df= df_port4ano3bi.loc[df_port4ano3bi['Turma']==turma]
    soma = df['EF15LP15'].values.sum()
    qtd = df['EF15LP15'].count()
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
    Output('EF04LP1913bi','children'),
    Output('cardEF04LP1913bi', 'color'),
    Input('drop-down143bi','value')
)
def hab3(turma):
    df= df_port4ano3bi.loc[df_port4ano3bi['Turma']==turma]
    soma = df['EF04LP19'].values.sum()
    qtd = df['EF04LP19'].count()
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
    Output('EF04LP243bi','children'),
    Output('cardEF04LP243bi', 'color'),
    Input('drop-down143bi','value')
)
def hab4(turma):
    df= df_port4ano3bi.loc[df_port4ano3bi['Turma']==turma]
    soma = df['EF04LP24'].values.sum()
    qtd = df['EF04LP24'].count()
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
    Output('EF04LP2713bi','children'),
    Output('cardEF04LP2713bi', 'color'),
    Input('drop-down143bi','value')
)
def hab5(turma):
    df= df_port4ano3bi.loc[df_port4ano3bi['Turma']==turma]
    soma = df['EF04LP27'].values.sum()
    qtd = df['EF04LP27'].count()
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
    Output('EF35LP2413bi','children'),
    Output('cardEF35LP2413bi', 'color'),
    Input('drop-down143bi','value')
)
def hab6(turma):
    df= df_port4ano3bi.loc[df_port4ano3bi['Turma']==turma]
    soma = df['EF35LP24'].values.sum()
    qtd = df['EF35LP24'].count()
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
    Output('EF15LP183bi','children'),
    Output('cardEF15LP183bi', 'color'),
    Input('drop-down143bi','value')
)
def hab7(turma):
    df= df_port4ano3bi.loc[df_port4ano3bi['Turma']==turma]
    soma = df['EF15LP18'].values.sum()
    qtd = df['EF15LP18'].count()
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
    Output('EF35LP303bi','children'),
    Output('cardEF35LP303bi', 'color'),
    Input('drop-down143bi','value')
)
def hab8(turma):
    df= df_port4ano3bi.loc[df_port4ano3bi['Turma']==turma]
    soma = df['EF35LP30'].values.sum()
    qtd = df['EF35LP30'].count()
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
@app.callback(
    Output('figacerto133bi','figure'),
    Input('drop-hab133bi','value'),
    Input('drop-turma133bi','value'),
)
def acertos(hab, turma):
    d = df_port4ano3bi.loc[df_port4ano3bi['Turma']==turma]
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
    Output('fighabs133bi','figure'),
    Input('drop-turma133bi','value'),
)
def habs( turma):
    df = df_port4ano3bi.loc[df_port4ano3bi['Turma']==turma]
    fig= px.histogram(df, x = 'Total', color='Total', labels= {'Total':'Percentual de Habilidades Desenvolvidas'}, title= 'Percentual de Habilidades Desenvolvidas <br> por Quantidade de Estudante'+' na turma '+str(turma).upper())
    fig.update_layout(showlegend=False)
    fig.update_yaxes( title= 'Quantidade de Estudantes')
    return fig



