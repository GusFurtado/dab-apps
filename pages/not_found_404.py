from dash import register_page
from components.fullscreen_message import FullscreenMessage



register_page(
    __name__,
    path = '/',
    title = '404 - Não Encontrado'
)



layout = FullscreenMessage(
    top_message = 'Página não encontrada',
    bottom_message = 'Navegue pela barra lateral',
    src = '/assets/img/not_found_404.svg'
)
