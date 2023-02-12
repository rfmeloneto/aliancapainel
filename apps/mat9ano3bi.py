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
df_mat9ano3bi = pd.read_csv(DATA_PATH.joinpath("mat9ano3bi.csv")) 
df_habs93bi= df_mat9ano3bi.drop(columns=['Escola','Estudante','Ano','Turma','Total'])

layout = html.Div(children=[
    
    dbc.Row(dbc.Col(dcc.Dropdown(df_mat9ano3bi['Turma'].unique(), value='u', style ={'margin-top':10, 'margin-left':5}, id='drop-down93bi',), width=2)),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("Domínio Geral das Habilidades"),dbc.CardBody( children=[], id='total93bi', style={'font-size':30, 'margin':'auto'})], id='cardtotal93bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF09MA06"),dbc.CardBody(children=[] , id='EF09MA063bi', style={'font-size':30, 'margin':'auto'})], id='cardEF09MA063bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF09MA13"),dbc.CardBody(children=[] , id='EF09MA133bi', style={'font-size':30, 'margin':'auto'})], id='cardEF09MA133bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF09MA21"),dbc.CardBody(children=[] , id='EF09MA213bi', style={'font-size':30, 'margin':'auto'})], id='cardEF09MA213bi')),
            ]
    ),
    dbc.Popover(
            totalgeral,
            target="total93bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF09MA06,
            target="EF09MA063bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF09MA13,
            target="EF09MA133bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF09MA21,
            target="EF09MA213bi",
            body=True,
            trigger="hover"),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF09MA18"),dbc.CardBody(children=[] , id='EF09MA183bi', style={'font-size':30, 'margin':'auto'})], id='cardEF09MA183bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF09MA14"),dbc.CardBody(children=[] , id='EF09MA143bi', style={'font-size':30, 'margin':'auto'})], id='cardEF09MA143bi')),
            ]
    ),
    dbc.Popover(
            EF09MA18,
            target="EF09MA183bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF09MA14,
            target="EF09MA143bi",
            body=True,
            trigger="hover"),
    
    
    html.Br(),
   
     dbc.Row(children=[

    dbc.Col(dcc.Dropdown(df_mat9ano3bi['Turma'].unique(), value='u', style ={'margin-top':10, 'margin-left':5}, id='drop-turma93bi')),
    dbc.Col(dcc.Dropdown(df_habs93bi.columns, value="EF09MA14", style ={'margin-top':10, 'margin-left':5}, id='drop-hab93bi')),
    ]),

    html.Br(),
    dbc.Row(children=[

    dbc.Col( dbc.Card(dcc.Graph(id='fighabs93bi',config= {'displaylogo': False}))),
    dbc.Col( dbc.Card(dcc.Graph(id='figacerto93bi',config= {'displaylogo': False}))),

])

])

@app.callback(
    Output('total93bi','children'),
    Output('cardtotal93bi', 'color'),
    Input('drop-down93bi','value')
)
def habtotal(turma):
    df = df_mat9ano3bi.loc[df_mat9ano3bi['Turma']==turma]
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
    Output('EF09MA063bi','children'),
    Output('cardEF09MA063bi', 'color'),
    Input('drop-down93bi','value')
)
def hab1(turma):
    df= df_mat9ano3bi.loc[df_mat9ano3bi['Turma']==turma]
    soma = df['EF09MA06'].values.sum()
    qtd = df['EF09MA06'].count()
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
    Output('EF09MA133bi','children'),
    Output('cardEF09MA133bi', 'color'),
    Input('drop-down93bi','value')
)
def hab2(turma):
    df= df_mat9ano3bi.loc[df_mat9ano3bi['Turma']==turma]
    soma = df['EF09MA13'].values.sum()
    qtd = df['EF09MA13'].count()
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
    Output('EF09MA213bi','children'),
    Output('cardEF09MA213bi', 'color'),
    Input('drop-down93bi','value')
)
def hab3(turma):
    df= df_mat9ano3bi.loc[df_mat9ano3bi['Turma']==turma]
    soma = df['EF09MA21'].values.sum()
    qtd = df['EF09MA21'].count()
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
    Output('EF09MA183bi','children'),
    Output('cardEF09MA183bi', 'color'),
    Input('drop-down93bi','value')
)
def hab4(turma):
    df= df_mat9ano3bi.loc[df_mat9ano3bi['Turma']==turma]
    soma = df['EF09MA18'].values.sum()
    qtd = df['EF09MA18'].count()
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

@app.callback(
    Output('EF09MA143bi','children'),
    Output('cardEF09MA143bi', 'color'),
    Input('drop-down93bi','value')
)
def hab10(turma):
    df= df_mat9ano3bi.loc[df_mat9ano3bi['Turma']==turma]
    soma = df['EF09MA14'].values.sum()
    qtd = df['EF09MA14'].count()
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



@app.callback(
    Output('figacerto93bi','figure'),
    Input('drop-hab93bi','value'),
    Input('drop-turma93bi','value'),
)
def acertos(hab, turma):
    d = df_mat9ano3bi.loc[df_mat9ano3bi['Turma']==turma]
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
    Output('fighabs93bi','figure'),
    Input('drop-turma93bi','value'),
)
def habs(turma):
    df = df_mat9ano3bi.loc[df_mat9ano3bi['Turma']==turma]
    fig= px.histogram(df, x = 'Total', color='Total', labels= {'Total':'Percentual de Habilidades Desenvolvidas'}, title= 'Percentual de Habilidades Desenvolvidas <br> por Quantidade de Estudante'+' na turma '+str(turma).upper())
    fig.update_layout(showlegend=False)
    fig.update_yaxes( title= 'Quantidade de Estudantes')
    return fig
