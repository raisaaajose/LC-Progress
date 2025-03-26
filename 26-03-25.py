#2033. Minimum Operations to Make a Uni-Value Grid
#finding median in a list to get calculate minimum number of additions/subtractions with a given integer x to reach one common value
#notes: using numpy to flatten 2d grid reduces runtime a LOT, use list comprehension instead
class Solution:
    
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        
        grid=[num for row in grid for num in row]
        mod=grid[0]%x
    
        #to find the median to find optimal goal for each element
        grid.sort()
        
        median=grid[len(grid)//2]
        count=0
        for i in grid:
            if i%x!=mod:
                return -1
            
            
        return sum(abs(num - median) // x for num in grid)

        

        
