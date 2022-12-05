class Node:
  def __init__(self, val = 0, next = None):
    self.val = val
    self.next = next

class LinkedList:
  def __init__(self, head = None):
    self.head = head

  # PRINTS ENTIRE LINKED LIST
  def printList(self):
    curr = self.head
    res = ""
    
    while curr:
      res += str(curr.val) + " --> "
      curr = curr.next
    
    print("\nPRINTING LINKED LIST")
    print(res + "NULL")

  # ADDS A NODE TO THE TAIL OF THE LINKED LIST - O(N)
  def addNodeTail(self, node):
    curr = self.head
    
    if not curr:
      self.head = node
      return

    while curr.next:
      curr = curr.next
    curr.next = node

  # ADDS A NODE TO THE HEAD OF THE LINKED LIST - O(1)
  def addNodeHead(self, node):
    curr = self.head
    node.next = curr
    self.head = node

  # SEARCH FOR A NODE BY VALUE - O(N)
  def searchNodeByVal(self, val):
    curr = self.head

    while curr:
      if curr.val == val:
        print(f'\nVALUE FOUND: {curr.val}')
        return curr
      curr = curr.next
    
    print(f'\nVALUE ({val}) NOT FOUND IN LIST')
    return None

  # DELETE A NODE BY VALUE - O(N)
  def deleteNodeByVal(self, val):
    curr = self.head
    prev = None

    if curr.val == val:
      self.head = curr.next
      print(f'\nNODE ({curr.val}) SUCCESFULLY DELETED')
      del curr
      return

    while curr:
      if curr.val == val:
        prev.next = curr.next
        print(f'\nNODE ({curr.val}) SUCCESFULLY DELETED')
        del curr
        return
      prev = curr
      curr = curr.next

    print(f'\nNODE TO BE DELETED ({val}) WAS NOT FOUND')

linkedList = LinkedList()
count = 0

for _ in range(5):
  linkedList.addNodeTail(Node(val=count))
  count += 10

linkedList.printList()

linkedList.addNodeHead(Node(val=-10))
linkedList.printList()

node = linkedList.searchNodeByVal(30)
node.val = 35
linkedList.printList()

linkedList.deleteNodeByVal(35)
linkedList.deleteNodeByVal(0)
linkedList.printList()