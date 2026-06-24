# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sort-even-and-odd-indices-independently
# source_path: LeetCode-Solutions-master/Python/sort-even-and-odd-indices-independently.py
# solution_class: Solution2
# submission_id: d597fdd03bef5054557daa853405cd853e712d22
# seed: 3153214264

# Time:  O(n)
# Space: O(c), c is the max of nums

# counting sort, inplace solution

class Solution2(object):
    def sortEvenOdd(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def partition(index, nums):
            for i in xrange(len(nums)):
                j = i
                while nums[i] >= 0:
                    j = index(j)
                    nums[i], nums[j] = nums[j], ~nums[i]  # processed
            for i in xrange(len(nums)):
                nums[i] = ~nums[i]  # restore values
        
        partition(lambda i: i//2 if i%2 == 0 else (len(nums)+1)//2+i//2, nums)
        nums[:(len(nums)+1)//2], nums[(len(nums)+1)//2:] = sorted(nums[:(len(nums)+1)//2]), sorted(nums[(len(nums)+1)//2:], reverse=True)
        partition(lambda i: 2*i if i < (len(nums)+1)//2 else 1+2*(i-(len(nums)+1)//2), nums)
        return nums