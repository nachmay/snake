
class Node:

    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

node3 = Node(3)
node2 = Node(2, node3)
node1 = Node(1, node2)
node_a = Node("a", Node("b", Node("c")))

def zipper(head1, head2):
    if head2.next == None:
        return
    s1 = head1.next
    s2 = head2.next
    head1.next = head2
    head2.next = s1
    return zipper(s1, s2)

zipper(node1, node_a)
print(node1.next.next.next.next.next)
print("A", ["A"], "AB", ["A", "B"])