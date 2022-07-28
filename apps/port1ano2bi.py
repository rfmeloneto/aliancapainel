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
df_port1ano2bi = pd.read_csv(DATA_PATH.joinpath("port1ano2bi.csv"))
df_habsport12bi = df_port1ano2bi.drop(columns=['Escola','Estudante','Ano','Turma','Total','Unnamed: 0'])
 

layout = html.Div(children=[
    
    dbc.Row(children = [ 
        dbc.Col(dcc.Dropdown(df_port1ano2bi['Escola'].unique(), value='Duque de Caxias', style ={'margin-top':10, 'margin-left':5}, id='escola22bi',), width=2), 
        dbc.Col(dcc.Dropdown(df_port1ano2bi['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-down202bi',), width=2)
        ]),
        
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("Domínio Geral das Habilidades"),dbc.CardBody( children=[], id='total202bi', style={'font-size':30, 'margin':'auto'})], id='cardtotal202bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF12LP04"),dbc.CardBody(children=[] , id='EF12LP042bi', style={'font-size':30, 'margin':'auto'})], id='cardEF12LP042bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF01LP08"),dbc.CardBody(children=[] , id='EF01LP082bi', style={'font-size':30, 'margin':'auto'})], id='cardEF01LP082bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF01LP10"),dbc.CardBody(children=[] , id='EF01LP102bi', style={'font-size':30, 'margin':'auto'})], id='cardEF01LP102bi')),
            ]
    ),
    dbc.Popover(
            totalgeral,
            target="total202bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF12LP04,
            target="EF12LP042bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF01LP08,
            target="EF01LP082bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF01LP10,
            target="EF01LP102bi",
            body=True,
            trigger="hover"),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF01LP11"),dbc.CardBody(children=[] , id='EF01LP112bi', style={'font-size':30, 'margin':'auto'})], id='cardEF01LP112bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF15LP16"),dbc.CardBody(children=[] , id='EF15LP162bi', style={'font-size':30, 'margin':'auto'})], id='cardEF15LP162bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF01LP26"),dbc.CardBody(children=[] , id='EF01LP262bi', style={'font-size':30, 'margin':'auto'})], id='cardEF01LP262bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF15LP18"),dbc.CardBody(children=[] , id='EF15LP182bi', style={'font-size':30, 'margin':'auto'})], id='cardEF15LP182bi')),
            ]
    ),
    dbc.Popover(
            EF01LP11,
            target="EF01LP112bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF15LP16,
            target="EF15LP162bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF01LP26,
            target="EF01LP262bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF15LP18,
            target="EF15LP182bi",
            body=True,
            trigger="hover"),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF12LP08"),dbc.CardBody(children=[] , id='EF12LP082bi', style={'font-size':30, 'margin':'auto'})], id='cardEF12LP082bi'), width=3),
            dbc.Col( dbc.Card([dbc.CardHeader("EF01LP12"),dbc.CardBody(children=[] , id='EF01LP122bi', style={'font-size':30, 'margin':'auto'})], id='cardEF01LP122bi'), width=3),
            dbc.Col( dbc.Card([dbc.CardHeader("EF12LP17"),dbc.CardBody(children=[] , id='EF12LP172bi', style={'font-size':30, 'margin':'auto'})], id='cardEF12LP172bi'), width=3),
            
            ]
    ),

    dbc.Popover(
            EF12LP08,
            target="EF12LP082bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
           EF01LP12,
            target="EF01LP122bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF12LP17,
            target="EF12LP172bi",
            body=True,
            trigger="hover"),
    
 html.Br(),
     dbc.Row(children=[
    dbc.Col(dcc.Dropdown(df_port1ano2bi['Escola'].unique(), value="Duque de Caxias", style ={'margin-top':10, 'margin-left':5}, id='drop-escola102bi')),    
    dbc.Col(dcc.Dropdown(df_port1ano2bi['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-turma102bi')),
    dbc.Col(dcc.Dropdown(df_habsport12bi.columns, value="EF12LP17", style ={'margin-top':10, 'margin-left':5}, id='drop-hab102bi')),
    ]),

    html.Br(),
    dbc.Row(children=[

    dbc.Col( dbc.Card(dcc.Graph(id='fighabs102bi',config= {'displaylogo': False}))),
    dbc.Col( dbc.Card(dcc.Graph(id='figacerto102bi',config= {'displaylogo': False}))),

])


])

@app.callback(
    Output('total202bi','children'),
    Output('cardtotal202bi', 'color'),
    Input('escola22bi','value'),
    Input('drop-down202bi','value')
)
def habtotal(escola,turma):

    dff = df_port1ano2bi.loc[df_port1ano2bi['Escola']==escola]
    df= dff.loc[dff['Turma']==turma]
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
    Output('EF12LP042bi','children'),
    Output('cardEF12LP042bi', 'color'),
    Input('escola22bi','value'),
    Input('drop-down202bi','value')
)
def hab1(escola,turma):
    dff = df_port1ano2bi.loc[df_port1ano2bi['Escola']==escola]
    df= dff.loc[dff['Turma']==turma]
    soma = df['EF12LP04'].values.sum()
    qtd = df['EF12LP04'].count()
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
    Output('EF01LP082bi','children'),
    Output('cardEF01LP082bi', 'color'),
    Input('escola22bi','value'),
    Input('drop-down202bi','value')
)
def hab2(escola,turma):
    dff = df_port1ano2bi.loc[df_port1ano2bi['Escola']==escola]
    df= dff.loc[dff['Turma']==turma]
    soma = df['EF01LP08'].values.sum()
    qtd = df['EF01LP08'].count()
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
    Output('EF01LP102bi','children'),
    Output('cardEF01LP102bi', 'color'),
    Input('escola22bi','value'),
    Input('drop-down202bi','value')
)
def hab3(escola,turma):
    dff = df_port1ano2bi.loc[df_port1ano2bi['Escola']==escola]
    df= dff.loc[dff['Turma']==turma]
    soma = df['EF01LP10'].values.sum()
    qtd = df['EF01LP10'].count()
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
    Output('EF01LP112bi','children'),
    Output('cardEF01LP112bi', 'color'),
    Input('escola22bi','value'),
    Input('drop-down202bi','value')
)
def hab4(escola,turma):
    dff = df_port1ano2bi.loc[df_port1ano2bi['Escola']==escola]
    df= dff.loc[dff['Turma']==turma]
    soma = df['EF01LP11'].values.sum()
    qtd = df['EF01LP11'].count()
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
    Output('EF15LP162bi','children'),
    Output('cardEF15LP162bi', 'color'),
    Input('escola22bi','value'),
    Input('drop-down202bi','value')
)
def hab5(escola,turma):
    dff = df_port1ano2bi.loc[df_port1ano2bi['Escola']==escola]
    df= dff.loc[dff['Turma']==turma]
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
    Output('EF01LP262bi','children'),
    Output('cardEF01LP262bi', 'color'),
    Input('escola22bi','value'),
    Input('drop-down202bi','value')
)
def hab6(escola,turma):
    dff = df_port1ano2bi.loc[df_port1ano2bi['Escola']==escola]
    df= dff.loc[dff['Turma']==turma]
    soma = df['EF01LP26'].values.sum()
    qtd = df['EF01LP26'].count()
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
    Output('EF15LP182bi','children'),
    Output('cardEF15LP182bi', 'color'),
    Input('escola22bi','value'),
    Input('drop-down202bi','value')
)
def hab7(escola,turma):
    dff = df_port1ano2bi.loc[df_port1ano2bi['Escola']==escola]
    df= dff.loc[dff['Turma']==turma]
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

@app.callback(
    Output('EF12LP082bi','children'),
    Output('cardEF12LP082bi', 'color'),
    Input('escola22bi','value'),
    Input('drop-down202bi','value')
)
def hab8(escola,turma):
    dff = df_port1ano2bi.loc[df_port1ano2bi['Escola']==escola]
    df= dff.loc[dff['Turma']==turma]
    soma = df['EF12LP08'].values.sum()
    qtd = df['EF12LP08'].count()
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
    Output('EF01LP122bi','children'),
    Output('cardEF01LP122bi', 'color'),
    Input('escola22bi','value'),
    Input('drop-down202bi','value')
)
def hab10(escola,turma):
    dff = df_port1ano2bi.loc[df_port1ano2bi['Escola']==escola]
    df= dff.loc[dff['Turma']==turma]
    soma = df['EF01LP12'].values.sum()
    qtd = df['EF01LP12'].count()
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
    Output('EF12LP172bi','children'),
    Output('cardEF12LP172bi', 'color'),
    Input('escola22bi','value'),
    Input('drop-down202bi','value')
)
def hab8(escola,turma):
    dff = df_port1ano2bi.loc[df_port1ano2bi['Escola']==escola]
    df= dff.loc[dff['Turma']==turma]
    soma = df['EF12LP17'].values.sum()
    qtd = df['EF12LP17'].count()
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
    Output('figacerto102bi','figure'),
    Input('drop-hab102bi','value'),
    Input('drop-turma102bi','value'),
    Input('drop-escola102bi','value')
)
def acertos(hab, turma, escola):
    d = df_port1ano2bi.loc[df_port1ano2bi['Escola']==escola]
    df = d[d['Turma']==turma]
    dff= df[hab]
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
    Output('fighabs102bi','figure'),
    Input('drop-turma102bi','value'),
    Input('drop-escola102bi','value')
)
def habs( turma,escola):
    d = df_port1ano2bi.loc[df_port1ano2bi['Escola']==escola]
    df = d[d['Turma']==turma]
    fig= px.histogram(df, x = 'Total', color='Total', labels= {'Total':'Percentual de Habilidades Desenvolvidas'}, title= 'Percentual de Habilidades Desenvolvidas <br> por Quantidade de Estudante'+' na turma '+str(turma).upper())
    fig.update_layout(showlegend=False)
    fig.update_yaxes( title= 'Quantidade de Estudantes')
    return fig


