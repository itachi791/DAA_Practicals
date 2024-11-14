import heapq

class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ""
    
    # This is the comparison function for the heap to work (min-heap based on frequency)
    def __lt__(self, other):
        return self.freq < other.freq
    
# Function to traverse the Huffman tree and print the codes
def printNodes(node, val=""):
    # Add the current node's huff value to the traversal path
    newval = val + node.huff
    # If the node is a leaf, print the character and its corresponding Huffman code
    if node.left is None and node.right is None:
        print(f"{node.symbol} -> {newval}")
    # Otherwise, continue traversing the tree
    if node.left:
        printNodes(node.left, newval)
    if node.right:
        printNodes(node.right, newval)

# Input symbols and their corresponding frequencies
chars = ["a", "b", "c", "d", "e", "f"]
freqs = [5, 9, 12, 13, 16, 45]
nodes = []

# Create the initial nodes (leaf nodes) and add them to the heap
for i in range(len(chars)):
    heapq.heappush(nodes, Node(freqs[i], chars[i]))

# Build the Huffman Tree
while len(nodes) > 1:
    # Pop the two nodes with the smallest frequencies
    left = heapq.heappop(nodes)
    right = heapq.heappop(nodes)
    
    # Assign 0 and 1 to the left and right child respectively
    left.huff = "0"
    right.huff = "1"
    
    # Create a new internal node with the sum of frequencies of the two popped nodes
    newnode = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)
    
    # Push the new internal node back into the heap
    heapq.heappush(nodes, newnode)

# The remaining node is the root of the Huffman tree
printNodes(nodes[0])
