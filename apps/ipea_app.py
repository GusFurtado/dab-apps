from dash_extensions.enrich import DashProxy
from dash.dependencies import Input, Output

import layouts.ipea_layout as layout
import utils.ipea_utils as utils



app = DashProxy(name=__name__)
app.layout = layout.layout



@app.callback(
    Output('main_graph', 'figure'),
    [Input('kpi_radio', 'value')])
def update_graph(kpi):
    return utils.figure(kpi)