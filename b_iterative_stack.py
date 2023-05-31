# b_stack.py - INSTRUCTOR USE ONLY
## author - nick s.

# type Node -> an internal, dynamic node
## contains a value for the stack and a next pointer
class Node:
    value: any
    next: any

    def __init__(self, value: any, next: any):
        self.value = value
        self.next = next


# type Sack -> a dynamic, linear, FILO data structure
## contains a value and a next pointer
class Stack:
    head: Node
    
    # initializer
    def __init__(self):
        self.head = None

    # returns the number of values in the stack
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
        while node is not None:
            values.append(node.value)
            node = node.next
        return values


# SOLUTIONS1
# output: an empty stack
def initialize() -> Stack:
    return Stack()


# input : a stack
# output: true if the stack is empty, false if the stack is not
def isEmpty(stack: Stack) -> bool:
    return stack.head == None


# input : a stack, a value to be inserted
# output: a modified stack with a value inserted at the front
def push(stack: Stack, value: int) -> Stack:
    new_node = Node(value, None)
    if stack.head is None:
        stack.head = new_node
        return stack

    old = stack.head
    stack.head = new_node
    new_node.next = old
    return stack


# input : a stack
# output: the front of an unmodified stack
def peek(stack: Stack) -> int:
    return stack.head.value


# input : a stack
# output: the front of a stack without the top
def pop(stack: Stack) -> tuple[int, Stack]:
    top = stack.head
    stack.head = top.next
    return top.value, stack


# input : a list
# output: an empty list
def clear(stack: Stack) -> Stack:
    stack.head = None
    return stack

