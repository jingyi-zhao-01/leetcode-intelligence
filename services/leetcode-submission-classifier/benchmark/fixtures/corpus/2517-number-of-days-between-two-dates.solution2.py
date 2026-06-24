# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-days-between-two-dates
# source_path: LeetCode-Solutions-master/Python/number-of-days-between-two-dates.py
# solution_class: Solution2
# submission_id: 075032cd26102efdcb973ec9e78d7c41d4e38548
# seed: 2078177300

# Time:  O(1)
# Space: O(1)

class Solution2(object):
    def daysBetweenDates(self, date1, date2):        
        delta = datetime.datetime.strptime(date1, "%Y-%m-%d")
        delta -= datetime.datetime.strptime(date2, "%Y-%m-%d")
        return abs(delta.days)