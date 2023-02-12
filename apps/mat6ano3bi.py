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
df_mat6ano3bi = pd.read_csv(DATA_PATH.joinpath("mat6ano3bi.csv"))
df_habs63bi= df_mat6ano3bi.drop(columns=['Unnamed: 0','Carimbo de data/hora','Escola','Estudante','Ano','Turma','Total']) 

layout = html.Div(children=[
    
    dbc.Row(dbc.Col(dcc.Dropdown(df_mat6ano3bi['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-down63bi',), width=2)),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("Domínio Geral das Habilidades"),dbc.CardBody( children=[], id='total63bi', style={'font-size':30, 'margin':'auto'})], id='cardtotal63bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF06MA02"),dbc.CardBody(children=[] , id='EF06MA023bi', style={'font-size':30, 'margin':'auto'})], id='cardEF06MA023bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF06MA17"),dbc.CardBody(children=[] , id='EF06MA173bi', style={'font-size':30, 'margin':'auto'})], id='cardEF06MA173bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF06MA15"),dbc.CardBody(children=[] , id='EF06MA153bi', style={'font-size':30, 'margin':'auto'})], id='cardEF06MA153bi')),
            ]
    ),
    dbc.Popover(
            totalgeral,
            target="total63bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF06MA02,
            target="EF06MA023bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF06MA17,
            target="EF06MA173bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF06MA15,
            target="EF06MA153bi",
            body=True,
            trigger="hover"),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF06MA11"),dbc.CardBody(children=[] , id='EF06MA113bi', style={'font-size':30, 'margin':'auto'})], id='cardEF06MA113bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF06MA24"),dbc.CardBody(children=[] , id='EF06MA243bi', style={'font-size':30, 'margin':'auto'})], id='cardEF06MA243bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF06MA34"),dbc.CardBody(children=[] , id='EF06MA343bi', style={'font-size':30, 'margin':'auto'})], id='cardEF06MA343bi')),
            ]
    ),
    dbc.Popover(
            EF06MA11,
            target="EF06MA113bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF06MA24,
            target="EF06MA243bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF06MA34,
            target="EF06MA343bi",
            body=True,
            trigger="hover"),
    
    html.Br(),
   

    dbc.Row(children=[

    dbc.Col(dcc.Dropdown(df_mat6ano3bi['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-turma63bi')),
    dbc.Col(dcc.Dropdown(df_habs63bi.columns, value="EF06MA34", style ={'margin-top':10, 'margin-left':5}, id='drop-hab63bi')),
    
]),

html.Br(),
dbc.Row(children=[

    dbc.Col( dbc.Card(dcc.Graph(id='fighabs63bi',config= {'displaylogo': False}))),
    dbc.Col( dbc.Card(dcc.Graph(id='figacerto63bi',config= {'displaylogo': False}))),
])

])

@app.callback(
    Output('total63bi','children'),
    Output('cardtotal63bi', 'color'),
    Input('drop-down63bi','value')
)
def habtotal(turma):
    df = df_mat6ano3bi.loc[df_mat6ano3bi['Turma']==turma]
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
    Output('EF06MA023bi','children'),
    Output('cardEF06MA023bi', 'color'),
    Input('drop-down63bi','value')
)
def hab1(turma):
    df= df_mat6ano3bi.loc[df_mat6ano3bi['Turma']==turma]
    soma = df['EF06MA02'].values.sum()
    qtd = df['EF06MA02'].count()
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
    Output('EF06MA173bi','children'),
    Output('cardEF06MA173bi', 'color'),
    Input('drop-down63bi','value')
)
def hab2(turma):
    df= df_mat6ano3bi.loc[df_mat6ano3bi['Turma']==turma]
    soma = df['EF06MA17'].values.sum()
    qtd = df['EF06MA17'].count()
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
    Output('EF06MA153bi','children'),
    Output('cardEF06MA153bi', 'color'),
    Input('drop-down63bi','value')
)
def hab3(turma):
    df= df_mat6ano3bi.loc[df_mat6ano3bi['Turma']==turma]
    soma = df['EF06MA15'].values.sum()
    qtd = df['EF06MA15'].count()
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
    Output('EF06MA113bi','children'),
    Output('cardEF06MA113bi', 'color'),
    Input('drop-down63bi','value')
)
def hab4(turma):
    df= df_mat6ano3bi.loc[df_mat6ano3bi['Turma']==turma]
    soma = df['EF06MA11'].values.sum()
    qtd = df['EF06MA11'].count()
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
    Output('EF06MA243bi','children'),
    Output('cardEF06MA243bi', 'color'),
    Input('drop-down63bi','value')
)
def hab5(turma):
    df= df_mat6ano3bi.loc[df_mat6ano3bi['Turma']==turma]
    soma = df['EF06MA24'].values.sum()
    qtd = df['EF06MA24'].count()
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
    Output('EF06MA343bi','children'),
    Output('cardEF06MA343bi', 'color'),
    Input('drop-down63bi','value')
)
def hab6(turma):
    df= df_mat6ano3bi.loc[df_mat6ano3bi['Turma']==turma]
    soma = df['EF06MA34'].values.sum()
    qtd = df['EF06MA34'].count()
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



#-----------------------------------------------------------------



#-----------------------------------------------------------------


#-----------------------------------------------------------------------
@app.callback(
    Output('figacerto63bi','figure'),
    Input('drop-hab63bi','value'),
    Input('drop-turma63bi','value'),
)
def acertos(hab, turma):
    d = df_mat6ano3bi.loc[df_mat6ano3bi['Turma']==turma]
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
    Output('fighabs63bi','figure'),
    Input('drop-turma63bi','value'),
)
def habs(turma):
    df = df_mat6ano3bi.loc[df_mat6ano3bi['Turma']==turma]
    fig= px.histogram(df, x = 'Total', color='Total', labels= {'Total':'Percentual de Habilidades Desenvolvidas'}, title= 'Percentual de Habilidades Desenvolvidas <br> por Quantidade de Estudante'+' na turma '+str(turma).upper())
    fig.update_layout(showlegend=False)
    fig.update_yaxes( title= 'Quantidade de Estudantes')
    return fig
