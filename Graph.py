import  Edge
def buildGraph(connectedNodes,newEdges,nodesNum):

    graph = [ [] for i in range(nodesNum+1)]
    connectedNodesSize = [ 0 for i in range(nodesNum+1)]

    for i in connectedNodes:
        graph.append([])
        connectedNodesSize.append(0)
        for e in newEdges:
            if e.firstNode == i:
                graph[i].append(e.secondNode)
                connectedNodesSize[i] += 1
            elif e.secondNode == i:
                graph[i].append(e.firstNode)
                connectedNodesSize[i] += 1
    return graph,connectedNodesSize

def calculateCost(edges):
    result = 0

    for i in edges:
        result += i.w()

    return result