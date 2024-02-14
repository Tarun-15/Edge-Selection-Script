import maya.cmds as cmds

def select_alternate_edges():
    # Get selected edges
    selected_edges = cmds.ls(selection=True, flatten=True)
    if not selected_edges:
        cmds.warning("Please select some edges.")
        return
    
    # Deselect all edges
    cmds.select(clear=True)
    
    # Select alternate edges
    for i, edge in enumerate(selected_edges):
        if i % 2 == 0:
            cmds.select(edge, add=True)

# Run the function
select_alternate_edges()
