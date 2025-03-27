#2780. Minimum Index of a Valid Split
#find minimum index which can split array into 
#2 subarrays with each having same dominant element as parent
#hashmap

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        
        n=len(nums)
        if n==1:
            return -1

        #to find dominant element
        hmap={}
        for i in nums:
            hmap[i]=hmap.get(i,0)+1
        max_count=max(hmap.values())
        max_value=max(hmap, key=hmap.get)

        #find minimum index which can split array into 
        #2 subarrays with each having same dominant element as parent
        left_count=0

        for i in range(0,n-1):
            if nums[i]==max_value:
                left_count+=1
            if left_count*2>(i+1):
                if (max_count-left_count)*2>n-i-1:
                    return i
                else:
                    return -1
        return -1
        
