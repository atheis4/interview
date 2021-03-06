class Node:

    def __init__(self, value):
        self.value = value

    @property
    def val(self):
        return self.value

    @property
    def data(self):
        return self.value


class ListNode(Node):

    def __init__(self, value, next_node=None, prev_node=None):
        super().__init__(value)
        self.next_node = next_node
        self.prev_node = prev_node

    @property
    def next(self):
        return self.next_node

    @property
    def prev(self):
        return self.prev_node


class TreeNode(Node):

    def __init__(
            self,
            value,
            parent_node=None,
            left_node=None,
            right_node=None,
            children=None
    ):
        super().__init__(value)
        self.parent_node = parent_node
        self.left_node = left_node
        self.right_node = right_node
        self.children = children

    @property
    def parent(self):
        return self.parent

    @parent.setter
    def parent(self, value):
        self.parent_node = value

    @property
    def left(self):
        return self.left_node

    @left.setter
    def left(self, value):
        self.left_node = value

    @property
    def right(self):
        return self.right_node

    @right.setter
    def right(self, value):
        self.right_node = value

    def add_child(self, node):
        self.children.append(node)
