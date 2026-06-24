# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sort-features-by-popularity
# source_path: LeetCode-Solutions-master/Python/sort-features-by-popularity.py
# solution_class: Solution
# submission_id: 57b7500593e93cdfd4296dc519c41d6bf689ac16
# seed: 3153048084

# Time:  O(nlogn)
# Space: O(n)

import collections

class Solution(object):
    def sortFeatures(self, features, responses):
        """
        :type features: List[str]
        :type responses: List[str]
        :rtype: List[str]
        """
        features_set = set(features)
        order = {word: i for i, word in enumerate(features)}
        freq = collections.defaultdict(int)
        for r in responses:
            for word in set(r.split(' ')):
                if word in features_set:
                    freq[word] += 1
        features.sort(key=lambda x: (-freq[x], order[x]))
        return features