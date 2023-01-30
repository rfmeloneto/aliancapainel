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
df_port8ano2bi = pd.read_csv(DATA_PATH.joinpath("port8ano2bi.csv")) 
df_habsport82bi = df_port8ano2bi.drop(columns=['Escola','Estudante','Ano','Turma','Total'])

layout = html.Div(children=[
    
    dbc.Row(dbc.Col(dcc.Dropdown(df_port8ano2bi['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-down182bi',), width=2)),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("Domínio Geral das Habilidades"),dbc.CardBody(children=[], id='total182bi', style={'font-size':30, 'margin':'auto'})], id='cardtotal182bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF89LP03"),dbc.CardBody(children=[] , id='EF89LP032bi', style={'font-size':30, 'margin':'auto'})], id='cardEF89LP032bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF89LP04"),dbc.CardBody(children=[] , id='EF89LP042bi1', style={'font-size':30, 'margin':'auto'})], id='cardEF89LP042bi1')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF89LP16"),dbc.CardBody(children=[] , id='EF89LP162bi', style={'font-size':30, 'margin':'auto'})], id='cardEF89LP162bi')),
            ]
    ),
    dbc.Popover(
            totalgeral,
            target="total182bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF89LP03,
            target="EF89LP032bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF89LP04,
            target="EF89LP042bi1",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF89LP16,
            target="EF89LP162bi",
            body=True,
            trigger="hover"),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF08LP06"),dbc.CardBody(children=[] , id='EF08LP062bi', style={'font-size':30, 'margin':'auto'})], id='cardEF08LP062bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF89LP29"),dbc.CardBody(children=[] , id='EF89LP292bi', style={'font-size':30, 'margin':'auto'})], id='cardEF89LP292bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF08LP04"),dbc.CardBody(children=[] , id='EF08LP042bi', style={'font-size':30, 'margin':'auto'})], id='cardEF08LP042bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF08LP05"),dbc.CardBody(children=[] , id='EF08LP052bi', style={'font-size':30, 'margin':'auto'})], id='cardEF08LP052bi')),
            ]
    ),
    dbc.Popover(
            EF08LP06,
            target="EF08LP062bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF89LP29,
            target="EF89LP292bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF08LP04,
            target="EF08LP042bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF08LP05,
            target="EF08LP052bi",
            body=True,
            trigger="hover"),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF89LP33"),dbc.CardBody(children=[] , id='EF89LP332bi1', style={'font-size':30, 'margin':'auto'})], id='cardEF89LP332bi1'), width=3),
            dbc.Col( dbc.Card([dbc.CardHeader("EF69LP29"),dbc.CardBody(children=[] , id='EF69LP292bi', style={'font-size':30, 'margin':'auto'})], id='cardEF69LP292bi'), width=3),

            
            ]
    ),
    dbc.Popover(
            EF89LP33,
            target="EF89LP332bi1",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF69LP29,
            target="EF69LP292bi",
            body=True,
            trigger="hover"),

    html.Br(),
dbc.Row(children=[

    dbc.Col(dcc.Dropdown(df_port8ano2bi['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-turma172bi')),
    dbc.Col(dcc.Dropdown(df_habsport82bi.columns, value="EF89LP33", style ={'margin-top':10, 'margin-left':5}, id='drop-hab172bi')),
    
]),

html.Br(),
dbc.Row(children=[

    dbc.Col( dbc.Card(dcc.Graph(id='fighabs172bi',config= {'displaylogo': False}))),
    dbc.Col( dbc.Card(dcc.Graph(id='figacerto172bi',config= {'displaylogo': False}))),


]),

])

@app.callback(
    Output('total182bi','children'),
    Output('cardtotal182bi', 'color'),
    Input('drop-down182bi','value')
)
def habtotal(turma):
    df = df_port8ano2bi.loc[df_port8ano2bi['Turma']==turma]
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
    Output('EF89LP032bi','children'),
    Output('cardEF89LP032bi', 'color'),
    Input('drop-down182bi','value')
)
def hab1(turma):
    df= df_port8ano2bi.loc[df_port8ano2bi['Turma']==turma]
    soma = df['EF89LP03'].values.sum()
    qtd = df['EF89LP03'].count()
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
    Output('EF89LP042bi1','children'),
    Output('cardEF89LP042bi1', 'color'),
    Input('drop-down182bi','value')
)
def hab2(turma):
    df= df_port8ano2bi.loc[df_port8ano2bi['Turma']==turma]
    soma = df['EF89LP04'].values.sum()
    qtd = df['EF89LP04'].count()
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
    Output('EF89LP162bi','children'),
    Output('cardEF89LP162bi', 'color'),
    Input('drop-down182bi','value')
)
def hab3(turma):
    df= df_port8ano2bi.loc[df_port8ano2bi['Turma']==turma]
    soma = df['EF89LP16'].values.sum()
    qtd = df['EF89LP16'].count()
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
    Output('EF08LP062bi','children'),
    Output('EF08LP062bi', 'color'),
    Input('drop-down182bi','value')
)
def hab4(turma):
    df= df_port8ano2bi.loc[df_port8ano2bi['Turma']==turma]
    soma = df['EF08LP06'].values.sum()
    qtd = df['EF08LP06'].count()
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
    Output('EF89LP292bi','children'),
    Output('cardEF89LP292bi', 'color'),
    Input('drop-down182bi','value')
)
def hab5(turma):
    df= df_port8ano2bi.loc[df_port8ano2bi['Turma']==turma]
    soma = df['EF89LP29'].values.sum()
    qtd = df['EF89LP29'].count()
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
    Output('EF08LP042bi','children'),
    Output('cardEF08LP042bi', 'color'),
    Input('drop-down182bi','value')
)
def hab6(turma):
    df= df_port8ano2bi.loc[df_port8ano2bi['Turma']==turma]
    soma = df['EF08LP04'].values.sum()
    qtd = df['EF08LP04'].count()
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
    Output('EF08LP052bi','children'),
    Output('cardEF08LP052bi', 'color'),
    Input('drop-down182bi','value')
)
def hab7(turma):
    df= df_port8ano2bi.loc[df_port8ano2bi['Turma']==turma]
    soma = df['EF08LP05'].values.sum()
    qtd = df['EF08LP05'].count()
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
    Output('EF89LP332bi1','children'),
    Output('cardEF89LP332bi1', 'color'),
    Input('drop-down182bi','value')
)
def hab8(turma):
    df= df_port8ano2bi.loc[df_port8ano2bi['Turma']==turma]
    soma = df['EF89LP33'].values.sum()
    qtd = df['EF89LP33'].count()
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
    Output('EF69LP292bi','children'),
    Output('cardEF69LP292bi', 'color'),
    Input('drop-down182bi','value')
)
def hab8(turma):
    df= df_port8ano2bi.loc[df_port8ano2bi['Turma']==turma]
    soma = df['EF69LP29'].values.sum()
    qtd = df['EF69LP29'].count()
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
    Output('figacerto172bi','figure'),
    Input('drop-hab172bi','value'),
    Input('drop-turma172bi','value'),
)
def acertos(hab, turma):
    d = df_port8ano2bi.loc[df_port8ano2bi['Turma']==turma]
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
    Output('fighabs172bi','figure'),
    Input('drop-turma172bi','value'),
)
def habs(turma):
    df = df_port8ano2bi.loc[df_port8ano2bi['Turma']==turma]
    fig= px.histogram(df, x = 'Total', color='Total', labels= {'Total':'Percentual de Habilidades Desenvolvidas'}, title= 'Percentual de Habilidades Desenvolvidas <br> por Quantidade de Estudante'+' na turma '+str(turma).upper())
    fig.update_layout(showlegend=False)
    fig.update_yaxes( title= 'Quantidade de Estudantes')
    return fig
