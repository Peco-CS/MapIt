import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output, State
import dash_cytoscape as cyto

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    dbc.Row([
        # Sidebar
        dbc.Col([
            dbc.Button("Toggle Sidebar", id="toggle-button", color="primary", className="mb-3"),
            dbc.Collapse(
                dbc.Card([
                    dbc.CardHeader(html.H4("Graph Management", className="text-center")),
                    dbc.CardBody([
                        dbc.Button("Create Graph", id="create-graph-btn", color="success", className="mb-3 w-100"),
                        dbc.Button("Create Topic", id="create-topic-btn", color="primary", className="mb-3 w-100"),
                        dbc.Button("Delete Topic", id="delete-topic-btn", color="danger", className="mb-3 w-100"),
                        dbc.Button("Add Relation", id="add-relation-btn", color="info", className="mb-3 w-100"),
                        dbc.Button("Delete Relation", id="delete-relation-btn", color="warning", className="mb-3 w-100"),
                        dbc.Button("Update Topic", id="update-topic-btn", color="secondary", className="mb-3 w-100"),
                        dbc.Button("See Relation Topic", id="see-relation-btn", color="dark", className="mb-3 w-100"),
                    ])
                ]), id="sidebar-collapse", is_open=True
            )
        ], width=3, id="sidebar-col"),

        # Main content with graph
        dbc.Col([
            cyto.Cytoscape(
                id='cytoscape-graph',
                elements=[
                    {'data': {'id': 'A', 'label': 'Node A'}, 'position': {'x': 50, 'y': 50}},
                    {'data': {'id': 'B', 'label': 'Node B'}, 'position': {'x': 200, 'y': 200}},
                    {'data': {'id': 'C', 'label': 'Node C'}, 'position': {'x': 350, 'y': 50}},
                    {'data': {'source': 'A', 'target': 'B', 'label': 'A to B'}},
                    {'data': {'source': 'B', 'target': 'C', 'label': 'B to C'}}
                ],
                layout={'name': 'preset'},  # Use preset to respect the specified positions
                style={'width': '100%', 'height': '500px'},
                stylesheet=[
                    {
                        'selector': 'node',
                        'style': {
                            'content': 'data(label)',
                            'text-valign': 'center',
                            'color': 'white',
                            'background-color': '#0074D9',
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
                ]
            )
        ], id="main-content", width=3)
    ]),

    # Information Panel
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(html.H5("Control", className="text-center")),
                dbc.CardBody([
                    html.Div(id="info-details", children="Acciones a realizar o problemas aparecerán aquí!"),
                    dbc.Alert("This is an alert message!", id="alert", color="warning", is_open=True, className="mt-3"),
                ])
            ])
        ], width=12)
    ], className="mt-4")
], fluid=True)


# Callback to toggle the sidebar and adjust the layout
@app.callback(
    [Output("sidebar-collapse", "is_open"),
     Output("sidebar-col", "width"),
     Output("main-content", "width")],
    Input("toggle-button", "n_clicks"),
    [State("sidebar-collapse", "is_open")]
)
def toggle_sidebar(n, is_open):
    if n:
        new_is_open = not is_open
        if new_is_open:
            return True, 3, 9  # Sidebar is open, normal widths
        else:
            return False, 0, 12  # Sidebar is closed, main content full width
    return is_open, 3, 9  # Default to sidebar open if no clicks


if __name__ == '__main__':
    app.run_server(debug=True)
