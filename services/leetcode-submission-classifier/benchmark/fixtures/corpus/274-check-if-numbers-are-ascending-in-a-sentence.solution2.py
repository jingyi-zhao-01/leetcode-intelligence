# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-if-numbers-are-ascending-in-a-sentence
# source_path: LeetCode-Solutions-master/Python/check-if-numbers-are-ascending-in-a-sentence.py
# solution_class: Solution2
# submission_id: 7eee78752fb4a0eea64c97d9fbf8eba55dfd1790
# seed: 3313608816

# Time:  O(n)
# Space: O(1)

class Solution2(object):
    def areNumbersAscending(self, s):
        """
        :type s: str
        :rtype: bool
        """
        nums = [int(x) for x in s.split() if x.isdigit()]
        return all(nums[i] < nums[i+1] for i in xrange(len(nums)-1))