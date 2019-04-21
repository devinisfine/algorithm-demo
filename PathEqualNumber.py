class TreeNode:
    def __init__(self,data):
        self.data = data
        self.lchild = None
        self.rchild = None
def ConstructTree():
    root  = TreeNode(6)
    node1 = TreeNode(3)
    node2 = TreeNode(-7)
    node3 = TreeNode(-1)
    node4 = TreeNode(9)
    root.lchild = node1
    root.rchild = node2
    node1.lchild = node3
    node1.rchild = node4
    node2.lchild = node2.rchild = None
    node3.lchild = node3.rchild = None
    node4.lchild = node4.rchild = None
    return root
def findroad(root,num,s):
    s.append(root.data)
    if root.data == num and root.lchild == None and root.rchild == None:
        for i in range(len(s)):
            print(s[i])
    else:
        if root.lchild != None:
            findroad(root.lchild,num-root.data,s)
        if root.rchild != None:
            findroad(root.rchild,num-root.data,s)
    s.pop()
if __name__ == '__main__':
    root = ConstructTree()
    s = []
    findroad(root,8,s)
    
