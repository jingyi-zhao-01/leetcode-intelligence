# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: distribute-candies-to-people
# source_path: LeetCode-Solutions-master/Python/distribute-candies-to-people.py
# solution_class: Solution3
# submission_id: 253c64f5a757ca59b9f83abfdaf12526818a8fa8
# seed: 1019795247

# Time:  O(n + logc), c is the number of candies
# Space: O(1)

class Solution3(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        result = [0]*num_people
        i = 0
        while candies != 0:
            result[i % num_people] += min(candies, i+1)
            candies -= min(candies, i+1)
            i += 1
        return result