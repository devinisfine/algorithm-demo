class TreeNode:
    def __init__(self,data):
        self.data = data
        self.lchild = None
        self.rchild = None

def ConstructTree():
    root  = TreeNode(4)
    node1 = TreeNode(2)
    node2 = TreeNode(6)
    node3 = TreeNode(1)
    node4 = TreeNode(3)
    node5 = TreeNode(5)
    node6 = TreeNode(7)
    root.lchild = node1
    root.rchild = node2
    node1.lchild = node3
    node1.rchild = node4
    node2.lchild = node5
    node2.rchild = node6
    node3.lchild = node3.rchild = None
    node4.lchild = node4.rchild = None
    node5.lchild = node5.rchild = None
    node6.lchild = node6.rchild = None
    return root
def printinpre(root):
    if root == None:
        return
    print(root.data)
    if root.lchild:
        printinpre(root.lchild)
    if root.rchild:
        printinpre(root.rchild)
def reverseTree(root):
    if root.lchild == None and root.rchild:
        return root
    else:
        temp1 = None
        temp2 = None
        if root.lchild:
            temp1 = reverseTree(root.lchild)
        if root.rchild:
            temp2 = reverseTree(root.rchild)
        root.rchild = temp1
        root.lchild = temp2
        return root
if __name__ == '__main__':
    root = ConstructTree()
    if root.lchild == None and root.rchild == None:
        printinpre(root)
    temp1 = None
    temp2 = None
    if root.rchild:
        temp1 = reverseTree(root.rchild)
    if root.lchild:
        temp2 = reverseTree(root.lchild)
    root.lchild = temp1
    root.rchild = temp2
    printinpre(root)




        
    
