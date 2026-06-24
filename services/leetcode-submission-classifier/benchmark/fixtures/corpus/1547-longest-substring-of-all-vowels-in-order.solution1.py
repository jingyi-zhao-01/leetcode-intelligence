# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-substring-of-all-vowels-in-order
# source_path: LeetCode-Solutions-master/Python/longest-substring-of-all-vowels-in-order.py
# solution_class: Solution
# submission_id: ec61c19140a50ac2786fa7d06dc223da3ae174f0
# seed: 1127526801

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def longestBeautifulSubstring(self, word):
        """
        :type word: str
        :rtype: int
        """
        result = 0
        l = cnt = 1
        for i in xrange(len(word)-1):
            if word[i] > word[i+1]:
                l = cnt = 1
            else:
                l += 1
                cnt += int(word[i] < word[i+1])
            if cnt == 5:
                result = max(result, l)
        return result