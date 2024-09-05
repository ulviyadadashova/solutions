class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)  # Count the frequency of each character in the string
        maxHeap = [[-cnt, char] for char, cnt in count.items()]  # Create a max-heap with negative counts
        heapq.heapify(maxHeap)  # Convert the list into a heap in O(n) time

        prev = None  # Variable to keep track of the previous character used
        res = ""  # Result string to build the reorganized string
        while maxHeap or prev:
            if prev and not maxHeap:
                return ""  # If there's a pending character but no other characters to use, return an empty string
            # Pop the most frequent character from the heap
            cnt, char = heapq.heappop(maxHeap)
            res += char  # Append this character to the result
            cnt += 1  # Decrease the count as this character is used once

            if prev:
                heapq.heappush(maxHeap, prev)  # Push the previous character back to the heap if it still has remaining count
                prev = None  # Reset the previous character

            if cnt != 0:
                prev = [cnt, char]  # Set the current character as the previous character to be used in the next iteration
        return res  # Return the reorganized string

'''
### **Explanation:**

The goal of this algorithm is to rearrange the characters in the input string `s` so that no two adjacent characters are the same. If it's not possible to rearrange the characters to meet this condition, return an empty string.

#### **Steps:**

1. **Count Character Frequencies:**
   ```python
   count = Counter(s)
   ```
   - **Purpose:** Create a frequency map of characters using `Counter` from the `collections` module.

2. **Create a Max-Heap:**
   ```python
   maxHeap = [[-cnt, char] for char, cnt in count.items()]
   heapq.heapify(maxHeap)
   ```

   Python’s Default Heap: Python’s heapq module provides a min-heap.
   Simulating Max-Heap: By storing counts as negative values, the min-heap effectively becomes a max-heap.
   Retrieving Most Frequent Character: The min-heap will give you the character with the highest frequency (most negative count) first.
   - **Purpose:** Create a max-heap (by using negative counts) from the frequency map. This allows us to efficiently retrieve the most frequent character.

3. **Initialize Variables:**
   ```python
   prev = None
   res = ""
   ```
   - **Purpose:** 
     - `prev`: To keep track of the last character used to avoid adjacent duplicates.
     - `res`: To build the final reorganized string.

4. **Rearrange Characters:**
   ```python
   while maxHeap or prev:
       if prev and not maxHeap:
           return ""
       cnt, char = heapq.heappop(maxHeap)
       res += char
       cnt += 1

       if prev:
           heapq.heappush(maxHeap, prev)
           prev = None

       if cnt != 0:
           prev = [cnt, char]
   ```
   - **Purpose:** 
     - **Check Feasibility:** If there's a pending character (`prev`) but no characters left in the heap, return an empty string.
     - **Process the Most Frequent Character:** Pop the most frequent character from the heap and append it to `res`. Decrease its count.
     - **Reinsert Previous Character:** If `prev` is not `None`, push it back into the heap (if it still has remaining count) and reset `prev`.
     - **Set the Current Character as Previous:** If the count of the current character is not zero, set it as the `prev` for the next iteration.

5. **Return the Result:**
   ```python
   return res
   ```
   - **Purpose:** Return the reorganized string that satisfies the condition where no two adjacent characters are the same.


Retrieve the Most Frequent Character: By always taking the most frequent character from the heap, you ensure that you're using characters as often as possible, which helps to distribute them evenly in the result.

Checking and Handling the Previous Character: After adding the most frequent character to the result string, if there was a previous character that still has a remaining count (i.e., it's not used up), it’s added back to the heap. This ensures that this character can be used again later, but not immediately after itself.

Resetting Previous: You reset prev to None after adding it back to the heap to signify that you’ve now moved on from that character. This ensures that the next character you pick is not immediately adjacent to the character just added.

Updating Previous Character: If the current character still has a remaining count, you update prev to this character. This setup ensures that in the next iteration, if the heap has other options, you don’t immediately use this character again right next to itself.


### **Example Walkthrough:**

Consider the input string `s = "aab"`.

1. **Frequency Count:**
   - `count = {'a': 2, 'b': 1}`

2. **Max-Heap:**
   - `maxHeap = [[-2, 'a'], [-1, 'b']]`
   - After heapification: `maxHeap` contains the character with the highest frequency on top.

3. **Rearrangement Process:**
   - **Iteration 1:**
     - Pop `['a', -2]`, append 'a' to `res` → `res = "a"`
     - `cnt` becomes `-1` (1 remaining), so `prev = [-1, 'a']`
   - **Iteration 2:**
     - Pop `['b', -1]`, append 'b' to `res` → `res = "ab"`
     - `prev` is pushed back into the heap.
     - `prev` is `None` as it was just used.
   - **Iteration 3:**
     - Pop `['a', -1]`, append 'a' to `res` → `res = "aba"`
     - No remaining count for 'a', so `prev = None`.

**Final Output:** `"aba"`

### **Complexity Analysis:**

- **Time Complexity:** O(n log k), where `n` is the length of the string and `k` is the number of unique characters. Heap operations (push and pop) take O(log k) time, and each character is processed once.
- **Space Complexity:** O(k), where `k` is the number of unique characters. The space is used by the heap and the result string.'''


'''
Brute-Force Solution:

The brute-force approach to solving the "Reorganized String" problem would be to generate all possible permutations of the input string and then check each permutation to see if it meets the requirement that no two adjacent characters are the same. This approach involves:

Generating Permutations: We would generate all possible permutations of the string. This can be done using a permutation function from a library or by implementing a permutation algorithm manually.

Checking Validity: For each permutation, we check if it satisfies the condition where no two adjacent characters are the same.

While this method guarantees finding a valid rearrangement if one exists, it is highly inefficient. The time complexity is factorial with respect to the length of the string (O(n!)), which becomes infeasible for strings of length greater than a few characters due to the explosive growth of permutations. Additionally, it requires generating and checking a massive number of permutations, which makes it impractical for large inputs.

Optimal Solution:

The optimal approach involves using a max-heap (priority queue) to efficiently rearrange the characters so that no two adjacent characters are the same. Here’s how it works:

Count Frequencies: Use a frequency counter to count how often each character appears in the string.

Build the Max-Heap: Insert characters into a max-heap where each character is represented by its negative frequency. The negative sign is used because Python's heapq implements a min-heap by default, and we need a max-heap behavior to get the most frequent characters first.

Reorganize String: While there are characters left in the heap:

Extract the most frequent character (which is the one with the highest negative frequency).
Add this character to the result string.
If the previous character has remaining count, push it back into the heap to be used later.
Update the previous character to the current one if it still has remaining count.
Handle Edge Cases: If at any point the heap is empty but there are still characters left that need to be placed, return an empty string as it indicates that a valid rearrangement is not possible.

This approach efficiently builds the result string in O(n log k) time complexity, where n is the length of the string and k is the number of unique characters. It ensures that no two adjacent characters are the same by always choosing the most frequent character available and correctly managing the order of characters.'''