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
df_port4ano = pd.read_csv(DATA_PATH.joinpath("port4ano.csv")) 
df_habsport4 = df_port4ano.drop(columns=['Escola','Estudante','Ano','Turma','Total'])

layout = html.Div(children=[
    
    dbc.Row(dbc.Col(dcc.Dropdown(df_port4ano['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-down14',), width=2)),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("Domínio Geral das Habilidades"),dbc.CardBody( children=[], id='total14', style={'font-size':30, 'margin':'auto'})], id='cardtotal14')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF35LP01"),dbc.CardBody(children=[] , id='EF35LP01', style={'font-size':30, 'margin':'auto'})], id='cardEF35LP01')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF04LP10"),dbc.CardBody(children=[] , id='EF04LP10', style={'font-size':30, 'margin':'auto'})], id='cardEF04LP10')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF35LP05"),dbc.CardBody(children=[] , id='EF35LP051', style={'font-size':30, 'margin':'auto'})], id='cardEF35LP051')),
            ]
    ),
    dbc.Popover(
            totalgeral,
            target="total14",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF35LP01,
            target="EF35LP01",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF04LP10,
            target="EF04LP10",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF35LP05,
            target="EF35LP051",
            body=True,
            trigger="hover"),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF35LP06"),dbc.CardBody(children=[] , id='EF35LP06', style={'font-size':30, 'margin':'auto'})], id='cardEF35LP06')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF15LP03"),dbc.CardBody(children=[] , id='EF15LP031', style={'font-size':30, 'margin':'auto'})], id='cardEF15LP031')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF35LP04"),dbc.CardBody(children=[] , id='EF35LP041', style={'font-size':30, 'margin':'auto'})], id='cardEF35LP041')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF04LP02"),dbc.CardBody(children=[] , id='EF04LP02', style={'font-size':30, 'margin':'auto'})], id='cardEF04LP02')),
            ]
    ),
    dbc.Popover(
            EF35LP06,
            target="EF35LP06",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF15LP03,
            target="EF15LP031",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF35LP04,
            target="EF35LP041",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF04LP02,
            target="EF04LP02",
            body=True,
            trigger="hover"),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF35LP12"),dbc.CardBody(children=[] , id='EF35LP12', style={'font-size':30, 'margin':'auto'})], id='cardEF35LP12'), width=3),
            dbc.Col( dbc.Card([dbc.CardHeader("EF35LP21"),dbc.CardBody(children=[] , id='EF35LP211', style={'font-size':30, 'margin':'auto'})], id='cardEF35LP211'), width=3),
            dbc.Col( dbc.Card([dbc.CardHeader("EF35LP13"),dbc.CardBody(children=[] , id='EF35LP13', style={'font-size':30, 'margin':'auto'})], id='cardEF35LP13'), width=3),
            dbc.Col( dbc.Card([dbc.CardHeader("EF35LP29"),dbc.CardBody(children=[] , id='EF35LP29', style={'font-size':30, 'margin':'auto'})], id='cardEF35LP29'), width=3)
            
            ]
    ),

    dbc.Popover(
            EF35LP12,
            target="EF35LP12",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF35LP21,
            target="EF35LP211",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF35LP13,
            target="EF35LP13",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF35LP29,
            target="EF35LP29",
            body=True,
            trigger="hover"),

dbc.Row(children=[

    dbc.Col(dcc.Dropdown(df_port4ano['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-turma13')),
    dbc.Col(dcc.Dropdown(df_habsport4.columns, value="EF35LP29", style ={'margin-top':10, 'margin-left':5}, id='drop-hab13')),
    
]),

html.Br(),
dbc.Row(children=[

    dbc.Col( dbc.Card(dcc.Graph(id='fighabs13',config= {'displaylogo': False}))),
    dbc.Col( dbc.Card(dcc.Graph(id='figacerto13',config= {'displaylogo': False}))),


]),


])

@app.callback(
    Output('total14','children'),
    Output('cardtotal14', 'color'),
    Input('drop-down14','value')
)
def habtotal(turma):
    df = df_port4ano.loc[df_port4ano['Turma']==turma]
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
    Output('EF35LP01','children'),
    Output('cardEF35LP01', 'color'),
    Input('drop-down14','value')
)
def hab1(turma):
    df= df_port4ano.loc[df_port4ano['Turma']==turma]
    soma = df['EF35LP01'].values.sum()
    qtd = df['EF35LP01'].count()
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
    Output('EF04LP10','children'),
    Output('cardEF04LP10', 'color'),
    Input('drop-down14','value')
)
def hab2(turma):
    df= df_port4ano.loc[df_port4ano['Turma']==turma]
    soma = df['EF04LP10'].values.sum()
    qtd = df['EF04LP10'].count()
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
    Output('EF35LP051','children'),
    Output('cardEF35LP051', 'color'),
    Input('drop-down14','value')
)
def hab3(turma):
    df= df_port4ano.loc[df_port4ano['Turma']==turma]
    soma = df['EF35LP05'].values.sum()
    qtd = df['EF35LP05'].count()
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
    Output('EF35LP06','children'),
    Output('cardEF35LP06', 'color'),
    Input('drop-down14','value')
)
def hab4(turma):
    df= df_port4ano.loc[df_port4ano['Turma']==turma]
    soma = df['EF35LP06'].values.sum()
    qtd = df['EF35LP06'].count()
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
    Output('EF15LP031','children'),
    Output('cardEF15LP031', 'color'),
    Input('drop-down14','value')
)
def hab5(turma):
    df= df_port4ano.loc[df_port4ano['Turma']==turma]
    soma = df['EF15LP03'].values.sum()
    qtd = df['EF15LP03'].count()
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
    Output('EF35LP041','children'),
    Output('cardEF35LP041', 'color'),
    Input('drop-down14','value')
)
def hab6(turma):
    df= df_port4ano.loc[df_port4ano['Turma']==turma]
    soma = df['EF35LP04'].values.sum()
    qtd = df['EF35LP04'].count()
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
    Output('EF04LP02','children'),
    Output('cardEF04LP02', 'color'),
    Input('drop-down14','value')
)
def hab7(turma):
    df= df_port4ano.loc[df_port4ano['Turma']==turma]
    soma = df['EF04LP02'].values.sum()
    qtd = df['EF04LP02'].count()
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
    Output('EF35LP12','children'),
    Output('cardEF35LP12', 'color'),
    Input('drop-down14','value')
)
def hab8(turma):
    df= df_port4ano.loc[df_port4ano['Turma']==turma]
    soma = df['EF35LP12'].values.sum()
    qtd = df['EF35LP12'].count()
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
    Output('EF35LP211','children'),
    Output('cardEF35LP211', 'color'),
    Input('drop-down14','value')
)
def hab10(turma):
    df= df_port4ano.loc[df_port4ano['Turma']==turma]
    soma = df['EF35LP21'].values.sum()
    qtd = df['EF35LP21'].count()
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
    Output('EF35LP13','children'),
    Output('cardEF35LP13', 'color'),
    Input('drop-down14','value')
)
def hab10(turma):
    df= df_port4ano.loc[df_port4ano['Turma']==turma]
    soma = df['EF35LP13'].values.sum()
    qtd = df['EF35LP13'].count()
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
    Output('EF35LP29','children'),
    Output('cardEF35LP29', 'color'),
    Input('drop-down14','value')
)
def hab11(turma):
    df= df_port4ano.loc[df_port4ano['Turma']==turma]
    soma = df['EF35LP29'].values.sum()
    qtd = df['EF35LP29'].count()
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
    Output('figacerto13','figure'),
    Input('drop-hab13','value'),
    Input('drop-turma13','value'),
)
def acertos(hab, turma):
    d = df_port4ano.loc[df_port4ano['Turma']==turma]
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
    Output('fighabs13','figure'),
    Input('drop-turma13','value'),
)
def habs( turma):
    df = df_port4ano.loc[df_port4ano['Turma']==turma]
    fig= px.histogram(df, x = 'Total', color='Total', labels= {'Total':'Percentual de Habilidades Desenvolvidas'}, title= 'Percentual de Habilidades Desenvolvidas <br> por Quantidade de Estudante'+' na turma '+str(turma).upper())
    fig.update_layout(showlegend=False)
    fig.update_yaxes( title= 'Quantidade de Estudantes')
    return fig



