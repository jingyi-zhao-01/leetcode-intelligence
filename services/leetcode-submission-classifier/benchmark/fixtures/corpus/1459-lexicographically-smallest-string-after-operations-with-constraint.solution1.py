# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: lexicographically-smallest-string-after-operations-with-constraint
# source_path: LeetCode-Solutions-master/Python/lexicographically-smallest-string-after-operations-with-constraint.py
# solution_class: Solution
# submission_id: e30558e597022488868deec83d12c829a8f60cc5
# seed: 755316105

# Time:  O(n)
# Space: O(1)

# greedy

class Solution(object):
    def getSmallestString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        result = map(lambda x: ord(x)-ord('a'), s)
        for i in xrange(len(result)):
            d = min(result[i]-0, 26-result[i])
            result[i] = 0 if d <= k else result[i]-k
            k -= min(d, k)
            if k == 0:
                break
        return "".join(map(lambda x: chr(x+ord('a')), result))