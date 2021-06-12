from DadosAbertosBrasil import ipea

import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio

pio.templates.default = 'plotly_white'



class Serie:

    def __init__(self, kpi:str):
        self.serie = ipea.Serie(kpi)
        self.kpi = kpi
        self.nome = self.serie.nome
        self.unidade = self.serie.unidade
        self.valores = self.serie.valores[['VALDATA','VALVALOR']]
        self.valores.columns = ['Ano', 'Valores']
        self.valores.Ano = pd.to_datetime(self.valores.Ano, utc=True).dt.year
        self.valores.Ano = self.valores.Ano[self.valores.Ano >= 1994]



def figure(kpi:str) -> go.Figure:

    serie = Serie(kpi)

    fig = go.Figure(
        data = go.Bar(
            x = serie.valores.Ano,
            y = serie.valores.Valores,
            name = serie.nome,
            marker = {
                'line': {
                    'width': 0
                }
            }
        ),
        layout = {
            'title': {
                'text': f'<b>{serie.nome}</b>',
                'font': {'family': 'Montserrat'}
            },
            'yaxis': {
                'title': serie.unidade
            },
            'xaxis': {
                'type': 'category'
            },
            'margin': {
                'l': 5,
                'r': 5,
                't': 50,
                'b': 5
            }
        }
    )

    return fig