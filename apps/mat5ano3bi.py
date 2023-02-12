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
df_mat5ano3bi = pd.read_csv(DATA_PATH.joinpath("mat5ano3bi.csv"))
df_habs53bi= df_mat5ano3bi.drop(columns=['Escola','Estudante','Ano','Turma','Total'])  

layout = html.Div(children=[
    
    dbc.Row(dbc.Col(dcc.Dropdown(df_mat5ano3bi['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-down53bi',), width=2)),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("Domínio Geral das Habilidades"),dbc.CardBody( children=[], id='total53bi', style={'font-size':30, 'margin':'auto'})], id='cardtotal53bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF05MA07"),dbc.CardBody(children=[] , id='EF05MA073bi', style={'font-size':30, 'margin':'auto'})], id='cardEF05MA073bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF05MA09"),dbc.CardBody(children=[] , id='EF05MA093bi', style={'font-size':30, 'margin':'auto'})], id='cardEF05MA093bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF05MA13"),dbc.CardBody(children=[] , id='EF05MA133bi', style={'font-size':30, 'margin':'auto'})], id='cardEF05MA133bi')),
            ]
    ),
    dbc.Popover(
            totalgeral,
            target="total53bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF05MA07,
            target="EF05MA073bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF05MA09,
            target="EF05MA093bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF05MA13,
            target="EF05MA133bi",
            body=True,
            trigger="hover"),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF05MA12"),dbc.CardBody(children=[] , id='EF05MA123bi', style={'font-size':30, 'margin':'auto'})], id='cardEF05MA123bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF05MA16"),dbc.CardBody(children=[] , id='EF05MA163bi', style={'font-size':30, 'margin':'auto'})], id='cardEF05MA163bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF05MA20"),dbc.CardBody(children=[] , id='EF05MA203bi', style={'font-size':30, 'margin':'auto'})], id='cardEF05MA203bi')),
            ]
    ),
    dbc.Popover(
            EF05MA12,
            target="EF05MA123bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF05MA16,
            target="EF05MA163bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF05MA20,
            target="EF05MA203bi",
            body=True,
            trigger="hover"),
    
    html.Br(),
dbc.Row(children=[

    dbc.Col(dcc.Dropdown(df_mat5ano3bi['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-turma53bi')),
    dbc.Col(dcc.Dropdown(df_habs53bi.columns, value="EF05MA20", style ={'margin-top':10, 'margin-left':5}, id='drop-hab53bi')),
    
]),

html.Br(),
dbc.Row(children=[

    dbc.Col( dbc.Card(dcc.Graph(id='fighabs53bi',config= {'displaylogo': False}))),
    dbc.Col( dbc.Card(dcc.Graph(id='figacerto53bi',config= {'displaylogo': False}))),
])

])

@app.callback(
    Output('total53bi','children'),
    Output('cardtotal53bi', 'color'),
    Input('drop-down53bi','value')
)
def habtotal(turma):
    df = df_mat5ano3bi.loc[df_mat5ano3bi['Turma']==turma]
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
    Output('EF05MA073bi','children'),
    Output('cardEF05MA073bi', 'color'),
    Input('drop-down53bi','value')
)
def hab1(turma):
    df= df_mat5ano3bi.loc[df_mat5ano3bi['Turma']==turma]
    soma = df['EF05MA07'].values.sum()
    qtd = df['EF05MA07'].count()
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
    Output('EF05MA093bi','children'),
    Output('cardEF05MA093bi', 'color'),
    Input('drop-down53bi','value')
)
def hab2(turma):
    df= df_mat5ano3bi.loc[df_mat5ano3bi['Turma']==turma]
    soma = df['EF05MA09'].values.sum()
    qtd = df['EF05MA09'].count()
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
    Output('EF05MA133bi','children'),
    Output('cardEF05MA133bi', 'color'),
    Input('drop-down53bi','value')
)
def hab3(turma):
    df= df_mat5ano3bi.loc[df_mat5ano3bi['Turma']==turma]
    soma = df['EF05MA13'].values.sum()
    qtd = df['EF05MA13'].count()
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
    Output('EF05MA123bi','children'),
    Output('cardEF05MA123bi', 'color'),
    Input('drop-down53bi','value')
)
def hab4(turma):
    df= df_mat5ano3bi.loc[df_mat5ano3bi['Turma']==turma]
    soma = df['EF05MA12'].values.sum()
    qtd = df['EF05MA12'].count()
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
    Output('EF05MA163bi','children'),
    Output('cardEF05MA163bi', 'color'),
    Input('drop-down53bi','value')
)
def hab5(turma):
    df= df_mat5ano3bi.loc[df_mat5ano3bi['Turma']==turma]
    soma = df['EF05MA16'].values.sum()
    qtd = df['EF05MA16'].count()
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
    Output('EF05MA203bi','children'),
    Output('cardEF05MA203bi', 'color'),
    Input('drop-down53bi','value')
)
def hab6(turma):
    df= df_mat5ano3bi.loc[df_mat5ano3bi['Turma']==turma]
    soma = df['EF05MA20'].values.sum()
    qtd = df['EF05MA20'].count()
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
    Output('figacerto53bi','figure'),
    Input('drop-hab53bi','value'),
    Input('drop-turma53bi','value'),
)
def acertos(hab, turma):
    d = df_mat5ano3bi.loc[df_mat5ano3bi['Turma']==turma]
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
    Output('fighabs53bi','figure'),
    Input('drop-turma53bi','value'),
)
def habs(turma):
    df = df_mat5ano3bi.loc[df_mat5ano3bi['Turma']==turma]
    fig= px.histogram(df, x = 'Total', color='Total', labels= {'Total':'Percentual de Habilidades Desenvolvidas'}, title= 'Percentual de Habilidades Desenvolvidas <br> por Quantidade de Estudante'+' na turma '+str(turma).upper())
    fig.update_layout(showlegend=False)
    fig.update_yaxes( title= 'Quantidade de Estudantes')
    return fig

