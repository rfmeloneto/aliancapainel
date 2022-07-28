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
df_mat8ano2bi = pd.read_csv(DATA_PATH.joinpath("mat8ano2bi.csv"))
df_habs82bi= df_mat8ano2bi.drop(columns=['Escola','Estudante','Ano','Turma','Total']) 

layout = html.Div(children=[
    
    dbc.Row(dbc.Col(dcc.Dropdown(df_mat8ano2bi['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-down82bi',), width=2)),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("Domínio Geral das Habilidades"),dbc.CardBody( children=[], id='total82bi', style={'font-size':30, 'margin':'auto'})], id='cardtotal82bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF08MA05"),dbc.CardBody(children=[] , id='EF08MA052bi', style={'font-size':30, 'margin':'auto'})], id='cardEF08MA052bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF08MA10"),dbc.CardBody(children=[] , id='EF08MA102bi', style={'font-size':30, 'margin':'auto'})], id='cardEF08MA102bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF08MA11"),dbc.CardBody(children=[] , id='EF08MA112bi', style={'font-size':30, 'margin':'auto'})], id='cardEF08MA112bi')),
            ]
    ),
    dbc.Popover(
            totalgeral,
            target="total82bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF08MA05,
            target="EF08MA052bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF08MA10,
            target="EF08MA102bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF08MA11,
            target="EF08MA112bi",
            body=True,
            trigger="hover"),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF08MA19"),dbc.CardBody(children=[] , id='EF08MA192bi', style={'font-size':30, 'margin':'auto'})], id='cardEF08MA192bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF08MA23"),dbc.CardBody(children=[] , id='EF08MA232bi', style={'font-size':30, 'margin':'auto'})], id='cardEF08MA232bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF08MA14"),dbc.CardBody(children=[] , id='EF08MA142bi', style={'font-size':30, 'margin':'auto'})], id='cardEF08MA142bi')),
            ]
    ),
    dbc.Popover(
            EF08MA19,
            target="EF08MA192bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF08MA23,
            target="EF08MA232bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF08MA14,
            target="EF08MA142bi",
            body=True,
            trigger="hover"),
    
    html.Br(),
   

    
    

    dbc.Row(children=[

    dbc.Col(dcc.Dropdown(df_mat8ano2bi['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-turma82bi')),
    dbc.Col(dcc.Dropdown(df_habs82bi.columns, value="EF08MA14", style ={'margin-top':10, 'margin-left':5}, id='drop-hab82bi')),
    ]),

    html.Br(),
    dbc.Row(children=[

    dbc.Col( dbc.Card(dcc.Graph(id='fighabs82bi',config= {'displaylogo': False}))),
    dbc.Col( dbc.Card(dcc.Graph(id='figacerto82bi',config= {'displaylogo': False}))),

])

])

@app.callback(
    Output('total82bi','children'),
    Output('cardtotal82bi', 'color'),
    Input('drop-down82bi','value')
)
def habtotal(turma):
    df = df_mat8ano2bi.loc[df_mat8ano2bi['Turma']==turma]
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
    Output('EF08MA052bi','children'),
    Output('cardEF08MA052bi', 'color'),
    Input('drop-down82bi','value')
)
def hab1(turma):
    df= df_mat8ano2bi.loc[df_mat8ano2bi['Turma']==turma]
    soma = df['EF08MA05'].values.sum()
    qtd = df['EF08MA05'].count()
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
    Output('EF08MA102bi','children'),
    Output('cardEF08MA102bi', 'color'),
    Input('drop-down82bi','value')
)
def hab2(turma):
    df= df_mat8ano2bi.loc[df_mat8ano2bi['Turma']==turma]
    soma = df['EF08MA10'].values.sum()
    qtd = df['EF08MA10'].count()
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
    Output('EF08MA112bi','children'),
    Output('cardEF08MA112bi', 'color'),
    Input('drop-down82bi','value')
)
def hab3(turma):
    df= df_mat8ano2bi.loc[df_mat8ano2bi['Turma']==turma]
    soma = df['EF08MA11'].values.sum()
    qtd = df['EF08MA11'].count()
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
    Output('EF08MA192bi','children'),
    Output('cardEF08MA192bi', 'color'),
    Input('drop-down82bi','value')
)
def hab4(turma):
    df= df_mat8ano2bi.loc[df_mat8ano2bi['Turma']==turma]
    soma = df['EF08MA19'].values.sum()
    qtd = df['EF08MA19'].count()
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
    Output('EF08MA232bi','children'),
    Output('cardEF08MA232bi', 'color'),
    Input('drop-down82bi','value')
)
def hab5(turma):
    df= df_mat8ano2bi.loc[df_mat8ano2bi['Turma']==turma]
    soma = df['EF08MA23'].values.sum()
    qtd = df['EF08MA23'].count()
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
    Output('EF08MA142bi','children'),
    Output('cardEF08MA142bi', 'color'),
    Input('drop-down82bi','value')
)
def hab6(turma):
    df= df_mat8ano2bi.loc[df_mat8ano2bi['Turma']==turma]
    soma = df['EF08MA14'].values.sum()
    qtd = df['EF08MA14'].count()
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
    Output('figacerto82bi','figure'),
    Input('drop-hab82bi','value'),
    Input('drop-turma82bi','value'),
)
def acertos(hab, turma):
    d = df_mat8ano2bi.loc[df_mat8ano2bi['Turma']==turma]
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
    Output('fighabs82bi','figure'),
    Input('drop-turma82bi','value'),
)
def habs(turma):
    df = df_mat8ano2bi.loc[df_mat8ano2bi['Turma']==turma]
    fig= px.histogram(df, x = 'Total', color='Total', labels= {'Total':'Percentual de Habilidades Desenvolvidas'}, title= 'Percentual de Habilidades Desenvolvidas <br> por Quantidade de Estudante'+' na turma '+str(turma).upper())
    fig.update_layout(showlegend=False)
    fig.update_yaxes( title= 'Quantidade de Estudantes')
    return fig
