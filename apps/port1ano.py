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
df_port1ano = pd.read_csv(DATA_PATH.joinpath("port1ano.csv"))
 

layout = html.Div(children=[
    
    dbc.Row(children = [ 
        dbc.Col(dcc.Dropdown(df_port1ano['Escola'].unique(), value='Duque de Caxias', style ={'margin-top':10, 'margin-left':5}, id='escola2',), width=2), 
        dbc.Col(dcc.Dropdown(df_port1ano['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-down20',), width=2)
        ]),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("Domínio Geral das Habilidades"),dbc.CardBody( children=[], id='total20', style={'font-size':30, 'margin':'auto'})], id='cardtotal20')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF01LP20"),dbc.CardBody(children=[] , id='EF01LP20', style={'font-size':30, 'margin':'auto'})], id='cardEF01LP20')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF12LP10"),dbc.CardBody(children=[] , id='EF12LP10', style={'font-size':30, 'margin':'auto'})], id='cardEF12LP10')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF12LP04"),dbc.CardBody(children=[] , id='EF12LP04', style={'font-size':30, 'margin':'auto'})], id='cardEF12LP04')),
            ]
    ),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF01LP03"),dbc.CardBody(children=[] , id='EF01LP03', style={'font-size':30, 'margin':'auto'})], id='cardEF01LP03')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF01LP05"),dbc.CardBody(children=[] , id='EF01LP05', style={'font-size':30, 'margin':'auto'})], id='cardEF01LP05')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF01LP08"),dbc.CardBody(children=[] , id='EF01LP08', style={'font-size':30, 'margin':'auto'})], id='cardEF01LP08')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF01LP16"),dbc.CardBody(children=[] , id='EF01LP16', style={'font-size':30, 'margin':'auto'})], id='cardEF01LP16')),
            ]
    ),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF01LP01"),dbc.CardBody(children=[] , id='EF01LP01', style={'font-size':30, 'margin':'auto'})], id='cardEF01LP01'), width=3),
            dbc.Col( dbc.Card([dbc.CardHeader("EF01LP06"),dbc.CardBody(children=[] , id='EF01LP06', style={'font-size':30, 'margin':'auto'})], id='cardEF01LP06'), width=3),
            dbc.Col( dbc.Card([dbc.CardHeader("EF12LP07"),dbc.CardBody(children=[] , id='EF12LP073', style={'font-size':30, 'margin':'auto'})], id='cardEF12LP073'), width=3),
            dbc.Col( dbc.Card([dbc.CardHeader("EF15LP15"),dbc.CardBody(children=[] , id='EF15LP153', style={'font-size':30, 'margin':'auto'})], id='cardEF15LP153'), width=3),
            
            ]
    ),


])

@app.callback(
    Output('total20','children'),
    Output('cardtotal20', 'color'),
    Input('escola2','value'),
    Input('drop-down20','value')
)
def habtotal(escola,turma):

    dff = df_port1ano.loc[df_port1ano['Escola']==escola]
    df= dff.loc[dff['Turma']==turma]
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
    Output('EF01LP20','children'),
    Output('cardEF01LP20', 'color'),
    Input('escola2','value'),
    Input('drop-down20','value')
)
def hab1(escola,turma):
    dff = df_port1ano.loc[df_port1ano['Escola']==escola]
    df= dff.loc[dff['Turma']==turma]
    soma = df['EF01LP20'].values.sum()
    qtd = df['EF01LP20'].count()
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
    Output('EF12LP10','children'),
    Output('cardEF12LP10', 'color'),
    Input('escola2','value'),
    Input('drop-down20','value')
)
def hab2(escola,turma):
    dff = df_port1ano.loc[df_port1ano['Escola']==escola]
    df= dff.loc[dff['Turma']==turma]
    soma = df['EF12LP10'].values.sum()
    qtd = df['EF12LP10'].count()
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
    Output('EF12LP04','children'),
    Output('cardEF12LP04', 'color'),
    Input('escola2','value'),
    Input('drop-down20','value')
)
def hab3(escola,turma):
    dff = df_port1ano.loc[df_port1ano['Escola']==escola]
    df= dff.loc[dff['Turma']==turma]
    soma = df['EF12LP04'].values.sum()
    qtd = df['EF12LP04'].count()
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
    Output('EF01LP03','children'),
    Output('cardEF01LP03', 'color'),
    Input('escola2','value'),
    Input('drop-down20','value')
)
def hab4(escola,turma):
    dff = df_port1ano.loc[df_port1ano['Escola']==escola]
    df= dff.loc[dff['Turma']==turma]
    soma = df['EF01LP03'].values.sum()
    qtd = df['EF01LP03'].count()
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
    Output('EF01LP05','children'),
    Output('cardEF01LP05', 'color'),
    Input('escola2','value'),
    Input('drop-down20','value')
)
def hab5(escola,turma):
    dff = df_port1ano.loc[df_port1ano['Escola']==escola]
    df= dff.loc[dff['Turma']==turma]
    soma = df['EF01LP05'].values.sum()
    qtd = df['EF01LP05'].count()
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
    Output('EF01LP08','children'),
    Output('cardEF01LP08', 'color'),
    Input('escola2','value'),
    Input('drop-down20','value')
)
def hab6(escola,turma):
    dff = df_port1ano.loc[df_port1ano['Escola']==escola]
    df= dff.loc[dff['Turma']==turma]
    soma = df['EF01LP08'].values.sum()
    qtd = df['EF01LP08'].count()
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
    Output('EF01LP16','children'),
    Output('cardEF01LP16', 'color'),
    Input('escola2','value'),
    Input('drop-down20','value')
)
def hab7(escola,turma):
    dff = df_port1ano.loc[df_port1ano['Escola']==escola]
    df= dff.loc[dff['Turma']==turma]
    soma = df['EF01LP16'].values.sum()
    qtd = df['EF01LP16'].count()
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
    Output('EF01LP01','children'),
    Output('cardEF01LP01', 'color'),
    Input('escola2','value'),
    Input('drop-down20','value')
)
def hab8(escola,turma):
    dff = df_port1ano.loc[df_port1ano['Escola']==escola]
    df= dff.loc[dff['Turma']==turma]
    soma = df['EF01LP01'].values.sum()
    qtd = df['EF01LP01'].count()
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
    Output('EF01LP06','children'),
    Output('cardEF01LP06', 'color'),
    Input('escola2','value'),
    Input('drop-down20','value')
)
def hab10(escola,turma):
    dff = df_port1ano.loc[df_port1ano['Escola']==escola]
    df= dff.loc[dff['Turma']==turma]
    soma = df['EF01LP06'].values.sum()
    qtd = df['EF01LP06'].count()
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
    Output('EF12LP073','children'),
    Output('cardEF12LP073', 'color'),
    Input('escola2','value'),
    Input('drop-down20','value')
)
def hab8(escola,turma):
    dff = df_port1ano.loc[df_port1ano['Escola']==escola]
    df= dff.loc[dff['Turma']==turma]
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
    Output('EF15LP153','children'),
    Output('cardEF15LP153', 'color'),
    Input('escola2','value'),
    Input('drop-down20','value')
)
def hab10(escola,turma):
    dff = df_port1ano.loc[df_port1ano['Escola']==escola]
    df= dff.loc[dff['Turma']==turma]
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

