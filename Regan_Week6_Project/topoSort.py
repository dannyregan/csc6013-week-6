def topoSort(V,E,A):
    size = len(A)
    for v in range(len(V)):
        if(v not in A):
            for e in E:
                if (v == e[1]) and (e[0] not in A):
                    break # Go to the next vertex
            else:
                A.append(v)
                break # Go to the next vertex
            continue
    if (len(A) == size):
        return False
    elif (len(V) == len(A)):
        return True
    else:
        return topoSort(V,E,A)

V = ["A","B","C","D","E","F","G","H","I","J","K"]
E = [[0,3,1],
    [1,0,1],
    [1,2,1],
    [2,6,1],
    [3,6,1],
    [4,1,1],
    [4,5,1],
    [5,3,1],
    [5,7,1],
    [7,9,1],
    [8,7,1],
    [8,10,1],
    [9,6,1],
    [10,7,1]]
A = []

if (topoSort(V,E,A)):
    print("Topological order found:")
    for a in A:
        print(V[a], end=' ')
    print()
else:
    print("The graph is not a DAG.")