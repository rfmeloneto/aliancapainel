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
df_port7ano = pd.read_csv(DATA_PATH.joinpath("port7ano.csv")) 

layout = html.Div(children=[
    
    dbc.Row(dbc.Col(dcc.Dropdown(df_port7ano['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-down17',), width=2)),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("Domínio Geral das Habilidades"),dbc.CardBody( children=[], id='total17', style={'font-size':30, 'margin':'auto'})], id='cardtotal17')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF67LP28"),dbc.CardBody(children=[] , id='EF67LP282', style={'font-size':30, 'margin':'auto'})], id='cardEF67LP282')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF67LP36"),dbc.CardBody(children=[] , id='EF67LP362', style={'font-size':30, 'margin':'auto'})], id='cardEF67LP362')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF67LP65"),dbc.CardBody(children=[] , id='EF67LP65', style={'font-size':30, 'margin':'auto'})], id='cardEF67LP65')),
            ]
    ),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF69LP01"),dbc.CardBody(children=[] , id='EF69LP011', style={'font-size':30, 'margin':'auto'})], id='cardEF69LP011')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF67LP32"),dbc.CardBody(children=[] , id='EF67LP321', style={'font-size':30, 'margin':'auto'})], id='cardEF67LP321')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF67LP33"),dbc.CardBody(children=[] , id='EF67LP331', style={'font-size':30, 'margin':'auto'})], id='cardEF67LP331')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF67LP01"),dbc.CardBody(children=[] , id='EF67LP011', style={'font-size':30, 'margin':'auto'})], id='cardEF67LP011')),
            ]
    ),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF07LP09"),dbc.CardBody(children=[] , id='EF07LP09', style={'font-size':30, 'margin':'auto'})], id='cardEF07LP09'), width=3),
            dbc.Col( dbc.Card([dbc.CardHeader("EF07LP01"),dbc.CardBody(children=[] , id='EF07LP011', style={'font-size':30, 'margin':'auto'})], id='cardEF07LP011'), width=3),
            dbc.Col( dbc.Card([dbc.CardHeader("EF07LP02"),dbc.CardBody(children=[] , id='EF07LP02', style={'font-size':30, 'margin':'auto'})], id='cardEF07LP02'), width=3),
            dbc.Col( dbc.Card([dbc.CardHeader("EF07LP03"),dbc.CardBody(children=[] , id='EF07LP03', style={'font-size':30, 'margin':'auto'})], id='cardEF07LP03'), width=3),
            
            
            ]
    ),


])

@app.callback(
    Output('total17','children'),
    Output('cardtotal17', 'color'),
    Input('drop-down17','value')
)
def habtotal(turma):
    df = df_port7ano.loc[df_port7ano['Turma']==turma]
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
    Output('EF67LP282','children'),
    Output('cardEF67LP282', 'color'),
    Input('drop-down17','value')
)
def hab1(turma):
    df= df_port7ano.loc[df_port7ano['Turma']==turma]
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
    Output('EF07LP02','children'),
    Output('cardEF07LP02', 'color'),
    Input('drop-down17','value')
)
def hab2(turma):
    df= df_port7ano.loc[df_port7ano['Turma']==turma]
    soma = df['EF07LP02'].values.sum()
    qtd = df['EF07LP02'].count()
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
    Output('EF67LP65','children'),
    Output('cardEF67LP65', 'color'),
    Input('drop-down17','value')
)
def hab3(turma):
    df= df_port7ano.loc[df_port7ano['Turma']==turma]
    soma = df['EF67LP65'].values.sum()
    qtd = df['EF67LP65'].count()
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
    Output('EF69LP011','children'),
    Output('cardEF69LP011', 'color'),
    Input('drop-down17','value')
)
def hab4(turma):
    df= df_port7ano.loc[df_port7ano['Turma']==turma]
    soma = df['EF69LP01'].values.sum()
    qtd = df['EF69LP01'].count()
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
    Output('EF67LP321','children'),
    Output('cardEF67LP321', 'color'),
    Input('drop-down17','value')
)
def hab5(turma):
    df= df_port7ano.loc[df_port7ano['Turma']==turma]
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
    Output('EF67LP331','children'),
    Output('cardEF67LP331', 'color'),
    Input('drop-down17','value')
)
def hab6(turma):
    df= df_port7ano.loc[df_port7ano['Turma']==turma]
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
    Output('EF67LP011','children'),
    Output('cardEF67LP011', 'color'),
    Input('drop-down17','value')
)
def hab7(turma):
    df= df_port7ano.loc[df_port7ano['Turma']==turma]
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
    Output('EF07LP09','children'),
    Output('cardEF07LP09', 'color'),
    Input('drop-down17','value')
)
def hab8(turma):
    df= df_port7ano.loc[df_port7ano['Turma']==turma]
    soma = df['EF07LP09'].values.sum()
    qtd = df['EF07LP09'].count()
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
    Output('EF07LP011','children'),
    Output('cardEF07LP011', 'color'),
    Input('drop-down17','value')
)
def hab10(turma):
    df= df_port7ano.loc[df_port7ano['Turma']==turma]
    soma = df['EF07LP01'].values.sum()
    qtd = df['EF07LP01'].count()
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
    Output('EF67LP362','children'),
    Output('cardEF67LP362', 'color'),
    Input('drop-down17','value')
)
def hab10(turma):
    df= df_port7ano.loc[df_port7ano['Turma']==turma]
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

#-----------------------------------------------------------------

@app.callback(
    Output('EF07LP03','children'),
    Output('cardEF07LP03', 'color'),
    Input('drop-down17','value')
)
def hab10(turma):
    df= df_port7ano.loc[df_port7ano['Turma']==turma]
    soma = df['EF07LP03'].values.sum()
    qtd = df['EF07LP03'].count()
    media= soma/qtd
    media = media*100
    media = int(media)
    if media >= 50:
        return str(media), 'success'
    elif media >= 30 and media < 50 :
        return str(media) , 'warning'
    else:
        return str(media), 'danger'

