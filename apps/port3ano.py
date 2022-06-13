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
df_port3ano = pd.read_csv(DATA_PATH.joinpath("port3ano.csv")) 

layout = html.Div(children=[
    
    dbc.Row(dbc.Col(dcc.Dropdown(df_port3ano['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-down12',), width=2)),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("Domínio Geral das Habilidades"),dbc.CardBody( children=[], id='total12', style={'font-size':30, 'margin':'auto'})], id='cardtotal12')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF03LP17"),dbc.CardBody(children=[] , id='EF03LP17', style={'font-size':30, 'margin':'auto'})], id='cardEF03LP17')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF03LP07"),dbc.CardBody(children=[] , id='EF03LP07', style={'font-size':30, 'margin':'auto'})], id='cardEF03LP07')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF35LP05"),dbc.CardBody(children=[] , id='EF35LP05', style={'font-size':30, 'margin':'auto'})], id='cardEF35LP05')),
            ]
    ),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF03LP12"),dbc.CardBody(children=[] , id='EF03LP12', style={'font-size':30, 'margin':'auto'})], id='cardEF03LP12')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF15LP01"),dbc.CardBody(children=[] , id='EF15LP01', style={'font-size':30, 'margin':'auto'})], id='cardEF15LP01')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF35LP03"),dbc.CardBody(children=[] , id='EF35LP03', style={'font-size':30, 'margin':'auto'})], id='cardEF35LP03')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF35LP21"),dbc.CardBody(children=[] , id='EF35LP21', style={'font-size':30, 'margin':'auto'})], id='cardEF35LP21')),
            ]
    ),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF15LP15"),dbc.CardBody(children=[] , id='EF15LP15', style={'font-size':30, 'margin':'auto'})], id='cardEF15LP15'), width=3),
            dbc.Col( dbc.Card([dbc.CardHeader("EF35LP04"),dbc.CardBody(children=[] , id='EF35LP04', style={'font-size':30, 'margin':'auto'})], id='cardEF35LP04'), width=3),
            
            ]
    ),

    html.Br(),
    

])

@app.callback(
    Output('total12','children'),
    Output('cardtotal12', 'color'),
    Input('drop-down12','value')
)
def habtotal(turma):
    df = df_port3ano.loc[df_port3ano['Turma']==turma]
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
    Output('EF03LP17','children'),
    Output('cardEF03LP17', 'color'),
    Input('drop-down12','value')
)
def hab1(turma):
    df= df_port3ano.loc[df_port3ano['Turma']==turma]
    soma = df['EF03LP17'].values.sum()
    qtd = df['EF03LP17'].count()
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
    Output('EF03LP07','children'),
    Output('cardEF03LP07', 'color'),
    Input('drop-down12','value')
)
def hab2(turma):
    df= df_port3ano.loc[df_port3ano['Turma']==turma]
    soma = df['EF03LP07'].values.sum()
    qtd = df['EF03LP07'].count()
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
    Output('EF35LP05','children'),
    Output('cardEF35LP05', 'color'),
    Input('drop-down12','value')
)
def hab3(turma):
    df= df_port3ano.loc[df_port3ano['Turma']==turma]
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
    Output('EF03LP12','children'),
    Output('cardEF03LP12', 'color'),
    Input('drop-down12','value')
)
def hab4(turma):
    df= df_port3ano.loc[df_port3ano['Turma']==turma]
    soma = df['EF03LP12'].values.sum()
    qtd = df['EF03LP12'].count()
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
    Output('EF15LP01','children'),
    Output('cardEF15LP01', 'color'),
    Input('drop-down12','value')
)
def hab5(turma):
    df= df_port3ano.loc[df_port3ano['Turma']==turma]
    soma = df['EF15LP01'].values.sum()
    qtd = df['EF15LP01'].count()
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
    Output('EF35LP03','children'),
    Output('cardEF35LP03', 'color'),
    Input('drop-down12','value')
)
def hab6(turma):
    df= df_port3ano.loc[df_port3ano['Turma']==turma]
    soma = df['EF35LP03'].values.sum()
    qtd = df['EF35LP03'].count()
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
    Output('EF35LP21','children'),
    Output('cardEF35LP21', 'color'),
    Input('drop-down12','value')
)
def hab7(turma):
    df= df_port3ano.loc[df_port3ano['Turma']==turma]
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
    Output('EF15LP15','children'),
    Output('cardEF15LP15', 'color'),
    Input('drop-down12','value')
)
def hab8(turma):
    df= df_port3ano.loc[df_port3ano['Turma']==turma]
    soma = df['EF15LP15'].values.sum()
    qtd = df['EF15LP15'].count()
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
    Output('EF35LP04','children'),
    Output('cardEF35LP04', 'color'),
    Input('drop-down12','value')
)
def hab10(turma):
    df= df_port3ano.loc[df_port3ano['Turma']==turma]
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

