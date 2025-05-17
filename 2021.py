
class Node:
    def __init__(self, data: int, nextNode: int):
        self.data = data
        self.nextNode = nextNode

# Initialize linkedList with given data and nextNode values
linkedList = [
    Node(5, 1),    # index 0
    Node(4, 2),    # index 1
    Node(7, 3),    # index 2
    Node(7, -1),   # index 3
    Node(2, 5),    # index 4 (extra node)
    Node(6, 6),    # index 5
    Node(8, 7),    # index 6
    Node(56, 8),   # index 7
    Node(0, -1),   # index 8
    None          # index 9 (empty)
]

# Pointers
startPointer = 0
emptyList = [9]

# ==== Question 1(c)(i) ====
# Procedure to output the nodes by following nextNode
def outputNodes(linkedList, startPointer):
    print("\nLinked List Traversal:")
    pointer = startPointer
    while pointer != -1 and pointer < len(linkedList) and linkedList[pointer] is not None:
        node = linkedList[pointer]
        print(f"Index: {pointer} | Data: {node.data} | Next: {node.nextNode}")
        pointer = node.nextNode

# ==== Question 1(d)(i) ====
# Function to add a node to the end of the linked list
def addNode(linkedList, emptyList, startPointer, dataToAdd):
    if not emptyList:
        return False  # No space left to add node

    # Find the last node
    pointer = startPointer
    if pointer == -1:
        # Empty list case
        newIndex = emptyList.pop(0)
        linkedList[newIndex] = Node(dataToAdd, -1)
        startPointer = newIndex
        return True

    while pointer != -1 and linkedList[pointer].nextNode != -1:
        pointer = linkedList[pointer].nextNode

    newIndex = emptyList.pop(0)

    # Extend list if needed
    if newIndex >= len(linkedList):
        linkedList.extend([None] * (newIndex - len(linkedList) + 1))

    # Add the new node
    linkedList[newIndex] = Node(dataToAdd, -1)
    linkedList[pointer].nextNode = newIndex

    return True

# ==== Question 1(c)(ii) & 1(d)(ii) ====
# Call outputNodes before adding
print("===== Before addNode() =====")
outputNodes(linkedList, startPointer)

# Call addNode with input value 5
print("\n===== Calling addNode() with data = 5 =====")
dataToAdd = 5
success = addNode(linkedList, emptyList, startPointer, dataToAdd)

# Show appropriate message
if success:
    print(f"Node with data {dataToAdd} added successfully.")
else:
    print("Failed to add node. No space available.")

# Call outputNodes after adding
print("\n===== After addNode() =====")
outputNodes(linkedList, startPointer)
