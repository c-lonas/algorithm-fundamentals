from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def PrintTree(self):
        if self.leftChild:
            self.leftChild.PrintTree()
        print(self.data)
        if self.rightChild:
            self.rightChild.PrintTree()

    def insert(self, data):
        if data < self.data:
            if self.leftChild:
                self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return
            
        else:
            if self.rightChild:
                self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return

    def depth_first_search(self, value):
        if value == self.data:
            return str(value)+ " is found in the Binary Search Tree!"
        elif value < self.data:
            if self.leftChild:
                return self.leftChild.depth_first_search(value)
            else:
                return str(value)+ " is not in the Binary Search Tree :("
        else:       
            if self.rightChild:
                return self.rightChild.depth_first_search(value)
            else:
                return str(value)+ " is not in the Binary Search Tree :("

    def breadth_first_search(self, value):
        queue = deque([self])

        while queue:
            node = queue.popleft()

            if node.data == value:
                return f"{value} is found in the Binary Search Tree!"
            if node.leftChild:
                queue.append(node.leftChild)
            if node.rightChild:
                queue.append(node.rightChild)
        return f"{value} is not in the Binary Search Tree :("


root = Node(10)
root.insert(5)
root.insert(2)
root.insert(99)

root.PrintTree()

print(root.breadth_first_search(99))
