class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0  # Initialize the slow pointer to track the position of the next non-zero element
        for fast in range(len(nums)):  # Iterate through the list with the fast pointer
            
            if nums[fast] != 0 and nums[slow] == 0:  # If fast finds a non-zero and slow points to a zero
                nums[slow], nums[fast] = nums[fast], nums[slow]  # Swap the elements at slow and fast

            if nums[slow] != 0:  # If slow is now pointing to a non-zero element, move it forward
                slow += 1

'''
### **Explanation:**

The task is to move all zeros in the array `nums` to the end while maintaining the relative order of non-zero elements. The solution uses two pointers (`slow` and `fast`) to accomplish this in-place with O(n) time complexity.

1. **Initialization:**
   ```python
   slow = 0
   ```
   - **Purpose:** `slow` tracks the position where the next non-zero element should be placed.

2. **Iterating through the List:**
   ```python
   for fast in range(len(nums)):
   ```
   - **Purpose:** The `fast` pointer iterates over every element in `nums`.

3. **Swapping Logic:**
   ```python
   if nums[fast] != 0 and nums[slow] == 0:
       nums[slow], nums[fast] = nums[fast], nums[slow]
   ```
   - **Purpose:** If `nums[fast]` is a non-zero element and `nums[slow]` is zero, swap them. This places the non-zero element in its correct position at `slow`, effectively moving the zero to where `fast` is.

4. **Advance the `slow` Pointer:**
   ```python
   if nums[slow] != 0:
       slow += 1
   ```
   - **Purpose:** Only increment `slow` when it is pointing to a non-zero element. This ensures `slow` always tracks the position for the next non-zero element. 
   the slow pointer moves forward only if you’ve just swapped a zero to the current position.

### **Example Walkthrough:**

For an input list: `nums = [0, 1, 0, 3, 12]`

1. **Initial State:** `slow = 0`, `fast = 0`, `nums = [0, 1, 0, 3, 12]`
2. **Iteration 1 (fast = 0):** No swap needed because `nums[fast]` is 0.
3. **Iteration 2 (fast = 1):** Swap `nums[slow]` and `nums[fast]`, making `nums = [1, 0, 0, 3, 12]`, then increment `slow`.
4. **Iteration 3 (fast = 2):** No swap needed because `nums[fast]` is 0.
5. **Iteration 4 (fast = 3):** Swap `nums[slow]` and `nums[fast]`, making `nums = [1, 3, 0, 0, 12]`, then increment `slow`.
6. **Iteration 5 (fast = 4):** Swap `nums[slow]` and `nums[fast]`, making `nums = [1, 3, 12, 0, 0]`, then increment `slow`.

**Final Output:** `nums = [1, 3, 12, 0, 0]`

### **Complexity Analysis:**

- **Time Complexity:** O(n), where `n` is the number of elements in `nums`. Each element is processed at most twice.
- **Space Complexity:** O(1), as no extra space is used; the operations are performed in-place.'''


'''
Brute Force Solution Explanation:

"Let's start with a brute-force approach for solving the Move Zeros problem. The idea is to iterate through the array and for each zero we encounter, we shift all the subsequent elements one position to the left and move the zero to the end. This process ensures that all zeros are eventually moved to the end while preserving the order of the non-zero elements.

However, this approach is inefficient because shifting elements to the left for each zero results in a time complexity of O(n^2) in the worst case, where n is the number of elements in the array. If the array has multiple zeros, we could end up doing a lot of unnecessary shifting, making this approach slow for larger arrays."

Transition to the Optimal Solution:

"Given the inefficiencies of the brute-force approach, we need a more optimal solution. We can achieve this by using two pointers, a 'slow' pointer and a 'fast' pointer, to keep track of the positions in the array as we iterate through it."

Optimal Solution Explanation:

"Here's how the optimal solution works:

We initialize a slow pointer at the beginning of the array. This pointer will track the position where the next non-zero element should be placed.
We then iterate through the array with a fast pointer. For each element at the fast pointer:
If it's a non-zero element and nums[slow] is zero, we swap the elements at nums[slow] and nums[fast]. This way, the zero is moved to the current fast position, and the non-zero element is moved to the correct position tracked by the slow pointer.
After swapping, we increment the slow pointer to track the next position where a non-zero element should go.
We continue this process until we've iterated through the entire array.
This approach ensures that all non-zero elements are moved to the front of the array, and all zeros are moved to the end, while maintaining the relative order of the non-zero elements.

The time complexity of this approach is O(n), where n is the number of elements in the array, because we only iterate through the array once. The space complexity is O(1) since we're performing the swaps in place without using any extra space."'''
        