class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        sorted_salaries = sorted(salary)
        total=0
        for i in range (1,len(sorted_salaries)-1):
            total = total + sorted_salaries[i]
        avg_salaries=total/float((len(sorted_salaries)-2))

        return avg_salaries
