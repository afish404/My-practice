#2、完成二叉树前序，中序，后序，层序遍历

class TreeNode():
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class Tree():
    def __init__(self):
        self.root = None
        self.queue = []

    def insert(self,node:TreeNode):
        self.queue.append(node)
        if self.root is None:
            self.root = node
        else:
            if self.queue[0].left is None:
                self.queue[0].left = node
            else:
                self.queue[0].right = node
                self.queue.pop(0)
    
    def pre_order(self,now_node:TreeNode):
        if now_node:
            print(now_node.value,end = " ")
            self.pre_order(now_node.left)
            self.pre_order(now_node.right)
    
    def in_order(self,now_node:TreeNode):
        if now_node:
            self.in_order(now_node.left)
            print(now_node.value,end = " ")
            self.in_order(now_node.right)
    
    def post_order(self,now_node:TreeNode):
        if now_node:
            self.post_order(now_node.left)
            self.post_order(now_node.right)
            print(now_node.value,end = " ")
    
    def level_order(self):
        queue = [self.root]
        while queue:
            queue_first: TreeNode = queue.pop(0)
            print(queue_first.value,end=" ")
            if queue_first.left:
                queue.append(queue_first.left)
            if queue_first.right:
                queue.append(queue_first.right)

if __name__ == "__main__":
    tree = Tree()
    for i in range(1,11):
        new = TreeNode(i)
        tree.insert(new)
    
    tree.pre_order(tree.root)
    print()
    tree.in_order(tree.root)
    print()
    tree.post_order(tree.root)
    print()
    tree.level_order()