# Class: NetMap
## Methods
    
    --- Node methods ---
    - add_node(self):
        Create new node with a local_id from id_stacks[PARENT_ID] deque. This node have no edges.

    - del_node(self, local_id: str)
        Delete node from context and return local_id to stack

    - select_node(self, local_id: str)
        Select node into context and set it as self.selection.

    - deselect_node()
        Delete selection from self.selection and set it as None.

    - 

    --- Edge methods ---

    --- Context methods ---
    - build_context(self, )
        Create new context. 
    - to_parent()
    - to_child()
    