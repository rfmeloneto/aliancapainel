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
df_mat4ano3bi = pd.read_csv(DATA_PATH.joinpath("mat4ano3bi.csv"))
df_habs43bi= df_mat4ano3bi.drop(columns=['Escola','Estudante','Ano','Turma','Total'])  

layout = html.Div(children=[
    
    dbc.Row(dbc.Col(dcc.Dropdown(df_mat4ano3bi['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-down43bi',), width=2)),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("Domínio Geral das Habilidades"),dbc.CardBody( children=[], id='total43bi', style={'font-size':30, 'margin':'auto'})], id='cardtotal43bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF04MA06"),dbc.CardBody(children=[] , id='EF04MA063bi', style={'font-size':30, 'margin':'auto'})], id='cardEF04MA063bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF04MA09"),dbc.CardBody(children=[] , id='EF04MA093bi', style={'font-size':30, 'margin':'auto'})], id='cardEF04MA093bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF04MA07"),dbc.CardBody(children=[] , id='EF04MA073bi', style={'font-size':30, 'margin':'auto'})], id='cardEF04MA073bi')),
            ]
    ),
    dbc.Popover(
            totalgeral,
            target="total43bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF04MA06,
            target="EF04MA063bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF04MA09,
            target="EF04MA093bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF04MA07,
            target="EF04MA073bi",
            body=True,
            trigger="hover"),

    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF04MA11"),dbc.CardBody(children=[] , id='EF04MA113bi', style={'font-size':30, 'margin':'auto'})], id='cardEF04MA113bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF04MA23"),dbc.CardBody(children=[] , id='EF04MA233bi', style={'font-size':30, 'margin':'auto'})], id='cardEF04MA233bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF04MA19"),dbc.CardBody(children=[] , id='EF04MA193bi', style={'font-size':30, 'margin':'auto'})], id='cardEF04MA193bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF04MA24"),dbc.CardBody(children=[] , id='EF04MA243bi', style={'font-size':30, 'margin':'auto'})], id='cardEF04MA243bi')),
            ]
    ),
    html.Br(),
    dbc.Popover(
            EF04MA11,
            target="EF04MA113bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF04MA23,
            target="EF04MA233bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF04MA19,
            target="EF04MA193bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF04MA24,
            target="EF04MA243bi",
            body=True,
            trigger="hover"),
    
    html.Br(),
    dbc.Row(
        children = [
            dbc.Col( dbc.Card([dbc.CardHeader("EF04MA28"),dbc.CardBody(children=[] , id='EF04MA283bi', style={'font-size':30, 'margin':'auto'})], id='cardEF04MA283bi')),
        ]
    ),
    dbc.Popover(
            EF04MA28,
            target="EF04MA283bi",
            body=True,
            trigger="hover"),

    html.Br(),

    dbc.Row(children=[

        dbc.Col(dcc.Dropdown(df_mat4ano3bi['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-turma43bi')),
        dbc.Col(dcc.Dropdown(df_habs43bi.columns, value="EF04MA24", style ={'margin-top':10, 'margin-left':5}, id='drop-hab43bi')),
    
]),

    html.Br(),
    dbc.Row(children=[

        dbc.Col( dbc.Card(dcc.Graph(id='fighabs43bi',config= {'displaylogo': False}))),
        dbc.Col( dbc.Card(dcc.Graph(id='figacerto43bi',config= {'displaylogo': False}))),
])

])

@app.callback(
    Output('total43bi','children'),
    Output('cardtotal43bi', 'color'),
    Input('drop-down43bi','value')
)
def habtotal(turma):
    df = df_mat4ano3bi.loc[df_mat4ano3bi['Turma']==turma]
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
    Output('EF04MA063bi','children'),
    Output('cardEF04MA063bi', 'color'),
    Input('drop-down43bi','value')
)
def hab1(turma):
    df= df_mat4ano3bi.loc[df_mat4ano3bi['Turma']==turma]
    soma = df['EF04MA06'].values.sum()
    qtd = df['EF04MA06'].count()
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
    Output('EF04MA093bi','children'),
    Output('cardEF04MA093bi', 'color'),
    Input('drop-down43bi','value')
)
def hab2(turma):
    df= df_mat4ano3bi.loc[df_mat4ano3bi['Turma']==turma]
    soma = df['EF04MA09'].values.sum()
    qtd = df['EF04MA09'].count()
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
    Output('EF04MA073bi','children'),
    Output('cardEF04MA073bi', 'color'),
    Input('drop-down43bi','value')
)
def hab3(turma):
    df= df_mat4ano3bi.loc[df_mat4ano3bi['Turma']==turma]
    soma = df['EF04MA07'].values.sum()
    qtd = df['EF04MA07'].count()
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
    Output('EF04MA113bi','children'),
    Output('cardEF04MA113bi', 'color'),
    Input('drop-down43bi','value')
)
def hab4(turma):
    df= df_mat4ano3bi.loc[df_mat4ano3bi['Turma']==turma]
    soma = df['EF04MA11'].values.sum()
    qtd = df['EF04MA11'].count()
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
    Output('EF04MA233bi','children'),
    Output('cardEF04MA233bi', 'color'),
    Input('drop-down43bi','value')
)
def hab5(turma):
    df= df_mat4ano3bi.loc[df_mat4ano3bi['Turma']==turma]
    soma = df['EF04MA23'].values.sum()
    qtd = df['EF04MA23'].count()
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
    Output('EF04MA193bi','children'),
    Output('cardEF04MA193bi', 'color'),
    Input('drop-down43bi','value')
)
def hab6(turma):
    df= df_mat4ano3bi.loc[df_mat4ano3bi['Turma']==turma]
    soma = df['EF04MA19'].values.sum()
    qtd = df['EF04MA19'].count()
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
    Output('EF04MA243bi','children'),
    Output('cardEF04MA243bi', 'color'),
    Input('drop-down43bi','value')
)
def hab7(turma):
    df= df_mat4ano3bi.loc[df_mat4ano3bi['Turma']==turma]
    soma = df['EF04MA24'].values.sum()
    qtd = df['EF04MA24'].count()
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
    Output('EF04MA283bi','children'),
    Output('cardEF04MA283bi', 'color'),
    Input('drop-down43bi','value')
)
def hab7(turma):
    df= df_mat4ano3bi.loc[df_mat4ano3bi['Turma']==turma]
    soma = df['EF04MA28'].values.sum()
    qtd = df['EF04MA28'].count()
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
    Output('figacerto43bi','figure'),
    Input('drop-hab43bi','value'),
    Input('drop-turma43bi','value'),
)
def acertos(hab, turma):
    d = df_mat4ano3bi.loc[df_mat4ano3bi['Turma']==turma]
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
    Output('fighabs43bi','figure'),
    Input('drop-turma43bi','value'),
)
def habs(turma):
    df = df_mat4ano3bi.loc[df_mat4ano3bi['Turma']==turma]
    fig= px.histogram(df, x = 'Total', color='Total', labels= {'Total':'Percentual de Habilidades Desenvolvidas'}, title= 'Percentual de Habilidades Desenvolvidas <br> por Quantidade de Estudante'+' na turma '+str(turma).upper())
    fig.update_layout(showlegend=False)
    fig.update_yaxes( title= 'Quantidade de Estudantes')
    return fig


