# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-product-of-word-lengths
# source_path: LeetCode-Solutions-master/Python/maximum-product-of-word-lengths.py
# solution_class: Solution2
# submission_id: bd27e764382233d66b76366b66f17c1b2c1c4dc2
# seed: 1814913538

# Time:  O(n) ~ O(n^2)
# Space: O(n)

class Solution2(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words.sort(key=lambda x: len(x), reverse=True)
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