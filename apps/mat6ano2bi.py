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
df_mat6ano2bi = pd.read_csv(DATA_PATH.joinpath("mat6ano2bi.csv"))
df_habs62bi= df_mat6ano2bi.drop(columns=['Escola','Estudante','Ano','Turma','Total']) 

layout = html.Div(children=[
    
    dbc.Row(dbc.Col(dcc.Dropdown(df_mat6ano2bi['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-down62bi',), width=2)),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("Domínio Geral das Habilidades"),dbc.CardBody( children=[], id='total62bi', style={'font-size':30, 'margin':'auto'})], id='cardtotal62bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF06MA07"),dbc.CardBody(children=[] , id='EF06MA072bi', style={'font-size':30, 'margin':'auto'})], id='cardEF06MA072bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF06MA32"),dbc.CardBody(children=[] , id='EF06MA322bi', style={'font-size':30, 'margin':'auto'})], id='cardEF06MA322bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF06MA10"),dbc.CardBody(children=[] , id='EF06MA102bi', style={'font-size':30, 'margin':'auto'})], id='cardEF06MA102bi')),
            ]
    ),
    dbc.Popover(
            totalgeral,
            target="total62bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF06MA07,
            target="EF06MA072bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF06MA32,
            target="EF06MA322bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF06MA10,
            target="EF06MA102bi",
            body=True,
            trigger="hover"),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF06MA08"),dbc.CardBody(children=[] , id='EF06MA082bi', style={'font-size':30, 'margin':'auto'})], id='cardEF06MA082bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF06MA22"),dbc.CardBody(children=[] , id='EF06MA222bi', style={'font-size':30, 'margin':'auto'})], id='cardEF06MA222bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF06MA09"),dbc.CardBody(children=[] , id='EF06MA092bi', style={'font-size':30, 'margin':'auto'})], id='cardEF06MA092bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF06MA28"),dbc.CardBody(children=[] , id='EF06MA282bi', style={'font-size':30, 'margin':'auto'})], id='cardEF06MA282bi')),
            ]
    ),
    dbc.Popover(
            EF06MA08,
            target="EF06MA082bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF06MA22,
            target="EF06MA222bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF06MA09,
            target="EF06MA092bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF06MA28,
            target="EF06MA282bi",
            body=True,
            trigger="hover"),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF06MA31"),dbc.CardBody(children=[] , id='EF06MA312bi', style={'font-size':30, 'margin':'auto'})], id='cardEF06MA312bi'), width=3),
            
            ]
    ),

    dbc.Popover(
            EF06MA31,
            target="EF06MA312bi",
            body=True,
            trigger="hover"),

    
    html.Br(),
    dbc.Row(children=[

    dbc.Col(dcc.Dropdown(df_mat6ano2bi['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-turma62bi')),
    dbc.Col(dcc.Dropdown(df_habs62bi.columns, value="EF06MA31", style ={'margin-top':10, 'margin-left':5}, id='drop-hab62bi')),
    
]),

html.Br(),
dbc.Row(children=[

    dbc.Col( dbc.Card(dcc.Graph(id='fighabs62bi',config= {'displaylogo': False}))),
    dbc.Col( dbc.Card(dcc.Graph(id='figacerto62bi',config= {'displaylogo': False}))),
])

])

@app.callback(
    Output('total62bi','children'),
    Output('cardtotal62bi', 'color'),
    Input('drop-down62bi','value')
)
def habtotal(turma):
    df = df_mat6ano2bi.loc[df_mat6ano2bi['Turma']==turma]
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
    Output('EF06MA072bi','children'),
    Output('cardEF06MA072bi', 'color'),
    Input('drop-down62bi','value')
)
def hab1(turma):
    df= df_mat6ano2bi.loc[df_mat6ano2bi['Turma']==turma]
    soma = df['EF06MA07'].values.sum()
    qtd = df['EF06MA07'].count()
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
    Output('EF06MA322bi','children'),
    Output('cardEF06MA322bi', 'color'),
    Input('drop-down62bi','value')
)
def hab2(turma):
    df= df_mat6ano2bi.loc[df_mat6ano2bi['Turma']==turma]
    soma = df['EF06MA32'].values.sum()
    qtd = df['EF06MA32'].count()
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
    Output('EF06MA102bi','children'),
    Output('cardEF06MA102bi', 'color'),
    Input('drop-down62bi','value')
)
def hab3(turma):
    df= df_mat6ano2bi.loc[df_mat6ano2bi['Turma']==turma]
    soma = df['EF06MA10'].values.sum()
    qtd = df['EF06MA10'].count()
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
    Output('EF06MA082bi','children'),
    Output('cardEF06MA082bi', 'color'),
    Input('drop-down62bi','value')
)
def hab4(turma):
    df= df_mat6ano2bi.loc[df_mat6ano2bi['Turma']==turma]
    soma = df['EF06MA08'].values.sum()
    qtd = df['EF06MA08'].count()
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
    Output('EF06MA222bi','children'),
    Output('cardEF06MA222bi', 'color'),
    Input('drop-down62bi','value')
)
def hab5(turma):
    df= df_mat6ano2bi.loc[df_mat6ano2bi['Turma']==turma]
    soma = df['EF06MA22'].values.sum()
    qtd = df['EF06MA22'].count()
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
    Output('EF06MA092bi','children'),
    Output('cardEF06MA092bi', 'color'),
    Input('drop-down62bi','value')
)
def hab6(turma):
    df= df_mat6ano2bi.loc[df_mat6ano2bi['Turma']==turma]
    soma = df['EF06MA09'].values.sum()
    qtd = df['EF06MA09'].count()
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
    Output('EF06MA312bi','children'),
    Output('cardEF06MA312bi', 'color'),
    Input('drop-down62bi','value')
)
def hab8(turma):
    df= df_mat6ano2bi.loc[df_mat6ano2bi['Turma']==turma]
    soma = df['EF06MA31'].values.sum()
    qtd = df['EF06MA31'].count()
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



#-----------------------------------------------------------------



#-----------------------------------------------------------------

@app.callback(
    Output('EF06MA282bi','children'),
    Output('cardEF06MA282bi', 'color'),
    Input('drop-down62bi','value')
)
def hab10(turma):
    df= df_mat6ano2bi.loc[df_mat6ano2bi['Turma']==turma]
    soma = df['EF06MA28'].values.sum()
    qtd = df['EF06MA28'].count()
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
    Output('figacerto62bi','figure'),
    Input('drop-hab62bi','value'),
    Input('drop-turma62bi','value'),
)
def acertos(hab, turma):
    d = df_mat6ano2bi.loc[df_mat6ano2bi['Turma']==turma]
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
    Output('fighabs62bi','figure'),
    Input('drop-turma62bi','value'),
)
def habs(turma):
    df = df_mat6ano2bi.loc[df_mat6ano2bi['Turma']==turma]
    fig= px.histogram(df, x = 'Total', color='Total', labels= {'Total':'Percentual de Habilidades Desenvolvidas'}, title= 'Percentual de Habilidades Desenvolvidas <br> por Quantidade de Estudante'+' na turma '+str(turma).upper())
    fig.update_layout(showlegend=False)
    fig.update_yaxes( title= 'Quantidade de Estudantes')
    return fig
