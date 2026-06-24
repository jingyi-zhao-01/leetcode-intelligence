# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: last-substring-in-lexicographical-order
# source_path: LeetCode-Solutions-master/Python/last-substring-in-lexicographical-order.py
# solution_class: Solution2
# submission_id: 86f893c636f28bd4688362e70ab70deeab2c9f41
# seed: 49023338

# Time:  O(n)
# Space: O(1)

class Solution2(object):
    def lastSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = collections.defaultdict(list)
        for i in xrange(len(s)):
            count[s[i]].append(i)

        max_c = max(count.iterkeys())
        starts = {}
        for i in count[max_c]:
            starts[i] = i+1
        while len(starts)-1 > 0:
            lookup = set()
            next_count = collections.defaultdict(list)
            for start, end in starts.iteritems():
                if end == len(s):  # finished
                    lookup.add(start)
                    continue
                next_count[s[end]].append(start)				
                if end in starts:  # overlapped
                    lookup.add(end)			
            next_starts = {}
            max_c = max(next_count.iterkeys())
            for start in next_count[max_c]:
                if start not in lookup:
                    next_starts[start] = starts[start]+1
            starts = next_starts
        return s[next(starts.iterkeys()):]