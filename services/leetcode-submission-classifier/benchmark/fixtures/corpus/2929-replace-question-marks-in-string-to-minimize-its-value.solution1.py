# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: replace-question-marks-in-string-to-minimize-its-value
# source_path: LeetCode-Solutions-master/Python/replace-question-marks-in-string-to-minimize-its-value.py
# solution_class: Solution
# submission_id: 43785e90bcc12dd6db4208a1ecd03c5b21e5cff0
# seed: 2218264937

# Time:  O(n + 26 * log(26))
# Space: O(26)

# greedy, counting sort, prefix sum

class Solution(object):
    def minimizeStringValue(self, s):
        """
        :type s: str
        :rtype: str
        """
        def counting_sort(cnt):
            for i in xrange(len(cnt)):
                for _ in xrange(cnt[i]):
                    yield i
        
        def fill(cnt):
            result = [0]*26
            a = [(x, i) for i, x in enumerate(cnt)]
            a.sort()
            total = s.count('?')
            curr = 0
            for i in xrange(len(a)-1):
                if curr+(a[i+1][0]-a[i][0])*(i+1) > total:
                    break
                curr += (a[i+1][0]-a[i][0])*(i+1)
            else:
                i = len(a)-1
            q, r = divmod(total-curr, i+1)
            for j in xrange(i+1):
                result[a[j][1]] = (a[i][0]-a[j][0])+q
            cnt2 = [0]*26
            for j in xrange(i+1):
                cnt2[a[j][1]] += 1
            it = counting_sort(cnt2)
            for _ in xrange(r):
                result[next(it)] += 1
            return result
    
        cnt = [0]*26
        for x in s:
            if x == '?':
                continue
            cnt[ord(x)-ord('a')] += 1
        it = counting_sort(fill(cnt))
        result = list(s)
        for i in xrange(len(result)):
            if result[i] != '?':
                continue
            result[i] = chr(ord('a')+next(it))
        return "".join(result)