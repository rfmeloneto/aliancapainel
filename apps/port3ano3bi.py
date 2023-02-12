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
df_port3ano3bi = pd.read_csv(DATA_PATH.joinpath("port3ano3bi.csv"))
df_habsport33bi = df_port3ano3bi.drop(columns=['Escola','Estudante','Ano','Turma','Total']) 

layout = html.Div(children=[
    
    dbc.Row(dbc.Col(dcc.Dropdown(df_port3ano3bi['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-down123bi',), width=2)),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("Domínio Geral das Habilidades"),dbc.CardBody( children=[], id='total123bi', style={'font-size':30, 'margin':'auto'})], id='cardtotal123bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF03LP11"),dbc.CardBody(children=[] , id='EF03LP113bi1', style={'font-size':30, 'margin':'auto'})], id='cardEF03LP113bi1')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF03LP16"),dbc.CardBody(children=[] , id='EF03LP163bi', style={'font-size':30, 'margin':'auto'})], id='cardEF03LP163bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF03LP04"),dbc.CardBody(children=[] , id='EF03LP043bi', style={'font-size':30, 'margin':'auto'})], id='cardEF03LP043bi')),
            ]
    ),
    dbc.Popover(
            totalgeral,
            target="total123bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF03LP11,
            target="EF03LP113bi1",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF03LP16,
            target="EF03LP163bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF03LP04,
            target="EF03LP043bi",
            body=True,
            trigger="hover"),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF03LP23"),dbc.CardBody(children=[] , id='EF03LP233bi', style={'font-size':30, 'margin':'auto'})], id='cardEF03LP233bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF03LP05"),dbc.CardBody(children=[] , id='EF03LP053bi', style={'font-size':30, 'margin':'auto'})], id='cardEF03LP053bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF03LP06"),dbc.CardBody(children=[] , id='EF03LP063bi', style={'font-size':30, 'margin':'auto'})], id='cardEF03LP063bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF15LP14"),dbc.CardBody(children=[] , id='EF15LP143bi', style={'font-size':30, 'margin':'auto'})], id='cardEF15LP143bi')),
            ]
    ),
    dbc.Popover(
            EF03LP23,
            target="EF03LP233bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF03LP05,
            target="EF03LP053bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF03LP06,
            target="EF03LP063bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF15LP14,
            target="EF15LP143bi",
            body=True,
            trigger="hover"),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF15LP18"),dbc.CardBody(children=[] , id='EF15LP183bi1', style={'font-size':30, 'margin':'auto'})], id='cardEF15LP183bi1'), width=3),
            dbc.Col( dbc.Card([dbc.CardHeader("EF03LP08"),dbc.CardBody(children=[] , id='EF03LP083bi1', style={'font-size':30, 'margin':'auto'})], id='cardEF03LP083bi1'), width=3),
            dbc.Col( dbc.Card([dbc.CardHeader("EF03LP10"),dbc.CardBody(children=[] , id='EF03LP103bi1', style={'font-size':30, 'margin':'auto'})], id='cardEF03LP103bi1'), width=3),
            
            ]
    ),
    dbc.Popover(
            EF15LP18,
            target="EF15LP183bi1",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF03LP08,
            target="EF03LP083bi1",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF03LP10,
            target="EF03LP103bi1",
            body=True,
            trigger="hover"),
    

    html.Br(),
    
    dbc.Row(children=[

    dbc.Col(dcc.Dropdown(df_port3ano3bi['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-turma123bi')),
    dbc.Col(dcc.Dropdown(df_habsport33bi.columns, value="EF15LP18", style ={'margin-top':10, 'margin-left':5}, id='drop-hab123bi')),
    
]),

html.Br(),
dbc.Row(children=[

    dbc.Col( dbc.Card(dcc.Graph(id='fighabs123bi',config= {'displaylogo': False}))),
    dbc.Col( dbc.Card(dcc.Graph(id='figacerto123bi',config= {'displaylogo': False}))),


]),

])

@app.callback(
    Output('total123bi','children'),
    Output('cardtotal123bi', 'color'),
    Input('drop-down123bi','value')
)
def habtotal(turma):
    df = df_port3ano3bi.loc[df_port3ano3bi['Turma']==turma]
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
    Output('EF03LP113bi1','children'),
    Output('cardEF03LP113bi1', 'color'),
    Input('drop-down123bi','value')
)
def hab1(turma):
    df= df_port3ano3bi.loc[df_port3ano3bi['Turma']==turma]
    soma = df['EF03LP11'].values.sum()
    qtd = df['EF03LP11'].count()
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
    Output('EF03LP163bi','children'),
    Output('cardEF03LP163bi', 'color'),
    Input('drop-down123bi','value')
)
def hab2(turma):
    df= df_port3ano3bi.loc[df_port3ano3bi['Turma']==turma]
    soma = df['EF03LP16'].values.sum()
    qtd = df['EF03LP16'].count()
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
    Output('EF03LP043bi','children'),
    Output('cardEF03LP043bi', 'color'),
    Input('drop-down123bi','value')
)
def hab3(turma):
    df= df_port3ano3bi.loc[df_port3ano3bi['Turma']==turma]
    soma = df['EF03LP04'].values.sum()
    qtd = df['EF03LP04'].count()
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
    Output('EF03LP233bi','children'),
    Output('cardEF03LP233bi', 'color'),
    Input('drop-down123bi','value')
)
def hab4(turma):
    df= df_port3ano3bi.loc[df_port3ano3bi['Turma']==turma]
    soma = df['EF03LP23'].values.sum()
    qtd = df['EF03LP23'].count()
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
    Output('EF03LP053bi','children'),
    Output('cardEF03LP053bi', 'color'),
    Input('drop-down123bi','value')
)
def hab5(turma):
    df= df_port3ano3bi.loc[df_port3ano3bi['Turma']==turma]
    soma = df['EF03LP05'].values.sum()
    qtd = df['EF03LP05'].count()
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
    Output('EF03LP063bi','children'),
    Output('cardEF03LP063bi', 'color'),
    Input('drop-down123bi','value')
)
def hab6(turma):
    df= df_port3ano3bi.loc[df_port3ano3bi['Turma']==turma]
    soma = df['EF03LP06'].values.sum()
    qtd = df['EF03LP06'].count()
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
    Output('EF15LP143bi','children'),
    Output('cardEF15LP143bi', 'color'),
    Input('drop-down123bi','value')
)
def hab7(turma):
    df= df_port3ano3bi.loc[df_port3ano3bi['Turma']==turma]
    soma = df['EF15LP14'].values.sum()
    qtd = df['EF15LP14'].count()
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
    Output('EF15LP183bi1','children'),
    Output('cardEF15LP183bi1', 'color'),
    Input('drop-down123bi','value')
)
def hab8(turma):
    df= df_port3ano3bi.loc[df_port3ano3bi['Turma']==turma]
    soma = df['EF15LP18'].values.sum()
    qtd = df['EF15LP18'].count()
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
    Output('EF03LP083bi1','children'),
    Output('cardEF03LP083bi1', 'color'),
    Input('drop-down123bi','value')
)
def hab8(turma):
    df= df_port3ano3bi.loc[df_port3ano3bi['Turma']==turma]
    soma = df['EF03LP08'].values.sum()
    qtd = df['EF03LP08'].count()
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
    Output('EF03LP103bi1','children'),
    Output('cardEF03LP103bi1', 'color'),
    Input('drop-down123bi','value')
)
def hab8(turma):
    df= df_port3ano3bi.loc[df_port3ano3bi['Turma']==turma]
    soma = df['EF03LP10'].values.sum()
    qtd = df['EF03LP10'].count()
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
    Output('figacerto123bi','figure'),
    Input('drop-hab123bi','value'),
    Input('drop-turma123bi','value'),
)
def acertos(hab, turma):
    d = df_port3ano3bi.loc[df_port3ano3bi['Turma']==turma]
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
    Output('fighabs123bi','figure'),
    Input('drop-turma123bi','value'),
)
def habs( turma):
    df = df_port3ano3bi.loc[df_port3ano3bi['Turma']==turma]
    fig= px.histogram(df, x = 'Total', color='Total', labels= {'Total':'Percentual de Habilidades Desenvolvidas'}, title= 'Percentual de Habilidades Desenvolvidas <br> por Quantidade de Estudante'+' na turma '+str(turma).upper())
    fig.update_layout(showlegend=False)
    fig.update_yaxes( title= 'Quantidade de Estudantes')
    return fig



