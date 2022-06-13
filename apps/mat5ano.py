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
df_mat5ano = pd.read_csv(DATA_PATH.joinpath("mat5ano.csv"))  

layout = html.Div(children=[
    
    dbc.Row(dbc.Col(dcc.Dropdown(df_mat5ano['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-down5',), width=2)),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("Domínio Geral das Habilidades"),dbc.CardBody( children=[], id='total5', style={'font-size':30, 'margin':'auto'})], id='cardtotal5')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF05MA01"),dbc.CardBody(children=[] , id='EF05MA01', style={'font-size':30, 'margin':'auto'})], id='cardEF05MA01')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF05MA05"),dbc.CardBody(children=[] , id='EF05MA05', style={'font-size':30, 'margin':'auto'})], id='cardEF05MA05')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF05MA04"),dbc.CardBody(children=[] , id='EF05MA04', style={'font-size':30, 'margin':'auto'})], id='cardEF05MA04')),
            ]
    ),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF05MA11"),dbc.CardBody(children=[] , id='EF05MA11', style={'font-size':30, 'margin':'auto'})], id='cardEF05MA11')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF05MA17"),dbc.CardBody(children=[] , id='EF05MA17', style={'font-size':30, 'margin':'auto'})], id='cardEF05MA17')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF05MA10"),dbc.CardBody(children=[] , id='EF05MA10', style={'font-size':30, 'margin':'auto'})], id='cardEF05MA10')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF05MA19"),dbc.CardBody(children=[] , id='EF05MA19', style={'font-size':30, 'margin':'auto'})], id='cardEF05MA19')),
            ]
    ),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF05MA24"),dbc.CardBody(children=[] , id='EF05MA24', style={'font-size':30, 'margin':'auto'})], id='cardEF05MA24'), width=3),
            dbc.Col( dbc.Card([dbc.CardHeader("EF05MA25"),dbc.CardBody(children=[] , id='EF05MA25', style={'font-size':30, 'margin':'auto'})], id='cardEF05MA25'), width=3),
           
            
            
            ]
    ),


])

@app.callback(
    Output('total5','children'),
    Output('cardtotal5', 'color'),
    Input('drop-down5','value')
)
def habtotal(turma):
    df = df_mat5ano.loc[df_mat5ano['Turma']==turma]
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
    Output('EF05MA01','children'),
    Output('cardEF05MA01', 'color'),
    Input('drop-down5','value')
)
def hab1(turma):
    df= df_mat5ano.loc[df_mat5ano['Turma']==turma]
    soma = df['EF05MA01'].values.sum()
    qtd = df['EF05MA01'].count()
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
    Output('EF05MA05','children'),
    Output('cardEF05MA05', 'color'),
    Input('drop-down5','value')
)
def hab2(turma):
    df= df_mat5ano.loc[df_mat5ano['Turma']==turma]
    soma = df['EF05MA05'].values.sum()
    qtd = df['EF05MA05'].count()
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
    Output('EF05MA04','children'),
    Output('cardEF05MA04', 'color'),
    Input('drop-down5','value')
)
def hab3(turma):
    df= df_mat5ano.loc[df_mat5ano['Turma']==turma]
    soma = df['EF05MA04'].values.sum()
    qtd = df['EF05MA04'].count()
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
    Output('EF05MA11','children'),
    Output('cardEF05MA11', 'color'),
    Input('drop-down5','value')
)
def hab4(turma):
    df= df_mat5ano.loc[df_mat5ano['Turma']==turma]
    soma = df['EF05MA11'].values.sum()
    qtd = df['EF05MA11'].count()
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
    Output('EF05MA17','children'),
    Output('cardEF05MA17', 'color'),
    Input('drop-down5','value')
)
def hab5(turma):
    df= df_mat5ano.loc[df_mat5ano['Turma']==turma]
    soma = df['EF05MA17'].values.sum()
    qtd = df['EF05MA17'].count()
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
    Output('EF05MA10','children'),
    Output('cardEF05MA10', 'color'),
    Input('drop-down5','value')
)
def hab6(turma):
    df= df_mat5ano.loc[df_mat5ano['Turma']==turma]
    soma = df['EF05MA10'].values.sum()
    qtd = df['EF05MA10'].count()
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
    Output('EF05MA19','children'),
    Output('cardEF05MA19', 'color'),
    Input('drop-down5','value')
)
def hab7(turma):
    df= df_mat5ano.loc[df_mat5ano['Turma']==turma]
    soma = df['EF05MA19'].values.sum()
    qtd = df['EF05MA19'].count()
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
    Output('EF05MA24','children'),
    Output('cardEF05MA24', 'color'),
    Input('drop-down5','value')
)
def hab8(turma):
    df= df_mat5ano.loc[df_mat5ano['Turma']==turma]
    soma = df['EF05MA24'].values.sum()
    qtd = df['EF05MA24'].count()
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
    Output('EF05MA25','children'),
    Output('cardEF05MA25', 'color'),
    Input('drop-down5','value')
)
def hab10(turma):
    df= df_mat5ano.loc[df_mat5ano['Turma']==turma]
    soma = df['EF05MA25'].values.sum()
    qtd = df['EF05MA25'].count()
    media= soma/qtd
    media = media*100
    media = int(media)
    if media >= 50:
        return str(media), 'success'
    elif media >= 30 and media < 50 :
        return str(media) , 'warning'
    else:
        return str(media), 'danger'

