# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: cracking-the-safe
# source_path: LeetCode-Solutions-master/Python/cracking-the-safe.py
# solution_class: Solution4
# submission_id: 7820848c7957adfb9ba9c613c272798e4dc2bf8d
# seed: 2183847747

# Time:  O(k^n)
# Space: O(k^n)

class Solution4(object):
    def crackSafe(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        result = [str(k-1)]*(n-1)
        lookup = set()
        total = k**n
        while len(lookup) < total:
            node = result[len(result)-n+1:]
            for i in xrange(k):  # preorder like traversal relative to initial result to avoid getting stuck, i.e. don't use k-1 until there is no other choice
                neighbor = "".join(node) + str(i)
                if neighbor not in lookup:
                    lookup.add(neighbor)
                    result.append(str(i))
                    break
        return "".join(result)