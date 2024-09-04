class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)  # Length of the input list
        result = [-1] * n  # Initialize the result list with -1
        stack = []  # Stack to store indices of elements

        # Iterate through the list twice to handle the circular nature
        for i in range(2 * n):
            num = nums[i % n]  # Current number in the circular array
            
            # Check if the current number is greater than the number at the index on top of the stack
            while stack and nums[stack[-1]] < num:
                index = stack.pop()  # Get the index from the top of the stack
                result[index] = num  # Update the result for that index with the current number
            
            # Only add indices of the first pass (0 to n-1) to the stack
            if i < n:
                stack.append(i)

        return result  # Return the result list with the next greater elements

'''
### **Explanation:**

The goal of this algorithm is to find the next greater element for each element in a circular array. In other words, for each element in the array, find the next greater element when considering the array as circular.

#### **Steps:**

1. **Initialization:**
   ```python
   n = len(nums)
   result = [-1] * n
   stack = []
   ```
   - **Purpose:** 
     - `n` holds the length of the `nums` list.
     - `result` is initialized with `-1` for each element, which will be updated with the next greater element.
     - `stack` will be used to keep track of indices where we haven't yet found the next greater element.

2. **Iterate through the List Twice:**
   ```python
   for i in range(2 * n):
       num = nums[i % n]
   ```
   - **Purpose:** Iterate through the array twice to handle the circular nature. Using `i % n` allows us to wrap around the end of the list.

3. **Find the Next Greater Element:**
   ```python
   while stack and nums[stack[-1]] < num:
       index = stack.pop()
       result[index] = num
   ```
   - **Purpose:** While there are indices in the stack and the current number is greater than the number at the index on the top of the stack, update the result for that index with the current number.

4. **Add Indices to the Stack:**
   ```python
   if i < n:
       stack.append(i)
   ```
   - **Purpose:** Add indices of the first pass (`i < n`) to the stack to keep track of elements for which we need to find the next greater element.

5. **Return the Result:**
   ```python
   return result
   ```
   - **Purpose:** Return the `result` list, which now contains the next greater element for each element in the array.

### **Example Walkthrough:**

Consider the input list `nums = [1, 2, 1]`.

1. **First Pass:**
   - **i = 0:** `num = 1`
     - Stack: `[0]`
   - **i = 1:** `num = 2`
     - Pop index 0 (value 1) from the stack and set `result[0] = 2`.
     - Stack: `[1]`
   - **i = 2:** `num = 1`
     - Stack: `[1, 2]`

2. **Second Pass:**
   - **i = 3:** `num = 1` (wrapped around, equivalent to `nums[0]`)
     - No change (Stack: `[1, 2]`)
   - **i = 4:** `num = 2` (wrapped around, equivalent to `nums[1]`)
     - Pop index 2 (value 1) from the stack and set `result[2] = 2`.
     - Stack: `[1]`
   - **i = 5:** `num = 1` (wrapped around, equivalent to `nums[2]`)
     - No change (Stack: `[1]`)

**Final Output:** `[2, -1, 2]`

### **Complexity Analysis:**

- **Time Complexity:** O(n), where `n` is the length of the list. Each index is pushed and popped from the stack at most once.
- **Space Complexity:** O(n), where `n` is the length of the list. The stack and result list require additional space proportional to the size of the input list.'''


'''
Brute-Force Solution:

The brute-force approach involves iterating through each element in the array and for each element, checking all subsequent elements to find the next greater element. For each element, you would start from the next position and keep checking if there's a greater element. If you find one, you record it; otherwise, you move to the next element in the array. This approach essentially uses two nested loops to compare elements, which leads to a time complexity of O(n²) where n is the number of elements in the array. This method is inefficient because it involves redundant comparisons, especially when dealing with large arrays.

Optimal Solution:

The optimal solution involves using a stack to keep track of indices of the elements while iterating through the array twice to handle the circular nature of the problem. Here’s how it works:

Initialize a result list with all elements set to -1 and an empty stack.
Iterate through the array twice to handle the circular aspect. For each element:
Check if the current element is greater than the element represented by the index on top of the stack.
If it is, update the result for that index with the current element and pop the stack.
Add the current index to the stack if you’re in the first pass.
Return the result list after the iteration, which now contains the next greater element for each element in the array.
This approach uses a single pass through the array to manage the stack and a second pass to handle the circular nature, achieving a time complexity of O(n). The space complexity is also O(n) due to the storage used for the stack and result list. This method is more efficient than the brute-force approach because it reduces the number of comparisons and operations required.'''

        