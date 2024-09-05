from random import choice

class RandomizedSet:
    
    def __init__(self):
        self.dict = {}  # A dictionary to store the value-to-index mapping
        self.list = []  # A list to store the actual elements

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False  # If the value is already present, return False
        
        self.dict[val] = len(self.list)  # Store the index of the value in the list
        self.list.append(val)  # Append the value to the list
        
        return True  # Return True as the insertion is successful

    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False  # If the value is not present, return False
        
        idx, last_element = self.dict[val], self.list[-1]  # Get the index and the last element
        self.list[idx], self.dict[last_element] = last_element, idx  # Swap the value with the last element
        self.list.pop()  # Remove the last element from the list
        del self.dict[val]  # Remove the value from the dictionary
        
        return True  # Return True as the removal is successful

    def getRandom(self) -> int:
        return choice(self.list)  # Return a random element from the list

'''
### **Explanation:**

The goal of this class is to implement a set-like data structure that allows insertion, deletion, and retrieval of a random element, all in average constant time.

#### **Steps:**

1. **Initialization:**
   ```python
   self.dict = {}
   self.list = []
   ```
   - **Purpose:** 
     - `self.dict`: A dictionary that maps each value to its index in the list.
     - `self.list`: A list that stores the actual values. This helps in `O(1)` access to any element, which is essential for getting a random element efficiently.

2. **Insert Method:**
   ```python
   if val in self.dict:
       return False
   self.dict[val] = len(self.list)
   self.list.append(val)
   return True
   ```
   - **Purpose:** The `insert` method adds a value to the set if it doesn't already exist.
     - **Check for Existence:** If the value is already present in the `dict`, return `False`.
     - **Insert the Value:** If the value is not present, insert it in `self.list` and store its index in `self.dict`.
     - Return `True` to indicate the insertion was successful.

3. **Remove Method:**
   ```python
   if val not in self.dict:
       return False
   idx, last_element = self.dict[val], self.list[-1]
   self.list[idx], self.dict[last_element] = last_element, idx
   self.list.pop()
   del self.dict[val]
   return True
   ```
   - **Purpose:** The `remove` method deletes a value from the set.
     - **Check for Existence:** If the value is not in `self.dict`, return `False`.
     - **Remove Efficiently:** To maintain constant time deletion:
       - Swap the value to be removed with the last element in the list.
       - Update the dictionary with the new index of the last element.
       - Remove the last element and delete the value from the dictionary.
     - Return `True` to indicate the deletion was successful.

4. **Get Random Method:**
   ```python
   return choice(self.list)
   ```
   - **Purpose:** The `getRandom` method returns a random element from the list using Python's `choice` function. Since the list maintains the values, getting a random element takes constant time.

### **Example Walkthrough:**

Let's go through an example:

```python
rs = RandomizedSet()
print(rs.insert(1))  # Output: True
print(rs.insert(2))  # Output: True
print(rs.remove(1))  # Output: True
print(rs.getRandom())  # Output: 2 (since 1 is removed)
```

1. **Insert 1:**
   - `list = [1]`, `dict = {1: 0}`.
   - Returns `True`.

2. **Insert 2:**
   - `list = [1, 2]`, `dict = {1: 0, 2: 1}`.
   - Returns `True`.

3. **Remove 1:**
   - Swap `1` with `2`, so the list becomes `[2]` and the dictionary becomes `{2: 0}`.
   - Returns `True`.

4. **Get Random:**
   - Only `2` is in the list, so `getRandom()` will return `2`.

### **Complexity Analysis:**

- **Time Complexity:** O(1) for all operations (`insert`, `remove`, `getRandom`), as all involve constant-time operations such as dictionary lookups and list operations.
- **Space Complexity:** O(n), where `n` is the number of elements in the set. The space is used by both the dictionary and the list.'''


'''
if in the question it says do it in O(1) then no need for bruteforce
Brute force Solution:

"To solve the Insert, Delete, and GetRandom problem, one approach might be to use a list to store the elements and perform operations directly on this list. For instance, to insert an element, we would check if it already exists and, if not, add it to the list. To delete an element, we would search for it and remove it from the list. To get a random element, we would use Python's random.choice() to pick an element from the list. However, this approach has inefficiencies. Insertion and deletion operations could take O(n) time in the worst case because finding an element and shifting elements in the list is costly. This inefficiency makes this solution impractical for scenarios where fast operations are required."

Optimal Solution:

"Instead, we can use a combination of a dictionary and a list. The dictionary will map each value to its index in the list, allowing us to perform insertions and deletions in O(1) time. The list will store the actual values and enable us to get a random element in O(1) time.

For insertion, we first check if the value is already in the dictionary. If it's not present, we add it to both the dictionary and the list, mapping the value to its index in the dictionary and appending it to the list.

For deletion, we check if the value is in the dictionary. If it is, we get its index and swap it with the last element in the list to facilitate removal in constant time. We then update the dictionary with the new index of the last element, pop the last element from the list, and delete the value from the dictionary.

In the GetRandom function, we use Python’s random.choice() to select a random element from the list, which is efficient because accessing an element in a list is O(1).

This approach ensures that all operations—insert, delete, and get random—are performed in O(1) time, and the space complexity is O(n) where n is the number of elements in the set, accounting for both the list and dictionary storage.'''
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()