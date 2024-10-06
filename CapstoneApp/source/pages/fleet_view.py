from dash import dcc, html, callback, Input, Output, State, dash_table
import dash
import dash_bootstrap_components as dbc
import pandas as pd
from components import fleet_viewer

layout = dbc.Container(children=[fleet_viewer.fleet_view])

dash.register_page("View", layout=layout, path="/view-datasets", order=2)
