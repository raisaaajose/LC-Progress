#368. Largest Divisible Subset
#Dynamic programming

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        
        if not nums:
            return []

        # Sort the array
        nums.sort()
        n = len(nums)
        
        # dp[i]: size of largest divisible subset that ends with nums[i]
        dp = [1] * n
        prev = [-1] * n  # to reconstruct path
        max_index = 0    # index of the largest element in the largest subset

        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        prev[i] = j

            # Update index of max subset
            if dp[i] > dp[max_index]:
                max_index = i

        # Reconstruct the subset
        result = []
        while max_index != -1:
            result.append(nums[max_index])
            max_index = prev[max_index]

        return result[::-1]  # Reverse for correct order
