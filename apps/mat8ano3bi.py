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
df_mat8ano3bi = pd.read_csv(DATA_PATH.joinpath("mat8ano3bi.csv"))
df_habs83bi= df_mat8ano3bi.drop(columns=['Escola','Estudante','Ano','Turma','Total']) 

layout = html.Div(children=[
    
    dbc.Row(dbc.Col(dcc.Dropdown(df_mat8ano3bi['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-down83bi',), width=2)),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("Domínio Geral das Habilidades"),dbc.CardBody( children=[], id='total83bi', style={'font-size':30, 'margin':'auto'})], id='cardtotal83bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF08MA04"),dbc.CardBody(children=[] , id='EF08MA043bi', style={'font-size':30, 'margin':'auto'})], id='cardEF08MA043bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF08MA22"),dbc.CardBody(children=[] , id='EF08MA223bi', style={'font-size':30, 'margin':'auto'})], id='cardEF08MA223bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF08MA08"),dbc.CardBody(children=[] , id='EF08MA083bi', style={'font-size':30, 'margin':'auto'})], id='cardEF08MA083bi')),
            ]
    ),
    dbc.Popover(
            totalgeral,
            target="total83bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF08MA04,
            target="EF08MA043bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF08MA22,
            target="EF08MA223bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF08MA08,
            target="EF08MA083bi",
            body=True,
            trigger="hover"),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF08MA07"),dbc.CardBody(children=[] , id='EF08MA073bi', style={'font-size':30, 'margin':'auto'})], id='cardEF08MA073bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF08MA17"),dbc.CardBody(children=[] , id='EF08MA173bi', style={'font-size':30, 'margin':'auto'})], id='cardEF08MA173bi')),
            ]
    ),
    dbc.Popover(
            EF08MA07,
            target="EF08MA073bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF08MA17,
            target="EF08MA173bi",
            body=True,
            trigger="hover"),
    
    
    html.Br(),
   

    
    

    dbc.Row(children=[

    dbc.Col(dcc.Dropdown(df_mat8ano3bi['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-turma83bi')),
    dbc.Col(dcc.Dropdown(df_habs83bi.columns, value="EF08MA17", style ={'margin-top':10, 'margin-left':5}, id='drop-hab83bi')),
    ]),

    html.Br(),
    dbc.Row(children=[

    dbc.Col( dbc.Card(dcc.Graph(id='fighabs83bi',config= {'displaylogo': False}))),
    dbc.Col( dbc.Card(dcc.Graph(id='figacerto83bi',config= {'displaylogo': False}))),

])

])

@app.callback(
    Output('total83bi','children'),
    Output('cardtotal83bi', 'color'),
    Input('drop-down83bi','value')
)
def habtotal(turma):
    df = df_mat8ano3bi.loc[df_mat8ano3bi['Turma']==turma]
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
    Output('EF08MA043bi','children'),
    Output('cardEF08MA043bi', 'color'),
    Input('drop-down83bi','value')
)
def hab1(turma):
    df= df_mat8ano3bi.loc[df_mat8ano3bi['Turma']==turma]
    soma = df['EF08MA04'].values.sum()
    qtd = df['EF08MA04'].count()
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
    Output('EF08MA223bi','children'),
    Output('cardEF08MA223bi', 'color'),
    Input('drop-down83bi','value')
)
def hab2(turma):
    df= df_mat8ano3bi.loc[df_mat8ano3bi['Turma']==turma]
    soma = df['EF08MA22'].values.sum()
    qtd = df['EF08MA22'].count()
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
    Output('EF08MA083bi','children'),
    Output('cardEF08MA083bi', 'color'),
    Input('drop-down83bi','value')
)
def hab3(turma):
    df= df_mat8ano3bi.loc[df_mat8ano3bi['Turma']==turma]
    soma = df['EF08MA08'].values.sum()
    qtd = df['EF08MA08'].count()
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
    Output('EF08MA073bi','children'),
    Output('cardEF08MA073bi', 'color'),
    Input('drop-down83bi','value')
)
def hab4(turma):
    df= df_mat8ano3bi.loc[df_mat8ano3bi['Turma']==turma]
    soma = df['EF08MA07'].values.sum()
    qtd = df['EF08MA07'].count()
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
    Output('EF08MA173bi','children'),
    Output('cardEF08MA173bi', 'color'),
    Input('drop-down83bi','value')
)
def hab5(turma):
    df= df_mat8ano3bi.loc[df_mat8ano3bi['Turma']==turma]
    soma = df['EF08MA17'].values.sum()
    qtd = df['EF08MA17'].count()
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
    Output('figacerto83bi','figure'),
    Input('drop-hab83bi','value'),
    Input('drop-turma83bi','value'),
)
def acertos(hab, turma):
    d = df_mat8ano3bi.loc[df_mat8ano3bi['Turma']==turma]
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
    Output('fighabs83bi','figure'),
    Input('drop-turma83bi','value'),
)
def habs(turma):
    df = df_mat8ano3bi.loc[df_mat8ano3bi['Turma']==turma]
    fig= px.histogram(df, x = 'Total', color='Total', labels= {'Total':'Percentual de Habilidades Desenvolvidas'}, title= 'Percentual de Habilidades Desenvolvidas <br> por Quantidade de Estudante'+' na turma '+str(turma).upper())
    fig.update_layout(showlegend=False)
    fig.update_yaxes( title= 'Quantidade de Estudantes')
    return fig
