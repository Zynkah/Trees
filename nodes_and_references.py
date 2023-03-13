class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None # instance of the Binary Tree class
        self.rightChild = None # instance of the Binary Tree class

    def insertLeft(self, newNode):
        if self.leftChild == None: # If there is no left child, add not to tree
            self.leftChild = BinaryTree(newNode) 
        else: # If there is an exisitng left child, we insert the node and push the existing child down one
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild == None: # If there is no rigth child, add not to tree
            self.rightChild = BinaryTree(newNode) 
        else:# If there is an exisitng right child, we insert the node and push the existing child down one
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key


r = BinaryTree('a') # root
print(r.getRootVal()) # prints a
print(r.getLeftChild()) # None
r.insertLeft('b') # child defined
print(r.getLeftChild()) # prints location of left child
print(r.getLeftChild().getRootVal()) # prints b
r.insertRight('c') # child defined
print(r.getRightChild()) # prints location of right child
print(r.getRightChild().getRootVal()) # prints b
r.getRightChild().setRootVal('hello') # defines hello in right child list
print(r.getRightChild().getRootVal()) # prints hello
