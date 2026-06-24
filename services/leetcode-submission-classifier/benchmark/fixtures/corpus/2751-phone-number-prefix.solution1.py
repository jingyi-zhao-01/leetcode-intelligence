# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: phone-number-prefix
# source_path: LeetCode-Solutions-master/Python/phone-number-prefix.py
# solution_class: Solution
# submission_id: 3a378f29a6ffdfa0e66ae3e916cf581f35cff6c1
# seed: 2364562660

# Time:  O(l * nlogn)
# Space: O(1)

# sort

class Solution(object):
    def phonePrefix(self, numbers):
        """
        :type numbers: List[str]
        :rtype: bool
        """
        numbers.sort()
        return all(not numbers[i+1].startswith(numbers[i]) for i in xrange(len(numbers)-1))