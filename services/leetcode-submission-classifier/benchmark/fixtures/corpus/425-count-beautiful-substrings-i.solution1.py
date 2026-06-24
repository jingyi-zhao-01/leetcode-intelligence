# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-beautiful-substrings-i
# source_path: LeetCode-Solutions-master/Python/count-beautiful-substrings-i.py
# solution_class: Solution
# submission_id: 571fb120084b00daa87ea26c4b14b926fba1c2d3
# seed: 3403579831

# Time:  O(n + sqrt(k))
# Space: O(n)

# number theory, prefix sum, freq table

class Solution(object):
    def beautifulSubstrings(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        VOWELS = set("aeiou")
        prefix = [0]*(len(s)+1)
        for i in xrange(len(s)):
            prefix[i+1] = prefix[i]+(+1 if s[i] in VOWELS else -1)
        new_k = 1
        x = k
        for i in xrange(2, k+1):
            if i*i > k:
                break
            cnt = 0
            while x%i == 0:
                x //= i
                cnt += 1
            if cnt:
                new_k *= i**((cnt+1)//2+int(i == 2))
        if x != 1:
            new_k *= x**((1+1)//2+int(x == 2))
        cnt = collections.Counter()
        result = 0
        for i, p in enumerate(prefix):
            result += cnt[p, i%new_k]
            cnt[p, i%new_k] += 1
        return result