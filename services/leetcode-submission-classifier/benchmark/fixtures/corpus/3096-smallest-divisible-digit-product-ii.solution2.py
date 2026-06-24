# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: smallest-divisible-digit-product-ii
# source_path: LeetCode-Solutions-master/Python/smallest-divisible-digit-product-ii.py
# solution_class: Solution2
# submission_id: d51d706b21f8b31d3ef7ecaffa09ce8fcedab60b
# seed: 3140249779

# Time:  O(n + logt)
# Space: O(1)

# freq table, greedy, prefix sum, number theory

class Solution2(object):
    def smallestNumber(self, num, t):
        """
        :type num: str
        :type t: int
        :rtype: str
        """
        def gcd(a, b):
            while b:
                a, b = b, a%b
            return a

        def find_candidates(t, l):  # Time: O(logt)
            candidates = []
            for x in reversed(xrange(2, 9+1)):
                while t%x == 0:
                    t //= x
                    candidates.append(x)
                    if len(candidates) > l:
                        return []
                if t == 1:
                    candidates.reverse()
                    return candidates
            return []
    
        def format(candidates, l):
            result = [1]*l
            i = len(result)-len(candidates)
            for x in candidates:
                result[i] = x
                i += 1
            return "".join(map(str, result))

        nums = map(int, num)
        candidates = find_candidates(t, float("inf"))
        if t != 1 and not candidates:
            return "-1"
        i = next((i for i in xrange(len(nums)) if not nums[i]), len(nums))
        for j in xrange(i, len(nums)):
            nums[j] = 1
        prefix = [1]*(len(nums)+1)
        for i in xrange(len(prefix)-1):
            prefix[i+1] = (prefix[i]*nums[i])%t
        if not prefix[-1]:
            return "".join(map(str, nums))
        for i in reversed(xrange(len(nums))):
             target = t//gcd(t, prefix[i])
             for x in xrange(nums[i]+1, 9+1):
                new_target = target//gcd(target, x)
                tmp = find_candidates(new_target, len(nums)-1-i)
                if new_target != 1 and not tmp:
                    continue
                nums[i] = x
                return "".join(map(str, nums[:i+1]))+format(tmp, len(nums)-1-i)
        return format(candidates, max(len(nums)+1, len(candidates)))