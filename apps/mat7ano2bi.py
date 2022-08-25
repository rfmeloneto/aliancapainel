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
df_mat7ano2bi = pd.read_csv(DATA_PATH.joinpath("mat7ano2bi.csv")) 
df_habs72bi= df_mat7ano2bi.drop(columns=['Escola','Estudante','Ano','Turma','Total'])

layout = html.Div(children=[
    
    dbc.Row(dbc.Col(dcc.Dropdown(df_mat7ano2bi['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-down72bi',), width=2)),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("Domínio Geral das Habilidades"),dbc.CardBody( children=[], id='total72bi', style={'font-size':30, 'margin':'auto'})], id='cardtotal72bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF07MA06"),dbc.CardBody(children=[] , id='EF07MA062bi', style={'font-size':30, 'margin':'auto'})], id='cardEF07MA062bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF07MA23"),dbc.CardBody(children=[] , id='EF07MA232bi', style={'font-size':30, 'margin':'auto'})], id='cardEF07MA232bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF07MA09"),dbc.CardBody(children=[] , id='EF07MA092bi', style={'font-size':30, 'margin':'auto'})], id='cardEF07MA092bi')),
            ]
    ),
    dbc.Popover(
            totalgeral,
            target="total72bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF07MA06,
            target="EF07MA062bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF07MA23,
            target="EF07MA232bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF07MA09,
            target="EF07MA092bi",
            body=True,
            trigger="hover"),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF07MA30"),dbc.CardBody(children=[] , id='EF07MA302bi', style={'font-size':30, 'margin':'auto'})], id='cardEF07MA302bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF07MA05"),dbc.CardBody(children=[] , id='EF07MA052bi', style={'font-size':30, 'margin':'auto'})], id='cardEF07MA052bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF07MA08"),dbc.CardBody(children=[] , id='EF07MA082bi', style={'font-size':30, 'margin':'auto'})], id='cardEF07MA082bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF07MA16"),dbc.CardBody(children=[] , id='EF07MA162bi', style={'font-size':30, 'margin':'auto'})], id='cardEF07MA162bi')),
            ]
    ),
    dbc.Popover(
            EF07MA30,
            target="EF07MA302bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF07MA05,
            target="EF07MA052bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF07MA08,
            target="EF07MA082bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF07MA16,
            target="EF07MA162bi",
            body=True,
            trigger="hover"),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF07MA37"),dbc.CardBody(children=[] , id='EF07MA372bi', style={'font-size':30, 'margin':'auto'})], id='cardEF07MA372bi'), width=3),
            dbc.Col( dbc.Card([dbc.CardHeader("EF07MA07"),dbc.CardBody(children=[] , id='EF07MA072bi', style={'font-size':30, 'margin':'auto'})], id='cardEF07MA072bi'), width=3),
            
            ]
    ),

    dbc.Popover(
            EF07MA37,
            target="EF07MA372bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF07MA07,
            target="EF07MA072bi",
            body=True,
            trigger="hover"),
    
    html.Br(),

    dbc.Row(children=[

    dbc.Col(dcc.Dropdown(df_mat7ano2bi['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-turma72bi')),
    dbc.Col(dcc.Dropdown(df_habs72bi.columns, value="EF07MA07", style ={'margin-top':10, 'margin-left':5}, id='drop-hab72bi')),
    ]),

    html.Br(),
    dbc.Row(children=[

    dbc.Col( dbc.Card(dcc.Graph(id='fighabs72bi',config= {'displaylogo': False}))),
    dbc.Col( dbc.Card(dcc.Graph(id='figacerto72bi',config= {'displaylogo': False}))),
])

])

@app.callback(
    Output('total72bi','children'),
    Output('cardtotal72bi', 'color'),
    Input('drop-down72bi','value')
)
def habtotal(turma):
    df = df_mat7ano2bi.loc[df_mat7ano2bi['Turma']==turma]
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


#-----------------------------------------------------------------

@app.callback(
    Output('EF07MA092bi','children'),
    Output('cardEF07MA092bi', 'color'),
    Input('drop-down72bi','value')
)
def hab3(turma):
    df= df_mat7ano2bi.loc[df_mat7ano2bi['Turma']==turma]
    soma = df['EF07MA09'].values.sum()
    qtd = df['EF07MA09'].count()
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
    Output('EF07MA302bi','children'),
    Output('cardEF07MA302bi', 'color'),
    Input('drop-down72bi','value')
)
def hab4(turma):
    df= df_mat7ano2bi.loc[df_mat7ano2bi['Turma']==turma]
    soma = df['EF07MA30'].values.sum()
    qtd = df['EF07MA30'].count()
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
    Output('EF07MA052bi','children'),
    Output('cardEF07MA052bi', 'color'),
    Input('drop-down72bi','value')
)
def hab5(turma):
    df= df_mat7ano2bi.loc[df_mat7ano2bi['Turma']==turma]
    soma = df['EF07MA05'].values.sum()
    qtd = df['EF07MA05'].count()
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
    Output('EF07MA062bi','children'),
    Output('cardEF07MA062bi', 'color'),
    Input('drop-down72bi','value')
)
def hab6(turma):
    df= df_mat7ano2bi.loc[df_mat7ano2bi['Turma']==turma]
    soma = df['EF07MA06'].values.sum()
    qtd = df['EF07MA06'].count()
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
    Output('EF07MA162bi','children'),
    Output('cardEF07MA162bi', 'color'),
    Input('drop-down72bi','value')
)
def hab8(turma):
    df= df_mat7ano2bi.loc[df_mat7ano2bi['Turma']==turma]
    soma = df['EF07MA16'].values.sum()
    qtd = df['EF07MA16'].count()
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
    Output('EF07MA372bi','children'),
    Output('cardEF07MA372bi', 'color'),
    Input('drop-down72bi','value')
)
def hab10(turma):
    df= df_mat7ano2bi.loc[df_mat7ano2bi['Turma']==turma]
    soma = df['EF07MA37'].values.sum()
    qtd = df['EF07MA37'].count()
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
    Output('EF07MA072bi','children'),
    Output('cardEF07MA072bi', 'color'),
    Input('drop-down72bi','value')
)
def hab10(turma):
    df= df_mat7ano2bi.loc[df_mat7ano2bi['Turma']==turma]
    soma = df['EF07MA07'].values.sum()
    qtd = df['EF07MA07'].count()
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
    Output('EF07MA082bi','children'),
    Output('cardEF07MA082bi', 'color'),
    Input('drop-down72bi','value')
)
def hab10(turma):
    df= df_mat7ano2bi.loc[df_mat7ano2bi['Turma']==turma]
    soma = df['EF07MA08'].values.sum()
    qtd = df['EF07MA08'].count()
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
    Output('EF07MA232bi','children'),
    Output('cardEF07MA232bi', 'color'),
    Input('drop-down72bi','value')
)
def hab10(turma):
    df= df_mat7ano2bi.loc[df_mat7ano2bi['Turma']==turma]
    soma = df['EF07MA23'].values.sum()
    qtd = df['EF07MA23'].count()
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
    Output('figacerto72bi','figure'),
    Input('drop-hab72bi','value'),
    Input('drop-turma72bi','value'),
)
def acertos(hab, turma):
    d = df_mat7ano2bi.loc[df_mat7ano2bi['Turma']==turma]
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
    Output('fighabs72bi','figure'),
    Input('drop-turma72bi','value'),
)
def habs(turma):
    df = df_mat7ano2bi.loc[df_mat7ano2bi['Turma']==turma]
    fig= px.histogram(df, x = 'Total', color='Total', labels= {'Total':'Percentual de Habilidades Desenvolvidas'}, title= 'Percentual de Habilidades Desenvolvidas <br> por Quantidade de Estudante'+' na turma '+str(turma).upper())
    fig.update_layout(showlegend=False)
    fig.update_yaxes( title= 'Quantidade de Estudantes')
    return fig
