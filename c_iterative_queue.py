# c_queue.py - INSTRUCTOR USE ONLY
## author - nick s.

# type Node -> an internal node
class Node:
    # the value in our data structure
    ## we're using integers
    value: any

    # the pointer to the next Node
    next: any

    # initialization of the data structure
    def __init__(self, value, next):
        self.value = value
        self.next = next


# type Queue -> contains nodes
class Queue:
    # the first element of the queue
    front: Node

    # initialization of the data structure
    def __init__(self):
        self.front = None

    # length of the queue returns how many elements there are
    def __len__(self) -> int:
        if self.front == None:
            return 0
        else:
            count: int = 0
            node: Node = self.front
            while node.next != None:
                count += 1
            return count

    def toPythonList(self) -> list:
        values = []
        node = self.front
        while node is not None:
            values.append(node.value)
            node = node.next
        return values


# SOLUTIONS
# output: an empty queue
def initialize() -> Queue:
    return Queue()


# input : a queue
# output: true if the queue is empty, false if the queue is not
def isEmpty(queue) -> bool:
    return queue.front == None


# input : a queue, a value to be inserted
# output: a modified queue with a value inserted at the back
def enqueue(queue, value) -> Queue:
    new_node: Node = Node(value, None)
    if queue.front is None:
        queue.front = new_node
    else:
        node: Node = queue.front
        while node.next is not None:
            node = node.next
        node.next = new_node
    return queue


# input : a queue
# output: the front of an unmodified queue
def peek(queue) -> int:
    return queue.front.value


# input : a queue
# output: the front of a queue without the top
def dequeue(queue) -> tuple[int, Queue]:
    if isEmpty(queue):
        return None, None
    else:
        front: Node = queue.front
        queue.front = front.next
        return front.value, queue


# input : a queue
# output: an empty queue
def clear(queue) -> Queue:
    queue.front = None
    return queue

