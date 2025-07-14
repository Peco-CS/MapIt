import pickle
from collections import deque
from typing import Dict, List, Deque

######### Models #########

def build_tokens(digits: int, exceptions: List[str] = []) -> Deque[str]:
    tokens: Deque[str] = deque()
    code_format: str = f"0{digits}x"  # Fixed lenght hexadecimal format
    for i in range(1, 16**digits):
        code = format(i, code_format)
        if code not in exceptions:
            tokens.append(code)
        else:
            exceptions.remove(code)
    return tokens


TOKEN_LEN: int = 3
TOKEN_STACK: Deque[str] = build_tokens(TOKEN_LEN) 

class Net:
    """
    Net is the definition of a single network container for cytoscape elements (nodes + edges).
    """

    def __init__(self) -> None:
        # Fundamentals
        self.nodes: Dict[str, dict] = {}
        self.edges: Dict[str, dict] = {}
        
        # Buildings
        self.tokens: Deque[str] = TOKEN_STACK.copy()
        self.selection: List[str] = [None, None]
        return
    
    def select_node(self, node_id: str):
        if node_id == "null":
            self.selection = [None, None]
        else:
            self.selection[0] = self.selection[1]
            self.selection[1] = node_id
        return

    def add_node(self):
        node_id = self.tokens.pop()
        self.nodes[node_id] = {
            "data": {"id": node_id, "label": None},
            "position": {"x": 750, "y": 200}, #change to 0,0 if padding enable
        }
    

    def del_node(self):
        node_id = self.selection[1]
        if node_id == None:
            return
        # Delete node and return id to tokens
        self.nodes.pop(node_id)
        self.tokens.append(node_id)
        return

    def add_edge(self):
        source_id = self.selection[0]
        target_id = self.selection[1]
        if (source_id == None) or (target_id == None):
            return
        # Create the edge from source to target
        edge_id = f"{source_id}-{target_id}"
        self.edges[edge_id] = {
            "data": {"source": source_id, "target": target_id}
        }
    

    def del_edge(self):
        source_id = self.selection[0]
        target_id = self.selection[1]
        edge_id = f"{source_id}-{target_id}"
        if (source_id == None) or (target_id == None):
            return
        if edge_id not in self.edges.keys():
            return
        # Delete the edge from source to target
        self.edges.pop(edge_id)
    

    def from_cytoscape(self, elements: List[Dict[str, str]]):
        # Rebuild object from elements
        new_nodes = {} # Nodes buffer
        new_edges = {} # Edges buffer
        token_exceptions = [] # Exceptions buffer
        for e in elements:
            if "position" in e: 
                # New node and exception
                node_id = e["data"]["id"]
                new_nodes[node_id] = e
                token_exceptions.append(node_id)
            else:               
                # New edge and relation
                source_id = e["data"]["source"]
                target_id = e["data"]["target"]
                edge_id = f"{source_id}-{target_id}"
                new_edges[edge_id] = e
        
        # Replace fundamentals and buildinds
        self.nodes = new_nodes
        self.edges = new_edges
        self.tokens = build_tokens(TOKEN_LEN, token_exceptions)
        

    def to_cytoscape(self) -> List[Dict[str, str]]:
        return list(self.nodes.values()) + list(self.edges.values())
    
    def is_empty(self):
        if 16**TOKEN_LEN - 1 == len(self.tokens):
            return True
        return False     
    



############ Write and Save ############

def serialize_mapit(instance: Net) -> bytes:
    """Serialize and save an instance of NetMap to a .mapit file."""
    return pickle.dumps(instance)
    
def deserialize_mapit(data: bytes) -> Net:
    """Deserialize and load an instance of NetMap from a .mapit file."""
    return pickle.loads(data)
    
