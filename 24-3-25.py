# 3169. Count Days Without Meetings
# meeting intervals can overlap, find days without any scheduled meetings
# sort, merge meetings with overlapping intervals, count booked days, subtract from total
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        merged_meetings=[]
        
        for meeting in meetings:
            if not merged_meetings or merged_meetings[-1][1]<meeting[0]:
                merged_meetings.append(meeting)
            elif meeting[0]<=merged_meetings[-1][1]:
                merged_meetings[-1][1]=max(meeting[1],merged_meetings[-1][1])
        count=0
        for x,y in merged_meetings:
            count+=(y-x+1)
        return days-count


        
