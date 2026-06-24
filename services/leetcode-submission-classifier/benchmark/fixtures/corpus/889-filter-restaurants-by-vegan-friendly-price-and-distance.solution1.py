# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: filter-restaurants-by-vegan-friendly-price-and-distance
# source_path: LeetCode-Solutions-master/Python/filter-restaurants-by-vegan-friendly-price-and-distance.py
# solution_class: Solution
# submission_id: 101eaa2ef659d3f790e75f722eded4be11af6f9a
# seed: 227257115

# Time:  O(rlogr), r is the number of result
# Space: O(r)

class Solution(object):
    def filterRestaurants(self, restaurants, veganFriendly, maxPrice, maxDistance):
        """
        :type restaurants: List[List[int]]
        :type veganFriendly: int
        :type maxPrice: int
        :type maxDistance: int
        :rtype: List[int]
        """
        result, lookup = [], {}
        for j, (i, _, v, p, d) in enumerate(restaurants):
            if v >= veganFriendly and p <= maxPrice and d <= maxDistance:
                lookup[i] = j
                result.append(i)
        result.sort(key=lambda i: (-restaurants[lookup[i]][1], -restaurants[lookup[i]][0]))
        return result