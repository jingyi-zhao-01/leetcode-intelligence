# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: search-suggestions-system
# source_path: LeetCode-Solutions-master/Python/search-suggestions-system.py
# solution_class: Solution3
# submission_id: d299a51781e2a8dbf7f001a8e45678566ee049b1
# seed: 94719670

# Time:  ctor: O(n * l), n is the number of products
#                      , l is the average length of product name
#        suggest: O(l^2)
# Space: O(t), t is the number of nodes in trie

import collections


class TrieNode(object):

    def __init__(self):
        self.__TOP_COUNT = 3
        self.leaves = collections.defaultdict(TrieNode)
        self.infos = []

    def insert(self, words, i):
        curr = self
        for c in words[i]:
            curr = curr.leaves[c]
            curr.add_info(words, i)

    def add_info(self, words, i):
        self.infos.append(i)
        self.infos.sort(key=lambda x: words[x])
        if len(self.infos) > self.__TOP_COUNT:
            self.infos.pop()

class Solution3(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        products.sort()  # Time: O(n * l * log(n * l))
        result = []
        prefix = ""
        for i, c in enumerate(searchWord):  # Time: O(l)
            prefix += c
            start = bisect.bisect_left(products, prefix)  # Time: O(log(n * l))
            new_products = []
            for j in xrange(start, len(products)):  # Time: O(n * l)
                if not (i < len(products[j]) and products[j][i] == c):
                    break
                new_products.append(products[j])
            products = new_products
            result.append(products[:3])
        return result