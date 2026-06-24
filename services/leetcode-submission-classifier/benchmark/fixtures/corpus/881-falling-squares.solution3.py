# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: falling-squares
# source_path: LeetCode-Solutions-master/Python/falling-squares.py
# solution_class: Solution3
# submission_id: 64e7916359cd7e860b128f2c2501f3395f4956d0
# seed: 947119353

# Time:  O(n^2), could be improved to O(nlogn) in cpp by ordered map (bst)
# Space: O(n)

import bisect

class Solution3(object):
    def fallingSquares(self, positions):
        def query(heights, left, right, B, blocks, blocks_read):
            result = 0
            while left % B and left <= right:
                result = max(result, heights[left], blocks[left//B])
                left += 1
            while right % B != B-1 and left <= right:
                result = max(result, heights[right], blocks[right//B])
                right -= 1
            while left <= right:
                result = max(result, blocks[left//B], blocks_read[left//B])
                left += B
            return result

        def update(heights, left, right, B, blocks, blocks_read, h):
            while left % B and left <= right:
                heights[left] = max(heights[left], h)
                blocks_read[left//B] = max(blocks_read[left//B], h)
                left += 1
            while right % B != B-1 and left <= right:
                heights[right] = max(heights[right], h)
                blocks_read[right//B] = max(blocks_read[right//B], h)
                right -= 1
            while left <= right:
                blocks[left//B] = max(blocks[left//B], h)
                left += B

        index = set()
        for left, size in positions:
            index.add(left)
            index.add(left+size-1)
        index = sorted(list(index))
        W = len(index)
        B = int(W**.5)
        heights = [0] * W
        blocks = [0] * (B+2)
        blocks_read = [0] * (B+2)

        max_height = 0
        result = []
        for left, size in positions:
            L, R = bisect.bisect_left(index, left), bisect.bisect_left(index, left+size-1)
            h = query(heights, L, R, B, blocks, blocks_read) + size
            update(heights, L, R, B, blocks, blocks_read, h)
            max_height = max(max_height, h)
            result.append(max_height)
        return result