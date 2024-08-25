from dash.dependencies import Input, Output, State

def register_callbacks(app):
    @app.callback(
        Output("navbar", "className"),
        Input("navbar-toggle", "n_clicks"),
        State("navbar", "className"),
    )
    def toggle_navbar(n, classname):
        if n:
            if "collapsed" in classname:
                return classname.replace(" collapsed", "")
            else:
                return classname + " collapsed"
        return classname
