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


if __name__ == "__main__":
    NodeTesting()


