# Traversals


## Inorder Traversal

1. Traverse left
1. Visit node
1. Traverse right

Uses:
- Binary Search Tree (BST)

## Preorder Traversal

1. Visit node
1. Traverse left
1. Traverse right

Uses:
- Create a copy of the tree

## Postorder Traversal

1. Traverse left
1. Traverse right
1. Visit node

Uses:
- Tree deletion


# Performance

- Lookup: O(n)


# BST

Tree that puts restrictions on the insertion order of the nodes with the goal of creating some predictable and desireable performance.

In a BST each left subtree contains values less than the root and every right subtree contains values greater than the root.

``` 
    5
   / \
  3   6
 / \   \
2   4   7
```

A BST is most performant when each left and right subtree are most similar in size. To me, it seems like this would occur when the root is the median value.

`Balanced BST`: When the depth of the left and right subtrees differ by no more than 1.
```
Balanced:
    3
   / \
  2   4
 /
1

Un balanced:
1
 \
  2
   \
    3
     \
      4
```

![code](https://user-images.githubusercontent.com/41017214/223981797-0be3e7bf-3ba5-4832-82eb-2344491ef84a.png)

## Performance

Average
- Insertion: O(log(n))
- Deletion: O(log(n))
- Lookup: O(log(n))

Worst (LinkedList):
- Insertion: O(n)
- Deletion: O(n)
- Lookup: O(n)

# Sources

- [tree-traversals-inorder-preorder-and-postorder](https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/)
