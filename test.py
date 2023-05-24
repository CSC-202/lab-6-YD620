import a_recursive_list as List
import b_recursive_stack as Stack

l = List.initialize()

l = List.addToFront(l, 0)
l = List.addAtIndex(l, 0, 1)
print(l.toPythonList())

v, l = Stack.pop(l)
print(v.value)
print(l.toPythonList())
