import dash
import dash_bootstrap_components as dbc
from dash import dcc, html

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    dbc.Row([
        # Sidebar Panel
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(html.H4("Map It", className="text-center")),
                dbc.CardBody([
                    dbc.Button("Crear Grafo", id="create-graph-btn", color="success", className="mb-3 w-100"),
                    dbc.Button("Añadir Tema", id="create-topic-btn", color="primary", className="mb-3 w-100"),
                    dbc.Button("Eliminar Tema", id="delete-topic-btn", color="danger", className="mb-3 w-100"),
                    dbc.Button("Añadir Relación", id="add-relation-btn", color="info", className="mb-3 w-100"),
                    dbc.Button("Eliminar Relación", id="delete-relation-btn", color="warning", className="mb-3 w-100"),
                    dbc.Button("Actualizar Tema", id="update-topic-btn", color="secondary", className="mb-3 w-100"),
                    dbc.Button("Ver relaciones del tema", id="see-relation-btn", color="dark", className="mb-3 w-100"),
                ])
            ])
        ], width=3),

        # Placeholder for Main Content Area
        dbc.Col([
            html.Div(id="main-content", children="Aquí va el grafo")
        ], width=9)
    ])
], fluid=True)

if __name__ == '__main__':
    app.run_server(debug=True)
