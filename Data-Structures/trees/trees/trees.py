class Node:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None


class Binary_Tree:
    def __init__(self,root = None):
        self.root = root

    def pre_order(self):
        output = []
        def traverse(root):
            if not root:
                return "Tree Empty"
            output.append(root.value)
            traverse(root.left)
            traverse(root.right)
        traverse(self.root)
        return output

        

    def in_order(self):
        output = []
        def traverse(root):
            if not root:
                return "Tree Empty"
            
            traverse(root.left)
            output.append(root.value)
            traverse(root.right)
        traverse(self.root)
        return output


    def post_order(self):
        output = []
        def traverse(root):
            if not root:
                return "Tree Empty"
            traverse(root.left)
            traverse(root.right)
            output.append(root.value)
        traverse(self.root)
        return output




class Binary_Search_Tree(Binary_Tree):
    def add(self,value):
        add_node = Node(value)
        def traverse(node):
            if add_node.value < node.value:
                if node.left:
                    traverse(node.left)
                else:
                    node.left = add_node
            else:
                if node.right:
                    traverse(node.right)
                else:
                    node.right = add_node
        if self.root:
            traverse(self.root)
        else:
            self.root = add_node

    def contains(self,value):
        def traverse(node):
            while node:
                if node.value == value:
                    print("true")
                    return True
                if value < node.value:
                    traverse(node.left)
                else:
                    traverse(node.right)
                print("false")
                return False
        return traverse(self.root)


    def max_value(self):
        maxv = 0
        def traverse(node):
            nonlocal maxv
            if node:
                if node.value > maxv:
                    maxv = node.value
                traverse(node.left)
                traverse(node.right)
    
        traverse(self.root)
        return maxv


if __name__ == "__main__":
    bst = Binary_Search_Tree()
    bst.add(10)
    bst.add(8)
    bst.add(17)
    bst.add(23)
    bst.add(3)
    bst.add(-1)
    bst.add(50)
    bst.add(34)
    print(bst.max_value())
    print(bst.post_order())


        