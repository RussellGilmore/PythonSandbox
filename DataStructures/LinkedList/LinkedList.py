class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next is not None:
                last_node = last_node.next
            last_node.next = new_node

    def print_list(self):
        head_node = self.head

        while head_node is not None:
            print(head_node.data)
            head_node = head_node.next

    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert_node_after(self, prev_node, data):
        if not prev_node:
            print("Not found")
            return
        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        cur_node = self.head
        if cur_node is not None and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return True
        else:
            prev = None
            while cur_node is not None and cur_node.data != key:
                prev = cur_node
                cur_node = cur_node.next
            prev.next = cur_node.next
            cur_node = None
            return True
        return False

    def delete_node_at_pos(self, pos):

        cur_node = self.head

        if pos == 0 and self.head is not None:
            self.head = cur_node.next
            cur_node = None
            return True
        if pos != 0 and self.head is not None:
            prev = None
            count = 0
            while cur_node is not None and count != pos:
                prev = cur_node
                cur_node = cur_node.next
                count += 1
            prev.next = cur_node.next
            cur_node = None
            return True

        return False

    def len_iterative(self):
        head_node = self.head
        count = 0
        while head_node is not None:
            count += 1
            head_node = head_node.next
        return count

    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)




llist = LinkedList()
llist.append("Dog")
llist.append("Cat")
llist.prepend("First")
# llist.insert_node_after(llist.head.next, "Inserted")
# llist.delete_node("Dog")
# llist.delete_node_at_pos(1)
print(llist.len_recursive(llist.head))

llist.print_list()
