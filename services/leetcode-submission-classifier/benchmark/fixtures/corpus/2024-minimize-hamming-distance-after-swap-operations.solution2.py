# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimize-hamming-distance-after-swap-operations
# source_path: LeetCode-Solutions-master/Python/minimize-hamming-distance-after-swap-operations.py
# solution_class: Solution2
# submission_id: 4f2b7dbcee4ba35ba5915326e67c21cf01e93774
# seed: 3765739657

# Time:  O(n)
# Space: O(n)

class Solution2(object):
    def minimumHammingDistance(self, source, target, allowedSwaps):
        """
        :type source: List[int]
        :type target: List[int]
        :type allowedSwaps: List[List[int]]
        :rtype: int
        """
        uf = UnionFind(len(source))
        for x, y in allowedSwaps: 
            uf.union_set(x, y)
        groups = collections.defaultdict(set)
        for i in xrange(len(source)):
            groups[uf.find_set(i)].add(i)
        result = 0
        for idxs in groups.itervalues():
            source_cnt = collections.Counter([source[i] for i in idxs])
            target_cnt = collections.Counter([target[i] for i in idxs])
            diff = source_cnt-target_cnt
            result += sum(diff.itervalues())
        return result