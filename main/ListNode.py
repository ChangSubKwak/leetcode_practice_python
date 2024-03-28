class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        c1 = self
        c2 = other

        while c1 is not None and c2 is not None:
            if c1.val != c2.val:
                return False
            c1 = c1.next
            c2 = c2.next

        if c1 is None and c2 is None:
            return True

        return False

    def __hash__(self):
        return id(self)

    @classmethod
    def from_list(cls, input_list):
        if not input_list:
            return None

        root = cls(input_list[0])
        current = root
        for value in input_list[1:]:
            current.next = cls(value)
            current = current.next

        return root
