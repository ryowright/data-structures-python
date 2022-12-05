class Stack:
  def __init__(self):
    self.stack = []

  def printStack(self):
    print(f'\n{self.stack}')

  def push(self, val):
    self.stack.append(val)

  def pop(self):
    if len(self.stack) == 0:
      print("\nStack is empty")
      return None

    return self.stack.pop()

  def peek(self):
    if len(self.stack) == 0:
      print("\nStack is empty")
      return None

    return self.stack[-1]

stack = Stack()
count = 10

for _ in range(5):
  stack.push(count)
  count += 10

stack.printStack()
print(f'\n{stack.peek()}')
print(f'\n{stack.pop()}')
print(f'\n{stack.peek()}')
stack.printStack()