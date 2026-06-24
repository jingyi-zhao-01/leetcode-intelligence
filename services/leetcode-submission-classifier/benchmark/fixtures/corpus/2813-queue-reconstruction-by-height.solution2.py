# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: queue-reconstruction-by-height
# source_path: LeetCode-Solutions-master/Python/queue-reconstruction-by-height.py
# solution_class: Solution2
# submission_id: 3566d778a229211f287f2661b5db15e42e57e319
# seed: 2196334285

# Time:  O(n * sqrt(n))
# Space: O(n)

class Solution2(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key=lambda h_k1: (-h_k1[0], h_k1[1]))
        result = []
        for p in people:
            result.insert(p[1], p)
        return result