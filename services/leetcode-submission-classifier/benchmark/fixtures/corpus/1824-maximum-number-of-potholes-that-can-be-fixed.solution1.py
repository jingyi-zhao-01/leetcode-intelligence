# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-number-of-potholes-that-can-be-fixed
# source_path: LeetCode-Solutions-master/Python/maximum-number-of-potholes-that-can-be-fixed.py
# solution_class: Solution
# submission_id: a4e408a95dd8c4872fe71dd904e838a1c1892d5c
# seed: 3439765281

# Time:  O(n)
# Space: O(n)

# counting sort, greedy

class Solution(object):
    def maxPotholes(self, road, budget):
        """
        :type road: str
        :type budget: int
        :rtype: int
        """
        def inplace_counting_sort(nums, reverse=False):  # Time: O(n)
            if not nums:
                return
            count = [0]*(max(nums)+1)
            for num in nums:
                count[num] += 1
            for i in xrange(1, len(count)):
                count[i] += count[i-1]
            for i in reversed(xrange(len(nums))):  # inplace but unstable sort
                while nums[i] >= 0:
                    count[nums[i]] -= 1
                    j = count[nums[i]]
                    nums[i], nums[j] = nums[j], ~nums[i]
            for i in xrange(len(nums)):
                nums[i] = ~nums[i]  # restore values
            if reverse:  # unstable sort
                nums.reverse()
    
        ls = []
        l = 0
        for i in xrange(len(road)):
            l += 1
            if i+1 == len(road) or road[i+1] != road[i]:
                if road[i] == 'x':
                    ls.append(l)
                l = 0
        inplace_counting_sort(ls)
        result = 0
        for l in reversed(ls):
            c = min(l+1, budget)
            if c-1 <= 0:
                break
            result += c-1
            budget -= c
        return result