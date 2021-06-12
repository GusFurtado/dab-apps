from dash_extensions.enrich import DashProxy
from dash.dependencies import Input, Output

import layouts.ipea_layout as layout
from utils import utils



app = DashProxy(name=__name__)
app.layout = layout.layout



@app.callback(
    Output('main_graph', 'figure'),
    [Input('kpi_radio', 'value')])
def update_graph(kpi):
    return utils.Serie(kpi).plot()