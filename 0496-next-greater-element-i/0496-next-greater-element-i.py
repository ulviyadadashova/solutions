class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []  # Stack to keep track of elements for which we need to find the next greater element
        next_greater = {}  # Dictionary to store the next greater element for each number in nums2
        
        # Process each element in nums2
        for num in nums2:
            # While the stack is not empty and the current number is greater than the top of the stack
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num  # Map the popped element to the current number
            stack.append(num)  # Push the current number onto the stack
        
        # After processing all elements, any remaining elements in the stack have no greater element
        while stack:
            next_greater[stack.pop()] = -1
        
        # Generate the result list for nums1 using the next_greater dictionary
        return [next_greater[num] for num in nums1]

'''
### **Explanation:**

The goal is to find the next greater element for each element in `nums1` within `nums2`. We are given two lists: `nums1` and `nums2`, and we need to find the next greater element for each element in `nums1` as it appears in `nums2`.

#### **Steps:**

1. **Initialize Stack and Dictionary:**
   ```python
   stack = []
   next_greater = {}
   ```
   - **Purpose:** `stack` keeps track of elements for which we need to find the next greater element. `next_greater` is a dictionary that maps each element to its next greater element.

2. **Process Each Element in `nums2`:**
   ```python
   for num in nums2:
   ```
   - **Purpose:** Iterate through each element in `nums2`.

3. **Find Next Greater Element:**
   ```python
   while stack and stack[-1] < num:
       next_greater[stack.pop()] = num
   ```
   - **Purpose:** While the stack is not empty and the current number is greater than the top of the stack, pop the stack and map the popped element to the current number. This means the current number is the next greater element for the popped element.

4. **Push Current Element onto Stack:**
   ```python
   stack.append(num)
   ```
   - **Purpose:** Push the current number onto the stack to check it against future numbers.

5. **Handle Remaining Elements in the Stack:**
   ```python
   while stack:
       next_greater[stack.pop()] = -1
   ```
   - **Purpose:** After processing all elements in `nums2`, any remaining elements in the stack have no greater element. Thus, map these elements to `-1`.

6. **Generate the Result List for `nums1`:**
   ```python
   return [next_greater[num] for num in nums1]
   ```
   - **Purpose:** Create a result list for `nums1` by looking up each element in the `next_greater` dictionary.

### **Complexity Analysis:**

- **Time Complexity:** O(n + m), where `n` is the length of `nums1` and `m` is the length of `nums2`. Each element is pushed and popped from the stack at most once, and each element in `nums2` is processed once.
- **Space Complexity:** O(m), where `m` is the length of `nums2`. The space is used by the stack and the `next_greater` dictionary.'''


'''
Brute-Force Solution:

"In the brute-force approach for the Next Greater Element problem, I would iterate through each element in nums1 and for each element, I would search for it in nums2. Once found, I would continue scanning the rest of the elements in nums2 to find the next greater element. If no greater element is found, we would simply set the result as -1 for that element.

This approach works but is inefficient because for each element in nums1, we potentially iterate through the majority of nums2. This gives us a time complexity of O(n * m), where n is the length of nums1 and m is the length of nums2. This can become very slow as the size of the arrays increases."

Optimal Solution:

"To optimize this, I used a stack-based approach that leverages the properties of the problem more effectively. Here's how it works:

I initialize an empty stack to keep track of elements for which we need to find the next greater element.
I also initialize a dictionary called next_greater to store the next greater element for each element in nums2.
Then, I iterate through nums2:

While the stack is not empty and the current number is greater than the element at the top of the stack, it means we've found the next greater element for the number on the stack. I pop the stack and update the next_greater dictionary with this number as the key and the current number as its next greater element.
After this, I push the current number onto the stack for future comparisons.
After completing the iteration through nums2, any elements remaining in the stack do not have a greater element in the array, so we map these elements to -1 in the next_greater dictionary.

Finally, I generate the result for nums1 by looking up each element in the next_greater dictionary.

This approach is much more efficient because each element is pushed and popped from the stack at most once, leading to a time complexity of O(n + m), where n is the length of nums1 and m is the length of nums2. The space complexity is O(m) due to the stack and dictionary storage'''
