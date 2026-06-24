# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-moves-to-make-array-complementary
# source_path: LeetCode-Solutions-master/Python/minimum-moves-to-make-array-complementary.py
# solution_class: Solution
# submission_id: 4188678f79b25ae98061b89eacec0c1db0b9309d
# seed: 4139747

# Time:  O(n + k)
# Space: O(k)

class Solution(object):
    def minMoves(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        diff = [0]*(2*(limit+1))
        for i in xrange(len(nums)//2):
            left, right = nums[i], nums[-1-i]
            diff[min(left, right)+1] -= 1        # if target total grows to min(left, right)+1, one less move
            diff[left+right] -= 1                # if target total grows to left+right, one less move
            diff[left+right+1] += 1              # if target total grows to left+right+1, one more move
            diff[max(left, right)+limit+1] += 1  # if target total grows to max(left, right)+limit+1, one more move
        result = count = len(nums)               # default is to move all nums
        for total in xrange(2, 2*limit+1):       # enumerate all possible target totals
            count += diff[total]
            result = min(result, count)
        return result