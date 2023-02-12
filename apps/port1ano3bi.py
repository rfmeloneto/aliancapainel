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
df_port1ano3bi = pd.read_csv(DATA_PATH.joinpath("port1ano3bi.csv"))
df_habsport13bi = df_port1ano3bi.drop(columns=['Escola','Estudante','Ano','Turma','Total'])
 

layout = html.Div(children=[
    
    dbc.Row(children = [ 
        dbc.Col(dcc.Dropdown(df_port1ano3bi['Escola'].unique(), value='Duque de Caxias', style ={'margin-top':10, 'margin-left':5}, id='escola23bi',), width=2), 
        dbc.Col(dcc.Dropdown(df_port1ano3bi['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-down203bi',), width=2)
        ]),
        
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("Domínio Geral das Habilidades"),dbc.CardBody( children=[], id='total203bi', style={'font-size':30, 'margin':'auto'})], id='cardtotal203bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF15LP14"),dbc.CardBody(children=[] , id='EF15LP143bi1', style={'font-size':30, 'margin':'auto'})], id='cardEF15LP143bi1')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF15LP16"),dbc.CardBody(children=[] , id='EF15LP163bi', style={'font-size':30, 'margin':'auto'})], id='cardEF15LP163bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF12LP09"),dbc.CardBody(children=[] , id='EF12LP093bi', style={'font-size':30, 'margin':'auto'})], id='cardEF12LP093bi')),
            ]
    ),
    dbc.Popover(
            totalgeral,
            target="total203bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF15LP14,
            target="EF15LP143bi1",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF15LP16,
            target="EF15LP163bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF12LP09,
            target="EF12LP093bi",
            body=True,
            trigger="hover"),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF12LP15"),dbc.CardBody(children=[] , id='EF12LP153bi', style={'font-size':30, 'margin':'auto'})], id='cardEF12LP153bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF01LP26"),dbc.CardBody(children=[] , id='EF01LP263bi', style={'font-size':30, 'margin':'auto'})], id='cardEF01LP263bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF01LP08"),dbc.CardBody(children=[] , id='EF01LP083bi', style={'font-size':30, 'margin':'auto'})], id='cardEF01LP083bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF01LP11"),dbc.CardBody(children=[] , id='EF01LP113bi', style={'font-size':30, 'margin':'auto'})], id='cardEF01LP113bi'), width=3),

            ]
    ),
    dbc.Popover(
            EF12LP15,
            target="EF12LP153bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF01LP26,
            target="EF01LP263bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF01LP08,
            target="EF01LP083bi",
            body=True,
            trigger="hover"),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF12LP17"),dbc.CardBody(children=[] , id='EF12LP173bi1', style={'font-size':30, 'margin':'auto'})], id='cardEF12LP173bi1'), width=3),
            
            ]
    ),

    dbc.Popover(
            EF01LP11,
            target="EF01LP113bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
           EF01LP12,
            target="EF01LP123bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF12LP17,
            target="EF12LP173bi1",
            body=True,
            trigger="hover"),
    
 html.Br(),
     dbc.Row(children=[
    dbc.Col(dcc.Dropdown(df_port1ano3bi['Escola'].unique(), value="Duque de Caxias", style ={'margin-top':10, 'margin-left':5}, id='drop-escola103bi')),    
    dbc.Col(dcc.Dropdown(df_port1ano3bi['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-turma103bi')),
    dbc.Col(dcc.Dropdown(df_habsport13bi.columns, value="EF12LP17", style ={'margin-top':10, 'margin-left':5}, id='drop-hab103bi')),
    ]),

    html.Br(),
    dbc.Row(children=[

    dbc.Col( dbc.Card(dcc.Graph(id='fighabs103bi',config= {'displaylogo': False}))),
    dbc.Col( dbc.Card(dcc.Graph(id='figacerto103bi',config= {'displaylogo': False}))),

])


])

@app.callback(
    Output('total203bi','children'),
    Output('cardtotal203bi', 'color'),
    Input('escola23bi','value'),
    Input('drop-down203bi','value')
)
def habtotal(escola,turma):

    dff = df_port1ano3bi.loc[df_port1ano3bi['Escola']==escola]
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
    Output('EF15LP143bi1','children'),
    Output('cardEF15LP143bi1', 'color'),
    Input('escola23bi','value'),
    Input('drop-down203bi','value')
)
def hab1(escola,turma):
    dff = df_port1ano3bi.loc[df_port1ano3bi['Escola']==escola]
    df= dff.loc[dff['Turma']==turma]
    soma = df['EF15LP14'].values.sum()
    qtd = df['EF15LP14'].count()
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
    Output('EF15LP163bi','children'),
    Output('cardEF15LP163bi', 'color'),
    Input('escola23bi','value'),
    Input('drop-down203bi','value')
)
def hab2(escola,turma):
    dff = df_port1ano3bi.loc[df_port1ano3bi['Escola']==escola]
    df= dff.loc[dff['Turma']==turma]
    soma = df['EF15LP16'].values.sum()
    qtd = df['EF15LP16'].count()
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
    Output('EF12LP093bi','children'),
    Output('cardEF12LP093bi', 'color'),
    Input('escola23bi','value'),
    Input('drop-down203bi','value')
)
def hab3(escola,turma):
    dff = df_port1ano3bi.loc[df_port1ano3bi['Escola']==escola]
    df= dff.loc[dff['Turma']==turma]
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
    Output('EF12LP153bi','children'),
    Output('cardEF12LP153bi', 'color'),
    Input('escola23bi','value'),
    Input('drop-down203bi','value')
)
def hab4(escola,turma):
    dff = df_port1ano3bi.loc[df_port1ano3bi['Escola']==escola]
    df= dff.loc[dff['Turma']==turma]
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




#-----------------------------------------------------------------

@app.callback(
    Output('EF01LP263bi','children'),
    Output('cardEF01LP263bi', 'color'),
    Input('escola23bi','value'),
    Input('drop-down203bi','value')
)
def hab6(escola,turma):
    dff = df_port1ano3bi.loc[df_port1ano3bi['Escola']==escola]
    df= dff.loc[dff['Turma']==turma]
    soma = df['EF01LP26'].values.sum()
    qtd = df['EF01LP26'].count()
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
    Output('EF01LP083bi','children'),
    Output('cardEF01LP083bi', 'color'),
    Input('escola23bi','value'),
    Input('drop-down203bi','value')
)
def hab7(escola,turma):
    dff = df_port1ano3bi.loc[df_port1ano3bi['Escola']==escola]
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
    Output('EF01LP113bi','children'),
    Output('cardEF01LP113bi', 'color'),
    Input('escola23bi','value'),
    Input('drop-down203bi','value')
)
def hab8(escola,turma):
    dff = df_port1ano3bi.loc[df_port1ano3bi['Escola']==escola]
    df= dff.loc[dff['Turma']==turma]
    soma = df['EF01LP11'].values.sum()
    qtd = df['EF01LP11'].count()
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

#-----------------------------------------------------------------

@app.callback(
    Output('EF12LP173bi1','children'),
    Output('cardEF12LP173bi1', 'color'),
    Input('escola23bi','value'),
    Input('drop-down203bi','value')
)
def hab8(escola,turma):
    dff = df_port1ano3bi.loc[df_port1ano3bi['Escola']==escola]
    df= dff.loc[dff['Turma']==turma]
    soma = df['EF12LP17'].values.sum()
    qtd = df['EF12LP17'].count()
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
    Output('figacerto103bi','figure'),
    Input('drop-hab103bi','value'),
    Input('drop-turma103bi','value'),
    Input('drop-escola103bi','value')
)
def acertos(hab, turma, escola):
    d = df_port1ano3bi.loc[df_port1ano3bi['Escola']==escola]
    df = d[d['Turma']==turma]
    dff= df[hab]
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
    Output('fighabs103bi','figure'),
    Input('drop-turma103bi','value'),
    Input('drop-escola103bi','value')
)
def habs( turma,escola):
    d = df_port1ano3bi.loc[df_port1ano3bi['Escola']==escola]
    df = d[d['Turma']==turma]
    fig= px.histogram(df, x = 'Total', color='Total', labels= {'Total':'Percentual de Habilidades Desenvolvidas'}, title= 'Percentual de Habilidades Desenvolvidas <br> por Quantidade de Estudante'+' na turma '+str(turma).upper())
    fig.update_layout(showlegend=False)
    fig.update_yaxes( title= 'Quantidade de Estudantes')
    return fig


