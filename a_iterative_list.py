# a_linked_list.py - INSTRUCTOR USE ONLY
## author - nick s.

# class Node -> an internal node
class Node:
    # the value at this Node
    value: any

    # the next Node in the Linked List 
    next: any

    def __init__(self, value: any, next: any):
        self.value = value
        self.next = next


# class List -> contains nodes
class List:
    # the head of our Linked List
	## the first Node
    head: Node
	
    # initialize the data structure
    def __init__(self):
        self.head = None

    # returns the number of elements in the list
    def __len__(self) -> int:
        if self.head == None:
            return 0
        else:
            count = 0
            node = self.head
            while node.next != None:
                count += 1
                node = node.next
            return count
    
    def toPythonList(self) -> list:
        values = []
        node = self.head
        while node != None:
            values.append(node.value)
            node = node.next
        return values


# SOLUTIONS
# output: an empty list
def initialize() -> List:
    return List()


# input : a list
# output: true if the list is empty, false if the list is not
def isEmpty(list: List) -> bool:
    return list.head == None


# input : a list, an index position, a value to be inserted
# output: a modified list with a value inserted at the index
def addAtIndex(list: List, index: int, value) -> List:
    node: Node = list.head
    for i in range(n := len(list)):
        if i == (index - 1):
            new_node = Node(value, node.next)
            node.next = new_node
            return list
        node = node.next
    raise ValueError('invalid index!')


# input : a list, a value to be inserted
# output: a modified list with a value inserted at the front
def addToFront(list: List, value: int) -> List:
    if list.head is None:
        list.head = Node(value, None)
        return list
    else:
        new_node = Node(value, list.head)
        list.head = new_node
        return list


# input : a list, a value to be inserted
# output: a modified list with a value inserted at the back
def addToBack(list: List, value: int):
    if list.head is None:
        list.head = Node(value, None)
        return list
    else:
        node = list.head
        while node.next != None:
            node = node.next
        new_node = Node(value, None)
        node.next = new_node
        return list


# input : a list
# output: a list containing the first element of the input
def head(list: List) -> List:
    h: List = List()
    h.head = Node(list.head.value, None)
    return h


# input : a list
# output: a list containing the original list without the head
def tail(list: List) -> List:
    new_list: List = List()
    new_list.head = list.head.next
    return new_list


# input : a list
# output: an element from the specified index
def getElementAtIndex(list: List, index: int) -> Node:
    node: Node = list.head
    i: int = 0
    while node != None:
        i += 1
        if (i - 1) == index:
            return node
        node = node.next
    raise ValueError('invalid index!')


# input : a list
# output: an empty list
def clear(list: List) -> List:
    list.head = None
    return list

