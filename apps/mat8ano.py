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
df_mat8ano = pd.read_csv(DATA_PATH.joinpath("mat8ano.csv"))
df_habs8= df_mat8ano.drop(columns=['Escola','Estudante','Ano','Turma','Total']) 

layout = html.Div(children=[
    
    dbc.Row(dbc.Col(dcc.Dropdown(df_mat8ano['Turma'].unique(), value='u', style ={'margin-top':10, 'margin-left':5}, id='drop-down8',), width=2)),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("Domínio Geral das Habilidades"),dbc.CardBody( children=[], id='total8', style={'font-size':30, 'margin':'auto'})], id='cardtotal8')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF08MA02"),dbc.CardBody(children=[] , id='EF08MA02', style={'font-size':30, 'margin':'auto'})], id='cardEF08MA02')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF08MA12"),dbc.CardBody(children=[] , id='EF08MA12', style={'font-size':30, 'margin':'auto'})], id='cardEF08MA12')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF08MA06"),dbc.CardBody(children=[] , id='EF08MA06', style={'font-size':30, 'margin':'auto'})], id='cardEF08MA06')),
            ]
    ),
    dbc.Popover(
            totalgeral,
            target="total8",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF08MA02,
            target="EF08MA02",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF08MA12,
            target="EF08MA12",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF08MA06,
            target="EF08MA06",
            body=True,
            trigger="hover"),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF08MA24"),dbc.CardBody(children=[] , id='EF08MA24', style={'font-size':30, 'margin':'auto'})], id='cardEF08MA24')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF08MA27"),dbc.CardBody(children=[] , id='EF08MA27', style={'font-size':30, 'margin':'auto'})], id='cardEF08MA27')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF08MA01"),dbc.CardBody(children=[] , id='EF08MA01', style={'font-size':30, 'margin':'auto'})], id='cardEF08MA01')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF08MA13"),dbc.CardBody(children=[] , id='EF08MA13', style={'font-size':30, 'margin':'auto'})], id='cardEF08MA13')),
            ]
    ),
    dbc.Popover(
            EF08MA24,
            target="EF08MA24",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF08MA27,
            target="EF08MA27",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF08MA01,
            target="EF08MA01",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF08MA13,
            target="EF08MA13",
            body=True,
            trigger="hover"),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF08MA15"),dbc.CardBody(children=[] , id='EF08MA15', style={'font-size':30, 'margin':'auto'})], id='cardEF08MA15'), width=3),
           
            
            ]
    ),

    
    dbc.Popover(
            EF08MA15,
            target="EF08MA15",
            body=True,
            trigger="hover"),

    html.Br(),

    dbc.Row(children=[

    dbc.Col(dcc.Dropdown(df_mat8ano['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-turma8')),
    dbc.Col(dcc.Dropdown(df_habs8.columns, value="EF08MA15", style ={'margin-top':10, 'margin-left':5}, id='drop-hab8')),
    ]),

    html.Br(),
    dbc.Row(children=[

    dbc.Col( dbc.Card(dcc.Graph(id='fighabs8',config= {'displaylogo': False}))),
    dbc.Col( dbc.Card(dcc.Graph(id='figacerto8',config= {'displaylogo': False}))),

])

])

@app.callback(
    Output('total8','children'),
    Output('cardtotal8', 'color'),
    Input('drop-down8','value')
)
def habtotal(turma):
    df = df_mat8ano.loc[df_mat8ano['Turma']==turma]
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
    Output('EF08MA02','children'),
    Output('cardEF08MA02', 'color'),
    Input('drop-down8','value')
)
def hab1(turma):
    df= df_mat8ano.loc[df_mat8ano['Turma']==turma]
    soma = df['EF08MA02'].values.sum()
    qtd = df['EF08MA02'].count()
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
    Output('EF08MA12','children'),
    Output('cardEF08MA12', 'color'),
    Input('drop-down8','value')
)
def hab2(turma):
    df= df_mat8ano.loc[df_mat8ano['Turma']==turma]
    soma = df['EF08MA12'].values.sum()
    qtd = df['EF08MA12'].count()
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
    Output('EF08MA06','children'),
    Output('cardEF08MA06', 'color'),
    Input('drop-down8','value')
)
def hab3(turma):
    df= df_mat8ano.loc[df_mat8ano['Turma']==turma]
    soma = df['EF08MA06'].values.sum()
    qtd = df['EF08MA06'].count()
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
    Output('EF08MA24','children'),
    Output('cardEF08MA24', 'color'),
    Input('drop-down8','value')
)
def hab4(turma):
    df= df_mat8ano.loc[df_mat8ano['Turma']==turma]
    soma = df['EF08MA24'].values.sum()
    qtd = df['EF08MA24'].count()
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
    Output('EF08MA27','children'),
    Output('cardEF08MA27', 'color'),
    Input('drop-down8','value')
)
def hab5(turma):
    df= df_mat8ano.loc[df_mat8ano['Turma']==turma]
    soma = df['EF08MA27'].values.sum()
    qtd = df['EF08MA27'].count()
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
    Output('EF08MA01','children'),
    Output('cardEF08MA01', 'color'),
    Input('drop-down8','value')
)
def hab6(turma):
    df= df_mat8ano.loc[df_mat8ano['Turma']==turma]
    soma = df['EF08MA01'].values.sum()
    qtd = df['EF08MA01'].count()
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
    Output('EF08MA13','children'),
    Output('cardEF08MA13', 'color'),
    Input('drop-down8','value')
)
def hab8(turma):
    df= df_mat8ano.loc[df_mat8ano['Turma']==turma]
    soma = df['EF08MA13'].values.sum()
    qtd = df['EF08MA13'].count()
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
    Output('EF08MA15','children'),
    Output('cardEF08MA15', 'color'),
    Input('drop-down8','value')
)
def hab10(turma):
    df= df_mat8ano.loc[df_mat8ano['Turma']==turma]
    soma = df['EF08MA15'].values.sum()
    qtd = df['EF08MA15'].count()
    media= soma/qtd
    media = media*100
    media = int(media)
    if media >= 50:
        return str(media), 'success'
    elif media >= 30 and media < 50 :
        return str(media) , 'warning'
    else:
        return str(media), 'danger'

@app.callback(
    Output('figacerto8','figure'),
    Input('drop-hab8','value'),
    Input('drop-turma8','value'),
)
def acertos(hab, turma):
    d = df_mat8ano.loc[df_mat8ano['Turma']==turma]
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
    Output('fighabs8','figure'),
    Input('drop-turma8','value'),
)
def habs(turma):
    df = df_mat8ano.loc[df_mat8ano['Turma']==turma]
    fig= px.histogram(df, x = 'Total', color='Total', labels= {'Total':'Percentual de Habilidades Desenvolvidas'}, title= 'Percentual de Habilidades Desenvolvidas <br> por Quantidade de Estudante'+' na turma '+str(turma).upper())
    fig.update_layout(showlegend=False)
    fig.update_yaxes( title= 'Quantidade de Estudantes')
    return fig
