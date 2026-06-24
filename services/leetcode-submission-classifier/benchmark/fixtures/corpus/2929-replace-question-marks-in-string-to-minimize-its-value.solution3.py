# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: replace-question-marks-in-string-to-minimize-its-value
# source_path: LeetCode-Solutions-master/Python/replace-question-marks-in-string-to-minimize-its-value.py
# solution_class: Solution3
# submission_id: c6dafbed6df4f231826766d98a34f67ae97a1cff
# seed: 878059958

# Time:  O(n + 26 * log(26))
# Space: O(26)

# greedy, counting sort, prefix sum

class Solution3(object):
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
        cnt2 = [0]*26
        for _ in xrange(s.count('?')):
            i = min(xrange(len(cnt)), key=lambda x: cnt[x]+cnt2[x])
            cnt2[i] += 1
        it = counting_sort(cnt2)
        result = list(s)
        for i in xrange(len(result)):
            if result[i] != '?':
                continue
            result[i] = chr(ord('a')+next(it))
        return "".join(result)