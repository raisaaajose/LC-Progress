#1863. Sum of All Subset XOR Totals
#recursion for xor of all subsets and summing then up (easy)

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def XORofsubset(nums,idx,xor):
            if idx==len(nums):
                return xor
            withcurr=XORofsubset(nums,idx+1,xor^nums[idx])
            withoutcurr=XORofsubset(nums,idx+1,xor)
            return withcurr+withoutcurr

        return XORofsubset(nums,0,0)
        
