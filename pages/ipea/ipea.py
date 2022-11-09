from dash import (
    Input,
    Output,
    callback,
    register_page
)

from .ipea_layout import IpeaLayout
from .ipea_plot import Serie



register_page(
    __name__,
    path = '/ipea',
    title = 'Séries Temporais'
)



layout = IpeaLayout()



@callback(
    Output('main_graph', 'figure'),
    Input('kpi_radio', 'value'))
def update_graph(kpi):
    return Serie(kpi).plot()
