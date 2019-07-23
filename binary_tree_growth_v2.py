import random
import math
import multiprocessing as mp
import platform
import time


'''
IMPORTANT: This program must be run from the command line.
'''

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

def tree_average(n):
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
        h = tree_height(rootNode)
            
        return(h)

def print_sysinfo():

    print('\nPython version  :', platform.python_version())
    print('compiler        :', platform.python_compiler())

    print('\nsystem     :', platform.system())
    print('release    :', platform.release())
    print('machine    :', platform.machine())
    print('processor  :', platform.processor())
    print('CPU count  :', mp.cpu_count())
    print('interpreter:', platform.architecture()[0])
    


if __name__ == '__main__':

    exp = 1
    iterations = 100
    maximum = 20 #set the maximum exponent
    pool = mp.Pool(mp.cpu_count())

    #print_sysinfo()
    print("\nNumber of processors          :", mp.cpu_count())
    print("Number of iterations per tree : " + str(iterations))
    print("Terminate program at exponent : " +str(maximum))

    while exp <= maximum:

        nodes = math.pow(2, exp)
        log2Nodes = math.log(nodes, 2)
        print("\n**********")
        print("Exponent                                    : " + str(exp))
        
        '''
        #no parallel
        for iteration in iterationList:
            results.append(tree_average(nodes))
        '''

        #parallel
        start = time.time()
        results = []
        iterationList = [nodes] * iterations
        results = pool.map(tree_average, iterationList)
        end = time.time()
        averageHeight = sum(results) / len(results)
        
        print("Nodes in Binary Tree                        : " + str((int)(nodes)))
        print("Average Tree Height                         : " + '%.3f'%(averageHeight))
        print("Depth ratio of average height / log2(nodes) : " + '%.3f'%(averageHeight / log2Nodes))
        print("Elapsed time                                : " + '%.3f'%(end - start) + "\n")

        exp +=1
        
    pool.close()

