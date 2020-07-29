import Edge


def KruskalAlgorithm(edges,connectedNodes,nodesNum,edgesNum):
    edges = SortEdges(edges)
    parent = [i for i in range(nodesNum+1)]
    ssize = [1 for i in range(nodesNum+1)]

    def find(x):
        p = parent[x]
        if p == x :
            return p
        parent[x] = find(p)
        return parent[x]


    def union(x , y):

        rx = find(x)
        ry = find(y)
        if  rx == ry :
            return None

        if ssize[ry] > ssize[rx]:
            temp = rx
            rx = ry
            ry = temp
        parent[ry] = rx
        ssize[rx] += ssize[ry]

    newEdges = []
    for i in range(len(edges)):
        x = find(edges[i].firstNode)
        y = find(edges[i].secondNode)
        if  x != y :
            newEdges.append(edges[i])
            union(x,y)


    return newEdges


    return newEdges

def SortEdges(edges):  # Merge sort
    if len(edges) <= 1:
        return edges

    middle = len(edges) // 2

    leftArray = edges[:middle]
    rightArray = edges[middle:]

    leftArray = SortEdges(leftArray)
    rightArray = SortEdges(rightArray)

    return merge(leftArray, rightArray)


def merge(arr1, arr2):
    i = j = 0
    arr = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i].w() < arr2[j].w():
            arr.append(arr1[i])
            i += 1
        else:
            arr.append(arr2[j])
            j += 1


    while i < len(arr1):
        arr.append(arr1[i])
        i += 1

    while j < len(arr2):
        arr.append(arr2[j])
        j += 1

    return arr
