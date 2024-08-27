import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
import dash_cytoscape as cyto

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP])

# Define the layout of the app
app.layout = dbc.Container([
    # Top Bar
    dbc.Row([
        dbc.Col([
            html.Div(
                html.Img(
                    src="assets/logo.png",
                    alt="Map It Logo",
                    style={"height": "auto", "max-width": "100%"}
                ), style={'border-radius': '50%'}
            )
        ], width=2),
        dbc.Col([
            html.H1("Map It", style={"margin": "auto", "padding-left": "1rem"})
        ], width=10, style={"display": "flex", "align-items": "center"})
    ], id="bar"),

    # Main Content
    dbc.Row([
        # Side Panel
        dbc.Col([
            # Section 1: Load, Save, Delete buttons
            dbc.Row([
                dbc.Button([
                    html.I(className="bi bi-cloud-arrow-down-fill me-2"),
                    "Load Graph"
                ], id="load-graph-btn", color="primary", className="mb-2 w-75 mx-auto"),
                dbc.Button([
                    html.I(className="bi bi-cloud-arrow-up-fill me-2"),
                    "Save Graph"
                ], id="save-graph-btn", color="success", className="mb-2 w-75 mx-auto"),
                dbc.Button([
                    html.I(className="bi bi-trash-fill me-2"),
                    "Delete Graph"
                ], id="delete-graph-btn", color="danger", className="mb-2 w-75 mx-auto"),
            ], style={"height": "33%"}),

            # Section 2: Add/Delete Node/Relation buttons
            dbc.Row([
                dbc.Col([
                    dbc.Button(html.I(className="bi bi-node-plus-fill"), id="add-node-btn", color="info", className="mb-2 w-100"),
                ], width=3),
                dbc.Col([
                    dbc.Button(html.I(className="bi bi-node-minus-fill"), id="delete-node-btn", color="warning", className="mb-2 w-100"),
                ], width=3),
                dbc.Col([
                    dbc.Button(html.I(className="bi bi-patch-plus-fill"), id="add-relation-btn", color="info", className="mb-2 w-100"),
                ], width=3),
                dbc.Col([
                    dbc.Button(html.I(className="bi bi-trash2-fill"), id="delete-relation-btn", color="warning", className="mb-2 w-100"),
                ], width=3),
            ], id="actions"),

            # Section 3: Node Information Box
            dbc.Row([
                dbc.Col([
                    html.Div([
                        html.H5("Node Title", id="node-title", className="text-center"),
                        html.P("Node content will be displayed here.", id="node-content", className="p-2")
                    ], className="info-container")
                ])
            ])
        ], id="side-panel", width=3),

        # Graph Area
        dbc.Col([
            cyto.Cytoscape(
                id='cytoscape-graph',
                layout={'name': 'preset'},
                elements=[
                    {'data': {'id': 'A', 'label': 'Node A'}, 'position': {'x': 50, 'y': 50}},
                    {'data': {'id': 'B', 'label': 'Node B'}, 'position': {'x': 200, 'y': 200}},
                    {'data': {'id': 'C', 'label': 'Node C'}, 'position': {'x': 350, 'y': 50}},
                    {'data': {'source': 'A', 'target': 'B', 'label': 'A to B'}},
                    {'data': {'source': 'B', 'target': 'C', 'label': 'B to C'}}
                ],
                stylesheet=[
                    {
                        'selector': 'node',
                        'style': {
                            'content': 'data(label)',
                            'text-valign': 'center',
                            'color': 'white',
                            'background-color': '#070F2B',
                            'font-size': '12px'
                        }
                    },
                    {
                        'selector': 'edge',
                        'style': {
                            'width': 2,
                            'line-color': '#ccc',
                            'target-arrow-color': '#ccc',
                            'target-arrow-shape': 'triangle',
                            'curve-style': 'bezier',
                            'label': 'data(label)',
                            'font-size': '10px',
                            'text-rotation': 'autorotate',
                            'color': '#555'
                        }
                    }
                ],
                style={'width': '100%', 'height': '100%'}
            )
        ], id="graph-container", width=9)
    ], id="main-container")
], fluid=True, style={"height": "100vh"})

if __name__ == '__main__':
    app.run_server(debug=True)
