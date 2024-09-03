class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""  # Initialize an empty string to store the result
        
        # Iterate over each character index of the first string
        for i in range(len(strs[0])):

            # Check each string in the list
            for s in strs:
                # If the current index is out of bounds for string 's' or characters do not match
                if i == len(s) or s[i] != strs[0][i]:
                    return res  # Return the result string if mismatch is found

            # If characters matched for all strings at the current index, append it to result
            res += strs[0][i]

        return res  # Return the longest common prefix found

'''
### **Explanation:**

1. **Initialization:**
   ```python
   res = ""
   ```
   - **Purpose:** Initializes an empty string `res` to store the longest common prefix as it is found.

2. **Outer Loop:**
   ```python
   for i in range(len(strs[0])):
   ```
   - **Purpose:** Iterates over each character index `i` of the first string in the list. This loop checks each character position in all strings.

3. **Inner Loop:**
   ```python
   for s in strs:
   ```
   - **Purpose:** Iterates over each string `s` in the list `strs`.

4. **Mismatch Check:**
   ```python
   if i == len(s) or s[i] != strs[0][i]:
       return res
   ```
   - **Purpose:** Checks if the current index `i` is out of bounds for string `s` or if the character at index `i` in string `s` does not match the character at index `i` in the first string. If either condition is true, it returns the current `res` as the longest common prefix found up to this point.

5. **Updating the Result:**
   ```python
   res += strs[0][i]
   ```
   - **Purpose:** If the characters at index `i` match for all strings, appends the character from the first string to `res`.

6. **Return Statement:**
   ```python
   return res
   ```
   - **Purpose:** Returns the final longest common prefix after all character positions have been checked.

### **Example Walkthrough:**

For `strs = ["flower", "flow", "flight"]`:

- **Iteration 1 (i = 0):** Characters `f`, `f`, and `f` match. `res` becomes `"f"`.
- **Iteration 2 (i = 1):** Characters `l`, `l`, and `l` match. `res` becomes `"fl"`.
- **Iteration 3 (i = 2):** Characters `o`, `o`, and `i` do not match. The function returns `"fl"` as the longest common prefix.

### **Complexity Analysis:**

- **Time Complexity:** O(S * N), where `S` is the length of the shortest string and `N` is the number of strings. The algorithm iterates through each character of the first string and checks it against every other string.
- **Space Complexity:** O(1), as no additional space is used apart from the result string.'''


'''
Brute-Force Solution:

To find the longest common prefix using a brute-force approach, you would start by comparing every character of each string in the array against each other. You can start by checking the first character of all strings, then move to the second character, and so on. For each character position, you compare all strings to see if they match. If a mismatch is found or if you reach the end of any string, you stop and return the prefix found up to that point. This approach is inefficient because it involves multiple nested loops and redundant comparisons, leading to a time complexity of O(s * n), where s is the length of the shortest string and n is the number of strings. This is because you are repeatedly checking characters against all strings, which can be slow, especially with a large number of strings or longer strings.

Optimal Solution:

In the optimal approach, you only need to iterate through the characters of the first string and compare each character with the corresponding characters in all other strings. Start with an empty result string. For each index, check if that character exists in the same position across all strings. If all strings have the same character at that position, add it to the result. If there's a mismatch or if the index is out of bounds for any string, stop and return the result found so far. This approach is more efficient because it minimizes the number of comparisons needed. It still has a time complexity of O(s * n), where s is the length of the shortest string and n is the number of strings, but it avoids redundant checks and is more straightforward. The space complexity is O(1) because you only need a constant amount of extra space beyond the input strings.'''


'''
Differences:
Brute-Force Approach:

Implementation:
You might directly compare the first character of every string, then the second character, and so on, for each position.
For each character position, you iterate through all strings to check if they match.
Efficiency:
Can be less efficient due to potential redundant comparisons and a straightforward implementation without optimizations.
For example, checking all characters for every position in a less optimized manner.
Optimal Approach:

Implementation:
Use the first string as the reference and compare its characters to the corresponding characters in all other strings.
This approach often involves fewer comparisons because once you find a mismatch, you can stop checking further positions.
Efficiency:
More optimized because it uses the first string as a reference and stops as soon as a mismatch is found.
Avoids unnecessary checks after the mismatch is detected.'''