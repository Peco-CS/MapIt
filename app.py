import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from callbacks import register_callbacks

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Navbar with a toggle button and the "Load", "Save", and "Options" buttons
navbar = html.Div(
    [
        dbc.Button(
            "☰", id="navbar-toggle", className="navbar-toggle"
        ),
        html.Div(
            [
                dbc.Button("Load", id="load-button", color="primary", className="mb-2"),
                dbc.Button("Save", id="save-button", color="success", className="mb-2"),
                dbc.Button("Options", id="options-button", color="warning", className="mb-2"),
            ],
            className="navbar-inner"
        ),
    ],
    id="navbar",
    className="vertical-navbar",
)

# The main layout of the app
app.layout = html.Div(
    [
        navbar,
        html.Div(
            id="main-content",
            className="main-content",
            children=[
                dcc.Graph(id="example-graph")
            ]
        ),
    ],
    className="app-container"
)

# Register callbacks
register_callbacks(app)

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
