class Solution(object):
    def longestObstacleCourseAtEachPosition(self, obstacles):
        """
        :type obstacles: List[int]
        :rtype: List[int]
        """
        valid_obstacle=[]
        out=[]
        
        for i in obstacles:
            br=bisect_right(valid_obstacle,i)
            if br==len(valid_obstacle):
                valid_obstacle.append(i)
            else:
                valid_obstacle[br]=i
            out.append(br+1)
        return out