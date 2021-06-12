from DadosAbertosBrasil import camara, bandeira

from datetime import datetime

from dash.dependencies import Input, Output
from dash_extensions.enrich import DashProxy

from pandas import read_json

import layouts.camara_layout as layout
import utils.camara_utils as utils



app = DashProxy(name=__name__)
app.layout = layout.layout



PARTIDOS = read_json('data/camara_data.json')



# Carregar opções do dropdown
@app.callback(
    Output('dep_dropdown', 'options'),
    [Input('uf_dropdown', 'value')])
def update_dropdown_options(uf):
    DEPUTADOS = camara.lista_deputados(
        legislatura = 56,
        uf = uf
    )
    return [{'label': row.nome, 'value': row.id} \
        for _, row in DEPUTADOS.iterrows()]



# Carregar informações de um deputado
@app.callback(
    [Output('dep_foto', 'src'),
    Output('dep_nome', 'children'),
    Output('dep_email', 'children'),
    Output('dep_telefone', 'children'),
    Output('dep_nascimento', 'children'),
    Output('dep_uf', 'children'),
    Output('uf_bandeira', 'src'),
    Output('dep_partido', 'children'),
    Output('partido_logo', 'src'),
    Output('plots', 'figure'),
    Output('dashboard', 'style'),
    Output('none_selected', 'style')],
    [Input('dep_dropdown', 'value'),
    Input('ano_input', 'value')],
    prevent_initial_call = True)
def update_deputado(cod, ano):

    dep = camara.Deputado(cod)
    partido = PARTIDOS.index[PARTIDOS.sigla==dep.partido][0]
    charts = utils.Charts(deputado=dep, ano=ano)

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
        utils.UFS[dep.uf],
        bandeira(dep.uf, tamanho=50),
        PARTIDOS.loc[partido, 'nome'],
        PARTIDOS.loc[partido, 'logo'],
        charts.plots(),
        None,
        {'display': 'none'}
    )