# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-unique-word-abbreviation
# source_path: LeetCode-Solutions-master/Python/minimum-unique-word-abbreviation.py
# solution_class: Solution2
# submission_id: 13a390139654ff040607f3445df25d6fa5f44ddb
# seed: 1566667800

# Time:  O((d + n) * 2^n)
# Space: O(d)

# optimized from Solution2

class Solution2(object):
    def minAbbreviation(self, target, dictionary):
        """
        :type target: str
        :type dictionary: List[str]
        :rtype: str
        """
        def bits_to_abbr(targets, bits):
            abbr = []
            pre = 0
            for i in xrange(len(target)):
                if bits & 1:
                    if i - pre > 0:
                        abbr.append(str(i - pre))
                    pre = i + 1
                    abbr.append(target[i])
                elif i == len(target) - 1:
                    abbr.append(str(i - pre + 1))
                bits >>= 1
            return "".join(abbr)
  
        diffs = []
        for word in dictionary:
            if len(word) != len(target):
                continue
            diffs.append(sum(2**i for i, c in enumerate(word) if target[i] != c))

        if not diffs:
            return str(len(target))

        result = target
        for mask in xrange(2**len(target)):
            abbr = bits_to_abbr(target, mask)
            if all(d & mask for d in diffs) and len(abbr) < len(result):
                result = abbr
        return result