class Node:
    def __init__(self, val = None, children = None):
        self.val = val
        self.children = children

    def __eq__(self, other):
        c1 = self
        c2 = other

        while c1 is not None and c2 is not None:
            if c1.val != c2.val:
                return False
            c1 = c1.children
            c2 = c2.children

        if c1 is None and c2 is None:
            return True

        return False

    def __hash__(self):
        return id(self)
