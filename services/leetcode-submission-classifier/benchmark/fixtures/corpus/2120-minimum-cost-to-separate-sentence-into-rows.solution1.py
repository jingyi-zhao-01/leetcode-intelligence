# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-cost-to-separate-sentence-into-rows
# source_path: LeetCode-Solutions-master/Python/minimum-cost-to-separate-sentence-into-rows.py
# solution_class: Solution
# submission_id: 4a2fd1150e3388693debf6b9e581c4efd7d1bef5
# seed: 1305706212

# Time:  O(s + n * k), n is the number of the word_lens
# Space: O(k)

class Solution(object):
    def minimumCost(self, sentence, k):
        """
        :type sentence: str
        :type k: int
        :rtype: int
        """
        def lens(sentence):
            j = len(sentence)-1
            for i in reversed(xrange(-1, len(sentence))):
                if i == -1 or sentence[i] == ' ':
                    yield j-i
                    j = i-1

        word_lens, dp = [], []  # dp[i]: min cost of word_lens[-1-i:]
        t = -1
        for l in lens(sentence):
            word_lens.append(l)
            dp.append(float("inf"))
            t += l+1
            if t <= k:
                dp[-1] = 0
                continue
            total = l
            for j in reversed(xrange(len(dp)-1)):
                dp[-1] = min(dp[-1], dp[j] + (k-total)**2)
                total += (word_lens[j]+1)
                if total > k:
                    word_lens = word_lens[j:]  # minimize len(word_lens) s.t. sum(word_lens) > k
                    dp = dp[j:]
                    break
        return dp[-1] if dp else 0