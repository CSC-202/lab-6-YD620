class Node:
    value: any
    next: any

    def __init__(self, value, next):
        self.value = value
        self.next = next


class Stack:
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


def initialize() -> Stack:
    raise NotImplementedError("Stack.initialize() not defined")


def isEmpty(data: Stack) -> bool:
    raise NotImplementedError("Stack.isEmpty() not defined")


def push(data: Stack, value: int) -> Stack:
    raise NotImplementedError("Stack.push() not defined")


def pop(data: Stack) -> tuple[Node, Stack]:
    raise NotImplementedError("Stack.pop() not defined")


def peek(data: Stack) -> Node:
    raise NotImplementedError("Stack.peek() not defined")


def clear(data: Stack) -> Stack:
    raise NotImplementedError("Stack.clear() not defined")
