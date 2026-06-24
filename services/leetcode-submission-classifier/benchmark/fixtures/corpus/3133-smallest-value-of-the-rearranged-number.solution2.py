# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: smallest-value-of-the-rearranged-number
# source_path: LeetCode-Solutions-master/Python/smallest-value-of-the-rearranged-number.py
# solution_class: Solution2
# submission_id: 158ae013cd9e41cea09bbc21638a8a37f5392e09
# seed: 1622494550

# Time:  O(d), d is the number of digits
# Space: O(d)

# greedy, counting sort

class Solution2(object):
    def smallestNumber(self, num):
        """
        :type num: int
        :rtype: int
        """
        sign = 1 if num >= 0 else -1
        nums = sorted(str(abs(num)), reverse=(sign == -1))
        i = next((i for i in xrange(len(nums)) if nums[i] != '0'), 0)
        nums[0], nums[i] = nums[i], nums[0]
        return sign*int("".join(nums))