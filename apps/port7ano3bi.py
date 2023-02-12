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
df_port7ano3bi = pd.read_csv(DATA_PATH.joinpath("port7ano3bi.csv"))
df_habsport73bi = df_port7ano3bi.drop(columns=['Escola','Estudante','Ano','Turma','Total']) 

layout = html.Div(children=[
    
    dbc.Row(dbc.Col(dcc.Dropdown(df_port7ano3bi['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-down173bi',), width=2)),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("Domínio Geral das Habilidades"),dbc.CardBody( children=[], id='total173bi', style={'font-size':30, 'margin':'auto'})], id='cardtotal173bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF67LP07"),dbc.CardBody(children=[] , id='EF67LP0723bi', style={'font-size':30, 'margin':'auto'})], id='cardEF67LP0723bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF67LP08"),dbc.CardBody(children=[] , id='EF67LP0823bi', style={'font-size':30, 'margin':'auto'})], id='cardEF67LP0823bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF07LP05"),dbc.CardBody(children=[] , id='EF07LP053bi', style={'font-size':30, 'margin':'auto'})], id='cardEF07LP053bi')),
            ]
    ),
    dbc.Popover(
            totalgeral,
            target="total173bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF67LP07,
            target="EF67LP0723bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF67LP08,
            target="EF67LP0823bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF07LP05,
            target="EF07LP053bi",
            body=True,
            trigger="hover"),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF07LP07"),dbc.CardBody(children=[] , id='EF07LP0713bi1', style={'font-size':30, 'margin':'auto'})], id='cardEF07LP0713bi1')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF07LP08"),dbc.CardBody(children=[] , id='EF07LP0813bi', style={'font-size':30, 'margin':'auto'})], id='cardEF07LP0813bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF67LP33"),dbc.CardBody(children=[] , id='EF67LP3313bi', style={'font-size':30, 'margin':'auto'})], id='cardEF67LP3313bi')),
            ]
    ),
    dbc.Popover(
            EF07LP07,
            target="EF07LP0713bi1",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF07LP08,
            target="EF07LP0813bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF67LP33,
            target="EF67LP3313bi",
            body=True,
            trigger="hover"),
  
    html.Br(),
    

dbc.Row(children=[

    dbc.Col(dcc.Dropdown(df_port7ano3bi['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-turma163bi')),
    dbc.Col(dcc.Dropdown(df_habsport73bi.columns, value="EF67LP33", style ={'margin-top':10, 'margin-left':5}, id='drop-hab163bi')),
    
]),

html.Br(),
dbc.Row(children=[

    dbc.Col( dbc.Card(dcc.Graph(id='fighabs163bi',config= {'displaylogo': False}))),
    dbc.Col( dbc.Card(dcc.Graph(id='figacerto163bi',config= {'displaylogo': False}))),


]),


])

@app.callback(
    Output('total173bi','children'),
    Output('cardtotal173bi', 'color'),
    Input('drop-down173bi','value')
)
def habtotal(turma):
    df = df_port7ano3bi.loc[df_port7ano3bi['Turma']==turma]
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
    Output('EF67LP0723bi','children'),
    Output('cardEF67LP0723bi', 'color'),
    Input('drop-down173bi','value')
)
def hab1(turma):
    df= df_port7ano3bi.loc[df_port7ano3bi['Turma']==turma]
    soma = df['EF67LP07'].values.sum()
    qtd = df['EF67LP07'].count()
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
    Output('EF67LP323bi','children'),
    Output('cardEF67LP323bi', 'color'),
    Input('drop-down173bi','value')
)
def hab2(turma):
    df= df_port7ano3bi.loc[df_port7ano3bi['Turma']==turma]
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
    Output('EF07LP053bi','children'),
    Output('cardEF07LP053bi', 'color'),
    Input('drop-down173bi','value')
)
def hab3(turma):
    df= df_port7ano3bi.loc[df_port7ano3bi['Turma']==turma]
    soma = df['EF07LP05'].values.sum()
    qtd = df['EF07LP05'].count()
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
    Output('EF07LP0713bi1','children'),
    Output('cardEF07LP0713bi1', 'color'),
    Input('drop-down173bi','value')
)
def hab4(turma):
    df= df_port7ano3bi.loc[df_port7ano3bi['Turma']==turma]
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
    Output('EF07LP0813bi','children'),
    Output('cardEF07LP0813bi', 'color'),
    Input('drop-down173bi','value')
)
def hab5(turma):
    df= df_port7ano3bi.loc[df_port7ano3bi['Turma']==turma]
    soma = df['EF07LP08'].values.sum()
    qtd = df['EF07LP08'].count()
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
    Output('EF67LP3313bi','children'),
    Output('cardEF67LP3313bi', 'color'),
    Input('drop-down173bi','value')
)
def hab6(turma):
    df= df_port7ano3bi.loc[df_port7ano3bi['Turma']==turma]
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
    Output('EF07LP0713bi','children'),
    Output('cardEF07LP0713bi', 'color'),
    Input('drop-down173bi','value')
)
def hab7(turma):
    df= df_port7ano3bi.loc[df_port7ano3bi['Turma']==turma]
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
    Output('EF07LP063bi','children'),
    Output('cardEF07LP063bi', 'color'),
    Input('drop-down173bi','value')
)
def hab8(turma):
    df= df_port7ano3bi.loc[df_port7ano3bi['Turma']==turma]
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
    Output('EF07LP0413bi','children'),
    Output('cardEF07LP0413bi', 'color'),
    Input('drop-down173bi','value')
)
def hab10(turma):
    df= df_port7ano3bi.loc[df_port7ano3bi['Turma']==turma]
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
    Output('EF67LP0823bi','children'),
    Output('cardEF67LP0823bi', 'color'),
    Input('drop-down173bi','value')
)
def hab10(turma):
    df= df_port7ano3bi.loc[df_port7ano3bi['Turma']==turma]
    soma = df['EF67LP08'].values.sum()
    qtd = df['EF67LP08'].count()
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
    Output('EF67LP383bi','children'),
    Output('cardEF67LP383bi', 'color'),
    Input('drop-down173bi','value')
)
def hab10(turma):
    df= df_port7ano3bi.loc[df_port7ano3bi['Turma']==turma]
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
    Output('EF67LP273bi','children'),
    Output('cardEF67LP273bi', 'color'),
    Input('drop-down173bi','value')
)
def hab10(turma):
    df= df_port7ano3bi.loc[df_port7ano3bi['Turma']==turma]
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
    Output('figacerto163bi','figure'),
    Input('drop-hab163bi','value'),
    Input('drop-turma163bi','value'),
)
def acertos(hab, turma):
    d = df_port7ano3bi.loc[df_port7ano3bi['Turma']==turma]
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
    Output('fighabs163bi','figure'),
    Input('drop-turma163bi','value'),
)
def habs(turma):
    df = df_port7ano3bi.loc[df_port7ano3bi['Turma']==turma]
    fig= px.histogram(df, x = 'Total', color='Total', labels= {'Total':'Percentual de Habilidades Desenvolvidas'}, title= 'Percentual de Habilidades Desenvolvidas <br> por Quantidade de Estudante'+' na turma '+str(turma).upper())
    fig.update_layout(showlegend=False)
    fig.update_yaxes( title= 'Quantidade de Estudantes')
    return fig
