class Solution:
    def romanToInt(self, s: str) -> int:
        # Dictionary to map Roman numerals to their integer values
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        
        res = 0  # Initialize the result variable to store the final integer value
        
        for i in range(len(s)):
            # If the current numeral is smaller than the next numeral, subtract its value
            if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
                res -= roman[s[i]]
            else:
                # Otherwise, add its value to the result
                res += roman[s[i]]
        
        return res  # Return the final result

'''
### **Explanation:**

**Problem Overview:**
The task is to convert a Roman numeral string into its integer equivalent. Roman numerals use combinations of the letters `I, V, X, L, C, D, M` to represent values. The numeral system involves both additive and subtractive combinations.

**Step-by-Step Breakdown with Code Snippets:**

1. **Initialize the Mapping Dictionary:**
   ```python
   roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
   ```
   - **Purpose:** Create a dictionary `roman` that maps each Roman numeral character to its corresponding integer value.

2. **Initialize the Result Variable:**
   ```python
   res = 0
   ```
   - **Purpose:** Initialize `res` to `0`. This will store the cumulative integer value of the Roman numeral string as we process each character.

3. **Iterate Over the Characters in the String:**
   ```python
   for i in range(len(s)):
   ```
   - **Purpose:** Iterate over each character in the string `s`.

4. **Check if the Current Numeral Should be Subtracted:**
   ```python
   if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
       res -= roman[s[i]]
   ```
   - **Purpose:** If the current numeral `s[i]` is less than the next numeral `s[i + 1]`, it indicates a subtractive combination (e.g., `IV` for `4`). In this case, subtract the value of the current numeral from `res`.

5. **Add the Value if No Subtraction is Needed:**
   ```python
   else:
       res += roman[s[i]]
   ```
   - **Purpose:** If the current numeral is not part of a subtractive combination, simply add its value to `res`.

6. **Return the Final Result:**
   ```python
   return res
   ```
   - **Purpose:** After processing all characters, return the final integer value stored in `res`.

### **Example Walkthrough:**

**Example Input:**
- `s = "MCMXCIV"`

**Execution:**

1. **Initialize:**
   - `roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}`
   - `res = 0`

2. **Iteration 1 (`i = 0`):**
   - `s[i] = "M"`, `s[i + 1] = "C"`
   - `roman["M"] = 1000`, `roman["C"] = 100`
   - `1000 > 100`, so add `1000` to `res`. 
   - `res = 1000`

3. **Iteration 2 (`i = 1`):**
   - `s[i] = "C"`, `s[i + 1] = "M"`
   - `roman["C"] = 100`, `roman["M"] = 1000`
   - `100 < 1000`, so subtract `100` from `res`. 
   - `res = 1000 - 100 = 900`

4. **Iteration 3 (`i = 2`):**
   - `s[i] = "M"`, `s[i + 1] = "X"`
   - `roman["M"] = 1000`, `roman["X"] = 10`
   - `1000 > 10`, so add `1000` to `res`. 
   - `res = 900 + 1000 = 1900`

5. **Iteration 4 (`i = 3`):**
   - `s[i] = "X"`, `s[i + 1] = "C"`
   - `roman["X"] = 10`, `roman["C"] = 100`
   - `10 < 100`, so subtract `10` from `res`. 
   - `res = 1900 - 10 = 1890`

6. **Iteration 5 (`i = 4`):**
   - `s[i] = "C"`, `s[i + 1] = "I"`
   - `roman["C"] = 100`, `roman["I"] = 1`
   - `100 > 1`, so add `100` to `res`. 
   - `res = 1890 + 100 = 1990`

7. **Iteration 6 (`i = 5`):**
   - `s[i] = "I"`, `s[i + 1] = "V"`
   - `roman["I"] = 1`, `roman["V"] = 5`
   - `1 < 5`, so subtract `1` from `res`. 
   - `res = 1990 - 1 = 1989`

8. **Iteration 7 (`i = 6`):**
   - `s[i] = "V"`
   - No next numeral, so add `5` to `res`.
   - `res = 1989 + 5 = 1994`

**Result:**
- The integer value of `"MCMXCIV"` is `1994`.

### **Complexity Analysis:**

- **Time Complexity:** `O(N)`
  - The algorithm iterates over the Roman numeral string `s` once, where `N` is the length of the string. Each operation inside the loop is O(1).

- **Space Complexity:** `O(1)`
  - The space complexity is constant, as the only additional space used is for the dictionary `roman` and a few variables. The space used does not grow with the size of the input.'''


'''
Brute-force Solution:

First, let’s discuss the brute-force approach to the Roman numeral problem. The idea is to try all possible ways to parse the Roman numeral string into its integer value. For each character in the string, you would check every possible combination of characters to determine their values, and then compute the total value. This approach would involve a lot of redundant calculations and checking of all possible combinations, leading to a very inefficient solution.

The time complexity of this brute-force approach is exponential, O(2^n), because for each character, you potentially consider all combinations of the subsequent characters. It’s also very space inefficient due to the large number of possible combinations that need to be stored or processed.

Optimal Solution:

Now, let’s move on to the optimal solution. We use a dictionary to map Roman numerals to their integer values. By iterating through the string from left to right, we can efficiently compute the integer value by following these steps:

Initialize a result variable to store the final integer value.
Iterate through each character in the string.
For each character, check if its value is less than the value of the next character (if there is a next character). If it is, subtract its value from the result. Otherwise, add its value to the result.
Return the final integer value stored in the result.
The dictionary allows for quick lookups, making the conversion process straightforward and efficient. The time complexity of this approach is O(n), where n is the length of the string, as you are iterating through the string once. The space complexity is O(1) because you only use a constant amount of extra space for the dictionary and a few variables.'''