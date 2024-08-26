import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output, State, callback_context
import dash_cytoscape as cyto

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Layout of the app
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            dbc.Button("Add Topic", id="add-topic-btn", color="primary", className="me-2"),
            dbc.Button("Delete Topic", id="delete-topic-btn", color="danger", className="me-2"),
            dbc.Button("Update Topic", id="update-topic-btn", color="warning", className="me-2"),
            dbc.Button("View Relations", id="view-relations-btn", color="info", className="me-2"),
        ], width=12),
    ], className="my-2"),
    dbc.Row([
        dbc.Col([
            dbc.Alert(id="node-alert", is_open=False, duration=4000, color="warning"),
        ], width=12)
    ]),
    dbc.Row([
        dbc.Col([
            cyto.Cytoscape(
                id='cytoscape-graph',
                layout={'name': 'breadthfirst'},
                style={'width': '100%', 'height': '600px'},
                elements=[],
                stylesheet=[
                    {
                        'selector': 'node',
                        'style': {
                            'content': 'data(label)',
                            'text-valign': 'center',
                            'color': 'black',
                            'background-color': 'BFD7B5',
                            'font-size': '12px'
                        }
                    },
                    {
                        'selector': 'edge',
                        'style': {
                            'width': 2,
                            'line-color': '#ccc',
                            'target-arrow-color': '#ccc',
                            'target-arrow-shape': 'triangle'
                        }
                    }
                ]
            )
        ], width=12)
    ])
])

# Callback to handle node actions and alert notification
@app.callback(
    [Output('cytoscape-graph', 'elements'),
     Output('node-alert', 'is_open'),
     Output('node-alert', 'children')],
    Input('add-topic-btn', 'n_clicks'),
    Input('delete-topic-btn', 'n_clicks'),
    Input('update-topic-btn', 'n_clicks'),
    Input('view-relations-btn', 'n_clicks'),
    State('cytoscape-graph', 'elements'),
    State('cytoscape-graph', 'selectedNodeData')
)
def modify_graph(add_clicks, delete_clicks, update_clicks, view_clicks, elements, selected_node):
    ctx = callback_context
    if not ctx.triggered:
        return elements, False, ""
    triggered_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if elements is None:
        elements = []

    show_alert = False
    alert_message = ""

    if triggered_id == 'add-topic-btn':
        new_node_id = f'node-{len(elements)}'
        elements.append({'data': {'id': new_node_id, 'label': f'Topic {len(elements)}'}, 'position': {'x': 50, 'y': 50}})
    
    elif triggered_id == 'delete-topic-btn' and selected_node:
        node_id_to_delete = selected_node[0]['id']
        elements = [el for el in elements if el['data']['id'] != node_id_to_delete]
    
    elif triggered_id == 'update-topic-btn' and selected_node:
        node_id_to_update = selected_node[0]['id']
        for el in elements:
            if el['data']['id'] == node_id_to_update:
                el['data']['label'] = f'Updated {node_id_to_update}'
    
    elif triggered_id == 'view-relations-btn' and selected_node:
        node_id_to_view = selected_node[0]['id']
        for el in elements:
            if el['data']['id'] == node_id_to_view:
                el['style'] = {'background-color': '#FF4136'}

    # Count the number of nodes
    node_count = len([el for el in elements if el['data']['id'].startswith('node')])

    # Trigger the alert if there are 10 or more nodes
    if node_count >= 10:
        show_alert = True
        alert_message = "You have added 10 or more nodes. Consider creating a deeper level for better organization."

    return elements, show_alert, alert_message

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
