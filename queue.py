class Node:
  def __init__(self, val = 0):
    self.val = val
    self.next = None
    self.prev = None

class Queue:
  def __init__(self):
    self.tail = None
    self.head = None

  def printQueue(self):
    print("\nPRINTING QUEUE...")
    curr = self.tail
    res = ""

    if not curr:
      print("Queue is empty")
      return

    while curr.next:
      res += str(curr.val) + " <--> "
      curr = curr.next
    res += str(curr.val)

    print(f'{res}')

  def enqueue(self, node):
    print(f'\nENQUEUEING: {node.val}')
    # Queue has no items
    if not self.tail:
      self.tail = node
      self.head = node
      return
    
    tail = self.tail
    node.next = tail
    tail.prev = node
    self.tail = node

  def dequeue(self):
    print(f'\nDEQUEUEING...')
    # Queue has no items
    if not self.head:
      print("Queue is empty")
      return

    head = self.head
    prev = head.prev

    # Queue has one item
    if prev is None:
      self.tail = None
      self.head = None
      return head

    prev.next = None
    head.prev = None
    self.head = prev
    return head

  def search(self, val):
    curr = self.tail

    while curr:
      if curr.val == val:
        print(f'\nValue ({curr.val}) found')
        return curr.val
      curr = curr.next

    print(f'\nValue ({val}) not found')
    return None

queue = Queue()

for i in range(1, 6):
  queue.enqueue(Node(val=i))

queue.printQueue()
queue.enqueue(Node(6))

queue.search(3)
queue.search(10)

for _ in range(6):
  queue.dequeue()
  queue.printQueue()
