class Edge:
    def __init__(self, fNode, sNode, weight):
        self.firstNode = fNode
        self.secondNode = sNode
        self.weight = weight

    def w(self):
        return self.weight

    def __repr__(self):
        return "<E "+str(self.firstNode) + " " + str(self.secondNode) + " " +str(self.weight)+" >"



class OptimizeEdge:
    def __init__(self, fNode, sNode):
        self.firstNode = fNode
        self.secondNode = sNode


    def __repr__(self):
        return "<E "+str(self.firstNode) + " " + str(self.secondNode) +" >"

