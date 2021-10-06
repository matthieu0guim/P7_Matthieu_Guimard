class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None
        self.parent = None
        self.config = []

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
            self.leftChild.parent = self
            toAdd = self.getRootVal()
            # self.config.append(toAdd)
            # self.config.append(newNode)
            # print("ajout d'un élément dans la liste")
            print(self.config)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t
            self.leftChild.parent = self
            toAdd = self.getRootVal()
            # self.config.append(toAdd)
            # self.config.append(newNode)
            # print("ajout d'un élément dans la liste")
    
    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
            self.rightChild.parent = self
            
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t
            self.rightChild.parent = self
    
    def getLeftChild(self):
        return self.leftChild
    
    def getRightChild(self):
        return self.rightChild

    def setRootVal(self, obj):
        self.key = obj
    
    def getRootVal(self):
        return self.key
    
    def getParent(self):
        return self.parent

