class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution():
    def __init__(self):
        self.head = None
    
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

    def insertValues(self, values):
        
        for i in range(len(values)-1,-1,-1):
            node = ListNode(values[i], self.head)
            self.head = node

    def length(self):
        curr_node = self.head
        length = 0

        while curr_node:
            length+=1
            curr_node = curr_node.next
        return length

    def getDecimalValue(self):
        length = self.length()
        decimal = 0
        current = self.head
        for i in range(length-1,-1,-1):
            if current.val ==0:
                temp = 0
            else:
                temp = 2**i

            decimal = decimal + temp
            current = current.next
        return decimal
    def getDecimalValue2(self):
        curr_node = self.head
        string = ""
        while curr_node:
            string+=str(curr_node.val)
            curr_node = curr_node.next
        return int(string,2)






ll = Solution()

ll.insertValues([1,0,1,1])
print(ll.getDecimalValue())
print(ll.getDecimalValue2())
ll.display()