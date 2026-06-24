# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: determine-if-two-events-have-conflict
# source_path: LeetCode-Solutions-master/Python/determine-if-two-events-have-conflict.py
# solution_class: Solution
# submission_id: 0e9a510a6bc40a3e691138fe4fe06ad480e77518
# seed: 1577006541

# Time:  O(1)
# Space: O(1)

# array

class Solution(object):
    def haveConflict(self, event1, event2):
        """
        :type event1: List[str]
        :type event2: List[str]
        :rtype: bool
        """
        return max(event1[0], event2[0]) <= min(event1[1], event2[1])