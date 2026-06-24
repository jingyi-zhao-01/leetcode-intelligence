# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: replace-question-marks-in-string-to-minimize-its-value
# source_path: LeetCode-Solutions-master/Python/replace-question-marks-in-string-to-minimize-its-value.py
# solution_class: Solution2
# submission_id: 34178aa1d750b74a7ccfef9a2de1e6b641696e14
# seed: 3405626749

# Time:  O(n + 26 * log(26))
# Space: O(26)

# greedy, counting sort, prefix sum

class Solution2(object):
    def minimizeStringValue(self, s):
        """
        :type s: str
        :rtype: str
        """
        def counting_sort(cnt):
            for i in xrange(len(cnt)):
                for _ in xrange(cnt[i]):
                    yield i

        cnt = [0]*26
        for x in s:
            if x == '?':
                continue
            cnt[ord(x)-ord('a')] += 1
        min_heap = [(x, i) for i, x in enumerate(cnt)]
        heapq.heapify(min_heap)
        cnt2 = [0]*26
        for _ in xrange(s.count('?')):
            c, i = heapq.heappop(min_heap)
            heapq.heappush(min_heap, (c+1, i))
            cnt2[i] += 1
        it = counting_sort(cnt2)
        result = list(s)
        for i in xrange(len(result)):
            if result[i] != '?':
                continue
            result[i] = chr(ord('a')+next(it))
        return "".join(result)