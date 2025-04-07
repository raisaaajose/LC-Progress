#416. Partition Equal Subset Sum
#Dynamic Programming

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s=sum(nums)
        if s%2!=0:
            return False
        else:
            target=s//2
            dp=[False]*(target+1)
            dp[0]=True

            for num in nums:
                for i in range(target,num-1,-1):
                    dp[i]=dp[i] or dp[i-num]
            return dp[target]
