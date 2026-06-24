# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: apple-redistribution-into-boxes
# source_path: LeetCode-Solutions-master/Python/apple-redistribution-into-boxes.py
# solution_class: Solution
# submission_id: 881852acd3260cd658f35e3ad33061cd7353c46e
# seed: 2047481150

# Time:  O(nlogn)
# Space: O(1)

# sort, greedy

class Solution(object):
    def minimumBoxes(self, apple, capacity):
        """
        :type apple: List[int]
        :type capacity: List[int]
        :rtype: int
        """
        capacity.sort(reverse=True)
        total = sum(apple)
        for i in xrange(len(capacity)):
            total -= capacity[i]
            if total <= 0:
                return i+1
        return -1