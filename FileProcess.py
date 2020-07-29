import Edge

def fileProcess(inputFile):
    '''

        input must be a string of read file

        and output is :
        (Number of nodes , Number of Edges , Number of Terminals , Nodes in Edges , Edges , terminalNodes)


    '''
    inputFile = inputFile.split("\n")  # deleting new lines

    if inputFile[0] == '33D32945 STP File, STP Format Version 1.0':
        Edges = []
        connectedNodes = []
        terminalNodes = []
        edgesNum = 0  # number of edges
        nodesNum = 0  # number of nodes
        terminalsNum = 0  # number of nodes

        if inputFile[1] == 'Section Comment':
            i = 0
            while i < len(inputFile) and inputFile[i] != 'SECTION Graph':
                i += 1
            inputFile = inputFile[i + 1:]

            if inputFile[0][:5] == "Nodes":
                nodesNum = int(inputFile[0].split(" ")[1])

            if inputFile[1][:5] == "Edges":
                edgesNum = int(inputFile[1].split(" ")[1])

            i = 2
            while i < len(inputFile) and inputFile[i][0] == 'E' and inputFile[i] != "End":
                dSplit = inputFile[i].split(" ")[1:]
                fNode = int(dSplit[0])
                sNode = int(dSplit[1])
                w = int(dSplit[2])

                if ( fNode not in connectedNodes ) and fNode <= nodesNum:
                    connectedNodes.append(fNode)

                if (int(sNode) not in connectedNodes ) and sNode <= nodesNum:
                    connectedNodes.append(sNode)

                Edges.append(Edge.Edge(fNode, sNode, w))

                i += 1

            while i < len(inputFile) and inputFile[i] != 'Section Terminals':
                i += 1
            inputFile = inputFile[i + 1:]

            if inputFile[0][:9] == "Terminals":
                terminalsNum = int(inputFile[0].split(" ")[1])

            i = 1
            while i < len(inputFile) and inputFile[i][0] == 'T' and inputFile[i] != "End":
                dSplit = int(inputFile[i].split(" ")[1])
                if dSplit <= nodesNum:
                    terminalNodes.append(dSplit)
                i += 1

            return (nodesNum,edgesNum,terminalsNum , connectedNodes ,Edges , terminalNodes)

    else:
        print("Syntax Error")