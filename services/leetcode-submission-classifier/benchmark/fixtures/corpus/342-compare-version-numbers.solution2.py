# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: compare-version-numbers
# source_path: LeetCode-Solutions-master/Python/compare-version-numbers.py
# solution_class: Solution2
# submission_id: a61c13c3be574661f2619f41c9dc45966d596d94
# seed: 3504444709

# Time:  O(n)
# Space: O(1)

import itertools

class Solution2(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1, v2 = version1.split("."), version2.split(".")

        if len(v1) > len(v2):
            v2 += ['0' for _ in xrange(len(v1) - len(v2))]
        elif len(v1) < len(v2):
            v1 += ['0' for _ in xrange(len(v2) - len(v1))]

        i = 0
        while i < len(v1):
            if int(v1[i]) > int(v2[i]):
                return 1
            elif int(v1[i]) < int(v2[i]):
                return -1
            else:
                i += 1

        return 0

    def compareVersion2(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = [int(x) for x in version1.split('.')]
        v2 = [int(x) for x in version2.split('.')]
        while len(v1) != len(v2):
            if len(v1) > len(v2):
                v2.append(0)
            else:
                v1.append(0)
        return cmp(v1, v2)

    def compareVersion3(self, version1, version2):
        splits = (map(int, v.split('.')) for v in (version1, version2))
        return cmp(*zip(*itertools.izip_longest(*splits, fillvalue=0)))

    def compareVersion4(self, version1, version2):
        main1, _, rest1 = ('0' + version1).partition('.')
        main2, _, rest2 = ('0' + version2).partition('.')
        return cmp(int(main1), int(main2)) or len(rest1 + rest2) and self.compareVersion4(rest1, rest2)