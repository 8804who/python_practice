class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        answer = 1440
        points = []
        time_set = set()

        for time in timePoints:
            if time in time_set:
                return 0
            time_set.add(time)
            spl = time.split(":")
            points.append(int(spl[0])*60+int(spl[1]))

        points.sort()

        for i in range(1, len(points)):
            if answer > points[i]-points[i-1]:
                answer = points[i]-points[i-1]

        if answer > points[0] + 1440 - points[-1]:
            answer = points[0] + 1440 - points[-1]
        return answer