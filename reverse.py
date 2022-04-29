# Comment it before submitting
class DoubleConnectedNode:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


def solution(node: DoubleConnectedNode) -> DoubleConnectedNode:
    """ Returns the new head of the reversed list. """
    curent_node = node
    next_node = node.next
    count = 0
    while curent_node:
        if not count:
            curent_node.prev = curent_node.next
            curent_node.next = None
            curent_node = next_node
        else:
            next_node = curent_node.next
            curent_node.next = curent_node.prev
            curent_node.prev = next_node
            if curent_node.prev is None:
                return curent_node
            curent_node = next_node
        count += 1


def test() -> None:
    """ Algorithm Verification. """
    node3 = DoubleConnectedNode("node3")
    node2 = DoubleConnectedNode("node2")
    node1 = DoubleConnectedNode("node1")
    node0 = DoubleConnectedNode("node0")

    node0.next = node1

    node1.prev = node0
    node1.next = node2

    node2.prev = node1
    node2.next = node3

    node3.prev = node2
    new_head = solution(node0)
    print(new_head.value)
    print(new_head.next.value)
    print(new_head.next.next.value)
    print(new_head.next.prev.value)

    print(new_head.next.next.next.value)
    print(new_head.next.next.prev.value)
    print(new_head.next.next.next.prev.value)
    # result is new_head == node3
    # node3.next == node2
    # node2.next == node1 node2.prev == node3
    # node1.next == node0 node1.prev == node2
    # node0.prev == node1


test()
