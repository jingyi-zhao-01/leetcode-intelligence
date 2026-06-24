# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: candy
# source_path: LeetCode-Solutions-master/Python/candy.py
# solution_class: Solution
# submission_id: dedd189b37f54fbeb354de9830440cf8b599c511
# seed: 1469186053

# Time:  O(n)
# Space: O(n)

class Solution(object):
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        candies = [1 for _ in xrange(len(ratings))]
        for i in xrange(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        for i in reversed(xrange(1, len(ratings))):
            if ratings[i - 1] > ratings[i] and candies[i - 1] <= candies[i]:
                candies[i - 1] = candies[i] + 1

        return sum(candies)