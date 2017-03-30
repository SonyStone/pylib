import pymel.core as pmc

GREEN = 14
BLUE = 6
YELLOW = 17

def safe_setparent(node, parent):
    """'node,setParent(parent)' if 'parent' is
    not the same as 'node''s existing parent.
    """
    if node.getParent() != parent:
        node.setParent(parent)

def convertto_joint(node, parent, prefix):
    j = pmc.joint(name=prefix + node.name())
    safe_setparent(j, parent)
    j.translate.set(node.translate.get())
    j.rotate.set(node.rotate.get())
    def calc_wirecolor():
        x = j.translateX.get()
        if x < 0.001:
            return GREEN
        elif x > 0.001:
            return BLUE
        else:
            return YELLOW
    j.overrideColor.set(calc_wirecolor())
    return j

def convert_to_skeleton(rootnode, prefix='skel_', parent=None):
    """Converts a hierarchy of nodes into joints that have the
    same transform, with their name prefixed with 'prefix'.
    Return the newly created root node.
    The new hierarchy will share the same parent as rootnode.

    :param rootnode: The root PyNode.
        Everything inder it will be converted.
    :param prefix: String to prefix newly created nodes with.
    """
    # Create a joint from the given node with the new name.
    # Copy the transform and rotation.
    # Set the parent to rootnode's parent if parent is None,
    # Otherwise set it to _parent.
    # Convert all the children recursively, using the newly
    # created joint as the parent.

    if parent is None:
        _parent = rootnode.getParent()
    j = convertto_joint(rootnode, _parent, prefix)
    for child in rootnode.children():
        convert_to_skeleton(child, prefix, j)
    return j

def ancestors(node):
    """Return a lost of ancestors, starting with the direct parent
    and ending with the top-level (root) parent."""
    result = []
    parent = node.getParent()
    while parent is not None:
        result.append(parent)
        parent = parent.getParent()
    return result

def uniqueroot(nodes):
    """Returns a list of the nodes in 'nodes' that are not
    children of any node in 'nodes'."""
    result = []
    def handle_node(n):
        """If any of the ancestors of n are in realroots,
        just return, otherwise, append n to realroots.
        """
        for ancestor in ancestors(n):
            if ancestor in nodes:
                return result.append(n)
    for node in nodes:
        handle_node(node)
    return result
