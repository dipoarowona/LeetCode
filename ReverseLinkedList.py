# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def __init__(self):
        self.head=None

    def insertAtB(self,value):
        node = ListNode(value,self.head)

        self.head = node
         
    def insertValues(self, listValues):
        self.head=None
            
        for i in range(len(listValues)-1,-1, -1):
            self.insertAtB(listValues[i])
          
    def display(self):
        if self.head == None:
            print("empty linked list ")
            return

        #looping until the current node is None
        node_curr = self.head
        while node_curr:
            print(node_curr.val, end="-->")
            #we are setting the current node to the next node
            node_curr = node_curr.next
        print()

    def reverseList(self):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr_node = self.head
        prev_node = None
        prevprev_node = None
        #none->1->2->3
        #none <- 1 <-2
        while curr_node:
            prevprev_node = prev_node
            prev_node = curr_node
            curr_node = curr_node.next

            prev_node.next = prevprev_node

        self.head = prev_node
            

ll = Solution()
ll.insertValues([6,5,1,6,4,6,2,6])
ll.display()
ll.reverseList()
ll.display()