# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-substrings-with-k-frequency-characters-i
# source_path: LeetCode-Solutions-master/Python/count-substrings-with-k-frequency-characters-i.py
# solution_class: Solution
# submission_id: fe99c87102183e6393c34cd1be470fc361bd689d
# seed: 1708638628

# Time:  O(n + 26)
# Space: O(26)

# freq table, two pointers, sliding window

class Solution(object):
    def numberOfSubstrings(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        def count():
            cnt = [0]*26
            result= left = 0
            for right in xrange(len(s)):
                cnt[ord(s[right])-ord('a')] += 1
                while cnt[ord(s[right])-ord('a')] == k:
                    cnt[ord(s[left])-ord('a')] -= 1
                    left += 1
                result += right-left+1
            return result
                
        return (len(s)+1)*len(s)//2-count()