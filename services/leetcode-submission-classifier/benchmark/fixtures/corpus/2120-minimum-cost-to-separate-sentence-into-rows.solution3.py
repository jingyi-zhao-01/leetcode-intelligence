# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-cost-to-separate-sentence-into-rows
# source_path: LeetCode-Solutions-master/Python/minimum-cost-to-separate-sentence-into-rows.py
# solution_class: Solution3
# submission_id: 494320ece9023b6cd998ed6d8072d3f150063ed4
# seed: 894701182

# Time:  O(s + n * k), n is the number of the word_lens
# Space: O(k)

class Solution3(object):
    def minimumCost(self, sentence, k):
        """
        :type sentence: str
        :type k: int
        :rtype: int
        """
        word_lens = []
        j = 0
        for i in xrange(len(sentence)+1):
            if i != len(sentence) and sentence[i] != ' ':
                continue
            word_lens.append(i-j)
            j = i+1
        dp = [float("inf")]*(1+(len(word_lens)-1))  # dp[i]: min cost of the first i word_lens where i in [0, len(words)-1]
        dp[0] = 0
        for i in xrange(1, (len(word_lens)-1)+1):
            total = word_lens[i-1]
            for j in reversed(xrange(i)):
                dp[i] = min(dp[i], dp[j] + (k-total)**2)
                if j-1 < 0:
                    continue
                total += (word_lens[j-1]+1)
                if total > k:
                    break
        i, total = len(word_lens)-1, -1
        while i >= 0 and total + (word_lens[i]+1) <= k:  # find max i s.t. the length of the last line > k
            total += (word_lens[i]+1)
            i -= 1
        return min(dp[j] for j in xrange(i+1, len(dp)))