from dash import Dash, Input, Output
from mapit.map import Net

def node_callbacks(app: Dash, net: Net):
    @app.callback(
        Output("cyto-graph", "elements", allow_duplicate=True),
        Input("cyto-addNode", "n_clicks"),
        prevent_initial_call = True
    )
    def add_node(_):
        nonlocal net
        net.add_node()
        return net.to_cytoscape()
    
    @app.callback(
        Output("cyto-graph", "elements", allow_duplicate=True),
        Input("cyto-delNode", "n_clicks"),
        prevent_initial_call = True
    )
    def del_node(_):
        nonlocal net
        net.del_node()
        return net.to_cytoscape()
    