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
df_mat4ano = pd.read_csv(DATA_PATH.joinpath("mat4ano.csv"))
df_habs4= df_mat4ano.drop(columns=['Escola','Estudante','Ano','Turma','Total'])  

layout = html.Div(children=[
    
    dbc.Row(dbc.Col(dcc.Dropdown(df_mat4ano['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-down4',), width=2)),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("Domínio Geral das Habilidades"),dbc.CardBody( children=[], id='total4', style={'font-size':30, 'margin':'auto'})], id='cardtotal4')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF04MA01TO"),dbc.CardBody(children=[] , id='EF04MA01TO', style={'font-size':30, 'margin':'auto'})], id='cardEF04MA01TO')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF04MA02"),dbc.CardBody(children=[] , id='EF04MA02', style={'font-size':30, 'margin':'auto'})], id='cardEF04MA02')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF04MA08"),dbc.CardBody(children=[] , id='EF04MA08', style={'font-size':30, 'margin':'auto'})], id='cardEF04MA08')),
            ]
    ),
    dbc.Popover(
            totalgeral,
            target="total4",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF04MA01TO,
            target="EF04MA01TO",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF04MA02,
            target="EF04MA02",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF04MA08,
            target="EF04MA08",
            body=True,
            trigger="hover"),

    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF04MA27"),dbc.CardBody(children=[] , id='EF04MA27', style={'font-size':30, 'margin':'auto'})], id='cardEF04MA27')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF04MA17"),dbc.CardBody(children=[] , id='EF04MA17', style={'font-size':30, 'margin':'auto'})], id='cardEF04MA17')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF04MA22"),dbc.CardBody(children=[] , id='EF04MA22', style={'font-size':30, 'margin':'auto'})], id='cardEF04MA22')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF04MA01"),dbc.CardBody(children=[] , id='EF04MA01', style={'font-size':30, 'margin':'auto'})], id='cardEF04MA01')),
            ]
    ),
    html.Br(),
    dbc.Popover(
            EF04MA27,
            target="EF04MA27",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF04MA17,
            target="EF04MA17",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF04MA22,
            target="EF04MA22",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF04MA01,
            target="EF04MA01",
            body=True,
            trigger="hover"),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF04MA20"),dbc.CardBody(children=[] , id='EF04MA20', style={'font-size':30, 'margin':'auto'})], id='cardEF04MA20'), width=3),
            dbc.Col( dbc.Card([dbc.CardHeader("EF04MA13"),dbc.CardBody(children=[] , id='EF04MA13', style={'font-size':30, 'margin':'auto'})], id='cardEF04MA13'), width=3),
            
            
            
            ]
    ),

    dbc.Popover(
            EF04MA20,
            target="EF04MA20",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF04MA13,
            target="EF04MA13",
            body=True,
            trigger="hover"),
    html.Br(),
 dbc.Row(children=[

    dbc.Col(dcc.Dropdown(df_mat4ano['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-turma4')),
    dbc.Col(dcc.Dropdown(df_habs4.columns, value="EF04MA13", style ={'margin-top':10, 'margin-left':5}, id='drop-hab4')),
    
]),

html.Br(),
dbc.Row(children=[

    dbc.Col( dbc.Card(dcc.Graph(id='fighabs4',config= {'displaylogo': False}))),
    dbc.Col( dbc.Card(dcc.Graph(id='figacerto4',config= {'displaylogo': False}))),
])

])

@app.callback(
    Output('total4','children'),
    Output('cardtotal4', 'color'),
    Input('drop-down4','value')
)
def habtotal(turma):
    df = df_mat4ano.loc[df_mat4ano['Turma']==turma]
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
    Output('EF04MA01TO','children'),
    Output('cardEF04MA01TO', 'color'),
    Input('drop-down4','value')
)
def hab1(turma):
    df= df_mat4ano.loc[df_mat4ano['Turma']==turma]
    soma = df['EF04MA01TO'].values.sum()
    qtd = df['EF04MA01TO'].count()
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
    Output('EF04MA02','children'),
    Output('cardEF04MA02', 'color'),
    Input('drop-down4','value')
)
def hab2(turma):
    df= df_mat4ano.loc[df_mat4ano['Turma']==turma]
    soma = df['EF04MA02'].values.sum()
    qtd = df['EF04MA02'].count()
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
    Output('EF04MA08','children'),
    Output('cardEF04MA08', 'color'),
    Input('drop-down4','value')
)
def hab3(turma):
    df= df_mat4ano.loc[df_mat4ano['Turma']==turma]
    soma = df['EF04MA08'].values.sum()
    qtd = df['EF04MA08'].count()
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
    Output('EF04MA27','children'),
    Output('cardEF04MA27', 'color'),
    Input('drop-down4','value')
)
def hab4(turma):
    df= df_mat4ano.loc[df_mat4ano['Turma']==turma]
    soma = df['EF04MA27'].values.sum()
    qtd = df['EF04MA27'].count()
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
    Output('EF04MA17','children'),
    Output('cardEF04MA17', 'color'),
    Input('drop-down4','value')
)
def hab5(turma):
    df= df_mat4ano.loc[df_mat4ano['Turma']==turma]
    soma = df['EF04MA17'].values.sum()
    qtd = df['EF04MA17'].count()
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
    Output('EF04MA22','children'),
    Output('cardEF04MA22', 'color'),
    Input('drop-down4','value')
)
def hab6(turma):
    df= df_mat4ano.loc[df_mat4ano['Turma']==turma]
    soma = df['EF04MA22'].values.sum()
    qtd = df['EF04MA22'].count()
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
    Output('EF04MA01','children'),
    Output('cardEF04MA01', 'color'),
    Input('drop-down4','value')
)
def hab7(turma):
    df= df_mat4ano.loc[df_mat4ano['Turma']==turma]
    soma = df['EF04MA01'].values.sum()
    qtd = df['EF04MA01'].count()
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
    Output('EF04MA20','children'),
    Output('cardEF04MA20', 'color'),
    Input('drop-down4','value')
)
def hab8(turma):
    df= df_mat4ano.loc[df_mat4ano['Turma']==turma]
    soma = df['EF04MA20'].values.sum()
    qtd = df['EF04MA20'].count()
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
    Output('EF04MA13','children'),
    Output('cardEF04MA13', 'color'),
    Input('drop-down4','value')
)
def hab10(turma):
    df= df_mat4ano.loc[df_mat4ano['Turma']==turma]
    soma = df['EF04MA13'].values.sum()
    qtd = df['EF04MA13'].count()
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
    Output('figacerto4','figure'),
    Input('drop-hab4','value'),
    Input('drop-turma4','value'),
)
def acertos(hab, turma):
    d = df_mat4ano.loc[df_mat4ano['Turma']==turma]
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
    Output('fighabs4','figure'),
    Input('drop-turma4','value'),
)
def habs(turma):
    df = df_mat4ano.loc[df_mat4ano['Turma']==turma]
    fig= px.histogram(df, x = 'Total', color='Total', labels= {'Total':'Percentual de Habilidades Desenvolvidas'}, title= 'Percentual de Habilidades Desenvolvidas <br> por Quantidade de Estudante'+' na turma '+str(turma).upper())
    fig.update_layout(showlegend=False)
    fig.update_yaxes( title= 'Quantidade de Estudantes')
    return fig


