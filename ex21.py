class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
        self.visited = set()

    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)

    def checkRoute(self, startNode, endNode):
        self.visited.add(startNode)
        if startNode not in self.gdict.keys():
            return False
        for k in self.gdict[startNode]:
            if k == endNode:
                return True
            if k not in self.visited:
                if self.checkRoute(k, endNode):
                    return True
        return False


obj = {
    "a": ["c", "d", "b"],
    "b": ["j"],
    "c": ["g"],
    "d": [],
    "e": ["f", "a"],
    "f": ["i"],
    "g": ["d", "h"],
    "h": [],
    "i": [],
    "j": [],
}


g = Graph(obj)
print(g.checkRoute("e", "h"))
