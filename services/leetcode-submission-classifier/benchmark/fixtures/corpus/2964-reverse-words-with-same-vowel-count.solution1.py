# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: reverse-words-with-same-vowel-count
# source_path: LeetCode-Solutions-master/Python/reverse-words-with-same-vowel-count.py
# solution_class: Solution
# submission_id: 7dae5a428b35a8e348065f94743136cfb92b2aeb
# seed: 2975509785

# Time:  O(n)
# Space: O(1)

# string, inplace

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        VOWELS = set("aeiou")
        def count(left, right):
            return sum(s[i] in VOWELS for i in xrange(left, right+1))

        def reverse(left, right):
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        s = list(s)
        l, cnt = 0, -1
        for i in xrange(len(s)):
            if s[i] == ' ':
                l = 0
                continue
            l += 1
            if i+1 < len(s) and s[i+1] != ' ':
                continue
            c = count(i-l+1, i)
            if cnt == -1:
                cnt = c
            elif cnt == c:
                reverse(i-l+1, i)
        return "".join(s)