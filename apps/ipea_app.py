import dash
from dash_extensions.enrich import DashProxy
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

import layouts.ipea_layout as layout
import utils.ipea_utils as utils



MONTSERRAT = {
    'href': 'https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap',
    'rel': 'stylesheet'
}



app = DashProxy(
    name = __name__,
    external_stylesheets = [dbc.themes.BOOTSTRAP, MONTSERRAT]
)

app.layout = layout.layout
app.title = 'Indicadores Econômicos'
server = app.server



@app.callback(
    Output('main_graph', 'figure'),
    [Input('kpi_radio', 'value')])
def update_graph(kpi):
    return utils.figure(kpi)



if __name__ == '__main__':
    app.run_server(
        host = '0.0.0.0',
        port = 1030
    )