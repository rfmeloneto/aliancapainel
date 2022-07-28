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
df_port7ano2bi = pd.read_csv(DATA_PATH.joinpath("port7ano2bi.csv"))
df_habsport72bi = df_port7ano2bi.drop(columns=['Escola','Estudante','Ano','Turma','Total']) 

layout = html.Div(children=[
    
    dbc.Row(dbc.Col(dcc.Dropdown(df_port7ano2bi['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-down172bi',), width=2)),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("Domínio Geral das Habilidades"),dbc.CardBody( children=[], id='total172bi', style={'font-size':30, 'margin':'auto'})], id='cardtotal172bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF67LP02"),dbc.CardBody(children=[] , id='EF67LP0222bi', style={'font-size':30, 'margin':'auto'})], id='cardEF67LP0222bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF67LP04"),dbc.CardBody(children=[] , id='EF67LP0422bi', style={'font-size':30, 'margin':'auto'})], id='cardEF67LP0422bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF67LP03"),dbc.CardBody(children=[] , id='EF67LP032bi', style={'font-size':30, 'margin':'auto'})], id='cardEF67LP032bi')),
            ]
    ),
    dbc.Popover(
            totalgeral,
            target="total172bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF67LP02,
            target="EF67LP0222bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF67LP04,
            target="EF67LP0422bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF67LP03,
            target="EF67LP032bi",
            body=True,
            trigger="hover"),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF67LP28"),dbc.CardBody(children=[] , id='EF67LP2812bi', style={'font-size':30, 'margin':'auto'})], id='cardEF67LP2812bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF67LP05"),dbc.CardBody(children=[] , id='EF67LP0512bi', style={'font-size':30, 'margin':'auto'})], id='cardEF67LP0512bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF67LP33"),dbc.CardBody(children=[] , id='EF67LP3312bi', style={'font-size':30, 'margin':'auto'})], id='cardEF67LP3312bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF07LP07"),dbc.CardBody(children=[] , id='EF07LP0712bi', style={'font-size':30, 'margin':'auto'})], id='cardEF07LP0712bi')),
            ]
    ),
    dbc.Popover(
            EF67LP28,
            target="EF67LP2812bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF67LP05,
            target="EF67LP0512bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF67LP33,
            target="EF67LP3312bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF07LP07,
            target="EF07LP0712bi",
            body=True,
            trigger="hover"),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF07LP06"),dbc.CardBody(children=[] , id='EF07LP062bi', style={'font-size':30, 'margin':'auto'})], id='cardEF07LP062bi'), width=3),
            dbc.Col( dbc.Card([dbc.CardHeader("EF07LP04"),dbc.CardBody(children=[] , id='EF07LP0412bi', style={'font-size':30, 'margin':'auto'})], id='cardEF07LP0412bi'), width=3),
            dbc.Col( dbc.Card([dbc.CardHeader("EF67LP32"),dbc.CardBody(children=[] , id='EF67LP322bi', style={'font-size':30, 'margin':'auto'})], id='cardEF67LP322bi'), width=3),
            dbc.Col( dbc.Card([dbc.CardHeader("EF67LP38"),dbc.CardBody(children=[] , id='EF67LP382bi', style={'font-size':30, 'margin':'auto'})], id='cardEF67LP382bi'), width=3),
            
            
            ]
    ),
    dbc.Row(
        children=[dbc.Col( dbc.Card([dbc.CardHeader("EF67LP27"),dbc.CardBody(children=[] , id='EF67LP272bi', style={'font-size':30, 'margin':'auto'})], id='cardEF67LP272bi'), width=3),
]
    ),
    dbc.Popover(
            EF07LP06,
            target="EF07LP062bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF07LP04,
            target="EF07LP0412bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF67LP32,
            target="EF67LP322bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF67LP38,
            target="EF67LP382bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF67LP27,
            target="EF67LP272bi",
            body=True,
            trigger="hover"),

dbc.Row(children=[

    dbc.Col(dcc.Dropdown(df_port7ano2bi['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-turma162bi')),
    dbc.Col(dcc.Dropdown(df_habsport72bi.columns, value="EF67LP38", style ={'margin-top':10, 'margin-left':5}, id='drop-hab162bi')),
    
]),

html.Br(),
dbc.Row(children=[

    dbc.Col( dbc.Card(dcc.Graph(id='fighabs162bi',config= {'displaylogo': False}))),
    dbc.Col( dbc.Card(dcc.Graph(id='figacerto162bi',config= {'displaylogo': False}))),


]),


])

@app.callback(
    Output('total172bi','children'),
    Output('cardtotal172bi', 'color'),
    Input('drop-down172bi','value')
)
def habtotal(turma):
    df = df_port7ano2bi.loc[df_port7ano2bi['Turma']==turma]
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
    Output('EF67LP0222bi','children'),
    Output('cardEF67LP0222bi', 'color'),
    Input('drop-down172bi','value')
)
def hab1(turma):
    df= df_port7ano2bi.loc[df_port7ano2bi['Turma']==turma]
    soma = df['EF67LP02'].values.sum()
    qtd = df['EF67LP02'].count()
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
    Output('EF67LP322bi','children'),
    Output('cardEF67LP322bi', 'color'),
    Input('drop-down172bi','value')
)
def hab2(turma):
    df= df_port7ano2bi.loc[df_port7ano2bi['Turma']==turma]
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
    Output('EF67LP032bi','children'),
    Output('cardEF67LP032bi', 'color'),
    Input('drop-down172bi','value')
)
def hab3(turma):
    df= df_port7ano2bi.loc[df_port7ano2bi['Turma']==turma]
    soma = df['EF67LP03'].values.sum()
    qtd = df['EF67LP03'].count()
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
    Output('EF67LP2812bi','children'),
    Output('cardEF67LP2812bi', 'color'),
    Input('drop-down172bi','value')
)
def hab4(turma):
    df= df_port7ano2bi.loc[df_port7ano2bi['Turma']==turma]
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

@app.callback(
    Output('EF67LP0512bi','children'),
    Output('cardEF67LP0512bi', 'color'),
    Input('drop-down172bi','value')
)
def hab5(turma):
    df= df_port7ano2bi.loc[df_port7ano2bi['Turma']==turma]
    soma = df['EF67LP05'].values.sum()
    qtd = df['EF67LP05'].count()
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
    Output('EF67LP3312bi','children'),
    Output('cardEF67LP3312bi', 'color'),
    Input('drop-down172bi','value')
)
def hab6(turma):
    df= df_port7ano2bi.loc[df_port7ano2bi['Turma']==turma]
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

@app.callback(
    Output('EF07LP0712bi','children'),
    Output('cardEF07LP0712bi', 'color'),
    Input('drop-down172bi','value')
)
def hab7(turma):
    df= df_port7ano2bi.loc[df_port7ano2bi['Turma']==turma]
    soma = df['EF07LP07'].values.sum()
    qtd = df['EF07LP07'].count()
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
    Output('EF07LP062bi','children'),
    Output('cardEF07LP062bi', 'color'),
    Input('drop-down172bi','value')
)
def hab8(turma):
    df= df_port7ano2bi.loc[df_port7ano2bi['Turma']==turma]
    soma = df['EF07LP06'].values.sum()
    qtd = df['EF07LP06'].count()
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
    Output('EF07LP0412bi','children'),
    Output('cardEF07LP0412bi', 'color'),
    Input('drop-down172bi','value')
)
def hab10(turma):
    df= df_port7ano2bi.loc[df_port7ano2bi['Turma']==turma]
    soma = df['EF07LP04'].values.sum()
    qtd = df['EF07LP04'].count()
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
    Output('EF67LP0422bi','children'),
    Output('cardEF67LP0422bi', 'color'),
    Input('drop-down172bi','value')
)
def hab10(turma):
    df= df_port7ano2bi.loc[df_port7ano2bi['Turma']==turma]
    soma = df['EF67LP04'].values.sum()
    qtd = df['EF67LP04'].count()
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
    Output('EF67LP382bi','children'),
    Output('cardEF67LP382bi', 'color'),
    Input('drop-down172bi','value')
)
def hab10(turma):
    df= df_port7ano2bi.loc[df_port7ano2bi['Turma']==turma]
    soma = df['EF67LP38'].values.sum()
    qtd = df['EF67LP38'].count()
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
    Output('EF67LP272bi','children'),
    Output('cardEF67LP272bi', 'color'),
    Input('drop-down172bi','value')
)
def hab10(turma):
    df= df_port7ano2bi.loc[df_port7ano2bi['Turma']==turma]
    soma = df['EF67LP27'].values.sum()
    qtd = df['EF67LP27'].count()
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
    Output('figacerto162bi','figure'),
    Input('drop-hab162bi','value'),
    Input('drop-turma162bi','value'),
)
def acertos(hab, turma):
    d = df_port7ano2bi.loc[df_port7ano2bi['Turma']==turma]
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
    Output('fighabs162bi','figure'),
    Input('drop-turma162bi','value'),
)
def habs(turma):
    df = df_port7ano2bi.loc[df_port7ano2bi['Turma']==turma]
    fig= px.histogram(df, x = 'Total', color='Total', labels= {'Total':'Percentual de Habilidades Desenvolvidas'}, title= 'Percentual de Habilidades Desenvolvidas <br> por Quantidade de Estudante'+' na turma '+str(turma).upper())
    fig.update_layout(showlegend=False)
    fig.update_yaxes( title= 'Quantidade de Estudantes')
    return fig
