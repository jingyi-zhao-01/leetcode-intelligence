# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: median-of-two-sorted-arrays
# source_path: LeetCode-Solutions-master/Python/median-of-two-sorted-arrays.py
# solution_class: Solution
# submission_id: 0993d107d959cbc0d6e62b2a91f52cbb85738ddd
# seed: 4258714849

# Time:  O(log(min(m, n)))
# Space: O(1)

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        def binary_search(left, right, check):
            while left <= right:
                mid = left+(right-left)//2
                if check(mid):
                    right = mid-1
                else:
                    left = mid+1
            return left

        def getKth(A, B, k):
            m, n = len(A), len(B)
            if m > n:
                m, n = n, m
                A, B = B, A
            i = binary_search(max(k-n, 0), min(m, k)-1, lambda i: A[i] >= B[k-1-i])
            return max(A[i-1] if i-1 >= 0 else float("-inf"), B[k-1-i] if k-1-i >= 0 else float("-inf"))

        len1, len2 = len(nums1), len(nums2)
        if (len1+len2) % 2 == 1:
            return getKth(nums1, nums2, (len1+len2)//2+1)
        else:
            return (getKth(nums1, nums2, (len1+len2)//2)+getKth(nums1, nums2, (len1+len2)//2+1))*0.5    