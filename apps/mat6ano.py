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
df_mat6ano = pd.read_csv(DATA_PATH.joinpath("mat6ano.csv"))
df_habs6= df_mat6ano.drop(columns=['Escola','Estudante','Ano','Turma','Total']) 

layout = html.Div(children=[
    
    dbc.Row(dbc.Col(dcc.Dropdown(df_mat6ano['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-down6',), width=2)),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("Domínio Geral das Habilidades"),dbc.CardBody( children=[], id='total6', style={'font-size':30, 'margin':'auto'})], id='cardtotal6')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF06MA01"),dbc.CardBody(children=[] , id='EF06MA01', style={'font-size':30, 'margin':'auto'})], id='cardEF06MA01')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF06MA06"),dbc.CardBody(children=[] , id='EF06MA06', style={'font-size':30, 'margin':'auto'})], id='cardEF06MA06')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF06MA03"),dbc.CardBody(children=[] , id='EF06MA03', style={'font-size':30, 'margin':'auto'})], id='cardEF06MA03')),
            ]
    ),
    dbc.Popover(
            totalgeral,
            target="total6",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF06MA01,
            target="EF06MA01",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF06MA06,
            target="EF06MA06",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF06MA03,
            target="EF06MA03",
            body=True,
            trigger="hover"),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF06MA20"),dbc.CardBody(children=[] , id='EF06MA20', style={'font-size':30, 'margin':'auto'})], id='cardEF06MA20')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF06MA19"),dbc.CardBody(children=[] , id='EF06MA19', style={'font-size':30, 'margin':'auto'})], id='cardEF06MA19')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF06MA25"),dbc.CardBody(children=[] , id='EF06MA25', style={'font-size':30, 'margin':'auto'})], id='cardEF06MA25')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF06MA33"),dbc.CardBody(children=[] , id='EF06MA33', style={'font-size':30, 'margin':'auto'})], id='cardEF06MA33')),
            ]
    ),
    dbc.Popover(
            EF06MA20,
            target="EF06MA20",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF06MA19,
            target="EF06MA19",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF06MA25,
            target="EF06MA25",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF06MA33,
            target="EF06MA33",
            body=True,
            trigger="hover"),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF06MA18"),dbc.CardBody(children=[] , id='EF06MA18', style={'font-size':30, 'margin':'auto'})], id='cardEF06MA18'), width=3),
            dbc.Col( dbc.Card([dbc.CardHeader("EF06MA14"),dbc.CardBody(children=[] , id='EF06MA14', style={'font-size':30, 'margin':'auto'})], id='cardEF06MA14'), width=3),
            dbc.Col( dbc.Card([dbc.CardHeader("EF06MA05"),dbc.CardBody(children=[] , id='EF06MA05', style={'font-size':30, 'margin':'auto'})], id='cardEF06MA05'), width=3),
            dbc.Col( dbc.Card([dbc.CardHeader("EF06MA26"),dbc.CardBody(children=[] , id='EF06MA26', style={'font-size':30, 'margin':'auto'})], id='cardEF06MA26'), width=3),
            
            ]
    ),

    dbc.Popover(
            EF06MA18,
            target="EF06MA18",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF06MA14,
            target="EF06MA14",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF06MA05,
            target="EF06MA05",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF06MA26,
            target="EF06MA26",
            body=True,
            trigger="hover"),

    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF06MA04"),dbc.CardBody(children=[] , id='EF06MA04', style={'font-size':30, 'margin':'auto'})], id='cardEF06MA04'), width=3),
            
            
            ]
    ),
    dbc.Popover(
            EF06MA04,
            target="EF06MA04",
            body=True,
            trigger="hover"),
    
    html.Br(),
    dbc.Row(children=[

    dbc.Col(dcc.Dropdown(df_mat6ano['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-turma6')),
    dbc.Col(dcc.Dropdown(df_habs6.columns, value="EF06MA04", style ={'margin-top':10, 'margin-left':5}, id='drop-hab6')),
    
]),

html.Br(),
dbc.Row(children=[

    dbc.Col( dbc.Card(dcc.Graph(id='fighabs6',config= {'displaylogo': False}))),
    dbc.Col( dbc.Card(dcc.Graph(id='figacerto6',config= {'displaylogo': False}))),
])

])

@app.callback(
    Output('total6','children'),
    Output('cardtotal6', 'color'),
    Input('drop-down6','value')
)
def habtotal(turma):
    df = df_mat6ano.loc[df_mat6ano['Turma']==turma]
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
    Output('EF06MA01','children'),
    Output('cardEF06MA01', 'color'),
    Input('drop-down6','value')
)
def hab1(turma):
    df= df_mat6ano.loc[df_mat6ano['Turma']==turma]
    soma = df['EF06MA01'].values.sum()
    qtd = df['EF06MA01'].count()
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
    Output('EF06MA06','children'),
    Output('cardEF06MA06', 'color'),
    Input('drop-down6','value')
)
def hab2(turma):
    df= df_mat6ano.loc[df_mat6ano['Turma']==turma]
    soma = df['EF06MA06'].values.sum()
    qtd = df['EF06MA06'].count()
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
    Output('EF06MA03','children'),
    Output('cardEF06MA03', 'color'),
    Input('drop-down6','value')
)
def hab3(turma):
    df= df_mat6ano.loc[df_mat6ano['Turma']==turma]
    soma = df['EF06MA03'].values.sum()
    qtd = df['EF06MA03'].count()
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
    Output('EF06MA20','children'),
    Output('cardEF06MA20', 'color'),
    Input('drop-down6','value')
)
def hab4(turma):
    df= df_mat6ano.loc[df_mat6ano['Turma']==turma]
    soma = df['EF06MA20'].values.sum()
    qtd = df['EF06MA20'].count()
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
    Output('EF06MA19','children'),
    Output('cardEF06MA19', 'color'),
    Input('drop-down6','value')
)
def hab5(turma):
    df= df_mat6ano.loc[df_mat6ano['Turma']==turma]
    soma = df['EF06MA19'].values.sum()
    qtd = df['EF06MA19'].count()
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
    Output('EF06MA25','children'),
    Output('cardEF06MA25', 'color'),
    Input('drop-down6','value')
)
def hab6(turma):
    df= df_mat6ano.loc[df_mat6ano['Turma']==turma]
    soma = df['EF06MA25'].values.sum()
    qtd = df['EF06MA25'].count()
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
    Output('EF06MA18','children'),
    Output('cardEF06MA18', 'color'),
    Input('drop-down6','value')
)
def hab8(turma):
    df= df_mat6ano.loc[df_mat6ano['Turma']==turma]
    soma = df['EF06MA18'].values.sum()
    qtd = df['EF06MA18'].count()
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
    Output('EF06MA14','children'),
    Output('cardEF06MA14', 'color'),
    Input('drop-down6','value')
)
def hab10(turma):
    df= df_mat6ano.loc[df_mat6ano['Turma']==turma]
    soma = df['EF06MA14'].values.sum()
    qtd = df['EF06MA14'].count()
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
    Output('EF06MA05','children'),
    Output('cardEF06MA05', 'color'),
    Input('drop-down6','value')
)
def hab10(turma):
    df= df_mat6ano.loc[df_mat6ano['Turma']==turma]
    soma = df['EF06MA05'].values.sum()
    qtd = df['EF06MA05'].count()
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
    Output('EF06MA26','children'),
    Output('cardEF06MA26', 'color'),
    Input('drop-down6','value')
)
def hab10(turma):
    df= df_mat6ano.loc[df_mat6ano['Turma']==turma]
    soma = df['EF06MA26'].values.sum()
    qtd = df['EF06MA26'].count()
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
    Output('EF06MA04','children'),
    Output('cardEF06MA04', 'color'),
    Input('drop-down6','value')
)
def hab10(turma):
    df= df_mat6ano.loc[df_mat6ano['Turma']==turma]
    soma = df['EF06MA04'].values.sum()
    qtd = df['EF06MA04'].count()
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
    Output('EF06MA33','children'),
    Output('cardEF06MA33', 'color'),
    Input('drop-down6','value')
)
def hab10(turma):
    df= df_mat6ano.loc[df_mat6ano['Turma']==turma]
    soma = df['EF06MA33'].values.sum()
    qtd = df['EF06MA33'].count()
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
    Output('figacerto6','figure'),
    Input('drop-hab6','value'),
    Input('drop-turma6','value'),
)
def acertos(hab, turma):
    d = df_mat6ano.loc[df_mat6ano['Turma']==turma]
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
    Output('fighabs6','figure'),
    Input('drop-turma6','value'),
)
def habs(turma):
    df = df_mat6ano.loc[df_mat6ano['Turma']==turma]
    fig= px.histogram(df, x = 'Total', color='Total', labels= {'Total':'Percentual de Habilidades Desenvolvidas'}, title= 'Percentual de Habilidades Desenvolvidas <br> por Quantidade de Estudante'+' na turma '+str(turma).upper())
    fig.update_layout(showlegend=False)
    fig.update_yaxes( title= 'Quantidade de Estudantes')
    return fig
