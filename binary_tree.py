class TreeNode(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def pre_order(root):
    if root.data is None:
        print "empty tree!"
    else:
        print root.data
        if root.left is not None:
            pre_order(root.left)
        if root.right is not None:
            pre_order(root.right)


def in_order(root):
    if root.data is None:
        print "empty tree!"
    else:
        if root.left is not None:
            in_order(root.left)
        print root.data
        if root.right is not None:
            in_order(root.right)

def post_order(root):
    if root.data is None:
        print "empty tree!"
    else:
        if root.left is not None:
            post_order(root.left)
        if root.right is not None:
            post_order(root.right)
        print root.data





if __name__ == "__main__":
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node2.left = TreeNode(8)
    root = TreeNode(0, node1, node2)
    print "pre_order"
    pre_order(root)
    print "in_order"
    in_order(root)
    print "post_order"
    post_order(root)
