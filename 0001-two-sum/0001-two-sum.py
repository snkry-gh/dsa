class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idxMap = {}

        for i, n in enumerate(nums):
            comp = target - n

            if comp in idxMap:
                return [i, idxMap[comp]]
            
            idxMap[n] = i