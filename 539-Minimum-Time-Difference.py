class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        ans = 2000
        minutes = [0]*(len(timePoints)) 
        # convert all into minutes 
        for i in range(len(minutes)):
            minutes[i] = (int(timePoints[i][:2])*60)+int(timePoints[i][3:])
            
        # sort minutes
        minutes.sort()

        # calc the min difference
        for i in range(1,len(minutes)):
            ans = min(ans,(minutes[i]-minutes[i-1]))

        return min(ans,(24*60)-minutes[-1]+minutes[0])

            
        