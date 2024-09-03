class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, count = 0, 0  # Initialize the result and count variables

        for n in nums:  # Iterate over each number in the list
            if count == 0:  # If the count is zero, update the result
                res = n
            # Update the count based on whether the current number is equal to the current result
            count += (1 if n == res else -1)
            
        return res  # Return the result, which is the majority element

'''
### **Explanation:**

**Problem Overview:**
The goal is to find the majority element in a list of integers. The majority element is the element that appears more than `n // 2` times in the list, where `n` is the length of the list. This problem can be efficiently solved using the Boyer-Moore Voting Algorithm.

**Step-by-Step Breakdown with Code Snippets:**

1. **Initialize Variables:**
   ```python
   res, count = 0, 0
   ```
   - **Purpose:** 
     - `res` is used to store the potential majority element.
     - `count` keeps track of the balance between the potential majority element and other elements.

2. **Iterate Over Each Number:**
   ```python
   for n in nums:
   ```
   - **Purpose:** Traverse through each element `n` in the list `nums`.

3. **Check and Update the Result:**
   ```python
   if count == 0:
       res = n
   ```
   - **Purpose:** 
     - When `count` is zero, it means there is no current candidate for the majority element. Set `res` to the current element `n`.

4. **Update the Count:**
   ```python
   count += (1 if n == res else -1)
   ```
   - **Purpose:** 
     - If `n` is the same as the current candidate `res`, increment `count` by 1. 
     - If `n` is different from `res`, decrement `count` by 1. This keeps track of how many times the candidate is "surviving" against other elements.
     When the count is incremented, it means the candidate is encountering itself more often, reinforcing its potential as the majority element. When decremented, it reflects the presence of other elements challenging the candidate. This balance helps determine the majority element efficiently.

5. **Return the Result:**
   ```python
   return res
   ```
   - **Purpose:** After processing all elements, `res` will contain the majority element, as the Boyer-Moore Voting Algorithm guarantees that if there is a majority element, it will be found by this method.

### **Example Walkthrough:**

**Example Input:**
- `nums = [3, 2, 3]`

**Execution:**

1. **Initialization:**
   - `res = 0`
   - `count = 0`

2. **Iteration 1 (`n = 3`):**
   - `count == 0`, so update `res` to `3`.
   - `count` is updated to `1` (since `n` is equal to `res`).

3. **Iteration 2 (`n = 2`):**
   - `n != res`, so `count` is decremented to `0`.

4. **Iteration 3 (`n = 3`):**
   - `count == 0`, so update `res` to `3`.
   - `count` is updated to `1` (since `n` is equal to `res`).

**Result:**
- The final value of `res` is `3`, which is the majority element.

### **Complexity Analysis:**

- **Time Complexity:** `O(N)`
  - The algorithm traverses the list `nums` once, where `N` is the length of the list. Each operation inside the loop is constant time.

- **Space Complexity:** `O(1)`
  - The space complexity is constant, as only a few variables (`res` and `count`) are used. The space used does not grow with the size of the input list.

The Boyer-Moore Voting Algorithm efficiently finds the majority element with linear time complexity and constant space complexity.'''


'''
### Brute-Force Solution

**Explanation:**

To solve the "Majority Element" problem using a brute-force approach, you can follow these steps:

1. **Iterate through Each Element:** For each element in the array, consider it as a potential majority element.
2. **Count Occurrences:** Count how many times this candidate appears in the entire array.
3. **Check Majority:** If the count of this candidate is greater than half the size of the array, then this candidate is the majority element.

**Inefficiency:**

- **Time Complexity:** The time complexity of this brute-force approach is \(O(n^2)\), where \(n\) is the number of elements in the array. This is because for each of the \(n\) elements, we are counting its occurrences, which takes \(O(n)\) time.
- **Space Complexity:** The space complexity is \(O(1)\) since we're using only a few extra variables for counting.

This brute-force solution is inefficient for large arrays due to its quadratic time complexity, which can be very slow as the size of the array increases.

### Optimal Solution

**Explanation:**

The optimal solution uses the Boyer-Moore Voting Algorithm. Here's how it works:

1. **Initialize Variables:**
   - `candidate` to store the current potential majority element.
   - `count` to keep track of the balance between the candidate and other elements.

2. **Iterate through the Array:**
   - For each element, if `count` is 0, set the current element as the new `candidate`.
   - If the current element is equal to `candidate`, increment `count`.
   - If it is not equal, decrement `count`.

3. **Return the Candidate:**
   - At the end of the iteration, the `candidate` will be the majority element if it exists.

**Efficiency:**

- **Time Complexity:** The time complexity of this optimal approach is \(O(n)\), where \(n\) is the number of elements in the array. This is because we make a single pass through the array to determine the candidate.
- **Space Complexity:** The space complexity is \(O(1)\) because we only use a few extra variables for tracking the candidate and count.

This approach is efficient and effective for finding the majority element with linear time complexity and constant space complexity.
'''
        