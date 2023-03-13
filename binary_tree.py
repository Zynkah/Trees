def binary_tree(r):
    # Constructs a list with a root node and two empty sublists for the children.
    return [r, [], []]


def insert_left(root, new_branch):
    # To add a left subtree to the root of the tree, we insert a new list into the second position of the root list.
    t = root.pop(1)
    # If the list already has something in the second position, we need to keep track of it and push it down the tree as the left child of the list we are adding.
    if len(t) > 1:
        root.insert(1, [new_branch, t, []])  # splice a new node into the tree
    else:
        root.insert(1, [new_branch, [], []])
    return root


def insert_right(root, new_branch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [new_branch, [], t])
    else:
        root.insert(2, [new_branch, [], []])
    return root


def get_root_val(root):
    return root[0]


def set_root_val(root, new_val):
    root[0] = new_val


def get_left_child(root):
    return root[1]


def get_right_child(root):
    return root[2]


r = binary_tree(3)
insert_left(r, 4)
insert_left(r, 5)
insert_right(r, 6)
insert_right(r, 7)
l = get_left_child(r)
print(l) # [5, [4, [], []], []]

set_root_val(l, 9)
print(r) # [3, [9, [4, [], []], []], [7, [], [6, [], []]]]
insert_left(l, 11)
print(r) # [3, [9, [11, [4, [], []], []], []], [7, [], [6, [], []]]]
print(get_right_child(get_right_child(r))) # [6, [], []]
