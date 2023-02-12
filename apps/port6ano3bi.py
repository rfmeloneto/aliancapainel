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
df_port6ano3bi = pd.read_csv(DATA_PATH.joinpath("port6ano3bi.csv")) 
df_habsport63bi = df_port6ano3bi.drop(columns=['Escola','Estudante','Ano','Turma','Total'])

layout = html.Div(children=[
    
    dbc.Row(dbc.Col(dcc.Dropdown(df_port6ano3bi['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-down163bi',), width=2)),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("Domínio Geral das Habilidades"),dbc.CardBody( children=[], id='total163bi', style={'font-size':30, 'margin':'auto'})], id='cardtotal163bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF67LP08"),dbc.CardBody(children=[] , id='EF67LP083bi', style={'font-size':30, 'margin':'auto'})], id='cardEF67LP083bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF06LP04"),dbc.CardBody(children=[] , id='EF06LP043bi1', style={'font-size':30, 'margin':'auto'})], id='cardEF06LP043bi1')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF67LP32"),dbc.CardBody(children=[] , id='EF67LP3213bi', style={'font-size':30, 'margin':'auto'})], id='cardEF67LP3213bi')),
            ]
    ),
     dbc.Popover(
            totalgeral,
            target="total163bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF67LP08,
            target="EF67LP083bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF06LP04,
            target="EF06LP043bi1",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF67LP32,
            target="EF67LP3213bi",
            body=True,
            trigger="hover"),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF67LP33"),dbc.CardBody(children=[] , id='EF67LP333bi', style={'font-size':30, 'margin':'auto'})], id='cardEF67LP333bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF06LP06"),dbc.CardBody(children=[] , id='EF06LP0613bi1', style={'font-size':30, 'margin':'auto'})], id='cardEF06LP0613bi1')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF67LP37"),dbc.CardBody(children=[] , id='EF67LP373bi', style={'font-size':30, 'margin':'auto'})], id='cardEF67LP373bi')),
            ]
    ),
    dbc.Popover(
            EF67LP33,
            target="EF67LP333bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF06LP06,
            target="EF06LP0613bi1",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF67LP37,
            target="EF67LP373bi",
            body=True,
            trigger="hover"),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF67LP28"),dbc.CardBody(children=[] , id='EF67LP283bi1', style={'font-size':30, 'margin':'auto'})], id='cardEF67LP283bi1'), width=3),
           
            ]
    ),
    dbc.Popover(
            EF67LP28,
            target="EF67LP283bi1",
            body=True,
            trigger="hover"),
   
           
dbc.Row(children=[

    dbc.Col(dcc.Dropdown(df_port6ano3bi['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-turma153bi')),
    dbc.Col(dcc.Dropdown(df_habsport63bi.columns, value="EF67LP28", style ={'margin-top':10, 'margin-left':5}, id='drop-hab153bi')),
    
]),

html.Br(),
dbc.Row(children=[

    dbc.Col( dbc.Card(dcc.Graph(id='fighabs153bi',config= {'displaylogo': False}))),
    dbc.Col( dbc.Card(dcc.Graph(id='figacerto153bi',config= {'displaylogo': False}))),


]),


])

@app.callback(
    Output('total163bi','children'),
    Output('cardtotal163bi', 'color'),
    Input('drop-down163bi','value')
)
def habtotal(turma):
    df = df_port6ano3bi.loc[df_port6ano3bi['Turma']==turma]
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
    Output('EF67LP083bi','children'),
    Output('cardEF67LP083bi', 'color'),
    Input('drop-down163bi','value')
)
def hab1(turma):
    df= df_port6ano3bi.loc[df_port6ano3bi['Turma']==turma]
    soma = df['EF67LP08'].values.sum()
    qtd = df['EF67LP08'].count()
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
    Output('EF06LP043bi1','children'),
    Output('cardEF06LP043bi1', 'color'),
    Input('drop-down163bi','value')
)
def hab2(turma):
    df= df_port6ano3bi.loc[df_port6ano3bi['Turma']==turma]
    soma = df['EF06LP04'].values.sum()
    qtd = df['EF06LP04'].count()
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
    Output('EF67LP3213bi','children'),
    Output('cardEF67LP3213bi', 'color'),
    Input('drop-down163bi','value')
)
def hab3(turma):
    df= df_port6ano3bi.loc[df_port6ano3bi['Turma']==turma]
    soma = df['EF67LP32'].values.sum()
    qtd = df['EF67LP32'].count()
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
    Output('EF67LP333bi','children'),
    Output('cardEF67LP333bi', 'color'),
    Input('drop-down163bi','value')
)
def hab4(turma):
    df= df_port6ano3bi.loc[df_port6ano3bi['Turma']==turma]
    soma = df['EF67LP33'].values.sum()
    qtd = df['EF67LP33'].count()
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
    Output('EF06LP0613bi1','children'),
    Output('cardEF06LP0613bi1', 'color'),
    Input('drop-down163bi','value')
)
def hab6(turma):
    df= df_port6ano3bi.loc[df_port6ano3bi['Turma']==turma]
    soma = df['EF06LP06'].values.sum()
    qtd = df['EF06LP06'].count()
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
    Output('EF67LP373bi','children'),
    Output('cardEF67LP373bi', 'color'),
    Input('drop-down163bi','value')
)
def hab7(turma):
    df= df_port6ano3bi.loc[df_port6ano3bi['Turma']==turma]
    soma = df['EF67LP37'].values.sum()
    qtd = df['EF67LP37'].count()
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
    Output('EF67LP283bi1','children'),
    Output('cardEF67LP283bi1', 'color'),
    Input('drop-down163bi','value')
)
def hab8(turma):
    df= df_port6ano3bi.loc[df_port6ano3bi['Turma']==turma]
    soma = df['EF67LP28'].values.sum()
    qtd = df['EF67LP28'].count()
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
    Output('figacerto153bi','figure'),
    Input('drop-hab153bi','value'),
    Input('drop-turma153bi','value'),
)
def acertos(hab, turma):
    d = df_port6ano3bi.loc[df_port6ano3bi['Turma']==turma]
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
    Output('fighabs153bi','figure'),
    Input('drop-turma153bi','value'),
)
def habs(turma):
    df = df_port6ano3bi.loc[df_port6ano3bi['Turma']==turma]
    fig= px.histogram(df, x = 'Total', color='Total', labels= {'Total':'Percentual de Habilidades Desenvolvidas'}, title= 'Percentual de Habilidades Desenvolvidas <br> por Quantidade de Estudante'+' na turma '+str(turma).upper())
    fig.update_layout(showlegend=False)
    fig.update_yaxes( title= 'Quantidade de Estudantes')
    return fig
