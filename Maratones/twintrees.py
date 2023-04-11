def create_node(value, secondary=False):
    """
    Creates a new node for the twin trees with the given value.
    Returns the new node.
    """
    return {'value': value, 'left': None, 'right': None, 'secondary': secondary}

def insert_node_primary(root, value):
    """
    Inserts a node with the given value into the primary twin tree.
    """
    if root is None:
        return create_node(value)

    if value < root['value']:
        root['left'] = insert_node_primary(root['left'], value)
    else:
        root['right'] = insert_node_primary(root['right'], value)

    return root

def insert_node_secondary(root, value):
    """
    Inserts a node with the given value into the secondary twin tree.
    """
    if root is None:
        return create_node(value, secondary=True)

    if value > root['value']:
        root['left'] = insert_node_secondary(root['left'], value)
    else:
        root['right'] = insert_node_secondary(root['right'], value)

    return root


def create_twin_trees(arr):
    """
    Creates two twin trees from the given array.
    Returns a dictionary containing the root nodes of both trees.
    """
    if not arr:
        return {'root_primary': None, 'root_secondary': None}

    # Sort the array to create the primary tree
    arr.sort()
    root_primary = create_node(arr[0])
    for value in arr[1:]:
        insert_node_primary(root_primary, value)

    # Create the secondary tree by reversing the order of the array
    arr.reverse()
    root_secondary = create_node(arr[0])
    for value in arr[1:]:
        insert_node_secondary(root_secondary, value)

    return {'root_primary': root_primary, 'root_secondary': root_secondary}
print(create_twin_trees([4,6,9,2,1,3,5,8]))