# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: button-with-longest-push-time
# source_path: LeetCode-Solutions-master/Python/button-with-longest-push-time.py
# solution_class: Solution
# submission_id: edf43378a1912f40f68d0fd8d191e723fd167b6a
# seed: 1430514184

# Time:  O(n)
# Space: O(1)

# array

class Solution(object):
    def buttonWithLongestTime(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        return -max((events[i][1]-(events[i-1][1] if i-1 >= 0 else 0), -events[i][0])for i in xrange(len(events)))[1]