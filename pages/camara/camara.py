from DadosAbertosBrasil import camara, bandeira

from datetime import datetime

from dash import (
    Input,
    Output,
    callback,
    register_page
)
from pandas import read_json

from .camara_layout import CamaraLayout
from .camara_plot import Charts
from utils import lists



register_page(
    __name__,
    path = '/camara',
    title = 'Painel de Deputados'
)



layout = CamaraLayout()
PARTIDOS = read_json('data/camara_data.json')



# Carregar opções do dropdown
@callback(
    Output('dep_dropdown', 'options'),
    Input('uf_dropdown', 'value'))
def update_dropdown_options(uf):
    DEPUTADOS = camara.lista_deputados(
        legislatura = 56,
        uf = uf
    )
    return [{'label': row.nome, 'value': row.codigo} \
        for _, row in DEPUTADOS.iterrows()]



# Carregar informações de um deputado
@callback(
    Output('dep_foto', 'src'),
    Output('dep_nome', 'children'),
    Output('dep_email', 'children'),
    Output('dep_telefone', 'children'),
    Output('dep_nascimento', 'children'),
    Output('dep_uf', 'children'),
    Output('uf_bandeira', 'src'),
    Output('dep_partido', 'children'),
    Output('partido_logo', 'src'),
    Output('plots', 'figure'),
    Input('dep_dropdown', 'value'),
    Input('ano_input', 'value'))
def update_deputado(cod, ano):
    
    if cod is None:
        cod = 160541
    dep = camara.Deputado(cod)
    partido = PARTIDOS.index[PARTIDOS.sigla==dep.partido][0]
    charts = Charts(deputado=dep, ano=ano)

    nascimento = datetime.strftime(
        datetime.strptime(dep.nascimento, '%Y-%m-%d'),
        format = '%d/%m/%Y'
    )

    return (
        dep.foto,
        dep.nome_eleitoral,
        dep.email,
        dep.gabinete['telefone'],
        nascimento,
        lists.UFS[dep.uf]['Nome'],
        bandeira(dep.uf, tamanho=50),
        PARTIDOS.loc[partido, 'nome'],
        PARTIDOS.loc[partido, 'logo'],
        charts.plots()
    )
