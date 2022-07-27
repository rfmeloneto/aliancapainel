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
df_port5ano = pd.read_csv(DATA_PATH.joinpath("port5ano.csv")) 
df_habsport5 = df_port5ano.drop(columns=['Escola','Estudante','Ano','Turma','Total'])

layout = html.Div(children=[
    
    dbc.Row(dbc.Col(dcc.Dropdown(df_port5ano['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-down15',), width=2)),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("Domínio Geral das Habilidades"),dbc.CardBody( children=[], id='total15', style={'font-size':30, 'margin':'auto'})], id='cardtotal15')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF05LP10"),dbc.CardBody(children=[] , id='EF05LP10', style={'font-size':30, 'margin':'auto'})], id='cardEF05LP10')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF35LP01"),dbc.CardBody(children=[] , id='EF35LP012', style={'font-size':30, 'margin':'auto'})], id='cardEF35LP012')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF35LP21"),dbc.CardBody(children=[] , id='EF35LP212', style={'font-size':30, 'margin':'auto'})], id='cardEF35LP212')),
            ]
    ),
    dbc.Popover(
            totalgeral,
            target="total15",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF05LP10,
            target="EF05LP10",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF35LP01,
            target="EF35LP012",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF35LP21,
            target="EF35LP212",
            body=True,
            trigger="hover"),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF05LP02"),dbc.CardBody(children=[] , id='EF05LP02', style={'font-size':30, 'margin':'auto'})], id='cardEF05LP02')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF15LP14"),dbc.CardBody(children=[] , id='EF15LP14', style={'font-size':30, 'margin':'auto'})], id='cardEF15LP14')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF05LP11"),dbc.CardBody(children=[] , id='EF05LP11', style={'font-size':30, 'margin':'auto'})], id='cardEF05LP11')),
            dbc.Col( dbc.Card([dbc.CardHeader("EF05LP01"),dbc.CardBody(children=[] , id='EF05LP01', style={'font-size':30, 'margin':'auto'})], id='cardEF05LP01')),
            ]
    ),

    dbc.Popover(
            EF05LP02,
            target="EF05LP02",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF15LP14,
            target="EF15LP14",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF05LP11,
            target="EF05LP11",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF05LP01,
            target="EF05LP01",
            body=True,
            trigger="hover"),
    html.Br(),
    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF05LP20"),dbc.CardBody(children=[] , id='EF05LP20', style={'font-size':30, 'margin':'auto'})], id='cardEF05LP20'), width=3),
            dbc.Col( dbc.Card([dbc.CardHeader("EF15LP04"),dbc.CardBody(children=[] , id='EF15LP042', style={'font-size':30, 'margin':'auto'})], id='cardEF15LP042'), width=3),
            dbc.Col( dbc.Card([dbc.CardHeader("EF15LP02"),dbc.CardBody(children=[] , id='EF15LP02', style={'font-size':30, 'margin':'auto'})], id='cardEF15LP02'), width=3),
            dbc.Col( dbc.Card([dbc.CardHeader("EF15LP18"),dbc.CardBody(children=[] , id='EF15LP18', style={'font-size':30, 'margin':'auto'})], id='cardEF15LP18'), width=3),
            ]
    ),
     dbc.Popover(
            EF05LP20,
            target="EF05LP20",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF15LP04,
            target="EF15LP042",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF15LP02,
            target="EF15LP02",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF15LP18,
            target="EF15LP18",
            body=True,
            trigger="hover"),

    html.Br(),

    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF05LP08"),dbc.CardBody(children=[] , id='EF05LP08', style={'font-size':30, 'margin':'auto'})], id='cardEF05LP08'), width=3),
            dbc.Col( dbc.Card([dbc.CardHeader("EF05LP04"),dbc.CardBody(children=[] , id='EF05LP04', style={'font-size':30, 'margin':'auto'})], id='cardEF05LP04'), width=3),
            dbc.Col( dbc.Card([dbc.CardHeader("EF35LP26"),dbc.CardBody(children=[] , id='EF35LP26', style={'font-size':30, 'margin':'auto'})], id='cardEF35LP26'), width=3),
            dbc.Col( dbc.Card([dbc.CardHeader("EF35LP29"),dbc.CardBody(children=[] , id='EF35LP292', style={'font-size':30, 'margin':'auto'})], id='cardEF35LP292'), width=3),
            ]
    ),
    dbc.Popover(
            EF05LP08,
            target="EF05LP08",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF05LP04,
            target="EF05LP04",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF35LP26,
            target="EF35LP26",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF35LP29,
            target="EF35LP292",
            body=True,
            trigger="hover"),

    html.Br(),

    dbc.Row(
            children=[
            dbc.Col( dbc.Card([dbc.CardHeader("EF35LP06"),dbc.CardBody(children=[] , id='EF35LP062', style={'font-size':30, 'margin':'auto'})], id='cardEF35LP062'), width=3),
            dbc.Col( dbc.Card([dbc.CardHeader("EF35LP30"),dbc.CardBody(children=[] , id='EF35LP30', style={'font-size':30, 'margin':'auto'})], id='cardEF35LP30'), width=3),
            
            ]
    ),

     dbc.Popover(
            EF35LP06,
            target="EF35LP062",
            body=True,
            trigger="hover"),
    dbc.Popover(
            EF35LP30,
            target="EF35LP30",
            body=True,
            trigger="hover"),
            
dbc.Row(children=[

    dbc.Col(dcc.Dropdown(df_port5ano['Turma'].unique(), value='a', style ={'margin-top':10, 'margin-left':5}, id='drop-turma14')),
    dbc.Col(dcc.Dropdown(df_habsport5.columns, value="EF35LP30", style ={'margin-top':10, 'margin-left':5}, id='drop-hab14')),
    
]),

html.Br(),
dbc.Row(children=[

    dbc.Col( dbc.Card(dcc.Graph(id='fighabs14',config= {'displaylogo': False}))),
    dbc.Col( dbc.Card(dcc.Graph(id='figacerto14',config= {'displaylogo': False}))),


]),

    

])

@app.callback(
    Output('total15','children'),
    Output('cardtotal15', 'color'),
    Input('drop-down15','value')
)
def habtotal(turma):
    df = df_port5ano.loc[df_port5ano['Turma']==turma]
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
    Output('EF05LP10','children'),
    Output('cardEF05LP10', 'color'),
    Input('drop-down15','value')
)
def hab1(turma):
    df= df_port5ano.loc[df_port5ano['Turma']==turma]
    soma = df['EF05LP10'].values.sum()
    qtd = df['EF05LP10'].count()
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
    Output('EF35LP012','children'),
    Output('cardEF35LP012', 'color'),
    Input('drop-down15','value')
)
def hab2(turma):
    df= df_port5ano.loc[df_port5ano['Turma']==turma]
    soma = df['EF35LP01'].values.sum()
    qtd = df['EF35LP01'].count()
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
    Output('EF05LP01','children'),
    Output('cardEF05LP01', 'color'),
    Input('drop-down15','value')
)
def hab3(turma):
    df= df_port5ano.loc[df_port5ano['Turma']==turma]
    soma = df['EF05LP01'].values.sum()
    qtd = df['EF05LP01'].count()
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
    Output('EF05LP02','children'),
    Output('cardEF05LP02', 'color'),
    Input('drop-down15','value')
)
def hab4(turma):
    df= df_port5ano.loc[df_port5ano['Turma']==turma]
    soma = df['EF05LP02'].values.sum()
    qtd = df['EF05LP02'].count()
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
    Output('EF15LP14','children'),
    Output('cardEF15LP14', 'color'),
    Input('drop-down15','value')
)
def hab5(turma):
    df= df_port5ano.loc[df_port5ano['Turma']==turma]
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
    Output('EF05LP11','children'),
    Output('cardEF05LP11', 'color'),
    Input('drop-down15','value')
)
def hab6(turma):
    df= df_port5ano.loc[df_port5ano['Turma']==turma]
    soma = df['EF05LP11'].values.sum()
    qtd = df['EF05LP11'].count()
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
    Output('EF35LP212','children'),
    Output('cardEF35LP212', 'color'),
    Input('drop-down15','value')
)
def hab7(turma):
    df= df_port5ano.loc[df_port5ano['Turma']==turma]
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
    Output('EF05LP20','children'),
    Output('cardEF05LP20', 'color'),
    Input('drop-down15','value')
)
def hab8(turma):
    df= df_port5ano.loc[df_port5ano['Turma']==turma]
    soma = df['EF05LP20'].values.sum()
    qtd = df['EF05LP20'].count()
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
    Output('EF15LP042','children'),
    Output('cardEF15LP042', 'color'),
    Input('drop-down15','value')
)
def hab10(turma):
    df= df_port5ano.loc[df_port5ano['Turma']==turma]
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
    Output('EF15LP02','children'),
    Output('cardEF15LP02', 'color'),
    Input('drop-down15','value')
)
def hab9(turma):
    df= df_port5ano.loc[df_port5ano['Turma']==turma]
    soma = df['EF15LP02'].values.sum()
    qtd = df['EF15LP02'].count()
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
    Output('EF15LP18','children'),
    Output('cardEF15LP18', 'color'),
    Input('drop-down15','value')
)
def hab11(turma):
    df= df_port5ano.loc[df_port5ano['Turma']==turma]
    soma = df['EF15LP18'].values.sum()
    qtd = df['EF15LP18'].count()
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
    Output('EF05LP08','children'),
    Output('cardEF05LP08', 'color'),
    Input('drop-down15','value')
)
def hab12(turma):
    df= df_port5ano.loc[df_port5ano['Turma']==turma]
    soma = df['EF05LP08'].values.sum()
    qtd = df['EF05LP08'].count()
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
    Output('EF05LP04','children'),
    Output('cardEF05LP04', 'color'),
    Input('drop-down15','value')
)
def hab13(turma):
    df= df_port5ano.loc[df_port5ano['Turma']==turma]
    soma = df['EF05LP04'].values.sum()
    qtd = df['EF05LP04'].count()
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
    Output('EF35LP26','children'),
    Output('cardEF35LP26', 'color'),
    Input('drop-down15','value')
)
def hab14(turma):
    df= df_port5ano.loc[df_port5ano['Turma']==turma]
    soma = df['EF35LP26'].values.sum()
    qtd = df['EF35LP26'].count()
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
    Output('EF35LP292','children'),
    Output('cardEF35LP292', 'color'),
    Input('drop-down15','value')
)
def hab15(turma):
    df= df_port5ano.loc[df_port5ano['Turma']==turma]
    soma = df['EF35LP29'].values.sum()
    qtd = df['EF35LP29'].count()
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
    Output('EF35LP062','children'),
    Output('cardEF35LP062', 'color'),
    Input('drop-down15','value')
)
def hab16(turma):
    df= df_port5ano.loc[df_port5ano['Turma']==turma]
    soma = df['EF35LP06'].values.sum()
    qtd = df['EF35LP06'].count()
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
    Output('EF35LP30','children'),
    Output('cardEF35LP30', 'color'),
    Input('drop-down15','value')
)
def hab17(turma):
    df= df_port5ano.loc[df_port5ano['Turma']==turma]
    soma = df['EF35LP30'].values.sum()
    qtd = df['EF35LP30'].count()
    media= soma/qtd
    media = media*100
    media = int(media)
    if media >= 50:
        return str(media), 'success'
    elif media >= 30 and media < 50 :
        return str(media) , 'warning'
    else:
        return str(media), 'danger'

@app.callback(
    Output('figacerto14','figure'),
    Input('drop-hab14','value'),
    Input('drop-turma14','value'),
)
def acertos(hab, turma):
    d = df_port5ano.loc[df_port5ano['Turma']==turma]
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
    Output('fighabs14','figure'),
    Input('drop-turma14','value'),
)
def habs(turma):
    df = df_port5ano.loc[df_port5ano['Turma']==turma]
    fig= px.histogram(df, x = 'Total', color='Total', labels= {'Total':'Percentual de Habilidades Desenvolvidas'}, title= 'Percentual de Habilidades Desenvolvidas <br> por Quantidade de Estudante'+' na turma '+str(turma).upper())
    fig.update_layout(showlegend=False)
    fig.update_yaxes( title= 'Quantidade de Estudantes')
    return fig



