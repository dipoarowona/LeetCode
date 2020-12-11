class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution():
    def merge2lists(self, l1, l2):
        curr1 = l1
        curr2 = l2
        l3 = ListNode(None)
        temp = l3
        curr3 = l3
        count = 0
        while curr1 or curr2:
            if not curr2:
                curr3.next = curr1
                curr3 = curr3.next
                curr1 = curr1.next
            elif not curr1:
                curr3.next = curr2
                curr3 = curr3.next
                curr2 = curr2.next
            elif curr1.val <= curr2.val:
                curr3.next = curr1
                curr3 = curr3.next
                curr1 = curr1.next
            else:
                curr3.next = curr2
                curr3 = curr3.next
                curr2 = curr2.next

        l3 = temp.next
        return l3

    def merge2lists2(self, l1, l2):
        l3 = ListNode(None)
        temp = l3
        while l1 and l2:
            if l1.val <= l2.val:
                l3.next = l1
                l1 = l1.next
            else:
                l3.next = l2
                l2 = l2.next
            l3 = l3.next
        if not l1:
            remain = l2
        else:
            remain = l1
        while remain:
            l3.next = remain
            remain = remain.next
            l3 = l3.next

        l3 = temp.next
        return l3
