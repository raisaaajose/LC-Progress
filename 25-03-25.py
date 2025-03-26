#3394. Check if Grid can be Cut into Sections
#horizontal and vertical sweeping to count gaps between rectangles to section area into 3 parts with lines

class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:

        rectangles=sorted(rectangles, key=lambda x:x[0])
        # horizontal sweeping, counting horizontal gaps for line
        gapcount1=0
        furthestEnd=rectangles[0][2]
        for i in range(1,len(rectangles)):
            if rectangles[i][0]>=furthestEnd:
                gapcount1+=1
                furthestEnd=rectangles[i][2]
            elif rectangles[i][0]<furthestEnd:
                furthestEnd=max(rectangles[i][2],furthestEnd)
        
        # vertical sweeping, counting vertical gaps for line
        rectangles=sorted(rectangles, key=lambda x:x[1])
        gapcount2=0
        furthestEnd=rectangles[0][3]
        for i in range(1,len(rectangles)):
            if rectangles[i][1]>=furthestEnd:
                gapcount2+=1
                furthestEnd=rectangles[i][3]
            elif rectangles[i][1]<furthestEnd:
                furthestEnd=max(rectangles[i][3],furthestEnd)

        if gapcount1>=2 or gapcount2>=2:
            return True
        else:
            return False


        
