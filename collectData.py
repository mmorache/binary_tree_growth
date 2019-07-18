import random
import math

class Tree():
    def __init__(self, root=None):
        self.root = root

class Node():
    def __init__(self, k):
        self.key = k
        self.p = None
        self.left = None
        self.right = None

def tree_insert(t, z):
    y = None
    x = t.root

    while x is not None:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.p = y
    if y is None:
        t.root = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z
    return z

def tree_height(node): 
    if node is None: 
        return 0 ;  
  
    else : 
        lDepth = tree_height(node.left) 
        rDepth = tree_height(node.right) 
  
        if (lDepth > rDepth): 
            return lDepth+1
        else: 
            return rDepth+1

def tree_collect(stop):
    file1 = open("f.txt","w") 

    n = 250

    while n <= stop:
        sum_height = 0

        j = 1
        while j <= 10:

            rooted = False
            i = 1
            randomT = Tree()
            
            while i <= n:      
                p = random.randint(0,n)
                z = Node(p)
                
                tree_insert(randomT, z)
                if rooted == False:
                    rootNode = z
                    rooted = True
                i += 1
                
            sum_height += tree_height(rootNode)
            j += 1
            
        print("**********************")  
        height = sum_height / (j-1)
        print("n = " + str(n))
        print("average height = " + str(height))
        logOfn = math.log(n, 2)
        print("log2(" + str(n) + ") = " + str(logOfn))
        h_div_logn = height / logOfn
        print("average height / log2(n) = " + str(h_div_logn))
        print("**********************")
        print("")
        file1.write(str(n) + "," + str(h_div_logn) + "\n")
        n += 250
        
    file1.close()          

tree_collect(10000)
