class MinHeap:
  def __init__(self):
    self.heap = []

  # HELPER FUNCTIONS
  def getLeftChildIndex(self, i): return (2 * i) + 1
  def getRightChildIndex(self, i): return (2 * i) + 2
  def getParentIndex(self, i): return (i - 1) // 2

  def hasLeftChild(self, i): return self.getLeftChildIndex(i) < len(self.heap)
  def hasRightChild(self, i): return self.getRightChildIndex(i) < len(self.heap)
  def hasParent(self, i): return self.getParentIndex(i) >= 0

  def getLeftChild(self, i): return self.heap[self.getLeftChildIndex(i)]
  def getRightChild(self, i): return self.heap[self.getRightChildIndex(i)] 
  def getParent(self, i): return self.heap[self.getParentIndex(i)]

  def swap(self, i, j):
    self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

  # MAIN FUNCTIONS
  # Prints the heap
  def printHeap(self):
    print(f'\n{self.heap}')

  # Used when inserting an element
  def heapifyUp(self):
    currIndex = len(self.heap) - 1
    while self.hasParent(currIndex) and self.getParent(currIndex) > self.heap[currIndex]:
      self.swap(self.getParentIndex(currIndex), currIndex)
      currIndex = self.getParentIndex(currIndex)

  # Used when removing the root element
  def heapifyDown(self, i):
    currIndex = i

    if self.hasLeftChild(currIndex) and self.getLeftChild(currIndex) < self.heap[currIndex]:
      currIndex = self.getLeftChildIndex(i)

    if self.hasRightChild(currIndex) and self.getRightChild(currIndex) < self.heap[currIndex]:
      currIndex = self.getRightChildIndex(i)

    if currIndex != i:
      self.swap(currIndex, i)
      self.heapifyDown(currIndex)

  # Inserts an element into the heap
  def insert(self, val):
    self.heap.append(val)
    self.heapifyUp()

  # Gets the smallest element in the heap
  def getMin(self):
    return self.heap[0]

  # Gets and removes the smallest element in the heap
  def removeMin(self):
    if len(self.heap) == 0:
      raise Exception("Cannot remove from an empty heap")
    
    val = self.heap[0]
    self.heap[0] = self.heap[len(self.heap) - 1]
    self.heap.pop()
    self.heapifyDown(0)
    return val

minHeap = MinHeap()
count = 50

for _ in range(5):
  minHeap.insert(count)
  count -= 10
minHeap.printHeap()

minHeap.insert(15)
minHeap.printHeap()

minHeap.insert(5)
minHeap.printHeap()

minHeap.removeMin()
minHeap.printHeap()