class Node:
    def _init_(self, data):
        self.data = data
        self.next = None
class Linkedlist:
    def _init_(self):
        self.head = None

    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    def push(self, new_data):
        new_node = Node(new_data)

        if self.head.data is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insertAfter(self, prev_node, new_data):
        new_node = Node(new_data)
        if self.head.data is None:
            self.head = new_node

        elif prev_node is None:
            print("Previous node must exist in linked list")
            return


        else:
            new_node = Node(new_data)
            
            new_node.next = prev_node.next
            prev_node.next = new_node

if __name__=='__main__':
    llist = Linkedlist()

    llist.head = Node(4)
    second = Node(7)
    third = Node(88)

    llist.head.next = second
    second.next = third

    llist.push(77)

    llist.insertAfter(77, 98)

    llist.printlist()