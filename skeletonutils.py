import pymel.core as pmc

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
    j = pmc.joint(name=prefix + rootnode.name())
    # Copy the transform and rotation.
    j.translate.set(rootnode.translate.get())
    j.rotate.set(rootnode.rotate.get())
    # Set the parent to rootnode's parent if parent is None,
    # Otherwise set it to _parent.
    if parent is None:
        parent = rootnode.getParent()
    j.setParent(parent)
    # Convert all the children recursively, using the newly
    # created joint as the parent.
    for child in rootnode.children():
        convert_to_skeleton(child, prefix, j)
    return j

