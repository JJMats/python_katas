class Node(object):
    def __init__(self, val):
        self.value = val
        self.left_child = None
        self.right_child = None

class BinaryTree(object):
    def __init__(self, r):
        return [r, [], []]

    def insert_left(self, root, new_branch):
        t = root.pop(1)
        if len(t) > 1:
            root.insert(1, [new_branch, t, []])
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

r = BinaryTree(3)