# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: delete-duplicate-folders-in-system
# source_path: LeetCode-Solutions-master/Python/delete-duplicate-folders-in-system.py
# solution_class: Solution2
# submission_id: 6bb740307529e17c48668e43440bdfaf9c51ef8e
# seed: 4107357500

# Time:  O(n * m * l + tlogt + l * t), m is the max number of folders in a path,
#                                    , n is the number of paths
#                                    , l is the max length of folder name
#                                    , t is the size of trie
# Space: O(l * t)

import collections

class Solution2(object):
    def deleteDuplicateFolder(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: List[List[str]]
        """
        def mark(node, lookup):
            serialized_tree = "(" + "".join(subfolder + mark(child, lookup) for subfolder, child in sorted(node.iteritems()) if child != "_del") + ")"
            if serialized_tree != "()":
                if serialized_tree in lookup:
                    lookup[serialized_tree]["_del"]
                    node["_del"]
                else:
                    lookup[serialized_tree] = node
            return serialized_tree
        
        def sweep(node, path, result):
            if path:
                result.append(path[:])
            for subfolder, child in node.iteritems():
                if "_del" in child:
                    continue
                path.append(subfolder)
                sweep(child, path, result)
                path.pop()

        _trie = lambda: collections.defaultdict(_trie)
        trie = _trie()
        for path in paths:
            reduce(dict.__getitem__, path, trie)
        mark(trie, {})
        result = []
        sweep(trie, [], result)
        return result