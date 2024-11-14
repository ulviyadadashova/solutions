class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        output = []
        def backtrack(first = 0, curr = [], currSum = 0):
            if currSum == target:
                output.append(curr[:])
            if currSum > target:
                return
            for i in range(first, n):
                curr.append(candidates[i])
                backtrack(i, curr, currSum + candidates[i])
                curr.pop()
        backtrack()
        return output


        