# UNDIRECTED, UNWEIGHTED GRAPH
class Graph:
  def __init__(self):
    self.adjList = {}

  # GETS ALL THE VERTICES IN THE GRAPH
  def getVertices(self):
    return self.adjList.keys()

  # ADDS A VERTEX TO THE GRAPH
  def addVertex(self, v):
    if v not in self.adjList:
      self.adjList[v] = set()

  # ADDS AN EDGE BETWEEN TWO VERTICES
  def addEdge(self, v1, v2):
    if v1 in self.adjList and v2 in self.adjList:
      self.adjList[v1].add(v2)

  # REMOVES A VERTEX FROM THE GRAPH
  def removeVertex(self, v):
    if v in self.adjList:
      del self.adjList[v]

  # REMOVES THE EDGE BETWEEN TWO VERTICES
  def removeEdge(self, v1, v2):
    if v1 in self.adjList and v2 in self.adjList:
      if v2 in self.adjList:
        self.adjList[v1].remove(v2)

  # CHECKS FOR ADJACENCY BETWEEN TWO VERTICES
  def checkAdjacency(self, v1, v2):
    if v1 in self.adjList and v2 in self.adjList:
      if v2 in self.adjList[v1]:
        return True
      return False
    
    print("\nOne or more vertices do not exist")
    return False