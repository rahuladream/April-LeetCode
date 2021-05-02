# https://leetcode.com/problems/course-schedule-iii/

from heapq import heapify, heappush, heappop

class Solution:
    def scheduleCourse(self, courses) -> int:
        """
        Sort the courses by their deadline
        Now one by one we start doing the courses.
        """

        if courses == None or len(courses) == 0:
            return 0
        
        courses.sort(key = lambda x: x[1])
        curr_time = count = 0
        max_heap = []
        heapify(max_heap)

        for i in range(len(courses)):
            heappush(max_heap, -1 * courses[i][0])
            curr_time += courses[i][0]
            count += 1
			
            if  curr_time > courses[i][1] :
                curr_time += heappop(max_heap)
                count -= 1

        return count


        


obj = Solution()
print(obj.scheduleCourse([[100,200],[200,1300],[1000,1250],[2000,3200]]))