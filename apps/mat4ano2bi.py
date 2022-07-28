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
df_mat4ano2bi = pd.read_csv(DATA_PATH.joinpath("mat4ano2bi.csv"))
df_habs42bi= df_mat4ano2bi.drop(columns=['Escola','Estudante','Ano','Turma','Total','Unnamed: 0'])  

layout = html.Div(children=[
    
    dbc.Row(dbc.Col(dcc.Dropdown(df_mat4ano2bi['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-down42bi',), width=2)),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("Domínio Geral das Habilidades"),dbc.CardBody( children=[], id='total42bi', style={'font-size':30, 'margin':'auto'})], id='cardtotal42bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF04MA04"),dbc.CardBody(children=[] , id='EF04MA042bi', style={'font-size':30, 'margin':'auto'})], id='cardEF04MA042bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF04MA03"),dbc.CardBody(children=[] , id='EF04MA032bi', style={'font-size':30, 'margin':'auto'})], id='cardEF04MA02bi3')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF04MA15"),dbc.CardBody(children=[] , id='EF04MA152bi', style={'font-size':30, 'margin':'auto'})], id='cardEF04MA152bi')),
            ]
    ),
    dbc.Popover(
            totalgeral,
            target="total42bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF04MA04,
            target="EF04MA042bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF04MA03,
            target="EF04MA032bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF04MA15,
            target="EF04MA152bi",
            body=True,
            trigger="hover"),

    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF04MA18"),dbc.CardBody(children=[] , id='EF04MA182bi', style={'font-size':30, 'margin':'auto'})], id='cardEF04MA182bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF04MA21"),dbc.CardBody(children=[] , id='EF04MA212bi', style={'font-size':30, 'margin':'auto'})], id='cardEF04MA212bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF04MA05"),dbc.CardBody(children=[] , id='EF04MA052bi', style={'font-size':30, 'margin':'auto'})], id='cardEF04MA052bi')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF04MA14"),dbc.CardBody(children=[] , id='EF04MA142bi', style={'font-size':30, 'margin':'auto'})], id='cardEF04MA142bi')),
            ]
    ),
    html.Br(),
    dbc.Popover(
            EF04MA18,
            target="EF04MA182bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF04MA21,
            target="EF04MA212bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF04MA05,
            target="EF04MA052bi",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF04MA14,
            target="EF04MA142bi",
            body=True,
            trigger="hover"),
    
    html.Br(),
 dbc.Row(children=[

    dbc.Col(dcc.Dropdown(df_mat4ano2bi['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-turma42bi')),
    dbc.Col(dcc.Dropdown(df_habs42bi.columns, value="EF04MA14", style ={'margin-top':10, 'margin-left':5}, id='drop-hab42bi')),
    
]),

html.Br(),
dbc.Row(children=[

    dbc.Col( dbc.Card(dcc.Graph(id='fighabs42bi',config= {'displaylogo': False}))),
    dbc.Col( dbc.Card(dcc.Graph(id='figacerto42bi',config= {'displaylogo': False}))),
])

])

@app.callback(
    Output('total42bi','children'),
    Output('cardtotal42bi', 'color'),
    Input('drop-down42bi','value')
)
def habtotal(turma):
    df = df_mat4ano2bi.loc[df_mat4ano2bi['Turma']==turma]
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
    Output('EF04MA042bi','children'),
    Output('cardEF04MA042bi', 'color'),
    Input('drop-down42bi','value')
)
def hab1(turma):
    df= df_mat4ano2bi.loc[df_mat4ano2bi['Turma']==turma]
    soma = df['EF04MA04'].values.sum()
    qtd = df['EF04MA04'].count()
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
    Output('EF04MA032bi','children'),
    Output('cardEF04MA032bi', 'color'),
    Input('drop-down42bi','value')
)
def hab2(turma):
    df= df_mat4ano2bi.loc[df_mat4ano2bi['Turma']==turma]
    soma = df['EF04MA03'].values.sum()
    qtd = df['EF04MA03'].count()
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
    Output('EF04MA152bi','children'),
    Output('cardEF04MA152bi', 'color'),
    Input('drop-down42bi','value')
)
def hab3(turma):
    df= df_mat4ano2bi.loc[df_mat4ano2bi['Turma']==turma]
    soma = df['EF04MA15'].values.sum()
    qtd = df['EF04MA15'].count()
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
    Output('EF04MA182bi','children'),
    Output('cardEF04MA182bi', 'color'),
    Input('drop-down4','value')
)
def hab4(turma):
    df= df_mat4ano2bi.loc[df_mat4ano2bi['Turma']==turma]
    soma = df['EF04MA18'].values.sum()
    qtd = df['EF04MA18'].count()
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
    Output('EF04MA21','children'),
    Output('cardEF04MA21', 'color'),
    Input('drop-down4','value')
)
def hab5(turma):
    df= df_mat4ano2bi.loc[df_mat4ano2bi['Turma']==turma]
    soma = df['EF04MA21'].values.sum()
    qtd = df['EF04MA21'].count()
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
    Output('EF04MA052bi','children'),
    Output('cardEF04MA052bi', 'color'),
    Input('drop-down42bi','value')
)
def hab6(turma):
    df= df_mat4ano2bi.loc[df_mat4ano2bi['Turma']==turma]
    soma = df['EF04MA05'].values.sum()
    qtd = df['EF04MA05'].count()
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
    Output('EF04MA142bi','children'),
    Output('cardEF04MA142bi', 'color'),
    Input('drop-down42bi','value')
)
def hab7(turma):
    df= df_mat4ano2bi.loc[df_mat4ano2bi['Turma']==turma]
    soma = df['EF04MA14'].values.sum()
    qtd = df['EF04MA14'].count()
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
    Output('figacerto42bi','figure'),
    Input('drop-hab42bi','value'),
    Input('drop-turma42bi','value'),
)
def acertos(hab, turma):
    d = df_mat4ano2bi.loc[df_mat4ano2bi['Turma']==turma]
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
    Output('fighabs42bi','figure'),
    Input('drop-turma42bi','value'),
)
def habs(turma):
    df = df_mat4ano2bi.loc[df_mat4ano2bi['Turma']==turma]
    fig= px.histogram(df, x = 'Total', color='Total', labels= {'Total':'Percentual de Habilidades Desenvolvidas'}, title= 'Percentual de Habilidades Desenvolvidas <br> por Quantidade de Estudante'+' na turma '+str(turma).upper())
    fig.update_layout(showlegend=False)
    fig.update_yaxes( title= 'Quantidade de Estudantes')
    return fig


