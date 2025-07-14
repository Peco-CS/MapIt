from dash import Dash, Input, Output
from mapit.map import Net

def edge_callbacks(app: Dash, net: Net):
    @app.callback(
        Output("cyto-graph", "elements", allow_duplicate=True),
        Input("cyto-addEdge", "n_clicks"),
        prevent_initial_call = True
    )
    def add_edge(_):
        nonlocal net
        net.add_edge()
        return net.to_cytoscape()
    
    @app.callback(
        Output("cyto-graph", "elements", allow_duplicate=True),
        Input("cyto-delEdge", "n_clicks"),
        prevent_initial_call = True
    )
    def del_edge(_):
        nonlocal net
        net.del_edge()
        return net.to_cytoscape()
    