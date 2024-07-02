
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

    def search(self, value):
        if value == self.data:
            return str(value)+ " is found in the Binary Search Tree!"
        elif value < self.data:
            if self.leftChild:
                return self.leftChild.search(value)
            else:
                return str(value)+ " is not in the Binary Search Tree :("
        else:       
            if self.rightChild:
                return self.rightChild.search(value)
            else:
                return str(value)+ " is not in the Binary Search Tree :("


root = Node(10)
root.insert(5)
root.insert(2)
root.insert(99)
root.insert(8)
root.insert(1)
root.insert(15)

root.PrintTree()

print(root.search(90))
