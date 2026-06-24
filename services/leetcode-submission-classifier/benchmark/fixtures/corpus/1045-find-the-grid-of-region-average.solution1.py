# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-grid-of-region-average
# source_path: LeetCode-Solutions-master/Python/find-the-grid-of-region-average.py
# solution_class: Solution
# submission_id: c96f0474debc187570bb81b6ad558855baaa3030
# seed: 1104906226

# Time:  O(m * n)
# Space: O(m * n)

# array

class Solution(object):
    def resultGrid(self, image, threshold):
        """
        :type image: List[List[int]]
        :type threshold: int
        :rtype: List[List[int]]
        """
        def check(i, j):
            return (all(abs(image[ni][nj]-image[ni+1][nj]) <= threshold for ni in xrange(i-1, i+1) for nj in xrange(j-1, j+2)) and
                    all(abs(image[ni][nj]-image[ni][nj+1]) <= threshold for ni in xrange(i-1, i+2) for nj in xrange(j-1, j+1)))
            
        result = [[0]*len(image[0]) for _ in xrange(len(image))]
        cnt = [[0]*len(image[0]) for _ in xrange(len(image))]
        for i in xrange(1, len(image)-1):
            for j in xrange(1, len(image[0])-1):
                if not check(i, j):
                    continue
                total = sum(image[ni][nj] for ni in xrange(i-1, i+2) for nj in xrange(j-1, j+2))//9
                for ni in xrange(i-1, i+2):
                    for nj in xrange(j-1, j+2):
                        cnt[ni][nj] += 1
                        result[ni][nj] += total
        for i in xrange(len(image)):
            for j in xrange(len(image[0])):
                if cnt[i][j]:
                    result[i][j] //= cnt[i][j]
                else:
                    result[i][j] = image[i][j]
        return result