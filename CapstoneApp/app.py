from dash import Dash, dcc
import dash
import dash_bootstrap_components as dbc
from source.pages import main_page
from source.components import navbar

# ------------------------------------------------------------------ #
# --------------------------- Styling ------------------------------ #
# ------------------------------------------------------------------ #

# App stylesheets
external_stylesheets = [dbc.themes.BOOTSTRAP]
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# ------------------------------------------------------------------ #
# --------------------------- App Setup ---------------------------- #
# ------------------------------------------------------------------ #
# Setup app
app = Dash(__package__,
            external_stylesheets=external_stylesheets,
            use_pages=True,
            suppress_callback_exceptions=True)
serve(app.server, host="0.0.0.0", port=8080)

# Register first screen of app as 'Main'
dash.register_page("Main", layout=main_page.main_layout, path='/')

# Define first screen layout
app.layout = dbc.Container(children=[
            dcc.Store(id='drone-data'),
            dcc.Store(id='query-log'),
            navbar.make_navbar,
            dash.page_container
    ], fluid=True, class_name='main-container')


if __name__ == '__main__':
    app.run(debug=False)

