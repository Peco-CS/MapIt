from dash import Dash, Output, Input, State
from mapit.map import Net
from typing import List, Dict

SELECT_BORDER_COLOR = "#ffffff"

def behavior_callbacks(app: Dash, net: Net, base_stylesheet: List[Dict[str, str]]):
    #---------- Persistence ----------#
    @app.callback(
        Output("cyto-graph", "elements"),
        Input("cyto-graph", "elements")
    )
    def persistence(elements):
        nonlocal net
        net.from_cytoscape(elements)
        return elements


    #---------- Element selection ----------#
    @app.callback(
        [Output("cyto-graph", 'stylesheet'),
         Output("cyto-editorText", "value"),
         Output("cyto-editor", "style")],
        Input('cyto-graph', 'selectedNodeData'),
        prevent_initial_call = True
    )
    def select_node(selected_node, *null):
        nonlocal net
        nonlocal base_stylesheet

        memory = base_stylesheet.copy()
        current_node = net.selection[-1]

        # If there's a selected node
        if selected_node:
            selected_id = selected_node[0]['id']

            # Update the previously selected node
            if isinstance(current_node, str) and current_node != selected_id:
                memory.append({
                    'selector': f'node#{current_node}',
                    'style': {
                        'border-color': SELECT_BORDER_COLOR,
                        'border-style': "dashed",
                    }
                })
            
            # Highlight the currently selected node
            memory.append({
                'selector': f'node#{selected_id}',
                'style': {
                    'border-color': SELECT_BORDER_COLOR,
                }
            })

            # Update state variables
            net.select_node(selected_id)
        else:
            # If no nodes are selected, reset previous_node
            net.select_node("null")
        
        # Content and visibility
        real_id = net.selection[-1]
        content = ""
        style = {"display": "none"}
        if isinstance(real_id, str):
            content = net.nodes[real_id]["data"]["label"]
            style = {"display": "block"}
        
        return memory, content, style
    
    @app.callback(
        Output("cyto-graph", "elements", allow_duplicate=True),
        Input("cyto-editorText", "value"),
        prevent_initial_call = True
    )
    def set_label(text):
        nonlocal net
        if net.selection[1] != None:
            net.nodes[net.selection[-1]]["data"]["label"] = text
        return net.to_cytoscape() 
