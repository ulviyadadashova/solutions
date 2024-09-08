class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1  # Initialize left and right pointers
        while l <= r:
            mid = (r + l) // 2  # Calculate the middle index
            # Check if the middle element is less than the next element
            if mid < len(nums) - 1 and nums[mid] < nums[mid + 1]:
                l = mid + 1  # Move the left pointer to the right of mid
            # Check if the middle element is less than the previous element
            elif mid > 0 and nums[mid] < nums[mid - 1]:
                r = mid - 1  # Move the right pointer to the left of mid
            else:
                break  # Mid is a peak if it's greater than or equal to both neighbors
        return mid  # Return the index of the peak element

'''
### **Explanation:**

The goal of this algorithm is to find a peak element in an array. A peak element is an element that is greater than its neighbors. The algorithm efficiently locates the peak using a binary search approach.

#### **Steps:**

1. **Initialization:**
   
   ```python
   l, r = 0, len(nums) - 1
   ```

   - **Purpose:** 
     - `l` and `r` are initialized to the first and last indices of the array, respectively. These pointers will help in narrowing down the search for the peak element.

2. **Binary Search:**
   
   ```python
   while l <= r:
       mid = (r + l) // 2
   ```

   - **Purpose:** 
     - This loop continues until the left pointer is greater than the right pointer. The middle index `mid` is recalculated in each iteration to check whether the element at `mid` is a peak.

3. **Checking Conditions:**
   
   ```python
   if mid < len(nums) - 1 and nums[mid] < nums[mid + 1]:
       l = mid + 1
   elif mid > 0 and nums[mid] < nums[mid - 1]:
       r = mid - 1
   else:
       break
   ```

   - **Purpose:** 
     - **First Condition:** If the element at `mid` is less than the next element, then a peak must lie to the right of `mid`. Hence, move the left pointer `l` to `mid + 1`.
     - **Second Condition:** If the element at `mid` is less than the previous element, then a peak must lie to the left of `mid`. Hence, move the right pointer `r` to `mid - 1`.
     - **Else:** If neither of these conditions is true, the element at `mid` is a peak, so the loop breaks.

4. **Return the Peak Index:**
   
   ```python
   return mid
   ```

   - **Purpose:** 
     - The loop terminates when `mid` is a peak, and the function returns the index of this peak element.

### **Example Walkthrough:**

Consider the input list `nums = [1, 2, 3, 1]`.

1. **First Iteration:**
   - `l = 0`, `r = 3`, `mid = 1`
   - `nums[mid] = 2`, `nums[mid + 1] = 3`
   - Since `nums[mid] < nums[mid + 1]`, move `l` to `mid + 1 = 2`.

2. **Second Iteration:**
   - `l = 2`, `r = 3`, `mid = 2`
   - `nums[mid] = 3`, `nums[mid + 1] = 1`
   - Since `nums[mid] > nums[mid + 1]`, the loop breaks, and `mid = 2` is returned as the peak.

**Final Output:** `2`, indicating that the peak element is `3` at index `2`.

### **Complexity Analysis:**

- **Time Complexity:** O(log n), where n is the length of the list. The binary search technique reduces the search space by half in each iteration, leading to a logarithmic time complexity.
- **Space Complexity:** O(1), as the algorithm uses only a constant amount of extra space, regardless of the input size.'''



'''
Initial Approach (Linear Search):

Explanation:

"To start with, I would use a simple linear search to find the peak element. A peak element is defined as an element that is greater than its neighbors.

So, the idea is to iterate through the array and check each element:

If the element at index i is greater than both its neighbors (i.e., nums[i] > nums[i-1] and nums[i] > nums[i+1]), then it's a peak element, and I can return its index.
Why this approach is inefficient:

The time complexity of this approach is O(n), where n is the number of elements in the array. While this is fine for small arrays, it's not the most efficient way to solve the problem, especially for larger arrays, because we can do better than linear time by taking advantage of the properties of the array.

Optimal Approach (Binary Search):

Explanation:

"To improve upon the linear search, I would use a binary search approach, which reduces the time complexity to O(log n). The key insight here is that in any subarray, if the middle element is not a peak, then at least one of the sides must contain a peak element.

Here’s how it works:

I start by initializing two pointers: left at the beginning of the array and right at the end.

I calculate the middle index, mid, as left + (right - left) / 2.

I then compare the middle element, nums[mid], with its neighbor, nums[mid + 1]:

If nums[mid] > nums[mid + 1], it means there is a peak in the left half of the array, so I move the right pointer to mid.
If nums[mid] < nums[mid + 1], it means there is a peak in the right half of the array, so I move the left pointer to mid + 1.
I continue this process until left equals right. At this point, left will point to a peak element, and I can return its index.

Why this approach is optimal:

This approach is efficient because each comparison effectively halves the search space, resulting in a time complexity of O(log n). This makes it significantly faster than the linear search approach, especially for large arrays.'''
        