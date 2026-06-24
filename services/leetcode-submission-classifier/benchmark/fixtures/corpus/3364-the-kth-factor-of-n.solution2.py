# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: the-kth-factor-of-n
# source_path: LeetCode-Solutions-master/Python/the-kth-factor-of-n.py
# solution_class: Solution2
# submission_id: 5bf3ac939865118650194ae99cd10702bf9b20c7
# seed: 3832226232

# Time:  O(sqrt(n))
# Space: O(1)

class Solution2(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        result = []
        i = 1
        while i*i <= n:
            if not n%i:
                if i*i != n:
                    result.append(i)
                k -= 1
                if not k:
                    return i
            i += 1
        return -1 if k > len(result) else n//result[-k]