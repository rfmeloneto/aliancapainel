from dash import dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import pathlib
from app import app


PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()
df_port2ano = pd.read_csv(DATA_PATH.joinpath("port2ano.csv")) 

layout = html.Div(children=[
    
    dbc.Row(dbc.Col(dcc.Dropdown(df_port2ano['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-down11',), width=2)),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("Domínio Geral das Habilidades"),dbc.CardBody( children=[], id='total11', style={'font-size':30, 'margin':'auto'})], id='cardtotal11')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF01LP12"),dbc.CardBody(children=[] , id='EF01LP12', style={'font-size':30, 'margin':'auto'})], id='cardEF01LP12')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF02LP06"),dbc.CardBody(children=[] , id='EF02LP06', style={'font-size':30, 'margin':'auto'})], id='cardEF02LP06')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF12LP07"),dbc.CardBody(children=[] , id='EF12LP07', style={'font-size':30, 'margin':'auto'})], id='cardEF12LP07')),
            ]
    ),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF02LP02"),dbc.CardBody(children=[] , id='EF02LP02', style={'font-size':30, 'margin':'auto'})], id='cardEF02LP02')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF12LP09"),dbc.CardBody(children=[] , id='EF12LP09', style={'font-size':30, 'margin':'auto'})], id='cardEF12LP09')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF15LP04"),dbc.CardBody(children=[] , id='EF15LP04', style={'font-size':30, 'margin':'auto'})], id='cardEF15LP04')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF12LP15"),dbc.CardBody(children=[] , id='EF12LP15', style={'font-size':30, 'margin':'auto'})], id='cardEF12LP15')),
            ]
    ),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF02LP28"),dbc.CardBody(children=[] , id='EF02LP28', style={'font-size':30, 'margin':'auto'})], id='cardEF02LP28'), width=3),
            dbc.Col( dbc.Card([dbc.CardHeader("EF15LP03"),dbc.CardBody(children=[] , id='EF15LP03', style={'font-size':30, 'margin':'auto'})], id='cardEF15LP03'), width=3),
            
            ]
    ),

    html.Br(),
    

])

@app.callback(
    Output('total11','children'),
    Output('cardtotal11', 'color'),
    Input('drop-down11','value')
)
def habtotal(turma):
    df = df_port2ano.loc[df_port2ano['Turma']==turma]
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
    Output('EF01LP12','children'),
    Output('cardEF01LP12', 'color'),
    Input('drop-down11','value')
)
def hab1(turma):
    df= df_port2ano.loc[df_port2ano['Turma']==turma]
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

@app.callback(
    Output('EF02LP06','children'),
    Output('cardEF02LP06', 'color'),
    Input('drop-down11','value')
)
def hab2(turma):
    df= df_port2ano.loc[df_port2ano['Turma']==turma]
    soma = df['EF02LP06'].values.sum()
    qtd = df['EF02LP06'].count()
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
    Output('EF12LP07','children'),
    Output('cardEF12LP07', 'color'),
    Input('drop-down11','value')
)
def hab3(turma):
    df= df_port2ano.loc[df_port2ano['Turma']==turma]
    soma = df['EF12LP07'].values.sum()
    qtd = df['EF12LP07'].count()
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
    Output('EF02LP02','children'),
    Output('cardEF02LP02', 'color'),
    Input('drop-down11','value')
)
def hab4(turma):
    df= df_port2ano.loc[df_port2ano['Turma']==turma]
    soma = df['EF02LP02'].values.sum()
    qtd = df['EF02LP02'].count()
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
    Output('EF12LP09','children'),
    Output('cardEF12LP09', 'color'),
    Input('drop-down11','value')
)
def hab5(turma):
    df= df_port2ano.loc[df_port2ano['Turma']==turma]
    soma = df['EF12LP09'].values.sum()
    qtd = df['EF12LP09'].count()
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
    Output('EF15LP04','children'),
    Output('cardEF15LP04', 'color'),
    Input('drop-down11','value')
)
def hab6(turma):
    df= df_port2ano.loc[df_port2ano['Turma']==turma]
    soma = df['EF15LP04'].values.sum()
    qtd = df['EF15LP04'].count()
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
    Output('EF12LP15','children'),
    Output('cardEF12LP15', 'color'),
    Input('drop-down11','value')
)
def hab7(turma):
    df= df_port2ano.loc[df_port2ano['Turma']==turma]
    soma = df['EF12LP15'].values.sum()
    qtd = df['EF12LP15'].count()
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
    Output('EF02LP28','children'),
    Output('cardEF02LP28', 'color'),
    Input('drop-down11','value')
)
def hab8(turma):
    df= df_port2ano.loc[df_port2ano['Turma']==turma]
    soma = df['EF02LP28'].values.sum()
    qtd = df['EF02LP28'].count()
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
    Output('EF15LP03','children'),
    Output('cardEF15LP03', 'color'),
    Input('drop-down11','value')
)
def hab10(turma):
    df= df_port2ano.loc[df_port2ano['Turma']==turma]
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

