class stack(list):
    def push(self, item):
        self.append(item)

    def is_empty(self):
        return not self



class TreeNode(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def pre_order(root):
    if root is None:
        pass
    else:
        print root.data
        pre_order(root.left)
        pre_order(root.right)

def nonrecursive_pre_order(root):
    s = stack()
    s.push(root)
    while not s.is_empty():
        node = s.pop()
        print node.data
        if node.right is not None:
            s.push(node.right)
        if node.left is not None:
            s.push(node.left)


def in_order(root):
    if root is None:
        pass
    else:
        in_order(root.left)
        print root.data
        in_order(root.right)


def post_order(root):
    if root is None:
        pass
    else:
        post_order(root.left)
        post_order(root.right)
        print root.data


def get_tree_depth(root, depth=0):
    if root is None:
        return 0
    else:
        left_depth = get_tree_depth(root.left)
        right_depth = get_tree_depth(root.right)
    return left_depth + 1 if left_depth > right_depth else right_depth + 1



if __name__ == "__main__":
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node2.left = TreeNode(8)
    node1.left = TreeNode(9)
    node1.right = TreeNode(10)
    root = TreeNode(0, node1, node2)
    #print "pre_order"
    #pre_order(root)
    #print "nonrecursive_pre_order"
    #nonrecursive_pre_order(root)
    #print "in_order"
    #in_order(root)
    #print "post_order"
    #post_order(root)

    print get_tree_depth(root)
