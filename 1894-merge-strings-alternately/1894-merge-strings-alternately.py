class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = j = 0  # Initialize pointers for both words
        res = []  # Initialize an empty list to store the merged characters

        # Merge characters alternately while both words have characters left
        while i < len(word1) and j < len(word2):
            res.append(word1[i])  # Add character from word1
            res.append(word2[j])  # Add character from word2
            i += 1  # Move pointer i to the next character in word1
            j += 1  # Move pointer j to the next character in word2

        # Add the remaining characters from word1 (if any)
        res.append(word1[i:])

        # Add the remaining characters from word2 (if any)
        res.append(word2[j:])

        # Join the list of characters into a string and return it
        return ''.join(res)

'''
### **Explanation:**

**Problem Overview:**
The goal is to merge two strings, `word1` and `word2`, by alternating characters from each string. If one string is longer than the other, the remaining characters from the longer string should be appended to the result.

**Step-by-Step Breakdown with Code Snippets:**

1. **Initialize Pointers and Result List:**
   ```python
   i = j = 0
   res = []
   ```
   - **Purpose:** 
     - `i` and `j` are pointers initialized to the start of `word1` and `word2` respectively.
     - `res` is an empty list that will store the characters of the merged string.

2. **Merge Characters Alternately:**
   ```python
   while i < len(word1) and j < len(word2):
       res.append(word1[i])
       res.append(word2[j])
       i += 1
       j += 1
   ```
   - **Purpose:** 
     - The loop continues as long as there are characters left in both `word1` and `word2`.
     - For each iteration, a character from `word1` and a character from `word2` are added to `res`.
     - The pointers `i` and `j` are incremented to move to the next character in each word.

3. **Append Remaining Characters (if any):**
   ```python
   res.append(word1[i:])
   res.append(word2[j:])
   ```
   - **Purpose:** 
     - After the loop, if there are remaining characters in `word1` or `word2`, they are appended to `res`.
     - `word1[i:]` slices `word1` from the current position of `i` to the end, adding all remaining characters.
     - `word2[j:]` does the same for `word2`.

4. **Join the List into a String:**
   ```python
   return ''.join(res)
   ```
   - **Purpose:** 
     - The list `res` contains all the characters in the desired order. The `join` method is used to concatenate the list into a single string, which is then returned as the result.

### **Example Walkthrough:**

**Example Input:**
- `word1 = "abc"`
- `word2 = "pqr"`

**Execution:**

1. **Initialization:**
   - `i = 0`, `j = 0`
   - `res = []`

2. **Iteration 1:**
   - `res.append(word1[i])` → `res = ['a']`
   - `res.append(word2[j])` → `res = ['a', 'p']`
   - Increment `i` and `j` → `i = 1`, `j = 1`

3. **Iteration 2:**
   - `res.append(word1[i])` → `res = ['a', 'p', 'b']`
   - `res.append(word2[j])` → `res = ['a', 'p', 'b', 'q']`
   - Increment `i` and `j` → `i = 2`, `j = 2`

4. **Iteration 3:**
   - `res.append(word1[i])` → `res = ['a', 'p', 'b', 'q', 'c']`
   - `res.append(word2[j])` → `res = ['a', 'p', 'b', 'q', 'c', 'r']`
   - Increment `i` and `j` → `i = 3`, `j = 3`

5. **Final Steps:**
   - Both `i` and `j` have reached the end of `word1` and `word2`.
   - The loop ends, and the remaining characters are appended (none in this case).
   - `''.join(res)` returns `"apbqcr"`.

**Result:**
- The merged string is `"apbqcr"`.

### **Complexity Analysis:**

- **Time Complexity:** `O(N + M)`
  - Where `N` is the length of `word1` and `M` is the length of `word2`. Each character is processed once.

- **Space Complexity:** `O(N + M)`
  - The space complexity is proportional to the total length of the output string, which contains all characters from both `word1` and `word2`.

This approach effectively merges the two strings alternately and handles any remaining characters at the end.'''


'''
Brute-force Solution:
In the brute-force approach, we can think of merging the two strings by simply taking each character one by one, without worrying too much about doing it efficiently.

Basic Idea: You start with an empty result string. Then, you go through each character in the first word, add it to the result, and then go through the second word, adding its character. You keep alternating between the two words until you’ve added all their characters.

Extra Steps: If one word is longer than the other, you would keep checking which word has leftover characters, then add those to the result at the end.

Why It's Inefficient:

Repeated Work: You might end up doing extra checks or operations, like repeatedly checking the length of each word to see if there are any characters left, which makes it slower.

More Memory Used: You might create new strings each time you add a character, which uses more memory and takes more time.because strings are immutable, every time you add a character to the string, a new string is created. This involves copying the existing string and then adding the new character to it.

---

**Optimal Solution:**

"Now, let's move on to a more optimal solution. Instead of repeatedly concatenating strings, we can use a list to store the merged characters. We start by initializing two pointers at the beginning of `word1` and `word2`. We also initialize an empty list `rest` to store the merged characters. We then use a `while` loop to alternate between adding characters from `word1` and `word2` to the list, advancing the pointers after each addition.

After the loop ends, if there are any remaining characters in either word, we append them to the list as well. Finally, we join the list into a string and return the result. This approach avoids the inefficiency of repeated string concatenation by using a list, which allows for efficient appending operations."

**Efficiency:**

"The time complexity of this solution is \(O(n + m)\), where \(n\) and \(m\) are the lengths of the two words, respectively. This is because we are iterating over each character in both words exactly once. The space complexity is also \(O(n + m)\) since we’re storing all the characters in a list before joining them into the final string. This makes the solution both time and space efficient, and it avoids the pitfalls of the brute-force approach."
'''
