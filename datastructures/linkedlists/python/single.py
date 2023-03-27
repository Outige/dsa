class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.head is None:
            return '[] ->'
        else:
            output = ''
            node = self.head
            while node is not None:
                output += f'[{node.value}] -> '
                node = node.next
            return output

    def append(self, node_to_append):
        if self.head is None:
            self.head = node_to_append
        else:        
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = node_to_append
    
    def remove(self, node_to_remove):
        if node_to_remove == self.head:
            self.head = self.head.next
        else:
            node = self.head
            while node is not None:
                if node.next == node_to_remove:
                    node.next = node_to_remove.next
                    node_to_remove.next = None
                    break
    

if __name__ == '__main__':
    l = LinkedList()
    l.append(Node(1))
    node_to_remove = Node(2)
    l.append(node_to_remove)
    l.append(Node(3))
    l.remove(node_to_remove)
    print(l)
