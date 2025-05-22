# --- Part 2(a)(i): Node class with constructor ---
class Node:
    

    def __init__(self, data):
        self.LeftPointer = -1
        self.Data = data
        self.RightPointer = -1

    # --- Part 2(a)(ii): Get methods ---
    def GetLeft(self):
        return self.LeftPointer

    def GetRight(self):
        return self.RightPointer

    def GetData(self):
        return self.Data

    # --- Part 2(a)(iii): Set methods ---
    def SetLeft(self, index):
        self.LeftPointer = index

    def SetRight(self, index):
        self.RightPointer = index

    def SetData(self, data):
        self.Data = data

# --- Part 2(b)(i): TreeClass with constructor ---
class TreeClass:
    def __init__(self):
        # Tree[0:19] : Node
        # FirstNode : INTEGER
        # NumberNodes : INTEGER
        self.Tree = [Node(-1) for _ in range(20)]
        self.FirstNode = -1
        self.NumberNodes = 0

    # --- Part 2(b)(ii): InsertNode() method ---
    def InsertNode(self, NewNode):
        if self.NumberNodes >= 20:
            print("Tree is full")
            return

        if self.FirstNode == -1:
            # Tree is empty
            self.Tree[0] = NewNode
            self.FirstNode = 0
            self.NumberNodes += 1
            return

        # Tree is not empty
        index = self.FirstNode
        while True:
            currentNode = self.Tree[index]
            if NewNode.GetData() < currentNode.GetData():
                if currentNode.GetLeft() == -1:
                    currentNode.SetLeft(self.NumberNodes)
                    break
                else:
                    index = currentNode.GetLeft()
            else:
                if currentNode.GetRight() == -1:
                    currentNode.SetRight(self.NumberNodes)
                    break
                else:
                    index = currentNode.GetRight()

        self.Tree[self.NumberNodes] = NewNode
        self.NumberNodes += 1

    # --- Part 2(b)(iii): OutputTree() method ---
    def OutputTree(self):
        if self.NumberNodes == 0:
            print("No nodes")
        else:
            print("Index | Left | Data | Right")
            for i in range(self.NumberNodes):
                node = self.Tree[i]
                print(f"  {i:<4}| {node.GetLeft():<5}| {node.GetData():<5}| {node.GetRight():<5}")

# --- Part 2(c): Main Program ---
if __name__ == "__main__":
    # 2(c)(i)
    TheTree = TreeClass()

    # 2(c)(ii): Insert values
    TheTree.InsertNode(Node(10))
    TheTree.InsertNode(Node(11))
    TheTree.InsertNode(Node(5))
    TheTree.InsertNode(Node(1))
    TheTree.InsertNode(Node(20))
    TheTree.InsertNode(Node(7))
    TheTree.InsertNode(Node(15))

    # Output the binary tree structure
    print("\nBinary Tree Structure:\n")
    TheTree.OutputTree()
