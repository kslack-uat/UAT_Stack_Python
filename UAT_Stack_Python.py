

class StackNode:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
    def GetData(self):
        return self.data
    
    def GetNext(self,):
        return self.next
    
    def SetNext(self, next):
        self.next = next

    

class UAT_Stack:
    def __init__(self, top=None, size=0):
        self.top = top
        self.size = size
    
    def GetSize(self):
        return self.size
    
    def PushNode(self, push_node:StackNode):
        # Add a new node to the top of the stack
        if(self.top == None):
            self.top = push_node    # Stack is empty, so simply point top to the new node
        else:
            push_node.SetNext(top)      # Establish link between the old top node and the push_node (new node)
            self.top = push_node        # Change the node on the top of the stack
        
        self.size += 1


    def Peek(self):
        return self.top

