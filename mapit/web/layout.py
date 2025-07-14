import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
import dash_cytoscape as cyto
import json
from typing import Dict 
from mapit.web.constructors import make_group


# Cyto stylesheet list
with open(f"mapit/assets/cytoscape_stylesheet.json", "r") as f:
    cyto_stylesheet = json.load(f)

# Toolbar styled as navbar
cyto_toolbar = dbc.Container(
    [
        # left groups container
        html.Div(
            id="left-toolbar",
            className="groupsContainer",
            children=[
                make_group("file", [("loadFile", "Load"), ("saveFile", "Save"), ("imgFile", "Img")], upload="loadFile"),
                make_group("node", [("addNode", "+N"), ("delNode", "-N")]),
                make_group("edge", [("addEdge", "+E"), ("delEdge", "-E")]),
            ],
        ),

        # space container
        html.Div(
            id="space-toolbar",
            className="groupsContainer",
        ),

        # right groups container
        html.Div(
            id="right-toolbar",
            className="groupsContainer",
            children=html.H1("MapIt", id="logo", className="text-light")
        ),
    ],
    id="toolbar"
)



editor = dbc.Container(
    [
        dcc.Textarea(
            id='cyto-editorText',
            value="",
            draggable=False,
            className="bg-dark text-light"
        ),
    ],
    id="cyto-editor",
    className="border border-light"
)

functions_block = html.Div([
    dcc.Download(id="download-file"),
])

cyto_space = dbc.Container([
        cyto.Cytoscape(
            id='cyto-graph',
            layout={'name': 'preset'},
            elements=[],
            stylesheet=cyto_stylesheet,
            panningEnabled=True,
            style={
                    'position': 'absolute',
                    'width': '100%',
                    'height': '100%',
                    'top': '0',
                    'left': '0',
                }
        ),
        editor,
    ],
    id="cyto-space",
    className="border border-light"
)


layout = html.Div(
    [
        cyto_toolbar,
        cyto_space,
        functions_block
    ],
    className="app-container bg-dark",
)
