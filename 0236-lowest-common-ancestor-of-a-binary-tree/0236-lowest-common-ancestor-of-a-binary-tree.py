# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Finds the lowest common ancestor (LCA) of two nodes in a binary tree.

        :param root: The root node of the binary tree.
        :param p: The first node.
        :param q: The second node.
        :return: The LCA of nodes p and q.
        """
        # Base case: if the current node is None, or if it's one of the target nodes
        if not root or root == p or root == q:
            return root

        # Recursively search for the LCA in the left and right subtrees
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        # If both left and right subtrees return a non-null value, the current node is the LCA
        if l and r:
            return root
        
        # If only one of the left or right subtree returns a non-null value, propagate it upwards
        return l or r

'''
### **Explanation:**

**Purpose:**
The `lowestCommonAncestor` function identifies the lowest (deepest) common ancestor of two nodes, `p` and `q`, in a binary tree. The LCA is the deepest node that is an ancestor of both `p` and `q`.

**Steps:**

1. **Base Case:**
   ```python
   if not root or root == p or root == q:
       return root
   ```
   - If the `root` is `None`, or if the current node is either `p` or `q`, the current node is returned. This indicates that either we've reached the end of a path or we've found one of the target nodes.

2. **Recursive Search:**
   ```python
   l = self.lowestCommonAncestor(root.left, p, q)
   r = self.lowestCommonAncestor(root.right, p, q)
   ```
   - Recursively search for the LCA in the left and right subtrees. The variables `l` and `r` store the results from the left and right subtree searches, respectively.

3. **Determine the LCA:**
   ```python
   if l and r:
       return root
   ```
   - If both `l` and `r` are non-null, it means `p` and `q` are found in different subtrees, and thus, the current node (`root`) is their LCA.

4. **Return the Non-null Result:**
   ```python
   return l or r
   ```
   - If only one of `l` or `r` is non-null, return the non-null value, indicating that either both nodes were found in one subtree, or one node was found in one subtree and the other was not found in either subtree.

### **Example Walkthrough:**

**Example:**
Consider the following binary tree:

```
        3
       / \
      5   1
     / \ / \
    6  2 0  8
      / \
     7   4
```

- Suppose `p = 5` and `q = 4`.

**Execution:**

1. Start at the root node `3`. Neither `p` nor `q` is `3`, so we recursively search in the left and right subtrees.

2. In the left subtree rooted at `5`, `p` is found (since `root == p`), so we return `5`.

3. In the right subtree rooted at `1`, search in its subtrees. The left subtree rooted at `0` does not contain `p` or `q`, and the right subtree rooted at `8` does not either. So, we return `None` from both subtrees.

4. Back at `3`, since `l` is `5` and `r` is `None`, we return `5`, which is the LCA of `p` and `q`.

**Result:** The LCA of nodes `5` and `4` is node `5`.

### **Complexity Analysis:**

- **Time Complexity:** `O(N)`, where `N` is the number of nodes in the binary tree. In the worst case, we may need to visit every node in the tree.

- **Space Complexity:** `O(H)`, where `H` is the height of the tree. This is the space required for the recursion stack in the worst case. For a balanced tree, `H` would be `O(log N)`, and for a skewed tree, it could be `O(N)`.'''


'''

**Brute-Force Solution:**

"To begin with, let's consider a brute-force approach to solve the problem of finding the lowest common ancestor (LCA) of two nodes in a binary tree. The brute-force method would involve traversing the tree multiple times. We could start by traversing the entire tree from the root to each of the target nodes `p` and `q`, recording the path from the root to `p` and the path from the root to `q`. Once we have both paths, we would then compare them to find the last common node, which would be our lowest common ancestor.

The time complexity of this approach would be \(O(n)\) for each traversal, where \(n\) is the number of nodes in the tree. Since we might need to traverse the tree twice (once for each node), the total time complexity would be \(O(2n)\), which simplifies to \(O(n)\). However, this doesn't account for the comparison of the two paths, which would add extra complexity. The space complexity would also be \(O(n)\), as we would need to store the paths in memory.

This approach is inefficient because it requires multiple traversals of the tree and extra space to store the paths, making it not ideal for large trees or cases where memory usage is a concern."

**Optimal Solution:**

"Now, let's discuss the optimal solution, which involves a single traversal of the tree using a recursive approach. 

In this method, we start at the root of the tree and recursively explore the left and right subtrees. The key idea is that if the current node is `None` or matches either `p` or `q`, we return the current node as it may be an ancestor of the other node. We store the results of the left and right subtree searches in variables `L` and `R`.

Next, we check if both `L` and `R` are not `None`. If they are both non-null, it means `p` and `q` are found in different subtrees, so the current node is their lowest common ancestor, and we return this node.

If only one of `L` or `R` is non-null, we return the non-null value because it indicates that both nodes are located in the same subtree or that one of the nodes is an ancestor of the other.

This approach is much more efficient. The time complexity remains \(O(n)\) because we still need to traverse the entire tree in the worst case. However, the space complexity is significantly improved. It’s \(O(h)\), where \(h\) is the height of the tree, as this is the maximum depth of the recursion stack. In a balanced tree, \(h\) would be \(O(\log n)\), and in a skewed tree, it would be \(O(n)\). This makes the recursive approach both time-efficient and space-efficient compared to the brute-force solution."
'''

        