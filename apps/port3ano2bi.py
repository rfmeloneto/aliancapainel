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
df_port3ano2bi = pd.read_csv(DATA_PATH.joinpath("port3ano2bi.csv"))
df_habsport32bi = df_port3ano2bi.drop(columns=['Escola','Estudante','Ano','Turma','Total']) 

layout = html.Div(children=[
    
    dbc.Row(dbc.Col(dcc.Dropdown(df_port3ano2bi['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-down122bi',), width=2)),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("Domínio Geral das Habilidades"),dbc.CardBody( children=[], id='total122bi', style={'font-size':30, 'margin':'auto'})], id='cardtotal122bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF35LP23"),dbc.CardBody(children=[] , id='EF35LP232bi1', style={'font-size':30, 'margin':'auto'})], id='cardEF35LP232bi1')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF15LP17"),dbc.CardBody(children=[] , id='EF15LP172bi', style={'font-size':30, 'margin':'auto'})], id='cardEF15LP172bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF03LP18"),dbc.CardBody(children=[] , id='EF03LP182bi', style={'font-size':30, 'margin':'auto'})], id='cardEF03LP182bi')),
            ]
    ),
    dbc.Popover(
            totalgeral,
            target="total122bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF35LP23,
            target="EF35LP232bi1",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF15LP17,
            target="EF15LP172bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF03LP18,
            target="EF03LP182bi",
            body=True,
            trigger="hover"),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF03LP23"),dbc.CardBody(children=[] , id='EF03LP232bi', style={'font-size':30, 'margin':'auto'})], id='cardEF03LP232bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF35LP08"),dbc.CardBody(children=[] , id='EF35LP082bi', style={'font-size':30, 'margin':'auto'})], id='cardEF35LP082bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF03LP02"),dbc.CardBody(children=[] , id='EF03LP022bi', style={'font-size':30, 'margin':'auto'})], id='cardEF03LP022bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF03LP01"),dbc.CardBody(children=[] , id='EF03LP012bi', style={'font-size':30, 'margin':'auto'})], id='cardEF03LP012bi')),
            ]
    ),
    dbc.Popover(
            EF03LP23,
            target="EF03LP232bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF35LP08,
            target="EF35LP082bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF03LP02,
            target="EF03LP022bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF03LP01,
            target="EF03LP012bi",
            body=True,
            trigger="hover"),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF35LP31"),dbc.CardBody(children=[] , id='EF35LP312bi1', style={'font-size':30, 'margin':'auto'})], id='cardEF35LP312bi1'), width=3),
            
            ]
    ),
    dbc.Popover(
            EF35LP31,
            target="EF35LP312bi1",
            body=True,
            trigger="hover"),
    

    html.Br(),
    
    dbc.Row(children=[

    dbc.Col(dcc.Dropdown(df_port3ano2bi['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-turma122bi')),
    dbc.Col(dcc.Dropdown(df_habsport32bi.columns, value="EF35LP31", style ={'margin-top':10, 'margin-left':5}, id='drop-hab122bi')),
    
]),

html.Br(),
dbc.Row(children=[

    dbc.Col( dbc.Card(dcc.Graph(id='fighabs122bi',config= {'displaylogo': False}))),
    dbc.Col( dbc.Card(dcc.Graph(id='figacerto122bi',config= {'displaylogo': False}))),


]),

])

@app.callback(
    Output('total122bi','children'),
    Output('cardtotal122bi', 'color'),
    Input('drop-down122bi','value')
)
def habtotal(turma):
    df = df_port3ano2bi.loc[df_port3ano2bi['Turma']==turma]
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
    Output('EF35LP232bi1','children'),
    Output('cardEF35LP232bi1', 'color'),
    Input('drop-down122bi','value')
)
def hab1(turma):
    df= df_port3ano2bi.loc[df_port3ano2bi['Turma']==turma]
    soma = df['EF35LP23'].values.sum()
    qtd = df['EF35LP23'].count()
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
    Output('EF15LP172bi','children'),
    Output('cardEF15LP172bi', 'color'),
    Input('drop-down122bi','value')
)
def hab2(turma):
    df= df_port3ano2bi.loc[df_port3ano2bi['Turma']==turma]
    soma = df['EF15LP17'].values.sum()
    qtd = df['EF15LP17'].count()
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
    Output('EF03LP182bi','children'),
    Output('cardEF03LP182bi', 'color'),
    Input('drop-down122bi','value')
)
def hab3(turma):
    df= df_port3ano2bi.loc[df_port3ano2bi['Turma']==turma]
    soma = df['EF03LP18'].values.sum()
    qtd = df['EF03LP18'].count()
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
    Output('EF03LP232bi','children'),
    Output('cardEF03LP232bi', 'color'),
    Input('drop-down122bi','value')
)
def hab4(turma):
    df= df_port3ano2bi.loc[df_port3ano2bi['Turma']==turma]
    soma = df['EF03LP23'].values.sum()
    qtd = df['EF03LP23'].count()
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
    Output('EF35LP082bi','children'),
    Output('cardEF35LP082bi', 'color'),
    Input('drop-down122bi','value')
)
def hab5(turma):
    df= df_port3ano2bi.loc[df_port3ano2bi['Turma']==turma]
    soma = df['EF35LP08'].values.sum()
    qtd = df['EF35LP08'].count()
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
    Output('EF03LP022bi','children'),
    Output('cardEF03LP022bi', 'color'),
    Input('drop-down122bi','value')
)
def hab6(turma):
    df= df_port3ano2bi.loc[df_port3ano2bi['Turma']==turma]
    soma = df['EF03LP02'].values.sum()
    qtd = df['EF03LP02'].count()
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
    Output('EF03LP012bi','children'),
    Output('cardEF03LP012bi', 'color'),
    Input('drop-down122bi','value')
)
def hab7(turma):
    df= df_port3ano2bi.loc[df_port3ano2bi['Turma']==turma]
    soma = df['EF03LP01'].values.sum()
    qtd = df['EF03LP01'].count()
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
    Output('EF35LP312bi1','children'),
    Output('cardEF35LP312bi1', 'color'),
    Input('drop-down122bi','value')
)
def hab8(turma):
    df= df_port3ano2bi.loc[df_port3ano2bi['Turma']==turma]
    soma = df['EF35LP31'].values.sum()
    qtd = df['EF35LP31'].count()
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
    Output('figacerto122bi','figure'),
    Input('drop-hab122bi','value'),
    Input('drop-turma122bi','value'),
)
def acertos(hab, turma):
    d = df_port3ano2bi.loc[df_port3ano2bi['Turma']==turma]
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
    Output('fighabs122bi','figure'),
    Input('drop-turma122bi','value'),
)
def habs( turma):
    df = df_port3ano2bi.loc[df_port3ano2bi['Turma']==turma]
    fig= px.histogram(df, x = 'Total', color='Total', labels= {'Total':'Percentual de Habilidades Desenvolvidas'}, title= 'Percentual de Habilidades Desenvolvidas <br> por Quantidade de Estudante'+' na turma '+str(turma).upper())
    fig.update_layout(showlegend=False)
    fig.update_yaxes( title= 'Quantidade de Estudantes')
    return fig



