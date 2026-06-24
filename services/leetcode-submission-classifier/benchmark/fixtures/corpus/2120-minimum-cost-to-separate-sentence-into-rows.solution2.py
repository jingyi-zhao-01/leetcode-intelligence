# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-cost-to-separate-sentence-into-rows
# source_path: LeetCode-Solutions-master/Python/minimum-cost-to-separate-sentence-into-rows.py
# solution_class: Solution2
# submission_id: 9fa4b5d045efccf76073851a1d8536b5c8e78960
# seed: 2437735436

# Time:  O(s + n * k), n is the number of the word_lens
# Space: O(k)

class Solution2(object):
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
        dp = [float("inf")]*(len(word_lens))  # dp[i]: min cost of word_lens[i:]
        i, total = len(word_lens)-1, -1
        while i >= 0 and total + (word_lens[i]+1) <= k:  # find max i s.t. the length of the last line > k
            total += (word_lens[i]+1)
            dp[i] = 0
            i -= 1
        for i in reversed(xrange(i+1)):
            total = word_lens[i]
            for j in xrange(i+1, len(dp)):
                dp[i] = min(dp[i], dp[j] + (k-total)**2)
                total += (word_lens[j]+1)
                if total > k:
                    break
        return dp[0]