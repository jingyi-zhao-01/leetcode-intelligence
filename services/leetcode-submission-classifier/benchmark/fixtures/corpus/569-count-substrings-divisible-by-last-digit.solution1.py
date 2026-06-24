# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-substrings-divisible-by-last-digit
# source_path: LeetCode-Solutions-master/Python/count-substrings-divisible-by-last-digit.py
# solution_class: Solution
# submission_id: 04c7a2bdc955a73eb583cc41af8a24194d38e7d0
# seed: 1126375714

# Time:  O(d * n)
# Space: O(d)

# case works, math, freq table

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        # digit 1, 2, 5
        for i in xrange(len(s)):
            if s[i] in ('1', '2', '5'):
                result += i+1
        # digit 3, 6
        remain = 0
        cnt = [0]*3
        cnt[0] = 1
        for i in xrange(len(s)):
            remain = (remain+(ord(s[i])-ord('0')))%3
            if s[i] in ('3', '6'):
                result += cnt[remain]
            cnt[remain] += 1
        # digit 9
        remain = 0
        cnt = [0]*9
        cnt[0] = 1
        for i in xrange(len(s)):
            remain = (remain+(ord(s[i])-ord('0')))%9
            if s[i] == '9':
                result += cnt[remain]
            cnt[remain] += 1
        # digit 4
        for i in xrange(len(s)):
            if s[i] == '4':
                result += 1
                if i-1 >= 0 and int(s[i-1:i+1])%4 == 0:
                    result += i
        # digit 8
        for i in xrange(len(s)):
            if s[i] == '8':
                result += 1
                if i-1 >= 0 and int(s[i-1:i+1])%8 == 0:
                    result += 1
                if i-2 >= 0 and int(s[i-2:i+1])%8 == 0:
                    result += i-1
        # digit 7
        base = 1
        remain = 0
        cnt = [0]*7
        for i in xrange(len(s)):
            remain = (remain+base*(ord(s[~i])-ord('0')))%7
            result += cnt[remain]
            if s[~i] == '7':
                result += 1
                cnt[remain] += 1
            base = (base*10)%7
        return result