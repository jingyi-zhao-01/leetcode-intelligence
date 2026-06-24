# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: subdomain-visit-count
# source_path: LeetCode-Solutions-master/Python/subdomain-visit-count.py
# solution_class: Solution
# submission_id: 30963ef419ec83d250602f3427356a5fb8b7067e
# seed: 2783207600

# Time:  O(n), is the length of cpdomains (assuming the length of cpdomains[i] is fixed)
# Space: O(n)

import collections

class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        result = collections.defaultdict(int)
        for domain in cpdomains:
            count, domain = domain.split()
            count = int(count)
            frags = domain.split('.')
            curr = []
            for i in reversed(xrange(len(frags))):
                curr.append(frags[i])
                result[".".join(reversed(curr))] += count

        return ["{} {}".format(count, domain) \
                for domain, count in result.iteritems()]