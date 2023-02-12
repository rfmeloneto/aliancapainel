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
df_mat3ano3bi = pd.read_csv(DATA_PATH.joinpath("mat3ano3bi.csv"))
df_habs33bi= df_mat3ano3bi.drop(columns=['Escola','Estudante','Ano','Turma','Total'])

layout = html.Div(children=[
    
    dbc.Row(dbc.Col(dcc.Dropdown(df_mat3ano3bi['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-down33bi',), width=2)), 
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("Domínio Geral das Habilidades"),dbc.CardBody( children=[], id='total33bi', style={'font-size':30, 'margin':'auto'})], id='cardtotal33bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF03MA06"),dbc.CardBody(children=[] , id='EF03MA063bi', style={'font-size':30, 'margin':'auto'})], id='cardEF03MA063bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF03MA05"),dbc.CardBody(children=[] , id='EF03MA053bi', style={'font-size':30, 'margin':'auto'})], id='cardEF03MA053bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF03MA03"),dbc.CardBody(children=[] , id='EF03MA033bi', style={'font-size':30, 'margin':'auto'})], id='cardEF03MA033bi')),
            ]
    ),

    dbc.Popover(
            totalgeral,
            target="total33bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF03MA06,
            target="EF03MA063bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF03MA05,
            target="EF03MA053bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF03MA03,
            target="EF03MA03bi",
            body=True,
            trigger="hover"),


    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF03MA08"),dbc.CardBody(children=[] , id='EF03MA083bi', style={'font-size':30, 'margin':'auto'})], id='cardEF03MA083bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF03MA11"),dbc.CardBody(children=[] , id='EF03MA113bi', style={'font-size':30, 'margin':'auto'})], id='cardEF03MA113bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF03MA12"),dbc.CardBody(children=[] , id='EF03MA123bi', style={'font-size':30, 'margin':'auto'})], id='cardEF03MA123bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF03MA22"),dbc.CardBody(children=[] , id='EF03MA223bi', style={'font-size':30, 'margin':'auto'})], id='cardEF03MA223bi')),
            ]
    ),
    html.Br(),

    dbc.Popover(
            EF03MA08,
            target="EF03MA083bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF03MA11,
            target="EF03MA113bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF03MA12,
            target="EF03MA123bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF03MA22,
            target="EF03MA223bi",
            body=True,
            trigger="hover"),

    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF03MA23"),dbc.CardBody(children=[] , id='EF03MA233bi', style={'font-size':30, 'margin':'auto'})], id='cardEF03MA233bi'), width=3),
            dbc.Col( dbc.Card([dbc.CardHeader("EF03MA25"),dbc.CardBody(children=[] , id='EF03MA253bi', style={'font-size':30, 'margin':'auto'})], id='cardEF03MA253bi'), width=3),
            
            ]
    ),

    dbc.Popover(
            EF03MA23,
            target="EF03MA233bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF03MA25,
            target="EF03MA253bi",
            body=True,
            trigger="hover"),

    html.Br(),

    dbc.Row(children=[

    dbc.Col(dcc.Dropdown(df_mat3ano3bi['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-turma32b')),
    dbc.Col(dcc.Dropdown(df_habs33bi.columns, value="EF03MA22", style ={'margin-top':10, 'margin-left':5}, id='drop-hab32b')),
    
]),

html.Br(),
dbc.Row(children=[

    dbc.Col( dbc.Card(dcc.Graph(id='fighabs33b',config= {'displaylogo': False}))),
    dbc.Col( dbc.Card(dcc.Graph(id='figacerto33b',config= {'displaylogo': False}))),


]),


])

@app.callback(
    Output('total33bi','children'),
    Output('cardtotal33bi', 'color'),
    Input('drop-down33bi','value')
)
def habtotal(turma):
    df = df_mat3ano3bi.loc[df_mat3ano3bi['Turma']==turma]
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
    Output('EF03MA063bi','children'),
    Output('cardEF03MA063bi', 'color'),
    Input('drop-down33bi','value')
)
def hab1(turma):
    df= df_mat3ano3bi.loc[df_mat3ano3bi['Turma']==turma]
    soma = df['EF03MA06'].values.sum()
    qtd = df['EF03MA06'].count()
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
    Output('EF03MA053bi','children'),
    Output('cardEF03MA053bi', 'color'),
    Input('drop-down33bi','value')
)
def hab2(turma):
    df= df_mat3ano3bi.loc[df_mat3ano3bi['Turma']==turma]
    soma = df['EF03MA05'].values.sum()
    qtd = df['EF03MA05'].count()
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
    Output('EF03MA033bi','children'),
    Output('cardEF03MA033bi', 'color'),
    Input('drop-down33bi','value')
)
def hab3(turma):
    df= df_mat3ano3bi.loc[df_mat3ano3bi['Turma']==turma]
    soma = df['EF03MA03'].values.sum()
    qtd = df['EF03MA03'].count()
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
    Output('EF03MA083bi','children'),
    Output('cardEF03MA083bi', 'color'),
    Input('drop-down33bi','value')
)
def hab4(turma):
    df= df_mat3ano3bi.loc[df_mat3ano3bi['Turma']==turma]
    soma = df['EF03MA08'].values.sum()
    qtd = df['EF03MA08'].count()
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
    Output('EF03MA113bi','children'),
    Output('cardEF03MA113bi', 'color'),
    Input('drop-down33bi','value')
)
def hab5(turma):
    df= df_mat3ano3bi.loc[df_mat3ano3bi['Turma']==turma]
    soma = df['EF03MA11'].values.sum()
    qtd = df['EF03MA11'].count()
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
    Output('EF03MA123bi','children'),
    Output('cardEF03MA123bi', 'color'),
    Input('drop-down33bi','value')
)
def hab6(turma):
    df= df_mat3ano3bi.loc[df_mat3ano3bi['Turma']==turma]
    soma = df['EF03MA12'].values.sum()
    qtd = df['EF03MA12'].count()
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
    Output('EF03MA223bi','children'),
    Output('cardEF03MA223bi', 'color'),
    Input('drop-down33bi','value')
)
def hab7(turma):
    df= df_mat3ano3bi.loc[df_mat3ano3bi['Turma']==turma]
    soma = df['EF03MA22'].values.sum()
    qtd = df['EF03MA22'].count()
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
    Output('EF03MA233bi','children'),
    Output('cardEF03MA233bi', 'color'),
    Input('drop-down33bi','value')
)
def hab8(turma):
    df= df_mat3ano3bi.loc[df_mat3ano3bi['Turma']==turma]
    soma = df['EF03MA23'].values.sum()
    qtd = df['EF03MA23'].count()
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
    Output('EF03MA253bi','children'),
    Output('cardEF03MA253bi', 'color'),
    Input('drop-down33bi','value')
)
def hab8(turma):
    df= df_mat3ano3bi.loc[df_mat3ano3bi['Turma']==turma]
    soma = df['EF03MA25'].values.sum()
    qtd = df['EF03MA25'].count()
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
    Output('figacerto33b','figure'),
    Input('drop-hab32b','value'),
    Input('drop-turma32b','value'),
)
def acertos(hab, turma):
    d = df_mat3ano3bi.loc[df_mat3ano3bi['Turma']==turma]
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
    Output('fighabs33b','figure'),
    Input('drop-turma32b','value'),
)
def habs(turma):
    df = df_mat3ano3bi.loc[df_mat3ano3bi['Turma']==turma]
    fig= px.histogram(df, x = 'Total', color='Total', labels= {'Total':'Percentual de Habilidades Desenvolvidas'}, title= 'Percentual de Habilidades Desenvolvidas <br> por Quantidade de Estudante'+' na turma '+str(turma).upper())
    fig.update_layout(showlegend=False)
    fig.update_yaxes( title= 'Quantidade de Estudantes')
    return fig

