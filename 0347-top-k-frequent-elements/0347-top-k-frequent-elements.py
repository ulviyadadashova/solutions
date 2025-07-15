class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums) + 1)]
        dic = {}
        result = []
        for num in nums:
            dic[num] = 1 + dic.get(num, 0)
        for num, count in dic.items():
            bucket[count].append(num)
        for i in range(len(bucket) - 1, 0, -1):
            for n in bucket[i]:
                result.append(n)
                if len(result) == k:
                    return result
# Time - O(n)
# Space - O(n)
# Brute - iterate over array and implement count opration to each number and find the most frequent number this way and add it to result array. if its lenght is not k then continue checking but the most frequest one cant be if it is in result array already so it will be for loop in while loop so the time will be o(n square)








        
        

            

        