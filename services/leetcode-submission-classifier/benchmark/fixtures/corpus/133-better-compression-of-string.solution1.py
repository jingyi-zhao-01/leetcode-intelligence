# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: better-compression-of-string
# source_path: LeetCode-Solutions-master/Python/better-compression-of-string.py
# solution_class: Solution
# submission_id: 25f5be888073ff9f435a72bd23db3adda9743a76
# seed: 2025103704

# Time:  O(n + 26)
# Space: O(26)

# freq table, counting sort

class Solution(object):
    def betterCompression(self, compressed):
        """
        :type compressed: str
        :rtype: str
        """
        cnt = [0]*26
        x, curr = -1, 0
        for i in xrange(len(compressed)):
            if not compressed[i].isdigit():
                x = ord(compressed[i])-ord('a')
                continue
            curr = curr*10+int(compressed[i])
            if i+1 == len(compressed) or not compressed[i+1].isdigit():
                cnt[x] += curr
                curr = 0
        return "".join("%s%s" % (chr(ord('a')+i), x) for i, x in enumerate(cnt) if x)