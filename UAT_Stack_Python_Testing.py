import UAT_Stack_Python

def NodeTesting():
    # Test Node Constructor
    new_node = UAT_Stack_Python.StackNode("node 1", None)
    # Verify Memory Address
    if(new_node != None):
        print("Success - Creating Node using constructor")
    else:
        print("FAIL - Creating Node using constructor - Should have returned memory address")

    # Test GetData function
    node_data = new_node.GetData()
    if(node_data == "node 1"):
        print("Success - Expected Node data retrieved.")
    else:
        print("FAIL - Expected data = node 1, Received=" + str(node_data))

    # Test GetNext function
    next_node = new_node.GetNext()
    if(next_node == None):
        print("Success - Next node object is set to None")
    else:
        print("FAIL - Next node object has a value that is not None")

    # Test SetNext function
    new_node.SetNext(new_node)
    if(new_node.GetNext() == new_node):
        print("Success - SetNext was used to set the next object variable to itself.")
    else:
        print("FAIL - SetNext does not function correctly revise the next_node variable.")



def StackTesting():
    # Stack Constructor Testing
    stack = UAT_Stack_Python.UAT_Stack()

    if(not(stack == None)):
        print("Success - Stack created with and references a memory address.")
    else:
        print("FAIL - Stack references None")
    

    # Test GetSize function
    if(stack.GetSize() == stack.size):
        print("Success - GetSize function reports the size value correctly.")
    else:
        print("FAIL - GetSize does not return the actual size of the stack.")

    # Continue the testing of the constructor
    initial_stack_size = stack.GetSize()
    if(initial_stack_size == 0):
        print("Success - Initial stack has a size of 0")
    else:
        print("FAIL - Stack size is not set to 0 as it should be for a new stack. Reported size=" + str(initial_stack_size))

    # Test Peek Function
    peek_stack = UAT_Stack_Python.UAT_Stack()
    peek_result = peek_stack.Peek()
    if(peek_result == None):
        print("Success - Peek returns None on an empty stack.")
    else:
        print("FAIL - Peek should have returned None. Instead it returned " + peek_result)


    # Test PushNode function
    push_node_stack = UAT_Stack_Python.UAT_Stack()
    node_to_push = UAT_Stack_Python.StackNode("first")
    push_node_stack.PushNode(node_to_push)

    pushnode_reported_size = push_node_stack.GetSize()
    if(pushnode_reported_size == 1):
        print("Success - Stack size is now 1.")
    else:
        print("FAIL - Stack size is not the expected size of 1. " + str(pushnode_reported_size))
    
    if(push_node_stack.Peek() == node_to_push):
        print("Success - Pushed Node is at the top of the stack.")
    else:
        print("FAIL - Newly created node is not found on the top of the stack. Instead, it found " + push_node_stack.Peek())


    # Test Push function
    push_stack = UAT_Stack_Python.UAT_Stack()
    push_stack.Push("First Value Pushed")
    top_push_stack = push_stack.Peek()
    if(top_push_stack.GetData() ==  "First Value Pushed"):
        print("Success - First Value Pushed is on the top of the stack.")
    else:
        print("FAIL - Newly created and pushed node is not at the top of the stack.")

    push_stack_size = push_stack.GetSize()
    if(push_stack_size == 1):
        print("Success - Stack is the correct size after Push function execution.")
    else:
        print("FAIL - Stack size is not correct following Push function execution. Expected 1, found " + str(push_stack_size))
    

    # Test Pop function
    pop_stack = UAT_Stack_Python.UAT_Stack()
    pop_stack.Push("first")
    pop_stack.Push("second")
    pop_stack.Push("third")
    pop1_node = pop_stack.Pop()
    if(pop1_node.GetData() == "third"):
        print("Success - Correct value popped off the stack.")
    else:
        print("FAIL - Incorrect value popped off the stack. Expected:third  Received:" + str(pop1_node.GetData()))
    if(pop_stack.GetSize() == 2):
        print("Success - After pop, stack is the correct size.")
    else:
        print("FAIL - After pop, incorrect size is reported. Expected: 2, Received:" + str(pop_stack.GetSize()))

    pop_stack.Pop()
    pop3_node = pop_stack.Pop()
    if(pop3_node.GetData() == "first"):
        print("Success - Correct value popped off the stack.")
    else:
        print("FAIL - Incorrect value popped off the stack. Expected:third  Received:" + str(pop3_node.GetData()))
    if(pop_stack.GetSize() == 0):
        print("Success - After pop, stack is the correct size.")
    else:
        print("FAIL - After pop, incorrect size is reported. Expected: 2, Received:" + str(pop_stack.GetSize()))
    

if __name__ == "__main__":
    NodeTesting()

    StackTesting()


