# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: distribute-candies-to-people
# source_path: LeetCode-Solutions-master/Python/distribute-candies-to-people.py
# solution_class: Solution2
# submission_id: 899b67564aae014ac72ea9b9c726465c0b785b2d
# seed: 1810498653

# Time:  O(n + logc), c is the number of candies
# Space: O(1)

class Solution2(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        # find max integer p s.t. sum(1 + 2 + ... + p) <= C
        left, right = 1, candies
        while left <= right:
            mid = left + (right-left)//2
            if not ((mid <= candies*2 // (mid+1))):
                right = mid-1
            else:
                left = mid+1
        p = right
        remaining = candies - (p+1)*p//2
        rows, cols = divmod(p, num_people)
        
        result = [0]*num_people
        for i in xrange(num_people):
            result[i] = (i+1)*(rows+1) + (rows*(rows+1)//2)*num_people if i < cols else \
                        (i+1)*rows + ((rows-1)*rows//2)*num_people
        result[cols] += remaining
        return result