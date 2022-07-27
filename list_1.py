class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f"{self.data} - {self.next}"


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        return str(self.head)

    def length(self):
        count = 0
        temp = self.head

        while temp:
            count += 1
            temp = temp.next

        return count


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse_list(self, head: ListNode) -> ListNode:
        if not head:
            return head

        temp = head
        tail = ListNode(val=head.val)
        while temp.next:
            temp = temp.next
            tail = ListNode(val=temp.val, next=tail)
        return tail


if __name__ == '__main__':
    linked_list = LinkedList()
    temp = Node(1)
    linked_list.head = temp

    for i in range(2, 5):
        temp.next = Node(i)
        temp = temp.next


    print(linked_list)
    print(linked_list.length())

