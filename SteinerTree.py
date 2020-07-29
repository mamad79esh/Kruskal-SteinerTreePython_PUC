import Graph

def buildSteinerTree(nodesNum,terminalNodes,connectedNodes, newEdges):
    notTerminalNum = 0
    for i in range(nodesNum + 1):
        if not i in terminalNodes:
            if i in connectedNodes:
                notTerminalNum += 1

    graph, connectedNodesSize = Graph.buildGraph(connectedNodes, newEdges, nodesNum)

    for i in range(notTerminalNum):

        size = len(connectedNodes)
        tempSize = len(connectedNodes)

        i = 0
        while i < size:
            if connectedNodesSize[connectedNodes[i]] == 1 and connectedNodes[i] not in terminalNodes:
                connectedNodesSize[graph[connectedNodes[i]][0]] -= 1
                j = 0
                eSize = len(newEdges)

                node1 = connectedNodes[i]
                node2 = graph[connectedNodes[i]][0]
                while j < eSize:
                    if (newEdges[j].firstNode == connectedNodes[i] and newEdges[j].secondNode ==
                        graph[connectedNodes[i]][0]) or (
                            newEdges[j].secondNode == connectedNodes[i] and newEdges[j].firstNode ==
                            graph[connectedNodes[i]][0]):
                        newEdges.pop(j)
                        eSize -= 1
                    j += 1
                connectedNodes.pop(i)
                size -= 1


            i += 1

        if tempSize == size:
            break

        graph, connectedNodesSize = Graph.buildGraph(connectedNodes, newEdges, nodesNum)

    return newEdges


