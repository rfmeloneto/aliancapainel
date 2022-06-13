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
df_mat2ano = pd.read_csv(DATA_PATH.joinpath("mat2ano.csv"))

layout = html.Div(children=[
    
    dbc.Row(dbc.Col(dcc.Dropdown(df_mat2ano['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-down2',), width=2)),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("Domínio Geral das Habilidades"),dbc.CardBody( children=[], id='total2', style={'font-size':30, 'margin':'auto'})], id='cardtotal2')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF02MA01"),dbc.CardBody(children=[] , id='EF02MA01', style={'font-size':30, 'margin':'auto'})], id='cardEF02MA01')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF02MA02"),dbc.CardBody(children=[] , id='EF02MA02', style={'font-size':30, 'margin':'auto'})], id='cardEF02MA02')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF02MA03"),dbc.CardBody(children=[] , id='EF02MA03', style={'font-size':30, 'margin':'auto'})], id='cardEF02MA03')),
            ]
    ),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF02MA05"),dbc.CardBody(children=[] , id='EF02MA05', style={'font-size':30, 'margin':'auto'})], id='cardEF02MA05')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF02MA06"),dbc.CardBody(children=[] , id='EF02MA06', style={'font-size':30, 'margin':'auto'})], id='cardEF02MA06')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF02MA12"),dbc.CardBody(children=[] , id='EF02MA12', style={'font-size':30, 'margin':'auto'})], id='cardEF02MA12')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF02MA18"),dbc.CardBody(children=[] , id='EF02MA18', style={'font-size':30, 'margin':'auto'})], id='cardEF02MA18')),
            ]
    ),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF02MA19"),dbc.CardBody(children=[] , id='EF02MA19', style={'font-size':30, 'margin':'auto'})], id='cardEF02MA19'), width=3),
            dbc.Col( dbc.Card([dbc.CardHeader("EF02MA21"),dbc.CardBody(children=[] , id='EF02MA21', style={'font-size':30, 'margin':'auto'})], id='cardEF02MA21'), width=3),
            dbc.Col( dbc.Card([dbc.CardHeader("EF02MA09"),dbc.CardBody(children=[] , id='EF02MA09', style={'font-size':30, 'margin':'auto'})], id='cardEF02MA09'), width=3),
            
            
            ]
    ),


])

@app.callback(
    Output('total2','children'),
    Output('cardtotal2', 'color'),
    Input('drop-down2','value')
)
def habtotal(turma):
    df = df_mat2ano.loc[df_mat2ano['Turma']==turma]
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
    Output('EF02MA01','children'),
    Output('cardEF02MA01', 'color'),
    Input('drop-down2','value')
)
def hab1(turma):
    df= df_mat2ano.loc[df_mat2ano['Turma']==turma]
    soma = df['EF02MA01'].values.sum()
    qtd = df['EF02MA01'].count()
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
    Output('EF02MA02','children'),
    Output('cardEF02MA02', 'color'),
    Input('drop-down2','value')
)
def hab2(turma):
    df= df_mat2ano.loc[df_mat2ano['Turma']==turma]
    soma = df['EF02MA02'].values.sum()
    qtd = df['EF02MA02'].count()
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
    Output('EF02MA03','children'),
    Output('cardEF02MA03', 'color'),
    Input('drop-down2','value')
)
def hab3(turma):
    df= df_mat2ano.loc[df_mat2ano['Turma']==turma]
    soma = df['EF02MA03'].values.sum()
    qtd = df['EF02MA03'].count()
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
    Output('EF02MA05','children'),
    Output('cardEF02MA05', 'color'),
    Input('drop-down2','value')
)
def hab4(turma):
    df= df_mat2ano.loc[df_mat2ano['Turma']==turma]
    soma = df['EF02MA05'].values.sum()
    qtd = df['EF02MA05'].count()
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
    Output('EF02MA06','children'),
    Output('cardEF02MA06', 'color'),
    Input('drop-down2','value')
)
def hab5(turma):
    df= df_mat2ano.loc[df_mat2ano['Turma']==turma]
    soma = df['EF02MA06'].values.sum()
    qtd = df['EF02MA06'].count()
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
    Output('EF02MA12','children'),
    Output('cardEF02MA12', 'color'),
    Input('drop-down2','value')
)
def hab6(turma):
    df= df_mat2ano.loc[df_mat2ano['Turma']==turma]
    soma = df['EF02MA12'].values.sum()
    qtd = df['EF02MA12'].count()
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
    Output('EF02MA18','children'),
    Output('cardEF02MA18', 'color'),
    Input('drop-down2','value')
)
def hab7(turma):
    df= df_mat2ano.loc[df_mat2ano['Turma']==turma]
    soma = df['EF02MA18'].values.sum()
    qtd = df['EF02MA18'].count()
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
    Output('EF02MA19','children'),
    Output('cardEF02MA19', 'color'),
    Input('drop-down2','value')
)
def hab8(turma):
    df= df_mat2ano.loc[df_mat2ano['Turma']==turma]
    soma = df['EF02MA19'].values.sum()
    qtd = df['EF02MA19'].count()
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
    Output('EF02MA21','children'),
    Output('cardEF02MA21', 'color'),
    Input('drop-down2','value')
)
def hab10(turma):
    df= df_mat2ano.loc[df_mat2ano['Turma']==turma]
    soma = df['EF02MA21'].values.sum()
    qtd = df['EF02MA21'].count()
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
    Output('EF02MA09','children'),
    Output('cardEF02MA09', 'color'),
    Input('drop-down2','value')
)
def hab10(turma):
    df= df_mat2ano.loc[df_mat2ano['Turma']==turma]
    soma = df['EF02MA09'].values.sum()
    qtd = df['EF02MA09'].count()
    media= soma/qtd
    media = media*100
    media = int(media)
    if media >= 50:
        return str(media), 'success'
    elif media >= 30 and media < 50 :
        return str(media) , 'warning'
    else:
        return str(media), 'danger'