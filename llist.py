
class LList(object):
    __slots__ = ['value', 'next_node']

    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def insert(self, value):
        new_node = LList(value)

        if not self.next_node:
            self.next_node = new_node
            return True

        next_node = self.next_node
        prev_node = self

        while next_node:
            if next_node.value > value:
                new_node.next_node = next_node
                prev_node.next_node = new_node
                return True
            prev_node = next_node
            next_node = next_node.next_node

        prev_node.next_node = new_node
        return True

    def find(self, value):
        next_node = self.next_node
        while next_node:
            if next_node.value == value:
                return True
            next_node = next_node.next_node
        return False

    def delete(self, value):
        current_node = self
        prev_node = self
        while current_node.next_node:
            if current_node.value == value:
                prev_node.next_node = current_node.next_node
                return True
            prev_node = current_node
            current_node = current_node.next_node
        return False

    def __repr__(self):
        res = str(self.value)
        next_node = self.next_node
        while next_node:
            res += ' -> ' + str(next_node.value)
            next_node = next_node.next_node
        return res


if __name__ == '__main__':
    head = LList(1)
    head.insert(2)
    head.insert(5)
    head.insert(3)
    head.insert(4)

    print(head)

    head.delete(3)

    print(head)
