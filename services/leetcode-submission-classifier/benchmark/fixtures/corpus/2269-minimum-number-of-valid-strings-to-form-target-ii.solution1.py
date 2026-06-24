# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-number-of-valid-strings-to-form-target-ii
# source_path: LeetCode-Solutions-master/Python/minimum-number-of-valid-strings-to-form-target-ii.py
# solution_class: Solution
# submission_id: 04bde0bc9654c572c6613499e780d7eb0388b3ac
# seed: 231810040

# Time:  O(n + w * l)
# Space: O(n + w * l)

# rolling hash, hash table, two pointers, sliding window, dp

class Solution(object):
    def minValidStrings(self, words, target):
        """
        :type words: List[str]
        :type target: str
        :rtype: int
        """
        MOD, P = 10**9+7, 131
        power = [1]
        for _ in xrange(len(target)):
            power.append(power[-1]*P%MOD)
        lookup = set()
        for w in words:
            h = 0
            for x in w:
                h = (h*P+(ord(x)-ord('a')+1))%MOD
                lookup.add(h)
        dp = [0]*(len(target)+1)
        left = h = 0
        for right in xrange(len(target)):
            h = (h*P+(ord(target[right])-ord('a')+1))%MOD
            while right-left+1 >= 1 and h not in lookup:
                h = (h-(ord(target[left])-ord('a')+1)*power[(right-left+1)-1])%MOD
                left += 1
            if right-left+1 == 0:
                return -1
            dp[right+1] = dp[(right-(right-left+1))+1]+1
        return dp[-1]