# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sort-an-array
# source_path: LeetCode-Solutions-master/Python/sort-an-array.py
# solution_class: Solution
# submission_id: c7707afa5e0ff47c61e0c4f168fd2f329df160b3
# seed: 2130075775

# Time:  O(nlogn)
# Space: O(n)

# merge sort solution

class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def mergeSort(left, right, nums):
            if left == right:
                return
            mid = left + (right-left)//2
            mergeSort(left, mid, nums)
            mergeSort(mid+1, right,  nums)
            r = mid+1
            tmp = []
            for l in xrange(left, mid+1):
                while r <= right and nums[r] < nums[l]:
                    tmp.append(nums[r])
                    r += 1
                tmp.append(nums[l])
            nums[left:left+len(tmp)] = tmp

        mergeSort(0, len(nums)-1, nums)
        return nums