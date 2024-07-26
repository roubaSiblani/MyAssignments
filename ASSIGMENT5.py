#EX1:
class Node:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

class Solution:
    def deleteNode(self, root, key):
        if not root:
            return root

        if key > root.value:
            root.right = self.deleteNode(root.right, key)
        elif key < root.value:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            # Find the min from right subtree
            cur = root.right
            while cur.left:
                cur = cur.left
            root.value = cur.value
            root.right = self.deleteNode(root.right, cur.value)

        return root

# Helper function to print in-order traversal of the tree
def print_in_order(root):
    if root:
        print_in_order(root.left)
        print(root.value, end=' ')
        print_in_order(root.right)

# Helper function to insert a new node with given key
def insert(node, key):
    if node is None:
        return Node(key)
    if key < node.value:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node

# Create a sample tree
root = None
keys = [50, 30, 20, 40, 70, 60, 80]
for key in keys:
    root = insert(root, key)

print("In-order traversal of the given tree:")
print_in_order(root)
print("\nDelete 20")
root = Solution().deleteNode(root, 20)
print("In-order traversal of the modified tree:")
print_in_order(root)

print("\nDelete 30")
root = Solution().deleteNode(root, 30)
print("In-order traversal of the modified tree:")
print_in_order(root)

print("\nDelete 50")
root = Solution().deleteNode(root, 50)
print("In-order traversal of the modified tree:")
print_in_order(root)

#EX2:
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class ExpressionTree:
    def __init__(self, root=None):
        self.root = root

    def printExpression(self, node):
        if node is None:
            return ""
        
        
        if node.left is None and node.right is None:
            return str(node.value)
        
        
        left_expr = self.printExpression(node.left)
        right_expr = self.printExpression(node.right)
        
        
        return f"({left_expr}{node.value}{right_expr})"


def buildSampleTree():
    # Building the expression tree for the expression ((3+2)*(7-4))
    root = Node('*')
    root.left = Node('+')
    root.right = Node('-')
    
    root.left.left = Node(3)
    root.left.right = Node(2)
    
    root.right.left = Node(7)
    root.right.right = Node(4)
    
    return root

tree = ExpressionTree(buildSampleTree())

# Print the expression
expression = tree.printExpression(tree.root)
print("The arithmetic equation is:", expression)
