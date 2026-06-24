# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: move-sub-tree-of-n-ary-tree
# source_path: LeetCode-Solutions-master/Python/move-sub-tree-of-n-ary-tree.py
# solution_class: Solution
# submission_id: 32b12cff9f64bc0f5c073ead8a2b506cb623527f
# seed: 989267377

# Time:  O(n)
# Space: O(h)

# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


# one pass solution without recursion

class Solution(object):
    def moveSubTree(self, root, p, q):
        """
        :type root: Node
        :type p: Node
        :type q: Node
        :rtype: Node
        """
        def iter_find_parents(node, parent, p, q, is_ancestor, lookup):
            stk = [(1, [node, None, False])]
            while stk:
                step, params = stk.pop()
                if step == 1:
                    node, parent, is_ancestor = params
                    if node in (p, q):
                        lookup[node] = parent
                        if len(lookup) == 2:
                            return is_ancestor
                    stk.append((2, [node, is_ancestor, reversed(node.children)]))
                else:
                    node, is_ancestor, it = params
                    child = next(it, None)
                    if not child:
                        continue
                    stk.append((2, [node, is_ancestor, it]))
                    stk.append((1, [child, node, is_ancestor or node == p]))
            assert(False)
            return False

        lookup = {}
        is_ancestor = iter_find_parents(root, None, p, q, False, lookup)
        if p in lookup and lookup[p] == q:
            return root
        q.children.append(p)
        if not is_ancestor:
            lookup[p].children.remove(p)
        else:
            lookup[q].children.remove(q)
            if p == root:
                root = q
            else:
                lookup[p].children[lookup[p].children.index(p)] = q
        return root