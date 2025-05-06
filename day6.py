# Part 1(a): Define the Node class (record type)
class Node:
    def __init__(self, data=0, nextNode=-1):
        self.data = data
        self.nextNode = nextNode

# Part 1(b): Declare and initialize the linked list and pointers
linkedList = [
    Node(1, 1),     # Index 0
    Node(15, 4),    # Index 1
    Node(6, 7),     # Index 2
    Node(7, -1),    # Index 3
    Node(2, 2),     # Index 4
    Node(0, 6),     # Index 5 -> unused (start of emptyList)
    Node(56, 3),    # Index 6
    Node(0, 8),     # Index 7 -> unused
    Node(0, 9),     # Index 8 -> unused
    Node(0, -1)     # Index 9 -> unused
]

startPointer = 0      # Starting node of the linked list
emptyList = 5         # First available free index

# Part 1(c)(i): Function to output the linked list nodes
def outputNodes(linkedList, startPointer):
    currentPointer = startPointer
    while currentPointer != -1:
        print(linkedList[currentPointer].data)
        currentPointer = linkedList[currentPointer].nextNode

# Part 1(d)(i): Function to add a new node at the end
def addNode(linkedList, startPointer, emptyList, newData):
    if emptyList == -1:
        return False, startPointer, emptyList  # No space left

    # Use the next available node
    newNodeIndex = emptyList
    emptyList = linkedList[newNodeIndex].nextNode  # Advance empty list pointer

    linkedList[newNodeIndex].data = newData
    linkedList[newNodeIndex].nextNode = -1

    if startPointer == -1:
        # If list was empty
        startPointer = newNodeIndex
    else:
        # Find last node and link new node
        currentPointer = startPointer
        while linkedList[currentPointer].nextNode != -1:
            currentPointer = linkedList[currentPointer].nextNode
        linkedList[currentPointer].nextNode = newNodeIndex

    return True, startPointer, emptyList

# ------------------------------
# Part 1(c)(ii) and 1(d)(ii): Main Program with calls
# ------------------------------

# Output before insertion
# print("Linked list before adding node:")
# outputNodes(linkedList, startPointer)

# Test input (Part 1(d)(iii))
newData = 5

# Try to add node with data = 5
success, startPointer, emptyList = addNode(linkedList, startPointer, emptyList, newData)

# Message depending on result
if success:
    print(f"\nNode with data {newData} added successfully.")
else:
    print("\nNo space available to add a new node.")

# Output after insertion
print("\nLinked list after adding node:")
outputNodes(linkedList, startPointer)
