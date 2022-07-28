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
df_port4ano2bi = pd.read_csv(DATA_PATH.joinpath("port4ano2bi.csv")) 
df_habsport42bi = df_port4ano2bi.drop(columns=['Escola','Estudante','Ano','Turma','Total','Unnamed: 0'])

layout = html.Div(children=[
    
    dbc.Row(dbc.Col(dcc.Dropdown(df_port4ano2bi['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-down142bi',), width=2)),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("Domínio Geral das Habilidades"),dbc.CardBody( children=[], id='total142bi', style={'font-size':30, 'margin':'auto'})], id='cardtotal142bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF35LP14"),dbc.CardBody(children=[] , id='EF35LP142bi', style={'font-size':30, 'margin':'auto'})], id='cardEF35LP142bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF15LP15"),dbc.CardBody(children=[] , id='EF15LP152bi', style={'font-size':30, 'margin':'auto'})], id='cardEF15LP152bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF15LP17"),dbc.CardBody(children=[] , id='EF15LP1712bi', style={'font-size':30, 'margin':'auto'})], id='cardEF15LP1712bi')),
            ]
    ),
    dbc.Popover(
            totalgeral,
            target="total142bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF35LP14,
            target="EF35LP142bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF15LP15,
            target="EF15LP152bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF15LP17,
            target="EF15LP1712bi",
            body=True,
            trigger="hover"),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF04LP26"),dbc.CardBody(children=[] , id='EF04LP262bi', style={'font-size':30, 'margin':'auto'})], id='cardEF04LP262bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF04LP04"),dbc.CardBody(children=[] , id='EF04LP0412bi', style={'font-size':30, 'margin':'auto'})], id='cardEF04LP0412bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF04LP05"),dbc.CardBody(children=[] , id='EF04LP0512bi', style={'font-size':30, 'margin':'auto'})], id='cardEF04LP0512bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF04LP06"),dbc.CardBody(children=[] , id='EF04LP062bi', style={'font-size':30, 'margin':'auto'})], id='cardEF04LP062bi')),
            ]
    ),
    dbc.Popover(
            EF04LP26,
            target="EF04LP262bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF04LP04,
            target="EF04LP0412bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF04LP05,
            target="EF04LP0512bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF04LP06,
            target="EF04LP062bi",
            body=True,
            trigger="hover"),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF35LP23"),dbc.CardBody(children=[] , id='EF35LP232bi', style={'font-size':30, 'margin':'auto'})], id='cardEF35LP232bi'), width=3),
            dbc.Col( dbc.Card([dbc.CardHeader("EF35LP27"),dbc.CardBody(children=[] , id='EF35LP271bi', style={'font-size':30, 'margin':'auto'})], id='cardEF35LP271bi'), width=3),
           
            ]
    ),

    dbc.Popover(
            EF35LP23,
            target="EF35LP232bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF35LP27,
            target="EF35LP271bi",
            body=True,
            trigger="hover"),
   

dbc.Row(children=[

    dbc.Col(dcc.Dropdown(df_port4ano2bi['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-turma132bi')),
    dbc.Col(dcc.Dropdown(df_habsport42bi.columns, value="EF35LP27", style ={'margin-top':10, 'margin-left':5}, id='drop-hab132bi')),
    
]),

html.Br(),
dbc.Row(children=[

    dbc.Col( dbc.Card(dcc.Graph(id='fighabs132bi',config= {'displaylogo': False}))),
    dbc.Col( dbc.Card(dcc.Graph(id='figacerto132bi',config= {'displaylogo': False}))),


]),


])

@app.callback(
    Output('total142bi','children'),
    Output('cardtotal142bi', 'color'),
    Input('drop-down142bi','value')
)
def habtotal(turma):
    df = df_port4ano2bi.loc[df_port4ano2bi['Turma']==turma]
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
    Output('EF35LP142bi','children'),
    Output('cardEF35LP142bi', 'color'),
    Input('drop-down142bi','value')
)
def hab1(turma):
    df= df_port4ano2bi.loc[df_port4ano2bi['Turma']==turma]
    soma = df['EF35LP14'].values.sum()
    qtd = df['EF35LP14'].count()
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
    Output('EF15LP152bi','children'),
    Output('cardEF15LP152bi', 'color'),
    Input('drop-down142bi','value')
)
def hab2(turma):
    df= df_port4ano2bi.loc[df_port4ano2bi['Turma']==turma]
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
    Output('EF15LP1712bi','children'),
    Output('cardEF15LP1712bi', 'color'),
    Input('drop-down142bi','value')
)
def hab3(turma):
    df= df_port4ano2bi.loc[df_port4ano2bi['Turma']==turma]
    soma = df['EF15LP17'].values.sum()
    qtd = df['EF15LP17'].count()
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
    Output('EF04LP262bi','children'),
    Output('cardEF04LP262bi', 'color'),
    Input('drop-down142bi','value')
)
def hab4(turma):
    df= df_port4ano2bi.loc[df_port4ano2bi['Turma']==turma]
    soma = df['EF04LP26'].values.sum()
    qtd = df['EF04LP26'].count()
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
    Output('EF04LP0412bi','children'),
    Output('cardEF04LP0412bi', 'color'),
    Input('drop-down142bi','value')
)
def hab5(turma):
    df= df_port4ano2bi.loc[df_port4ano2bi['Turma']==turma]
    soma = df['EF04LP04'].values.sum()
    qtd = df['EF04LP04'].count()
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
    Output('EF04LP0512bi','children'),
    Output('cardEF04LP0512bi', 'color'),
    Input('drop-down142bi','value')
)
def hab6(turma):
    df= df_port4ano2bi.loc[df_port4ano2bi['Turma']==turma]
    soma = df['EF04LP05'].values.sum()
    qtd = df['EF04LP05'].count()
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
    Output('EF04LP062bi','children'),
    Output('cardEF04LP062bi', 'color'),
    Input('drop-down142bi','value')
)
def hab7(turma):
    df= df_port4ano2bi.loc[df_port4ano2bi['Turma']==turma]
    soma = df['EF04LP06'].values.sum()
    qtd = df['EF04LP06'].count()
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
    Output('EF35LP232bi','children'),
    Output('cardEF35LP232bi', 'color'),
    Input('drop-down142bi','value')
)
def hab8(turma):
    df= df_port4ano2bi.loc[df_port4ano2bi['Turma']==turma]
    soma = df['EF35LP23'].values.sum()
    qtd = df['EF35LP23'].count()
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
    Output('EF35LP271bi','children'),
    Output('cardEF35LP271bi', 'color'),
    Input('drop-down142bi','value')
)
def hab10(turma):
    df= df_port4ano2bi.loc[df_port4ano2bi['Turma']==turma]
    soma = df['EF35LP27'].values.sum()
    qtd = df['EF35LP27'].count()
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
    Output('figacerto132bi','figure'),
    Input('drop-hab132bi','value'),
    Input('drop-turma132bi','value'),
)
def acertos(hab, turma):
    d = df_port4ano2bi.loc[df_port4ano2bi['Turma']==turma]
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
    Output('fighabs132bi','figure'),
    Input('drop-turma132bi','value'),
)
def habs( turma):
    df = df_port4ano2bi.loc[df_port4ano2bi['Turma']==turma]
    fig= px.histogram(df, x = 'Total', color='Total', labels= {'Total':'Percentual de Habilidades Desenvolvidas'}, title= 'Percentual de Habilidades Desenvolvidas <br> por Quantidade de Estudante'+' na turma '+str(turma).upper())
    fig.update_layout(showlegend=False)
    fig.update_yaxes( title= 'Quantidade de Estudantes')
    return fig



