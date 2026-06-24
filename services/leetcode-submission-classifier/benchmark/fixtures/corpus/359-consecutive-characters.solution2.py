# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: consecutive-characters
# source_path: LeetCode-Solutions-master/Python/consecutive-characters.py
# solution_class: Solution2
# submission_id: 30e868df7ea92e9ffe6c98fc0bc3d2e211ab410b
# seed: 909560623

# Time:  O(n)
# Space: O(1)

class Solution2(object):
    def maxPower(self, s):
        return max(len(list(v)) for _, v in itertools.groupby(s))