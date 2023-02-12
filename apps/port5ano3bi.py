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
df_port5ano3bi = pd.read_csv(DATA_PATH.joinpath("port5ano3bi.csv")) 
df_habsport53bi = df_port5ano3bi.drop(columns=['Escola','Estudante','Ano','Turma','Total'])

layout = html.Div(children=[
    
    dbc.Row(dbc.Col(dcc.Dropdown(df_port5ano3bi['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-down153bi',), width=2)),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("Domínio Geral das Habilidades"),dbc.CardBody( children=[], id='total153bi', style={'font-size':30, 'margin':'auto'})], id='cardtotal153bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF05LP22"),dbc.CardBody(children=[] , id='EF05LP223bi', style={'font-size':30, 'margin':'auto'})], id='cardEF05LP223bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF15LP15"),dbc.CardBody(children=[] , id='EF15LP1523bi', style={'font-size':30, 'margin':'auto'})], id='cardEF15LP1523bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF15LP16"),dbc.CardBody(children=[] , id='EF15LP1623bi', style={'font-size':30, 'margin':'auto'})], id='cardEF15LP1623bi')),
            ]
    ),
    dbc.Popover(
            totalgeral,
            target="total153bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF05LP22,
            target="EF05LP223bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF15LP15,
            target="EF15LP1523bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF15LP16,
            target="EF15LP1623bi",
            body=True,
            trigger="hover"),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF05LP07"),dbc.CardBody(children=[] , id='EF05LP073bi', style={'font-size':30, 'margin':'auto'})], id='cardEF05LP073bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF35LP14"),dbc.CardBody(children=[] , id='EF35LP143bi', style={'font-size':30, 'margin':'auto'})], id='cardEF35LP143bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF35LP24"),dbc.CardBody(children=[] , id='EF35LP243bi1', style={'font-size':30, 'margin':'auto'})], id='cardEF35LP243bi1')),
            ]
    ),

    dbc.Popover(
            EF05LP07,
            target="EF05LP073bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF35LP14,
            target="EF35LP143bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF35LP24,
            target="EF35LP243bi1",
            body=True,
            trigger="hover"),
 
    html.Br(),
    
            
dbc.Row(children=[

    dbc.Col(dcc.Dropdown(df_port5ano3bi['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-turma143bi')),
    dbc.Col(dcc.Dropdown(df_habsport53bi.columns, value="EF35LP24", style ={'margin-top':10, 'margin-left':5}, id='drop-hab143bi')),
    
]),

html.Br(),
dbc.Row(children=[

    dbc.Col( dbc.Card(dcc.Graph(id='fighabs143bi',config= {'displaylogo': False}))),
    dbc.Col( dbc.Card(dcc.Graph(id='figacerto143bi',config= {'displaylogo': False}))),


]),

    

])

@app.callback(
    Output('total153bi','children'),
    Output('cardtotal153bi', 'color'),
    Input('drop-down153bi','value')
)
def habtotal(turma):
    df = df_port5ano3bi.loc[df_port5ano3bi['Turma']==turma]
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
    Output('EF05LP223bi','children'),
    Output('cardEF05LP223bi', 'color'),
    Input('drop-down153bi','value')
)
def hab1(turma):
    df= df_port5ano3bi.loc[df_port5ano3bi['Turma']==turma]
    soma = df['EF05LP22'].values.sum()
    qtd = df['EF05LP22'].count()
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
    Output('EF15LP1523bi','children'),
    Output('cardEF15LP1523bi', 'color'),
    Input('drop-down153bi','value')
)
def hab2(turma):
    df= df_port5ano3bi.loc[df_port5ano3bi['Turma']==turma]
    soma = df['EF15LP15'].values.sum()
    qtd = df['EF15LP15'].count()
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
    Output('EF35LP273bi','children'),
    Output('cardEF35LP273bi', 'color'),
    Input('drop-down153bi','value')
)
def hab3(turma):
    df= df_port5ano3bi.loc[df_port5ano3bi['Turma']==turma]
    soma = df['EF35LP27'].values.sum()
    qtd = df['EF35LP27'].count()
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
    Output('EF05LP073bi','children'),
    Output('cardEF05LP073bi', 'color'),
    Input('drop-down153bi','value')
)
def hab4(turma):
    df= df_port5ano3bi.loc[df_port5ano3bi['Turma']==turma]
    soma = df['EF05LP07'].values.sum()
    qtd = df['EF05LP07'].count()
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
    Output('EF35LP143bi','children'),
    Output('cardEF35LP143bi', 'color'),
    Input('drop-down153bi','value')
)
def hab5(turma):
    df= df_port5ano3bi.loc[df_port5ano3bi['Turma']==turma]
    soma = df['EF35LP14'].values.sum()
    qtd = df['EF35LP14'].count()
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
    Output('EF35LP243bi1','children'),
    Output('cardEF35LP243bi1', 'color'),
    Input('drop-down153bi','value')
)
def hab6(turma):
    df= df_port5ano3bi.loc[df_port5ano3bi['Turma']==turma]
    soma = df['EF35LP24'].values.sum()
    qtd = df['EF35LP24'].count()
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
    Output('EF15LP1623bi','children'),
    Output('cardEF15LP1623bi', 'color'),
    Input('drop-down153bi','value')
)
def hab7(turma):
    df= df_port5ano3bi.loc[df_port5ano3bi['Turma']==turma]
    soma = df['EF15LP16'].values.sum()
    qtd = df['EF15LP16'].count()
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
    Output('EF05LP033bi','children'),
    Output('cardEF05LP033bi', 'color'),
    Input('drop-down153bi','value')
)
def hab8(turma):
    df= df_port5ano3bi.loc[df_port5ano3bi['Turma']==turma]
    soma = df['EF05LP03'].values.sum()
    qtd = df['EF05LP03'].count()
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
    Output('EF05LP0123bi','children'),
    Output('cardEF05LP0123bi', 'color'),
    Input('drop-down153bi','value')
)
def hab10(turma):
    df= df_port5ano3bi.loc[df_port5ano3bi['Turma']==turma]
    soma = df['EF05LP01'].values.sum()
    qtd = df['EF05LP01'].count()
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

#-----------------------------------------------------------------


@app.callback(
    Output('figacerto143bi','figure'),
    Input('drop-hab143bi','value'),
    Input('drop-turma143bi','value'),
)
def acertos(hab, turma):
    d = df_port5ano3bi.loc[df_port5ano3bi['Turma']==turma]
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
    Output('fighabs143bi','figure'),
    Input('drop-turma143bi','value'),
)
def habs(turma):
    df = df_port5ano3bi.loc[df_port5ano3bi['Turma']==turma]
    fig= px.histogram(df, x = 'Total', color='Total', labels= {'Total':'Percentual de Habilidades Desenvolvidas'}, title= 'Percentual de Habilidades Desenvolvidas <br> por Quantidade de Estudante'+' na turma '+str(turma).upper())
    fig.update_layout(showlegend=False)
    fig.update_yaxes( title= 'Quantidade de Estudantes')
    return fig



