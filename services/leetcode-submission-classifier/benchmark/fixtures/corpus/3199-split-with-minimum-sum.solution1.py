# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: split-with-minimum-sum
# source_path: LeetCode-Solutions-master/Python/split-with-minimum-sum.py
# solution_class: Solution
# submission_id: 23be19bc9053b30d59b9174dd7a4d0d5f2685c63
# seed: 1977810006

# Time:  O(mlogm), m = O(logn)
# Space: O(m)

# sort, greedy

class Solution(object):
    def splitNum(self, num):
        """
        :type num: int
        :rtype: int
        """
        sorted_num = "".join(sorted(str(num)))
        return int(sorted_num[::2])+int(sorted_num[1::2])