class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)  # Convert wordDict to a set for O(1) lookups
        def backtrack(i):
            if i == len(s):
                return [""]  # Base case: if we reach the end of the string, return an empty string
            
            res = []  # List to store the possible sentences
            for j in range(i, len(s)):
                w = s[i:j+1]  # Extract the substring from index i to j
                if w not in wordDict:  # If the substring is not in wordDict, skip it
                    continue
                
                strings = backtrack(j + 1)  # Recursively call backtrack from index j+1
                if not strings:  # If no valid sentences are returned, skip this word
                    continue
                
                # For each valid substring, form sentences
                for substr in strings:
                    sentence = w
                    if substr:  # If the substring is not empty, append it to the current word
                        sentence += " " + substr
                    res.append(sentence)  # Add the full sentence to the result
            return res
        
        return backtrack(0)  # Start backtracking from the first character

'''
### **Explanation:**

The goal of this algorithm is to find all possible sentences that can be formed by segmenting the string `s` using words from the given `wordDict`. Each word in the sentence must be from `wordDict`, and the entire string `s` must be used. This problem is solved using backtracking, where we try different word splits and recursively solve the rest of the string.

#### **Steps:**

1. **Convert wordDict to a Set:**
   ```python
   wordDict = set(wordDict)
   ```
   - **Purpose:** Convert `wordDict` into a set for O(1) lookups, making the substring checks faster.

2. **Backtracking Function:**
   ```python
   def backtrack(i):
       if i == len(s):
           return [""]
   ```
   - **Purpose:** This function tries to find all possible valid word combinations starting from index `i`.
   - **Base Case:** If `i == len(s)`, it means we have reached the end of the string, so we return a list containing an empty string, which indicates that no further words need to be added.

3. **Try Different Word Splits:**
   ```python
   for j in range(i, len(s)):
       w = s[i:j+1]
       if w not in wordDict:
           continue
   ```
   - **Purpose:** Iterate over the substring from index `i` to `j` and extract potential words (`w`). If the word is not in `wordDict`, continue to the next substring.

4. **Recursively Call Backtrack:**
   ```python
   strings = backtrack(j + 1)
   if not strings:
       continue
   ```
   - **Purpose:** Recursively call `backtrack` starting from index `j + 1` (the character after the current word `w`). This step helps explore further word combinations after the current word.

5. **Form Full Sentences:**
   ```python
   for substr in strings:
       sentence = w
       if substr:
           sentence += " " + substr
       res.append(sentence)
   ```
   - **Purpose:** For each valid substring `substr` returned from the recursive call, form a sentence by combining `w` with the valid `substr`. If `substr` is not empty, concatenate it with `w` using a space. Add the full sentence to the result list `res`.

6. **Return the Result:**
   ```python
   return res
   ```
   - **Purpose:** After processing all valid word splits for the current position `i`, return the list of valid sentences.

7. **Initial Call:**
   ```python
   return backtrack(0)
   ```
   - **Purpose:** Start the backtracking process from the first character of the string `s`.

### **Example Walkthrough:**

Consider the input `s = "catsanddog"` and `wordDict = ["cat", "cats", "and", "sand", "dog"]`.

1. **First Call:**
   - `backtrack(0)` checks the substring "cat", which is in `wordDict`.
     - Recursively calls `backtrack(3)`.
   
2. **Second Call:**
   - `backtrack(3)` checks the substring "sand", which is in `wordDict`.
     - Recursively calls `backtrack(7)`.

3. **Third Call:**
   - `backtrack(7)` checks "dog", which is in `wordDict`.
     - Returns `["dog"]` as a valid sentence.

4. **Combining Results:**
   - `backtrack(3)` forms "sand dog" and returns it.
   - `backtrack(0)` forms "cat sand dog" and continues to check other possibilities.

5. **Final Output:**
   - Returns all valid combinations: `["cats and dog", "cat sand dog"]`.

### **Complexity Analysis:**

- **Time Complexity:** O(n * 2^n), where `n` is the length of the string `s`. The algorithm explores all possible splits and combinations of words, making the time complexity exponential in the worst case.
- **Space Complexity:** O(n), where `n` is the length of the string `s`. This is due to the recursion stack and the space needed to store the results.'''   


'''
**Brute-Force Solution:**

To solve the problem, we could use a brute-force approach where we generate all possible substrings of the input string and then check each one against the dictionary to see if it forms a valid word. This method involves recursively trying all possible splits of the string, which results in exploring every possible combination of words.

However, this brute-force approach is inefficient because it has exponential time complexity. The number of possible substrings grows exponentially with the length of the input string. Specifically, it would be \( O(2^n) \), where \( n \) is the length of the string. This is because for each character, we decide whether to include it in a substring or not, leading to a large number of potential combinations. As a result, this approach would be very slow for longer strings due to the high number of combinations to check.

brute force t explores all possible substrings without any pruning or optimization. but optimal the use of efficient set lookups and pruning of invalid paths during backtracking often makes it more feasible in practice than the brute-force method.
**Optimal Solution:**

The optimal solution uses a backtracking approach combined with a set for efficient word lookups. First, we convert the dictionary of valid words into a set to allow \( O(1) \) average time complexity for checking if a substring is a valid word. 

We then use a recursive backtracking function that explores all possible valid word combinations starting from each index of the string. The function checks if the substring from the current index to the next index is in the dictionary. If it is, the function recursively explores further from the next index. 

This approach allows us to build valid sentences efficiently and avoids exploring unnecessary combinations. The time complexity is \( O(n \cdot 2^n) \), as we need to explore all possible splits and combinations, but with the added efficiency of using a set for lookups. The space complexity is \( O(n) \), due to the recursion stack and the storage needed for the result list.
'''