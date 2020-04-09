class Node:
   def __init__(self, data):
      self.data = data
      self.next = None
      self.prev = None

class SLinkedList:
    def __init__(self):
        self.headval = None
    def AtBegining(self,newdata):
        NewNode = Node(newdata)        
    # Update the new nodes next val to existing node
        NewNode.next = self.headval
        self.headval = NewNode
    # Function to add newnode
    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        laste = self.headval
        while(laste.next):
            laste = laste.next
        laste.next=NewNode
    # Function to add node
    def Inbetween(self,middle_node,newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return

        NewNode = Node(newdata)
        NewNode.next = middle_node.next
        middle_node.next = NewNode
    # Function to remove node
    def RemoveNode(self, Removekey):

        HeadVal = self.headval

        if (HeadVal is not None):
            if (HeadVal.data == Removekey):
                self.headval = HeadVal.next
                HeadVal = None
                return

        while (HeadVal is not None):
            if HeadVal.data == Removekey:
                break
            prev = HeadVal
            HeadVal = HeadVal.next

        if (HeadVal == None):
            return

        prev.next = HeadVal.next

        HeadVal = None
    # Print the linked list
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.data)
            printval = printval.next

# Create the doubly linked list
class doubly_linked_list:

   def __init__(self):
      self.head = None

# Define the push method to add elements		
   def push(self, NewVal):

      NewNode = Node(NewVal)
      NewNode.next = self.head
      if self.head is not None:
         self.head.prev = NewNode
      self.head = NewNode

# Define the insert method to insert the element		
   def insert(self, prev_node, NewVal):
      if prev_node is None:
         return
      NewNode = Node(NewVal)
      NewNode.next = prev_node.next
      prev_node.next = NewNode
      NewNode.prev = prev_node
      if NewNode.next is not None:
         NewNode.next.prev = NewNode
# Define the append method to add elements at the end
   def append(self, NewVal):

      NewNode = Node(NewVal)
      NewNode.next = None
      if self.head is None:
         NewNode.prev = None
         self.head = NewNode
         return
      last = self.head
      while (last.next is not None):
         last = last.next
      last.next = NewNode
      NewNode.prev = last
      return

# Define the method to print the linked list 
   def listprint(self, node):
      while (node is not None):
         print(node.data),
         last = node
         node = node.next