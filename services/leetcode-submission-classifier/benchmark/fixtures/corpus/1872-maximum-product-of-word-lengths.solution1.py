# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-product-of-word-lengths
# source_path: LeetCode-Solutions-master/Python/maximum-product-of-word-lengths.py
# solution_class: Solution
# submission_id: eb9d8c8f97da976c4569b16ad4bc3e4415ab6a1a
# seed: 3070579235

# Time:  O(n) ~ O(n^2)
# Space: O(n)

class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        def counting_sort(words):
            k = 1000  # k is max length of words in the dictionary
            buckets = [[] for _ in xrange(k)]
            for word in words:
                buckets[len(word)].append(word)
            res = []
            for i in reversed(xrange(k)):
                if buckets[i]:
                    res += buckets[i]
            return res

        words = counting_sort(words)
        bits = [0] * len(words)
        for i, word in enumerate(words):
            for c in word:
                bits[i] |= (1 << (ord(c) - ord('a')))

        max_product = 0
        for i in xrange(len(words) - 1):
            if len(words[i]) ** 2 <= max_product:
                break
            for j in xrange(i + 1, len(words)):
                if len(words[i]) * len(words[j]) <= max_product:
                    break
                if not (bits[i] & bits[j]):
                    max_product = len(words[i]) * len(words[j])
        return max_product