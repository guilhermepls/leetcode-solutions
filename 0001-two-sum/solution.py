class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        vistos = {} 
        for i, num in enumerate(nums): 
            complemento = target - num 

            if complemento in vistos: 
                return [vistos[complemento], i]
        
            vistos[num] = i