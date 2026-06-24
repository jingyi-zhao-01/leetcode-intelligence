# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: move-sub-tree-of-n-ary-tree
# source_path: LeetCode-Solutions-master/Python/move-sub-tree-of-n-ary-tree.py
# solution_class: Solution2
# submission_id: c376ed751cf2b870a73fc83f293c2c27d569cce1
# seed: 2748681820

# Time:  O(n)
# Space: O(h)

# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


# one pass solution without recursion

class Solution2(object):
    def moveSubTree(self, root, p, q):
        """
        :type root: Node
        :type p: Node
        :type q: Node
        :rtype: Node
        """
        def iter_find_parents(node, parent, p, q, lookup):
            stk = [(1, [node, None])]
            while stk:
                step, params = stk.pop()
                if step == 1:
                    node, parent = params
                    if node in (p, q):
                        lookup[node] = parent
                        if len(lookup) == 2:
                            return
                    stk.append((2, [node, reversed(node.children)]))
                else:
                    node, it = params
                    child = next(it, None)
                    if not child:
                        continue
                    stk.append((2, [node, it]))
                    stk.append((1, [child, node]))

        def iter_is_ancestor(node, q):
            stk = [(1, [node])]
            while stk:
                step, params = stk.pop()
                if step == 1:
                    node = params[0]
                    stk.append((2, [reversed(node.children)]))
                else:
                    it = params[0]
                    child = next(it, None)
                    if not child:
                        continue
                    if child == q:
                        return True
                    stk.append((2, [it]))
                    stk.append((1, [child]))
            return False

        lookup = {}
        iter_find_parents(root, None, p, q, lookup)
        if p in lookup and lookup[p] == q:
            return root
        q.children.append(p)
        if not iter_is_ancestor(p, q):
            lookup[p].children.remove(p)
        else:
            lookup[q].children.remove(q)
            if p == root:
                root = q
            else:
                lookup[p].children[lookup[p].children.index(p)] = q
        return root