from typing import Any


class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


def solution(node: Node, elem: Any) -> int:
    """ Returns the element's index by value. """
    index = 0
    while node:
        if node.value == elem:
            return index
        index += 1
        node = node.next_item
    return -1


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    idx = solution(node0, "node1")
    # result is idx == 2
    print(idx)


test()
