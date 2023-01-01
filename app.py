from dash import Dash, Input, Output, page_container
from flask import Flask
import plotly.io as pio

from components import Dashboard, Drawer, DrawerSingleItem, DrawerFooter, Navbar


# Create server with secret key
server = Flask(__name__)
server.secret_key = "SECRET_KEY"
pio.templates.default = "plotly_white"


# Instanciate Dash app
app = Dash(
    name=__name__,
    server=server,
    title="My Web App",
    use_pages=True,
    update_title="Updating...",
)


# Create Drawer
nav_links = [
    DrawerSingleItem(name="IBGE", icon="fa-solid:map-marker-alt", href="/ibge"),
    DrawerSingleItem(name="IPEA", icon="icomoon-free:stats-bars", href="/ipea"),
    DrawerSingleItem(name="Deputados", icon="map:political", href="/camara"),
    DrawerSingleItem(
        name="GitHub",
        icon="akar-icons:github-fill",
        href="https://github.com/GusFurtado/DadosAbertosBrasil",
    ),
    DrawerFooter(
        title="Gustavo Furtado",
        subtitle="Cientista de Dados",
        img_src="https://raw.githubusercontent.com/GusFurtado/MyWebsite/master/assets/profile_pic.JPG",
    ),
]


# Create Dashboard Layout
app.layout = Dashboard(
    children=page_container,
    id="dashboard",
    navbar=Navbar(title="Dados Abertos Brasil", id="dashboard-navbar"),
    drawer=Drawer(
        menu=nav_links,
        logo_name="DAB",
        logo_img="https://raw.githubusercontent.com/GusFurtado/dab_assets/main/images/favicon.ico",
    ),
)


@app.callback(
    Output("dashboard-navbar--title", "children"),
    Input("dashboard--location", "pathname"),
)
def init_app(path):
    """Redirects to login page if user is not logged in.

    Inputs
    ------
    dashboard--location.pathname
        Page the user is trying to access.
    Outputs
    -------
    dashboard-navbar--title.children
        Updated navbar title.

    """

    try:
        return {
            "/ibge": "Indicadores Municipais",
            "/ipea": "Séries Temporais",
            "/camara": "Painel de Deputados",
        }[path]
    except KeyError:
        return "Dados Abertos Brasil"


# Run app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1000)
