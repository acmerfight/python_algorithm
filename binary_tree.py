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
    return max(left_depth, right_depth) + 1

def is_banlanced(root, depth_info={}):
    """ O(n)"""
    if root is None:
        depth_info["depth"] = 0
        return True
    left_depth = {}
    right_depth = {}
    if is_banlanced(root.left, left_depth) and is_banlanced(root.right, right_depth):
        if abs(left_depth["depth"] - right_depth["depth"]) <= 1:
            depth_info["depth"] = max(left_depth["depth"], right_depth["depth"]) + 1
            return True
        else:
            return False
    else:
        return False

def is_banlanced_one(root):
    """ O(n2)"""
    if root is None:
        return True
    if abs(get_tree_depth(root.left) - get_tree_depth(root.right)) > 1:
        return False
    else:
        return is_banlanced_one(root.left) and is_banlanced_one(root.right)

def lca():
    pass



if __name__ == "__main__":
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    #node2.left = TreeNode(8)
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
    print is_banlanced(root)
    print is_banlanced(root)
