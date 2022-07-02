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
df_port6ano = pd.read_csv(DATA_PATH.joinpath("port6ano.csv")) 
df_habsport6 = df_port6ano.drop(columns=['Escola','Estudante','Ano','Turma','Total'])

layout = html.Div(children=[
    
    dbc.Row(dbc.Col(dcc.Dropdown(df_port6ano['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-down16',), width=2)),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("Domínio Geral das Habilidades"),dbc.CardBody( children=[], id='total16', style={'font-size':30, 'margin':'auto'})], id='cardtotal16')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF67LP01"),dbc.CardBody(children=[] , id='EF67LP01', style={'font-size':30, 'margin':'auto'})], id='cardEF67LP01')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF06LP05"),dbc.CardBody(children=[] , id='EF06LP05', style={'font-size':30, 'margin':'auto'})], id='cardEF06LP05')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF67LP28"),dbc.CardBody(children=[] , id='EF67LP281', style={'font-size':30, 'margin':'auto'})], id='cardEF67LP281')),
            ]
    ),
     dbc.Popover(
            totalgeral,
            target="total16",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF67LP01,
            target="EF67LP01",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF06LP05,
            target="EF06LP05",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF67LP28,
            target="EF67LP281",
            body=True,
            trigger="hover"),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF06LP04"),dbc.CardBody(children=[] , id='EF06LP04', style={'font-size':30, 'margin':'auto'})], id='cardEF06LP04')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF69LP55"),dbc.CardBody(children=[] , id='EF69LP551', style={'font-size':30, 'margin':'auto'})], id='cardEF69LP551')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF06LP02"),dbc.CardBody(children=[] , id='EF06LP021', style={'font-size':30, 'margin':'auto'})], id='cardEF06LP021')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF67LP32"),dbc.CardBody(children=[] , id='EF67LP32', style={'font-size':30, 'margin':'auto'})], id='cardEF67LP32')),
            ]
    ),
    dbc.Popover(
            EF06LP04,
            target="EF06LP04",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF69LP55,
            target="EF69LP551",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF06LP02,
            target="EF06LP021",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF67LP32,
            target="EF67LP32",
            body=True,
            trigger="hover"),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF67LP33"),dbc.CardBody(children=[] , id='EF67LP33', style={'font-size':30, 'margin':'auto'})], id='cardEF67LP33'), width=3),
            dbc.Col( dbc.Card([dbc.CardHeader("EF67LP35"),dbc.CardBody(children=[] , id='EF67LP351', style={'font-size':30, 'margin':'auto'})], id='cardEF67LP351'), width=3),
            dbc.Col( dbc.Card([dbc.CardHeader("EF67LP36"),dbc.CardBody(children=[] , id='EF67LP36', style={'font-size':30, 'margin':'auto'})], id='cardEF67LP36'), width=3),
            
            
            ]
    ),
    dbc.Popover(
            EF67LP33,
            target="EF67LP33",
            body=True,
            trigger="hover"),
    dbc.Popover(
           EF67LP35,
            target="EF67LP351",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF67LP36,
            target="EF67LP36",
            body=True,
            trigger="hover"),

           
dbc.Row(children=[

    dbc.Col(dcc.Dropdown(df_port6ano['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-turma15')),
    dbc.Col(dcc.Dropdown(df_habsport6.columns, value="EF67LP36", style ={'margin-top':10, 'margin-left':5}, id='drop-hab15')),
    
]),

html.Br(),
dbc.Row(children=[

    dbc.Col( dbc.Card(dcc.Graph(id='fighabs15',config= {'displaylogo': False}))),
    dbc.Col( dbc.Card(dcc.Graph(id='figacerto15',config= {'displaylogo': False}))),


]),


])

@app.callback(
    Output('total16','children'),
    Output('cardtotal16', 'color'),
    Input('drop-down16','value')
)
def habtotal(turma):
    df = df_port6ano.loc[df_port6ano['Turma']==turma]
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
    Output('EF67LP01','children'),
    Output('cardEF67LP01', 'color'),
    Input('drop-down16','value')
)
def hab1(turma):
    df= df_port6ano.loc[df_port6ano['Turma']==turma]
    soma = df['EF67LP01'].values.sum()
    qtd = df['EF67LP01'].count()
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
    Output('EF06LP05','children'),
    Output('cardEF06LP05', 'color'),
    Input('drop-down16','value')
)
def hab2(turma):
    df= df_port6ano.loc[df_port6ano['Turma']==turma]
    soma = df['EF06LP05'].values.sum()
    qtd = df['EF06LP05'].count()
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
    Output('EF67LP281','children'),
    Output('cardEF67LP281', 'color'),
    Input('drop-down16','value')
)
def hab3(turma):
    df= df_port6ano.loc[df_port6ano['Turma']==turma]
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
    Output('EF06LP04','children'),
    Output('cardEF06LP04', 'color'),
    Input('drop-down16','value')
)
def hab4(turma):
    df= df_port6ano.loc[df_port6ano['Turma']==turma]
    soma = df['EF06LP04'].values.sum()
    qtd = df['EF06LP04'].count()
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
    Output('EF69LP551','children'),
    Output('cardEF69LP551', 'color'),
    Input('drop-down16','value')
)
def hab5(turma):
    df= df_port6ano.loc[df_port6ano['Turma']==turma]
    soma = df['EF69LP55'].values.sum()
    qtd = df['EF69LP55'].count()
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
    Output('EF06LP021','children'),
    Output('cardEF06LP021', 'color'),
    Input('drop-down16','value')
)
def hab6(turma):
    df= df_port6ano.loc[df_port6ano['Turma']==turma]
    soma = df['EF06LP02'].values.sum()
    qtd = df['EF06LP02'].count()
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
    Output('EF67LP32','children'),
    Output('cardEF67LP32', 'color'),
    Input('drop-down16','value')
)
def hab7(turma):
    df= df_port6ano.loc[df_port6ano['Turma']==turma]
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
    Output('EF67LP33','children'),
    Output('cardEF67LP33', 'color'),
    Input('drop-down16','value')
)
def hab8(turma):
    df= df_port6ano.loc[df_port6ano['Turma']==turma]
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
    Output('EF67LP351','children'),
    Output('cardEF67LP351', 'color'),
    Input('drop-down16','value')
)
def hab10(turma):
    df= df_port6ano.loc[df_port6ano['Turma']==turma]
    soma = df['EF67LP35'].values.sum()
    qtd = df['EF67LP35'].count()
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
    Output('EF67LP36','children'),
    Output('cardEF67LP36', 'color'),
    Input('drop-down16','value')
)
def hab10(turma):
    df= df_port6ano.loc[df_port6ano['Turma']==turma]
    soma = df['EF67LP36'].values.sum()
    qtd = df['EF67LP36'].count()
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
    Output('figacerto15','figure'),
    Input('drop-hab15','value'),
    Input('drop-turma15','value'),
)
def acertos(hab, turma):
    d = df_port6ano.loc[df_port6ano['Turma']==turma]
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
    Output('fighabs15','figure'),
    Input('drop-turma15','value'),
)
def habs(turma):
    df = df_port6ano.loc[df_port6ano['Turma']==turma]
    fig= px.histogram(df, x = 'Total', color='Total', labels= {'Total':'Percentual de Habilidades Desenvolvidas'}, title= 'Percentual de Habilidades Desenvolvidas <br> por Quantidade de Estudante'+' na turma '+str(turma).upper())
    fig.update_layout(showlegend=False)
    fig.update_yaxes( title= 'Quantidade de Estudantes')
    return fig
