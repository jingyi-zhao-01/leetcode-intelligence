# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: make-string-anti-palindrome
# source_path: LeetCode-Solutions-master/Python/make-string-anti-palindrome.py
# solution_class: Solution2
# submission_id: f1e516d42fe2827901fea54866272cfaa84c5f85
# seed: 1409978423

# Time:  O(n + 26)
# Space: O(26)

# counting sort, greedy

class Solution2(object):
    def makeAntiPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        cnt = [0]*26
        for x in s:
            cnt[ord(x)-ord('a')] += 1
        if max(cnt) > len(s)//2:
            return "-1"
        result = [i for i, x in enumerate(cnt) for _ in xrange(x)]
        left = len(s)//2
        right = left+1
        while right < len(s) and result[right] == result[left]:
            right += 1 
        while result[left] == result[len(s)-1-left]:
            result[left] , result[right] = result[right], result[left]
            left += 1
            right += 1
        return "".join(map(lambda x: chr(ord('a')+x), result))