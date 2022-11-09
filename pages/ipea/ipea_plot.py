from DadosAbertosBrasil import ipea
import pandas as pd
import plotly.graph_objects as go



class Serie:

    def __init__(self, kpi:str):
        self.serie = ipea.Serie(kpi)
        self.serie.dados.data = pd.to_datetime(self.serie.dados.data, utc=True).dt.year
        self.dados = self.serie.dados.loc[self.serie.dados.data > 1994, ['data','valor']]


    def plot(self) -> go.Figure:
        fig = go.Figure(
            data = go.Bar(
                x = self.dados.data,
                y = self.dados.valor,
                name = self.serie.nome,
                marker = {
                    'line': {
                        'width': 0
                    }
                }
            ),
            layout = {
                'title': {
                    'text': f'<b>{self.serie.nome}</b>',
                    'font': {'family': 'Montserrat'}
                },
                'yaxis': {
                    'title': self.serie.unidade
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
