# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: finding-3-digit-even-numbers
# source_path: LeetCode-Solutions-master/Python/finding-3-digit-even-numbers.py
# solution_class: Solution2
# submission_id: 9c59d9724f76d5950e4d1265f32645271a08c0a4
# seed: 586504248

# Time:  O(1) ~ O(n), n is 10^3
# Space: O(1)

class Solution2(object):
    def findEvenNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        result, cnt = [], collections.Counter(digits)
        for i in xrange(1, 10):
            for j in xrange(10):
                for k in xrange(0, 10, 2):
                    if cnt[i] > 0 and cnt[j] > (j == i) and cnt[k] > (k == i) + (k == j):
                        result.append(i*100 + j*10 + k)
        return result