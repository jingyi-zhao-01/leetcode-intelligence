# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: lexicographically-smallest-string-after-reverse
# source_path: LeetCode-Solutions-master/Python/lexicographically-smallest-string-after-reverse.py
# solution_class: Solution2
# submission_id: 4bc22f155fab2c4c9a150251a758f21c00e2c607
# seed: 3184385005

# Time:  O(nlogn)
# Space: O(n)

# rolling hash, binary search

class Solution2(object):
    def lexSmallest(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = s
        for k in xrange(2, len(s)+1):
            result = min(result, s[:k][::-1]+s[k:], s[:-k]+s[-k:][::-1])
        return result