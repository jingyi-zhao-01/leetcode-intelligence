# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: self-dividing-numbers
# source_path: LeetCode-Solutions-master/Python/self-dividing-numbers.py
# solution_class: Solution2
# submission_id: dc8ab640a2c44e13d15c4b951503a19306a61a6d
# seed: 344480754

# Time:  O(nlogr) = O(n)
# Space: O(logr) = O(1)

class Solution2(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        return [num for num in xrange(left, right+1) \
                if not any(itertools.imap(lambda x: int(x) == 0 or num%int(x) != 0, str(num)))]