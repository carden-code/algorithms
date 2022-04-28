class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


def solution_2(node) -> None:
    """ Prints the objects of the linked list. """
    node = node
    print(node.value)
    while node.next_item:
        node = node.next_item
        print(node.value)


def solution(node, idx) -> Node:
    """ Removing by index from a linked list. """
    current_node = node
    count = 0
    while current_node is not None:
        if idx == 0:
            node = current_node.next_item
            return node
        if idx == count + 1:
            if current_node.next_item.next_item:
                current_node.next_item = current_node.next_item.next_item
            else:
                current_node.next_item = None
            return node
        count += 1
        current_node = current_node.next_item


node3 = Node("node3", None)
node2 = Node("node2", node3)
node1 = Node("node1", node2)
node0 = Node("node0", node1)
print(solution_2(solution(node0, 2)))
