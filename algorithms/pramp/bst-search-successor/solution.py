#########################################################
# CODE INSTRUCTIONS:                                    #
# 1) The method findInOrderSuccessor you're asked      #
#    to implement is located at line 30.                #
# 2) Use the helper code below to implement it.         #
# 3) In a nutshell, the helper code allows you to       #
#    to build a Binary Search Tree.                     #
# 4) Jump to line 88 to see an example for how the      #
#    helper code is used to test findInOrderSuccessor.  #
#########################################################


# A node 
class Node:

  # Constructor to create a new node
  def __init__(self, key):
    self.key = key 
    self.left = None
    self.right = None
    self.parent = None

# A binary search tree 
class BinarySearchTree:

  # Constructor to create a new BST
  def __init__(self):
    self.root = None
  
######################################### 
#            Start of my code           #
#########################################
  def find_root_from_node(self, node):
    """
      This method finds the root of the tree by iterating up to the node.parent node
      Until node.parent is None, indicating the root is reached
    """
    if node is None:
      return node
    
    while node.parent is not None:
      node = node.parent
    return node
  
  def minnode(self, minnode, node, m):
    if node is None:
      return minnode
    
    if minnode is None:
        if node.key > m:
          return node
    else:
      if node.key > m and node.key < minnode.key:
        return node
    return minnode
      
  
  def bst_successor_search(self, node, m):
    """
      This function takes in the root and the min maximum min value
      that the min must be greater than.
      
      My solution then linearly checks every node and find this min
    """
    # Base case: Terminal node
    if node is None:
      return None

    left = self.bst_successor_search(node.left, m)
    right = self.bst_successor_search(node.right, m)

    # Case: 'node' is new min > m
    minnode = self.minnode(None, node, m)

    # Case: 'left' result is new min > m
    minnode = self.minnode(minnode, left, m)

    # Case: 'left' result is new min > m
    minnode = self.minnode(minnode, right, m)

    return minnode
    

  def find_in_order_successor(self, inputNode):
    """
      This is just the setup function provided by pramp.
      It gets the root and then performs bst successor search
    """
    root = self.find_root_from_node(inputNode)
    node = self.bst_successor_search(root, inputNode.key)
    return node
######################################### 
#             End of my code            #
#########################################

  # Given a binary search tree and a number, inserts a
  # new node with the given number in the correct place
  # in the tree. Returns the new root pointer which the
  # caller should then use(the standard trick to avoid 
  # using reference parameters)
  def insert(self, key):
    
    # 1) If tree is empty, create the root
    if (self.root is None):
      self.root = Node(key)
      return
        
    # 2) Otherwise, create a node with the key
    #    and traverse down the tree to find where to
    #    to insert the new node
    currentNode = self.root
    newNode = Node(key)
    while(currentNode is not None):
      
      if(key < currentNode.key):
        if(currentNode.left is None):
          currentNode.left = newNode;
          newNode.parent = currentNode;
          break
        else:
          currentNode = currentNode.left;
      else:
        if(currentNode.right is None):
          currentNode.right = newNode;
          newNode.parent = currentNode;
          break
        else:
          currentNode = currentNode.right;

  # Return a reference to a node in the BST by its key.
  # Use this method when you need a node to test your
  # findInOrderSuccessor function on
  def getNodeByKey(self, key):
    
    currentNode = self.root
    while(currentNode is not None):
      if(key == currentNode.key):
        return currentNode
        
      if(key < currentNode.key):
        currentNode = currentNode.left
      else:
        currentNode = currentNode.right
        
    return None
#########################################
#         Custom Testing Scripts        #
#########################################
def test_input(bst, key, expected_key):
  inputNode = bst.getNodeByKey(key)
  assert inputNode is not None
  
  expected_node = bst.find_in_order_successor(inputNode)
  try:
    if expected_key is None:
      assert expected_node is None
    else:
      assert expected_node.key == expected_key
  except:
    if expected_node is not None:
      raise AssertionError('INCORRECT: Expected ' + str(expected_key) + ' is the successor to ' + str(key) +' but got ' + str(expected_node.key))
    else:
      raise AssertionError('INCORRECT: Expected ' + str(expected_key) + ' is the successor to ' + str(key) +' but got ' + str(None))
  print('CORRECT: ' + str(expected_key) + ' is the successor to ' + str(key))
######################################### 
# Driver program to test above function #
#########################################

# Create a Binary Search Tree
bst  = BinarySearchTree()
bst.insert(20)
bst.insert(9);
bst.insert(25);
bst.insert(5);
bst.insert(12);
bst.insert(11);  
bst.insert(14);    

test_input(bst, 20, 25)
test_input(bst, 9, 11)
test_input(bst, 5, 9)
test_input(bst, 12, 14)
test_input(bst, 11, 12)
test_input(bst, 14, 20)
test_input(bst, 25, None)


# Some notes on performance
"""
There are 2 distinct parts to the program. Those being:
1. Find the root
2. Find the successor
3. 1 + 2

Find the root:
- Time: log(n)
- Space: 1

Find the successor:
- Time: n
- Space: 1

Final:
- Time = n + log(n) = n
- Space: 1 + 1 = 1

Points of improvement:
I believe that given a proper amount of time to think about the solution. I could rather do a back track and forward
track using the structure of the bst to turn runtime into log(n).
"""
