import dash
import dash_bootstrap_components as dbc
from mapit.web.layout import layout, cyto_stylesheet
from mapit.map.model import Net
from mapit.callbacks import (
    file_callbacks,
    node_callbacks,
    edge_callbacks,
    behavior_callbacks,
)

# Init Dash app
net = Net()
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

# The main layout of the app
app.layout = layout
#app.index_string = VIEWPORT

# Register callbacks
behavior_callbacks(app, net, cyto_stylesheet)
file_callbacks(app, net)
node_callbacks(app, net)
edge_callbacks(app, net)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
