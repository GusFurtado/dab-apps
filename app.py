from apps import ibge_app
from apps import ipea_app
from apps import camara_app
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash_extensions.enrich import DashProxy
from dash_extensions.multipage import PageCollection, app_to_page, CONTENT_ID, URL_ID



def simple_menu(page_collection):
    children = []
    pages = page_collection.pages
    for i, page in enumerate(pages):
        children.append(html.A(children=page.label, href="/{}".format(page.id)))
        if i < (len(pages) - 1):
            children.append(html.Br())
    return children



# Create pages.
pc = PageCollection(pages=[
    app_to_page(ibge_app.app, "ibge", "Mapa de Indicadores"),
    app_to_page(ipea_app.app, "ipea", "Indicadores Econômicos"),
    app_to_page(camara_app.app, "camara", "Painel de Deputados")
],
    default_page_id = 'ibge'
)



# Create app.
app = DashProxy(suppress_callback_exceptions=True)
app.layout = html.Div(simple_menu(pc) + [html.Div(id=CONTENT_ID), dcc.Location(id=URL_ID)])



# Register callbacks.
pc.navigation(app)
pc.callbacks(app)



if __name__ == '__main__':
    app.run_server()