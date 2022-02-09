a = [1,2,3,5,-1,6,3,5,6,1,-2,3,5]
b = [1,0,-1,4,5,6,1,4,-2,5,3,2,5,5]



def pathSwap( pathA, pathB, node1, node2):
        
        pathA1 = pathA[: pathA.index(node1)]
        pathA2 = pathA[pathA.index(node1) : pathA.index(node2)]
        pathA3 = pathA[pathA.index(node2) : ]
  
        pathB1 = pathB[: pathB.index(node1)]
        pathB2 = pathB[pathB.index(node1) : pathB.index(node2)]
        pathB3 = pathB[pathB.index(node2): ]
        
        new_pathA = pathA1 + pathB2 + pathA3
        new_pathB = pathB1 + pathA2 + pathB3

        return new_pathA, new_pathB

c, d = pathSwap(a,b, -1, -2)
print(c)
print(d)