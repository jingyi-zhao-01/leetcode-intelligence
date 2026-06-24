# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-length-of-a-concatenated-string-with-unique-characters
# source_path: LeetCode-Solutions-master/Python/maximum-length-of-a-concatenated-string-with-unique-characters.py
# solution_class: Solution2
# submission_id: 13693a2336bfb99766f2f96d712b65c94f019eb3
# seed: 3876495638

# Time:  O(n) ~ O(2^n)
# Space: O(1) ~ O(2^n)

power = [1]
log2 = {1:0}
for i in xrange(1, 26):
    power.append(power[-1]<<1)
    log2[power[i]] = i

class Solution2(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """ 
        def bitset(s):
            result = 0
            for c in s:
                if result & power[ord(c)-ord('a')]:
                    return 0
                result |= power[ord(c)-ord('a')]
            return result
    
        bitsets = [bitset(x) for x in arr]
        result = 0
        for i in xrange(power[len(arr)]):
            curr_bitset, curr_len = 0, 0
            while i:
                j = i & -i  # rightmost bit
                i ^= j
                j = log2[j]  # log2(j)
                if not bitsets[j] or (curr_bitset & bitsets[j]):
                    break
                curr_bitset |= bitsets[j]
                curr_len += len(arr[j])
            else:
                result = max(result, curr_len)
        return result