

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
    def __init__():
        pass


if __name__ == "__main__":
    new_node = StackNode("node 1", None)
    print(new_node)
    print(new_node.GetData())
    print(new_node.GetNext())
    new_node.SetNext(new_node)
    print(new_node.GetNext())