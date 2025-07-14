from dash import html, dcc
import dash_bootstrap_components as dbc
from typing import Dict, List, Tuple


def make_group(group_name: str, buttons_list: List[Tuple[str]], upload: str = None) -> html.Div:
    buttons = []
    color = "light"
    for btn_id, btn_label in buttons_list:
        if btn_id == upload:
            btn = dcc.Upload(
                id=f'cyto-{btn_id}',
                children=dbc.Button(btn_label, outline=True, color=color, className="btn-sm")
            )
        else:
            btn = dbc.Button(btn_label, id=f"cyto-{btn_id}", outline=True, color=color, className="btn-sm")
        
        buttons.append(btn)

    group = dbc.Card(
        dbc.CardBody(
            [
                html.H4(group_name.title(), id=f"{group_name}-title", className="groupTitle text-light card-title"), 
                dbc.ButtonGroup(buttons, id=f"{group_name}-buttons", class_name="groupButtons")
            ],
        ),
        id=f"{group_name}-group",
        className="functionBox border-light p-0",
    )
    return group