class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums) + 1)]
        dic = {}
        result = []
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        for el, freq in  dic.items():
            bucket[freq].append(el)
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result





        
        

            

        