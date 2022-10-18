class LinkList:
    # write your __init__ method here that should store a 'head' value which the first Node in the LinkedList and a 'length' value which is the total number of Nodes in the LinkedList
    def __init__(self):
        self.head = None

    def add(self, data):
        # write your code to ADD an element to the Linked List
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def remove(self, data):
        # write your code to REMOVE an element from the Linked List
        head_val = self.head
        if head_val is not None:
            if head_val.val == data:
                self.head = head_val.next
                head_val = None
                return
        while head_val is not None:
            if head_val.val == data:
                break
            prev = head_val
            head_val = head_val.next

        if head_val == None:
            return

        prev.next = head_val.next
        head_val = None

    def get(self, element_to_get):
        # write you code to GET and return an element from the Linked List
        head_val = self.head
        while head_val is not None:
            if head_val.val == element_to_get:
                return head_val
            head_val = head_val.next


# ----- Node ------
class Node:
    # store your DATA and NEXT values here
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


l = LinkList()
l.add(1)
l.add(2)
l.add(3)
l.add(4)
l.add(5)
print(l.get(3).val)
