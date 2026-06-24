# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: shopping-offers
# source_path: LeetCode-Solutions-master/Python/shopping-offers.py
# solution_class: Solution
# submission_id: 718aa8a12a9c42c9f1b00c08805c000f3ca2a282
# seed: 1648017549

# Time:  O(n * 2^n)
# Space: O(n)

class Solution(object):
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        def shoppingOffersHelper(price, special, needs, i):
            if i == len(special):
                return sum(map(lambda x, y: x*y, price, needs))
            result = shoppingOffersHelper(price, special, needs, i+1)
            for j in xrange(len(needs)):
                needs[j] -= special[i][j]
            if all(need >= 0 for need in needs):
                result = min(result, special[i][-1] + shoppingOffersHelper(price, special, needs, i))
            for j in xrange(len(needs)):
                needs[j] += special[i][j]
            return result

        return shoppingOffersHelper(price, special, needs, 0)