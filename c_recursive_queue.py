class Node:
    value: any
    next: any

    def __init__(self, value, next):
        self.value = value
        self.next = next


class Queue:
    first: Node
    last: Node

    def __init__(self):
        self.first = None
        self.last = None

    def __len__(self):
        n: int = 0
        current = self.first
        while current != None:
            n += 1
            current = current.next
        return n

    def toPythonList(self):
        result: list = []
        current = self.first
        while current != None:
            result.append(current.value)
            current = current.next
        return result


def initialize() -> Queue:
    return Queue()

def isEmpty(data: Queue) -> bool:
    return data.first == None


def enqueue(data: Queue, value: int) -> Queue:
    def helper(v:Node):
        if v.next == None:
            last_node = Node(value, None)
            v.next = last_node
        else:
            v = v.next
            helper(v)
    if data.first is None:
        data.first = Node(value,None)
        return data
    else:
        helper(data.first)
        return data

def dequeue(data: Queue) -> tuple[Node, Queue]:
    def helper(v:Node, i:int):
        if i == 0:
            node = v.next
            data.first = node
        elif v is None:
            raise IndexError ("Oops")
        else:
            helper(v.next, i)
    if isEmpty(data):
        raise IndexError ("Cannot Remove")
    else:
        helper(data.first, i=0)
        return data.first, data


def peek(data: Queue) -> Node:
    return data.first.value

    

def clear(data: Queue) -> Queue:
    data.first == None
    return data
