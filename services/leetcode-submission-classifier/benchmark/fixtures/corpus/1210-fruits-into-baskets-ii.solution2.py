# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: fruits-into-baskets-ii
# source_path: LeetCode-Solutions-master/Python/fruits-into-baskets-ii.py
# solution_class: Solution2
# submission_id: 31f8d4d3be306c300f1c8a85da0ffe2814e0d020
# seed: 2600841233

# Time:  O(nlogn)
# Space: O(n)

# segment tree, binary search

class Solution2(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        """
        :type fruits: List[int]
        :type baskets: List[int]
        :rtype: int
        """
        result = 0
        for x in fruits:
            i = next((i for i in xrange(len(baskets)) if baskets[i] >= x), -1)
            if i ==-1:
                result += 1
            else:
                baskets[i] = 0
        return result