class Node():
    def __init__(self, data, n=None):
        self.data = data
        self.n = n


class LinkedList():
    def __init__(self):
        self.head = None
    
    def insertAtB(self,value):
        #create a node with the info that they want to add
        #make new node point to current node, 
        node = Node(value,self.head)
        #set current node to the new node made
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
            print(node_curr.data, end="-->")
            #we are setting the current node to the next node
            node_curr = node_curr.n
    
    def removeElements(self,val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
        #none->->b->c->b->d
        #none -> a -> a -> none
        while self.head!=None and self.head.data==val:
            self.head=self.head.n
        
        curr_node = self.head
       
        while curr_node and  curr_node.n:
            if curr_node.n.data==val:
                curr_node.n= curr_node.n.n
            else:
                curr_node = curr_node.n

            
            
            
        
ll = LinkedList()

ll.insertValues([6,5,1,6,4,6,2,6])

ll.display()
print()
ll.removeElements(6)
ll.display()
print()
