class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def addTwoNumbers(l1, l2):  
    prev = ListNode()
    x = prev
    carryOver = 0
    
    while l1 or l2:
        if l1 and l2:
            add = l1.val+l2.val+carryOver if l1.val+l2.val+carryOver<10 else l1.val+l2.val+carryOver-10
            carryOver = 0 if l1.val+l2.val+carryOver<10 else 1

            l1 = l1.next
            l2 = l2.next
        elif l1:
            add = l1.val+carryOver if l1.val+carryOver<10 else l1.val+carryOver-10
            carryOver = 0 if l1.val+carryOver<10 else 1
            
            l1 = l1.next
        elif l2:
            add = l2.val+carryOver if l2.val+carryOver<10 else l2.val+carryOver-10
            carryOver = 0 if l2.val+carryOver<10 else 1

            l2 = l2.next
        
        result = ListNode(add)
        prev.next = result
        prev = result
                    
    if carryOver:
        result = ListNode(carryOver)
        prev.next = result
        prev = result
        
    return x.next