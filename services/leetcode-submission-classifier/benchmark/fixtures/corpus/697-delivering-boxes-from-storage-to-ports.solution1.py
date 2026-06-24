# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: delivering-boxes-from-storage-to-ports
# source_path: LeetCode-Solutions-master/Python/delivering-boxes-from-storage-to-ports.py
# solution_class: Solution
# submission_id: d67b32df861c8d4a51c0528470593b543fa4fc40
# seed: 2370708502

# Time:  O(n)
# Space: O(n)

class Solution(object):
    def boxDelivering(self, boxes, portsCount, maxBoxes, maxWeight):
        """
        :type boxes: List[List[int]]
        :type portsCount: int
        :type maxBoxes: int
        :type maxWeight: int
        :rtype: int
        """
        dp = [0]*(len(boxes)+1)
        left, cost, curr = 0, 1, 0
        for right in xrange(len(boxes)):
            if right == 0 or boxes[right][0] != boxes[right-1][0]:
                cost += 1
            curr += boxes[right][1]
            while right-left+1 > maxBoxes or \
                  curr > maxWeight or \
                  (left+1 < right+1 and dp[left+1] == dp[left]):  # greedily drop box to make cost as smaller as possible
                curr -= boxes[left][1]
                if boxes[left+1][0] != boxes[left][0]:
                    cost -= 1
                left += 1
            dp[right+1] = dp[(left-1)+1] + cost
        return dp[len(boxes)]