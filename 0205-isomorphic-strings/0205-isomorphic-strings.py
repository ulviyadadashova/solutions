class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapST, mapTS = {}, {}  # Dictionaries to map characters from s to t and t to s
        
        for c1, c2 in zip(s, t):  # Iterate through pairs of characters from s and t
            if (c1 in mapST and mapST[c1] != c2) or (c2 in mapTS and mapTS[c2] != c1):
                return False  # If there's a mismatch in the current mapping, return False
            mapST[c1] = c2  # Map character c1 from s to c2 from t
            mapTS[c2] = c1  # Map character c2 from t to c1 from s

        return True  # If all mappings are consistent, return True

'''
### **Explanation:**

1. **Initialization:**
   ```python
   mapST, mapTS = {}, {}
   ```
   - **Purpose:**
     - `mapST` will store mappings from characters in `s` to characters in `t`.
     - `mapTS` will store mappings from characters in `t` to characters in `s`.

2. **Iterate Through Character Pairs:**
   ```python
   for c1, c2 in zip(s, t):
   ```
   - **Purpose:**
     - Use `zip` to iterate through characters from both strings `s` and `t` simultaneously. Each pair `(c1, c2)` corresponds to characters from `s` and `t` at the same position.

3. **Check for Consistency:**
   ```python
   if (c1 in mapST and mapST[c1] != c2) or (c2 in mapTS and mapTS[c2] != c1):
       return False
   ```
   - **Purpose:**
     - Ensure that if `c1` is already mapped to a character in `t`, it must map to `c2`.
     - Similarly, if `c2` is already mapped to a character in `s`, it must map to `c1`.
     - If there is any inconsistency in these mappings, return `False`.

4. **Update Mappings:**
   ```python
   mapST[c1] = c2
   mapTS[c2] = c1
   ```
   - **Purpose:**
     - Update the dictionaries to reflect the current character pair. `c1` from `s` maps to `c2` in `t`, and `c2` from `t` maps to `c1` in `s`.

5. **Return Result:**
   ```python
   return True
   ```
   - **Purpose:**
     - If all character mappings are consistent throughout the loop, return `True`, indicating that the strings `s` and `t` are isomorphic.

### **Example Walkthrough:**

For `s = "paper"` and `t = "title"`:

- **Initialization:** `mapST = {}`, `mapTS = {}`
- **Iteration 1:** `c1 = 'p'`, `c2 = 't'`
  - `mapST` becomes `{'p': 't'}`
  - `mapTS` becomes `{'t': 'p'}`
- **Iteration 2:** `c1 = 'a'`, `c2 = 'i'`
  - `mapST` becomes `{'p': 't', 'a': 'i'}`
  - `mapTS` becomes `{'t': 'p', 'i': 'a'}`
- **Iteration 3:** `c1 = 'p'`, `c2 = 't'`
  - Consistent with previous mappings
- **Iteration 4:** `c1 = 'e'`, `c2 = 'l'`
  - `mapST` becomes `{'p': 't', 'a': 'i', 'e': 'l'}`
  - `mapTS` becomes `{'t': 'p', 'i': 'a', 'l': 'e'}`
- **Iteration 5:** `c1 = 'r'`, `c2 = 'e'`
  - `mapST` becomes `{'p': 't', 'a': 'i', 'e': 'l', 'r': 'e'}`
  - `mapTS` becomes `{'t': 'p', 'i': 'a', 'l': 'e', 'e': 'r'}`

**Result:** All mappings are consistent, so the function returns `True`.

### **Complexity Analysis:**

- **Time Complexity:** O(n), where `n` is the length of the strings `s` and `t`. We iterate through the characters once.
- **Space Complexity:** O(1), as the space used for the dictionaries is limited to the number of unique characters, which is constant for the given problem constraints.'''


'''
Brute Force Solution
To solve the isomorphic strings problem using a brute-force approach, we would:

Iterate through Both Strings: For each character in string S, compare it with the corresponding character in string T.
Check for Consistency: Check if the current character in S consistently maps to the current character in T and vice versa. This involves two primary checks:
If a character in S is already mapped to a different character in T than expected.
If a character in T is already mapped to a different character in S than expected.
Return Result: If any inconsistencies are found during the checks, return false. If all character mappings are consistent, return true.
Why It Is Inefficient:

Time Complexity: The brute force approach involves checking all character mappings for every position, resulting in a time complexity of O(n^2), where n is the length of the strings. This inefficiency arises because we are comparing each character with all previous mappings in a nested loop.
Space Complexity: This approach may also use additional space to store mappings, resulting in a higher space complexity depending on the implementation.
Optimal Solution
For an optimal solution, we use two hash maps (or dictionaries) to track the character mappings:

Initialize Mappings: Create two dictionaries:

mapST to store the mapping from characters in S to characters in T.
mapTS to store the mapping from characters in T to characters in S.
Iterate Through Both Strings Simultaneously: As you iterate through both strings:

For each pair of characters (c1, c2) where c1 is from S and c2 is from T:
Check Mapping Consistency:
Ensure that c1 is consistently mapped to c2 using mapST.
Ensure that c2 is consistently mapped to c1 using mapTS.
If c1 is mapped to a different character than c2 or c2 is mapped to a different character than c1, return false.
Otherwise, update both mappings: mapST[c1] = c2 and mapTS[c2] = c1.
Return Result: If all pairs are consistent throughout the iteration, return true.

Why It Is Efficient:

Time Complexity: The optimal solution has a time complexity of O(n) because we only iterate through the strings once, performing constant-time operations for each character.
Space Complexity: The space complexity is O(1) since the size of the mappings is bounded by the number of unique characters, which is limited to a fixed number of characters (e.g., 256 for ASCII). This makes the space requirement effectively constant.'''