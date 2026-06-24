# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: equalize-strings-by-adding-or-removing-characters-at-ends
# source_path: LeetCode-Solutions-master/Python/equalize-strings-by-adding-or-removing-characters-at-ends.py
# solution_class: Solution2
# submission_id: a01b4eda505d01ec2c0553c248fdea42bb6e78fb
# seed: 231259436

# Time:  O((n + m) * log(min(n, m)))
# Space: O(min(n, m))

# binary search, rolling hash

class Solution2(object):
    def minOperations(self, initial, target):
        """
        :type initial: str
        :type target: str
        :rtype: int
        """
        result = 0
        for k in xrange(2):
            for i in xrange(k, len(initial)):
                curr = 0
                for j in xrange(min(len(initial)-i, len(target))):
                    curr = curr+1 if initial[i+j] == target[j] else 0
                    result = max(result, curr)
            initial, target = target, initial
        return len(initial)+len(target)-2*result