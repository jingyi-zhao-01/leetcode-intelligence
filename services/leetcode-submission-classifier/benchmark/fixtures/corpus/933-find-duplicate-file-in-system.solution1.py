# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-duplicate-file-in-system
# source_path: LeetCode-Solutions-master/Python/find-duplicate-file-in-system.py
# solution_class: Solution
# submission_id: 2316545174ea77302fc8040f4feb09f90a088804
# seed: 3955496017

# Time:  O(n * l), l is the average length of file content
# Space: O(n * l)

import collections

class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        files = collections.defaultdict(list)
        for path in paths:
           s = path.split(" ")
           for i in xrange(1,len(s)):
               file_name = s[0] + "/" + s[i][0:s[i].find("(")]
               file_content = s[i][s[i].find("(")+1:s[i].find(")")]
               files[file_content].append(file_name)

        result = []
        for file_content, file_names in files.iteritems():
            if len(file_names)>1:
                result.append(file_names)
        return result