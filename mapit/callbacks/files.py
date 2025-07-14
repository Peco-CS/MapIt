from dash import Dash, Input, Output, State, dcc
from mapit.map.model import Net, serialize_mapit, deserialize_mapit
import io
import base64


def file_callbacks(app: Dash, net: Net):      


    #---------- Load File Callbacks ----------#
    @app.callback(
        Output("cyto-graph", "elements", allow_duplicate=True),
        Input("cyto-loadFile", "contents"),
        prevent_initial_call=True
    )
    def load_file(contents):
        nonlocal net
        _, content_bytes = contents.split(',')
        decoded = io.BytesIO(base64.b64decode(content_bytes))
        net = deserialize_mapit(decoded.read())
        return net.to_cytoscape()


    #---------- Save File Callbacks ----------#
    @app.callback(
        Output("download-file", "data"),
        Input("cyto-saveFile", "n_clicks"),
        prevent_initial_call = True
    )
    def save_file(_):
        nonlocal net
        if net.is_empty():
            return None
        return dcc.send_bytes(serialize_mapit(net), "file.mapit")
    
    #----------- Img File Callback -----------#
    @app.callback(
    Output("cyto-graph", "generateImage"),
    Input("cyto-imgFile", "n_clicks"),
    prevent_initial_call = True
    )
    def img_file(_):
        img_info = {
            "type": "png",
            "action": "download"
        }
        return img_info

