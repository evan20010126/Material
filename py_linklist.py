class NodeIter:
    def __init__(self, node) -> None:
        self.curr_node = node
    
    def __next__(self):
        if self.curr_node is None:
            raise StopIteration
        
        node, self.curr_node = self.curr_node, self.curr_node.next
        return node
    
    def __iter__(self):
        return self

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None
    
    def __iter__(self) -> NodeIter:
        return NodeIter(self)
    

if (__name__ == "__main__"):
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)

    # node1.next = node2
    # node2.next = node3

    node1.next = Node(5)
    node1.next.next = Node(6)
    
    for node in node1:
        print(node.val)

