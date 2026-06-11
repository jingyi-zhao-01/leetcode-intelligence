type PatternTagDimension = 'template' | 'data_structure';
type PatternTagKind = 'template_group' | 'tag';
type PatternTagSource = 'seeded' | 'manually_created' | 'llm_generated';

type TemplateMetadata = {
  classicProblems: string[];
  whenToUse: string[];
  whenNotToUse: string[];
  signals: string[];
  pseudocode: string[];
  invariants: string[];
  defaultComplexity: {
    time: string;
    space: string;
  };
  relatedDataStructures: string[];
  similarTemplates: string[];
};

type TemplateTagSeed = {
  key: string;
  label: string;
  description: string;
  metadata: TemplateMetadata;
};

type TemplateGroupSeed = {
  key: string;
  label: string;
  description: string;
  children: TemplateTagSeed[];
};

type DataStructureSeed = {
  key: string;
  label: string;
  description: string;
};

function m(input: TemplateMetadata): TemplateMetadata {
  return input;
}

const TEMPLATE_GROUPS: TemplateGroupSeed[] = [
  {
    key: 'group-linear-state',
    label: 'Linear state and hashing',
    description: 'Canonical one-pass templates that maintain compact state while scanning arrays or strings.',
    children: [
      {
        key: 'hash-map-lookup',
        label: 'Hash map lookup',
        description: 'Scan once while storing previously seen values, counts, or indices for O(1) expected lookup.',
        metadata: m({
          classicProblems: ['1. Two Sum', '560. Subarray Sum Equals K', '128. Longest Consecutive Sequence'],
          whenToUse: [
            'The current element needs to match a value, state, or complement seen earlier.',
            'Membership, count, or index lookup is the bottleneck.',
          ],
          whenNotToUse: [
            'Sorted order gives a monotonic two-pointer discard rule.',
            'The state is a contiguous window that must be shrunk online.',
          ],
          signals: ['seen', 'complement', 'count previous', 'lookup', 'deduplicate'],
          pseudocode: ['state = map_or_set()', 'for item in input:', '  use state to answer with item', '  update state'],
          invariants: ['State only represents processed elements.', 'Lookup state is sufficient to decide local matches.'],
          defaultComplexity: { time: 'O(n)', space: 'O(n)' },
          relatedDataStructures: ['hash-map', 'hash-set'],
          similarTemplates: ['prefix-sum', 'sliding-window'],
        }),
      },
      {
        key: 'hash-map-grouping',
        label: 'Hash map grouping',
        description: 'Map each item to a canonical signature and group equal signatures together.',
        metadata: m({
          classicProblems: ['49. Group Anagrams', '242. Valid Anagram', '347. Top K Frequent Elements'],
          whenToUse: [
            'Objects are equivalent after normalization.',
            'Need bucket, group, or aggregate items by a derived key.',
          ],
          whenNotToUse: ['Need preserve exact order as the primary constraint.', 'Need range or neighbor queries.'],
          signals: ['group by', 'signature', 'frequency', 'bucket', 'canonical key'],
          pseudocode: ['groups = map()', 'for item in items:', '  key = normalize(item)', '  groups[key].append_or_count(item)'],
          invariants: ['Equivalent inputs map to the same key.', 'The grouped value contains all items for that key.'],
          defaultComplexity: { time: 'O(n * normalize_cost)', space: 'O(n)' },
          relatedDataStructures: ['hash-map', 'counter'],
          similarTemplates: ['hash-map-lookup', 'heap-priority-queue'],
        }),
      },
      {
        key: 'prefix-sum',
        label: 'Prefix sum',
        description: 'Transform contiguous range queries into differences between accumulated prefix states.',
        metadata: m({
          classicProblems: ['303. Range Sum Query', '560. Subarray Sum Equals K', '974. Subarray Sums Divisible by K'],
          whenToUse: [
            'A contiguous range property can be expressed as prefix[j] - prefix[i].',
            'Need count, existence, or value of many range sums or modular states.',
          ],
          whenNotToUse: ['All numbers are positive and a shrinkable window solves it simpler.', 'Need non-contiguous choices.'],
          signals: ['subarray sum', 'range sum', 'prefix', 'modulo prefix', 'difference of accumulated state'],
          pseudocode: ['prefix = base', 'seen = {base: 1}', 'for x in nums:', '  prefix = update(prefix, x)', '  query prior prefix state', '  record prefix'],
          invariants: ['Every range ending now corresponds to one prior prefix.', 'Prior prefixes are recorded before current updates are reused.'],
          defaultComplexity: { time: 'O(n)', space: 'O(n) or O(1)' },
          relatedDataStructures: ['array', 'hash-map'],
          similarTemplates: ['hash-map-lookup', 'sliding-window'],
        }),
      },
      {
        key: 'prefix-suffix-accumulation',
        label: 'Prefix/suffix accumulation',
        description: 'Combine independent left and right accumulated information for each position.',
        metadata: m({
          classicProblems: ['238. Product of Array Except Self', '42. Trapping Rain Water', '135. Candy'],
          whenToUse: [
            'Answer at each index depends on information from both sides.',
            'Forward and backward passes can compute independent contributions.',
          ],
          whenNotToUse: ['A single local recurrence is enough.', 'Need online answers without seeing the full input.'],
          signals: ['left right pass', 'prefix and suffix', 'except self', 'from both sides'],
          pseudocode: ['left = scan_left(input)', 'right = scan_right(input)', 'for i:', '  ans[i] = combine(left[i], right[i])'],
          invariants: ['Left state excludes future elements.', 'Right state excludes earlier elements until combined.'],
          defaultComplexity: { time: 'O(n)', space: 'O(n) or O(1) extra' },
          relatedDataStructures: ['array'],
          similarTemplates: ['linear-scan-state', 'dynamic-programming'],
        }),
      },
      {
        key: 'linear-scan-state',
        label: 'Linear scan state',
        description: 'Carry a small state machine through the input and update the best answer as you scan.',
        metadata: m({
          classicProblems: ['53. Maximum Subarray', '121. Best Time to Buy and Sell Stock', '122. Best Time to Buy and Sell Stock II'],
          whenToUse: [
            'The answer can be updated from a fixed-size local state.',
            'Each step only needs the previous state and current item.',
          ],
          whenNotToUse: ['Need branch over multiple choices with overlapping subproblems.', 'Need maintain a variable-size valid window.'],
          signals: ['one pass', 'best so far', 'current state', 'extend or reset', 'state machine'],
          pseudocode: ['state = initial', 'best = initial', 'for item in input:', '  state = transition(state, item)', '  best = update(best, state)'],
          invariants: ['State summarizes all needed history.', 'Best is the optimum over processed prefixes.'],
          defaultComplexity: { time: 'O(n)', space: 'O(1)' },
          relatedDataStructures: ['array'],
          similarTemplates: ['dynamic-programming', 'prefix-suffix-accumulation'],
        }),
      },
    ],
  },
  {
    key: 'group-pointer-search',
    label: 'Pointers, windows, and search',
    description: 'Canonical templates for monotonic movement, search-space reduction, and in-place partitioning.',
    children: [
      {
        key: 'two-pointers',
        label: 'Two pointers',
        description: 'Move two indices according to a monotonic proof to discard impossible candidates.',
        metadata: m({
          classicProblems: ['167. Two Sum II', '11. Container With Most Water', '15. 3Sum'],
          whenToUse: [
            'A sorted or structured input gives a safe pointer movement rule.',
            'The answer depends on a pair or boundary choice.',
          ],
          whenNotToUse: ['Input order is arbitrary and cannot be sorted safely.', 'Need a dynamic multiset of prior states.'],
          signals: ['left right', 'sorted', 'move inward', 'pair', 'boundary'],
          pseudocode: ['l, r = 0, n - 1', 'while l < r:', '  evaluate(l, r)', '  move one pointer by proof'],
          invariants: ['Pointer movement never discards a valid better candidate.', 'Pointers move monotonically.'],
          defaultComplexity: { time: 'O(n) after optional sort', space: 'O(1)' },
          relatedDataStructures: ['array', 'string'],
          similarTemplates: ['sliding-window', 'binary-search'],
        }),
      },
      {
        key: 'sliding-window',
        label: 'Sliding window',
        description: 'Maintain a contiguous window and expand or shrink it until the invariant is satisfied.',
        metadata: m({
          classicProblems: ['3. Longest Substring Without Repeating Characters', '76. Minimum Window Substring', '209. Minimum Size Subarray Sum'],
          whenToUse: [
            'Need optimize over contiguous ranges.',
            'A window validity condition can be maintained incrementally.',
          ],
          whenNotToUse: ['The property is not monotonic under shrinking/expanding.', 'Ranges are better expressed as prefix differences.'],
          signals: ['substring', 'subarray', 'window', 'at most', 'at least', 'expand shrink'],
          pseudocode: ['left = 0', 'for right in range(n):', '  add input[right]', '  while window invalid or can improve:', '    remove input[left]; left += 1', '  update answer'],
          invariants: ['Window state exactly represents input[left:right+1].', 'left only moves forward.'],
          defaultComplexity: { time: 'O(n)', space: 'O(alphabet or window state)' },
          relatedDataStructures: ['counter', 'hash-map', 'deque'],
          similarTemplates: ['two-pointers', 'prefix-sum'],
        }),
      },
      {
        key: 'fast-slow-pointers',
        label: 'Fast/slow pointers',
        description: 'Use pointers moving at different speeds or offsets to detect cycles, midpoints, or gaps.',
        metadata: m({
          classicProblems: ['141. Linked List Cycle', '876. Middle of the Linked List', '19. Remove Nth Node From End of List'],
          whenToUse: [
            'Need cycle detection without extra memory.',
            'Need midpoint or fixed gap in a linked structure.',
          ],
          whenNotToUse: ['Need random access or sorted-array boundary movement.', 'Need modify many links in place.'],
          signals: ['cycle', 'middle', 'nth from end', 'runner', 'gap'],
          pseudocode: ['slow = head; fast = head', 'while fast and fast.next:', '  slow = slow.next', '  fast = fast.next.next', '  check relation'],
          invariants: ['Fast pointer encodes progress relative to slow.', 'The relative distance has the intended meaning.'],
          defaultComplexity: { time: 'O(n)', space: 'O(1)' },
          relatedDataStructures: ['linked-list'],
          similarTemplates: ['linked-list-rewire', 'two-pointers'],
        }),
      },
      {
        key: 'binary-search',
        label: 'Binary search',
        description: 'Use a monotonic predicate to repeatedly discard half of the search space.',
        metadata: m({
          classicProblems: ['704. Binary Search', '34. Find First and Last Position', '875. Koko Eating Bananas'],
          whenToUse: [
            'There is a sorted domain or monotonic yes/no predicate.',
            'Need find boundary, minimum feasible value, or exact target.',
          ],
          whenNotToUse: ['No monotonic predicate can be stated.', 'Need enumerate all valid candidates.'],
          signals: ['sorted', 'lower bound', 'upper bound', 'minimum feasible', 'search answer'],
          pseudocode: ['lo, hi = search_space', 'while lo < hi:', '  mid = choose_mid(lo, hi)', '  if predicate(mid): hi = mid', '  else: lo = mid + 1'],
          invariants: ['The answer remains inside [lo, hi].', 'Predicate partitions the domain into false then true or vice versa.'],
          defaultComplexity: { time: 'O(log n) or O(check * log range)', space: 'O(1)' },
          relatedDataStructures: ['array'],
          similarTemplates: ['two-pointers', 'greedy'],
        }),
      },
      {
        key: 'partition-selection',
        label: 'Partition selection',
        description: 'Rearrange around a pivot or write boundary to select, deduplicate, or compact in place.',
        metadata: m({
          classicProblems: ['26. Remove Duplicates from Sorted Array', '75. Sort Colors', '215. Kth Largest Element in an Array'],
          whenToUse: [
            'Need in-place compaction, partitioning, or kth selection.',
            'Elements can be classified relative to a pivot or write boundary.',
          ],
          whenNotToUse: ['Need stable grouping with arbitrary keys.', 'Need maintain sorted frontier across multiple streams.'],
          signals: ['in place', 'write pointer', 'partition', 'quickselect', 'deduplicate'],
          pseudocode: ['boundary = start', 'for item in input:', '  if belongs_left(item):', '    place item at boundary', '    boundary += 1'],
          invariants: ['Processed region is partitioned correctly.', 'Boundary marks the first unknown or right-side position.'],
          defaultComplexity: { time: 'O(n) average or one pass', space: 'O(1)' },
          relatedDataStructures: ['array'],
          similarTemplates: ['two-pointers', 'heap-priority-queue'],
        }),
      },
    ],
  },
  {
    key: 'group-structures-traversal',
    label: 'Structures and traversal',
    description: 'Canonical templates where the main idea is traversal order or an auxiliary data structure.',
    children: [
      {
        key: 'stack',
        label: 'Stack',
        description: 'Use last-in-first-out state to match, unwind, or simulate nested structure.',
        metadata: m({
          classicProblems: ['20. Valid Parentheses', '150. Evaluate Reverse Polish Notation', '394. Decode String'],
          whenToUse: ['Need match nested pairs.', 'Need process most recent unresolved item first.'],
          whenNotToUse: ['Need maintain sorted candidates.', 'Need FIFO shortest-path traversal.'],
          signals: ['parentheses', 'nested', 'undo', 'evaluate', 'recent unresolved'],
          pseudocode: ['stack = []', 'for token in input:', '  if opens_or_defers(token): push', '  else: pop and resolve'],
          invariants: ['Stack contains unresolved items in nesting order.', 'Top of stack is the next item to resolve.'],
          defaultComplexity: { time: 'O(n)', space: 'O(n)' },
          relatedDataStructures: ['stack'],
          similarTemplates: ['monotonic-stack', 'backtracking'],
        }),
      },
      {
        key: 'monotonic-stack',
        label: 'Monotonic stack',
        description: 'Maintain a stack in sorted order so each new item resolves dominated previous items.',
        metadata: m({
          classicProblems: ['739. Daily Temperatures', '496. Next Greater Element I', '84. Largest Rectangle in Histogram'],
          whenToUse: ['Need next/previous greater or smaller.', 'Need resolve spans or boundaries by dominance.'],
          whenNotToUse: ['Need arbitrary priority updates.', 'Need plain nested matching without ordering.'],
          signals: ['next greater', 'previous smaller', 'histogram', 'span', 'monotonic'],
          pseudocode: ['stack = []', 'for i, x in enumerate(input):', '  while stack and violates_order(stack[-1], x): resolve stack.pop()', '  push i'],
          invariants: ['Stack is monotonic by the chosen key.', 'Each index is pushed and popped at most once.'],
          defaultComplexity: { time: 'O(n)', space: 'O(n)' },
          relatedDataStructures: ['stack'],
          similarTemplates: ['stack', 'heap-priority-queue'],
        }),
      },
      {
        key: 'heap-priority-queue',
        label: 'Heap / priority queue',
        description: 'Keep the best or next frontier element available under a dynamic ordering.',
        metadata: m({
          classicProblems: ['23. Merge k Sorted Lists', '347. Top K Frequent Elements', '295. Find Median from Data Stream'],
          whenToUse: ['Need repeatedly extract min/max.', 'Only top k or frontier candidates matter.'],
          whenNotToUse: ['Need O(1) direct key lookup.', 'A monotonic stack resolves each item once.'],
          signals: ['top k', 'merge k', 'priority', 'frontier', 'median stream'],
          pseudocode: ['heap = initial candidates', 'while heap:', '  item = pop_best(heap)', '  process item', '  push next candidates'],
          invariants: ['Heap top is the next candidate by priority.', 'All needed frontier items are represented in the heap.'],
          defaultComplexity: { time: 'O(n log k)', space: 'O(k)' },
          relatedDataStructures: ['heap', 'priority-queue'],
          similarTemplates: ['partition-selection', 'monotonic-stack'],
        }),
      },
      {
        key: 'linked-list-rewire',
        label: 'Linked-list rewire',
        description: 'Use dummy nodes and pointer rewiring to transform linked structure safely.',
        metadata: m({
          classicProblems: ['206. Reverse Linked List', '21. Merge Two Sorted Lists', '143. Reorder List'],
          whenToUse: ['Need change next pointers.', 'Dummy node or previous/current/next tracking simplifies edge cases.'],
          whenNotToUse: ['Need only detect cycle or midpoint.', 'Array indexing is available and simpler.'],
          signals: ['reverse list', 'dummy node', 'merge list', 'prev current next', 'rewire'],
          pseudocode: ['dummy = Node()', 'prev, cur = dummy_or_head, head', 'while cur:', '  save next', '  rewrite links', '  advance pointers'],
          invariants: ['Already rewired prefix is valid.', 'Unprocessed suffix remains reachable.'],
          defaultComplexity: { time: 'O(n)', space: 'O(1)' },
          relatedDataStructures: ['linked-list'],
          similarTemplates: ['fast-slow-pointers'],
        }),
      },
      {
        key: 'tree-dfs',
        label: 'Tree DFS',
        description: 'Traverse a tree recursively or iteratively and pass information down or return information up.',
        metadata: m({
          classicProblems: ['104. Maximum Depth of Binary Tree', '543. Diameter of Binary Tree', '236. Lowest Common Ancestor'],
          whenToUse: ['Need visit all nodes with parent-child structure.', 'Answer depends on subtree summary or path state.'],
          whenNotToUse: ['Need shortest unweighted levels.', 'Need arbitrary graph cycle handling.'],
          signals: ['tree', 'recursive', 'subtree', 'root to leaf', 'postorder', 'preorder'],
          pseudocode: ['dfs(node, state):', '  if not node: return base', '  left = dfs(node.left, next_state)', '  right = dfs(node.right, next_state)', '  return combine(node, left, right)'],
          invariants: ['Each node is processed once.', 'Return value or carried state has a consistent meaning.'],
          defaultComplexity: { time: 'O(n)', space: 'O(h)' },
          relatedDataStructures: ['tree', 'recursion', 'stack'],
          similarTemplates: ['graph-bfs-dfs', 'dynamic-programming'],
        }),
      },
      {
        key: 'graph-bfs-dfs',
        label: 'Graph BFS/DFS',
        description: 'Explore graph or grid states while tracking visited nodes to avoid repeated work.',
        metadata: m({
          classicProblems: ['200. Number of Islands', '133. Clone Graph', '994. Rotting Oranges'],
          whenToUse: ['Need connected components, reachability, flood fill, or shortest unweighted expansion.', 'States form a graph or grid.'],
          whenNotToUse: ['Dependencies form a DAG and require ordering.', 'Need dynamic connectivity under unions.'],
          signals: ['graph', 'grid', 'visited', 'component', 'shortest unweighted', 'flood fill'],
          pseudocode: ['frontier = [start]', 'visited = set(start)', 'while frontier:', '  node = pop frontier', '  for nei in neighbors(node):', '    if nei not visited: add'],
          invariants: ['Visited nodes are never processed twice.', 'Frontier contains discovered but unresolved states.'],
          defaultComplexity: { time: 'O(V + E)', space: 'O(V)' },
          relatedDataStructures: ['queue', 'stack', 'set'],
          similarTemplates: ['tree-dfs', 'topological-order'],
        }),
      },
      {
        key: 'union-find',
        label: 'Union find',
        description: 'Maintain disjoint sets with near-constant connectivity queries and merges.',
        metadata: m({
          classicProblems: ['547. Number of Provinces', '684. Redundant Connection', '721. Accounts Merge'],
          whenToUse: ['Need connectivity under repeated union operations.', 'Order of edges is not primarily shortest path.'],
          whenNotToUse: ['Need actual traversal path.', 'Need topological dependency order.'],
          signals: ['connected components', 'union', 'find root', 'disjoint set', 'merge groups'],
          pseudocode: ['parent[i] = i', 'find(x): compress path to root', 'union(a, b): parent[root_a] = root_b', 'query roots for connectivity'],
          invariants: ['Each set has one representative root.', 'Path compression preserves membership.'],
          defaultComplexity: { time: 'O(alpha(n)) amortized per op', space: 'O(n)' },
          relatedDataStructures: ['disjoint-set'],
          similarTemplates: ['graph-bfs-dfs', 'topological-order'],
        }),
      },
    ],
  },
  {
    key: 'group-recursive-optimization',
    label: 'Recursion, optimization, and design',
    description: 'Canonical templates for search trees, dependency order, optimization recurrences, and stateful APIs.',
    children: [
      {
        key: 'backtracking',
        label: 'Backtracking',
        description: 'Explore a decision tree by choosing, recursing, and undoing choices.',
        metadata: m({
          classicProblems: ['78. Subsets', '46. Permutations', '39. Combination Sum'],
          whenToUse: ['Need enumerate combinations, permutations, or constrained choices.', 'Search state can be advanced and reverted cleanly.'],
          whenNotToUse: ['Need only optimal value with overlapping subproblems.', 'Choices form a monotonic greedy proof.'],
          signals: ['all combinations', 'permutations', 'choose undo', 'decision tree', 'DFS search'],
          pseudocode: ['path = []', 'dfs(start_or_state):', '  if complete: record path', '  for choice in choices:', '    choose', '    dfs(next_state)', '    undo'],
          invariants: ['Path represents exactly the choices on the recursion stack.', 'Undo restores state before trying the next choice.'],
          defaultComplexity: { time: 'O(branching^depth)', space: 'O(depth)' },
          relatedDataStructures: ['recursion', 'array', 'set'],
          similarTemplates: ['dynamic-programming', 'stack'],
        }),
      },
      {
        key: 'topological-order',
        label: 'Topological order',
        description: 'Process directed dependencies only after prerequisites are resolved.',
        metadata: m({
          classicProblems: ['207. Course Schedule', '210. Course Schedule II', '269. Alien Dictionary'],
          whenToUse: ['Need detect cycles in prerequisites.', 'Need an order that respects directed dependencies.'],
          whenNotToUse: ['Graph is undirected connectivity.', 'Need shortest path levels instead of dependency order.'],
          signals: ['prerequisite', 'DAG', 'in-degree', 'dependency', 'order'],
          pseudocode: ['build graph and indegree', 'queue nodes with indegree 0', 'while queue:', '  node = pop', '  for next: decrement indegree; enqueue if 0'],
          invariants: ['Queue nodes have no unresolved prerequisites.', 'Processed count detects cycles.'],
          defaultComplexity: { time: 'O(V + E)', space: 'O(V + E)' },
          relatedDataStructures: ['queue', 'graph'],
          similarTemplates: ['graph-bfs-dfs', 'union-find'],
        }),
      },
      {
        key: 'dynamic-programming',
        label: 'Dynamic programming',
        description: 'Define states and transitions to reuse overlapping subproblem answers.',
        metadata: m({
          classicProblems: ['70. Climbing Stairs', '198. House Robber', '322. Coin Change'],
          whenToUse: ['Optimal answer decomposes into smaller overlapping states.', 'Need count, min/max, or feasibility over choices.'],
          whenNotToUse: ['No overlapping states and enumeration is required.', 'A greedy exchange proof exists.'],
          signals: ['state transition', 'memo', 'dp', 'min max count', 'overlapping subproblems'],
          pseudocode: ['define dp[state]', 'initialize base cases', 'for state in valid order:', '  dp[state] = combine(previous states)', 'return target state'],
          invariants: ['Each dp value has one precise meaning.', 'Transition only uses already solved or memoized states.'],
          defaultComplexity: { time: 'O(number_of_states * transition_cost)', space: 'O(number_of_states)' },
          relatedDataStructures: ['array', 'map', 'memoization'],
          similarTemplates: ['linear-scan-state', 'backtracking', 'interval-dp'],
        }),
      },
      {
        key: 'interval-dp',
        label: 'Interval DP',
        description: 'Solve ranges by choosing a split, boundary, or last operation inside an interval.',
        metadata: m({
          classicProblems: ['312. Burst Balloons', '516. Longest Palindromic Subsequence', '1039. Minimum Score Triangulation'],
          whenToUse: ['Subproblem is naturally an interval [l, r].', 'Combining answers requires choosing a split or last action.'],
          whenNotToUse: ['State is a simple prefix or capacity.', 'Greedy boundary movement is sufficient.'],
          signals: ['interval', 'split', 'range DP', 'last operation', 'palindrome subsequence'],
          pseudocode: ['for length in 1..n:', '  for l in range:', '    r = l + length - 1', '    dp[l][r] = best over split/action k'],
          invariants: ['Shorter intervals are solved before longer intervals.', 'dp[l][r] only depends on strict subintervals.'],
          defaultComplexity: { time: 'O(n^3) typical', space: 'O(n^2)' },
          relatedDataStructures: ['2d-array'],
          similarTemplates: ['dynamic-programming', 'backtracking'],
        }),
      },
      {
        key: 'greedy',
        label: 'Greedy',
        description: 'Make a locally optimal choice backed by an exchange or dominance argument.',
        metadata: m({
          classicProblems: ['55. Jump Game', '435. Non-overlapping Intervals', '763. Partition Labels'],
          whenToUse: ['A local choice can be proven safe.', 'Sorting or scanning exposes a dominance rule.'],
          whenNotToUse: ['Need explore competing choices without a safety proof.', 'Subproblems overlap and require DP.'],
          signals: ['furthest', 'earliest finish', 'locally optimal', 'exchange argument', 'sort then choose'],
          pseudocode: ['order candidates if needed', 'state = initial', 'for candidate in candidates:', '  if candidate is safe or improves frontier:', '    take/update candidate'],
          invariants: ['Chosen prefix can be extended to an optimal solution.', 'Rejected candidates are dominated by kept state.'],
          defaultComplexity: { time: 'O(n log n) with sorting or O(n)', space: 'O(1) to O(n)' },
          relatedDataStructures: ['array'],
          similarTemplates: ['binary-search', 'dynamic-programming'],
        }),
      },
      {
        key: 'trie-prefix-tree',
        label: 'Trie / prefix tree',
        description: 'Represent strings by shared prefixes to support prefix queries or word search transitions.',
        metadata: m({
          classicProblems: ['208. Implement Trie', '211. Design Add and Search Words', '212. Word Search II'],
          whenToUse: ['Need many prefix queries.', 'Need prune string search by shared prefixes.'],
          whenNotToUse: ['Only need exact membership with no prefix relation.', 'Number of strings is tiny and a set is simpler.'],
          signals: ['prefix', 'trie', 'dictionary', 'word search', 'startsWith'],
          pseudocode: ['root = TrieNode()', 'insert(word): walk/create child per char', 'search(prefix): walk child per char; fail if missing'],
          invariants: ['Each root-to-node path is one prefix.', 'Terminal marker distinguishes full word from prefix.'],
          defaultComplexity: { time: 'O(length) per query', space: 'O(total characters)' },
          relatedDataStructures: ['trie', 'hash-map'],
          similarTemplates: ['backtracking', 'hash-map-lookup'],
        }),
      },
      {
        key: 'design-stateful-api',
        label: 'Stateful API design',
        description: 'Combine multiple data structures to satisfy operation contracts and complexity constraints.',
        metadata: m({
          classicProblems: ['146. LRU Cache', '155. Min Stack', '380. Insert Delete GetRandom O(1)'],
          whenToUse: ['Problem asks to implement a class or API.', 'Each operation has explicit complexity requirements.'],
          whenNotToUse: ['Problem is a one-shot algorithm without persistent operations.', 'One simple data structure already satisfies all operations.'],
          signals: ['design', 'class', 'get put', 'O(1)', 'operation contract', 'data structure composition'],
          pseudocode: ['identify operations and required complexity', 'choose state structures for each operation', 'keep structures synchronized on every mutation'],
          invariants: ['All internal structures describe the same logical state.', 'Every public operation preserves representation consistency.'],
          defaultComplexity: { time: 'Depends on API, often O(1) per op', space: 'O(number of stored items)' },
          relatedDataStructures: ['hash-map', 'linked-list', 'stack', 'array'],
          similarTemplates: ['hash-map-lookup', 'linked-list-rewire'],
        }),
      },
    ],
  },
];

const DATA_STRUCTURE_TAGS: DataStructureSeed[] = [
  { key: 'ds-array', label: 'Array', description: 'Index-addressable contiguous sequence.' },
  { key: 'ds-string', label: 'String', description: 'Character sequence with substring or scanning operations.' },
  { key: 'ds-matrix', label: 'Matrix', description: 'Two-dimensional indexed grid or table.' },
  { key: 'ds-grid', label: 'Grid', description: '2D traversal surface with neighbor movement.' },
  { key: 'ds-hash-map', label: 'Hash map', description: 'Key-value lookup table for counts, indices, or state.' },
  { key: 'ds-hash-set', label: 'Hash set', description: 'Membership set for deduplication or visited checks.' },
  { key: 'ds-counter', label: 'Counter', description: 'Frequency map for characters, values, or signatures.' },
  { key: 'ds-stack', label: 'Stack', description: 'Last-in-first-out container.' },
  { key: 'ds-queue', label: 'Queue', description: 'First-in-first-out frontier container.' },
  { key: 'ds-deque', label: 'Deque', description: 'Double-ended queue for window or monotonic frontier state.' },
  { key: 'ds-heap', label: 'Heap', description: 'Priority-ordered container for repeated best extraction.' },
  { key: 'ds-linked-list', label: 'Linked list', description: 'Node chain manipulated through next pointers.' },
  { key: 'ds-doubly-linked-list', label: 'Doubly linked list', description: 'Node chain with previous and next pointers.' },
  { key: 'ds-tree', label: 'Tree', description: 'Hierarchical acyclic node structure.' },
  { key: 'ds-binary-tree', label: 'Binary tree', description: 'Tree where each node has left and right children.' },
  { key: 'ds-graph', label: 'Graph', description: 'Nodes connected by directed or undirected edges.' },
  { key: 'ds-trie', label: 'Trie', description: 'Prefix tree for strings or token paths.' },
  { key: 'ds-disjoint-set', label: 'Disjoint set', description: 'Union-find structure for dynamic connectivity.' },
  { key: 'ds-bitset', label: 'Bitset', description: 'Compact boolean state represented with bits.' },
];

type FlatSeed = TemplateTagSeed & {
  dimension: PatternTagDimension;
  kind: PatternTagKind;
  source: PatternTagSource;
  isActive: boolean;
  parentKey: string | null;
  sortOrder: number;
};

function flattenSeeds(): FlatSeed[] {
  const seeds: FlatSeed[] = [];

  TEMPLATE_GROUPS.forEach((group, groupIndex) => {
    seeds.push({
      key: group.key,
      label: group.label,
      description: group.description,
      metadata: m({
        classicProblems: [],
        whenToUse: [group.description],
        whenNotToUse: ['Parent group only; choose a concrete canonical template for submissions.'],
        signals: [],
        pseudocode: [],
        invariants: ['Parent groups organize canonical templates but are not selectable submission templates.'],
        defaultComplexity: { time: 'n/a', space: 'n/a' },
        relatedDataStructures: [],
        similarTemplates: [],
      }),
      dimension: 'template',
      kind: 'template_group',
      source: 'seeded',
      isActive: true,
      parentKey: null,
      sortOrder: groupIndex * 100,
    });

    group.children.forEach((child, childIndex) => {
      seeds.push({
        ...child,
        dimension: 'template',
        kind: 'tag',
        source: 'seeded',
        isActive: true,
        parentKey: group.key,
        sortOrder: groupIndex * 100 + childIndex + 1,
      });
    });
  });

  DATA_STRUCTURE_TAGS.forEach((tag, index) => {
    seeds.push({
      key: tag.key,
      label: tag.label,
      description: tag.description,
      metadata: m({
        classicProblems: [],
        whenToUse: [],
        whenNotToUse: [],
        signals: [],
        pseudocode: [],
        invariants: [],
        defaultComplexity: { time: 'n/a', space: 'n/a' },
        relatedDataStructures: [],
        similarTemplates: [],
      }),
      dimension: 'data_structure',
      kind: 'tag',
      source: 'seeded',
      isActive: true,
      parentKey: null,
      sortOrder: 10_000 + index,
    });
  });

  return seeds;
}

function validateSelectableTemplateMetadata(seeds: FlatSeed[]) {
  const errors: string[] = [];

  for (const seed of seeds.filter((entry) => entry.isActive && entry.dimension === 'template' && entry.kind === 'tag')) {
    const metadata = seed.metadata;
    const checks: Array<[string, boolean]> = [
      ['classicProblems', metadata.classicProblems.length > 0],
      ['whenToUse', metadata.whenToUse.length > 0],
      ['whenNotToUse', metadata.whenNotToUse.length > 0],
      ['signals', metadata.signals.length > 0],
      ['pseudocode', metadata.pseudocode.length > 0],
      ['invariants', metadata.invariants.length > 0],
      ['defaultComplexity.time', metadata.defaultComplexity.time.trim().length > 0],
      ['defaultComplexity.space', metadata.defaultComplexity.space.trim().length > 0],
    ];

    for (const [field, ok] of checks) {
      if (!ok) {
        errors.push(`${seed.key} missing ${field}`);
      }
    }
  }

  if (errors.length > 0) {
    throw new Error(`Invalid selectable template metadata:\n${errors.map((entry) => `- ${entry}`).join('\n')}`);
  }
}

async function seedPatternTags() {
  const { PrismaClient } = await import('@prisma/client');
  const prisma = new PrismaClient();
  const seeds = flattenSeeds();
  validateSelectableTemplateMetadata(seeds);
  const seedKeys = seeds.map((seed) => seed.key);
  const parentIds = new Map<string, string>();

  try {
    await prisma.patternTag.updateMany({
      where: {
        dimension: { in: ['template', 'data_structure'] },
        source: 'seeded',
        key: { notIn: seedKeys },
        isActive: true,
      },
      data: { isActive: false },
    });

    for (const seed of seeds.filter((entry) => entry.parentKey === null)) {
      const tag = await prisma.patternTag.upsert({
        where: { key: seed.key },
        create: {
          key: seed.key,
          label: seed.label,
          dimension: seed.dimension,
          kind: seed.kind,
          source: seed.source,
          description: seed.description,
          metadata: seed.metadata,
          isActive: seed.isActive,
          sortOrder: seed.sortOrder,
        },
        update: {
          label: seed.label,
          dimension: seed.dimension,
          kind: seed.kind,
          source: seed.source,
          description: seed.description,
          metadata: seed.metadata,
          parentId: null,
          isActive: seed.isActive,
          sortOrder: seed.sortOrder,
        },
      });
      parentIds.set(seed.key, tag.id);
    }

    for (const seed of seeds.filter((entry) => entry.parentKey !== null)) {
      const parentId = parentIds.get(seed.parentKey ?? '');
      if (!parentId) {
        throw new Error(`Missing parent pattern tag for ${seed.key}: ${seed.parentKey}`);
      }

      await prisma.patternTag.upsert({
        where: { key: seed.key },
        create: {
          key: seed.key,
          label: seed.label,
          dimension: seed.dimension,
          kind: seed.kind,
          source: seed.source,
          description: seed.description,
          metadata: seed.metadata,
          parentId,
          isActive: seed.isActive,
          sortOrder: seed.sortOrder,
        },
        update: {
          label: seed.label,
          dimension: seed.dimension,
          kind: seed.kind,
          source: seed.source,
          description: seed.description,
          metadata: seed.metadata,
          parentId,
          isActive: seed.isActive,
          sortOrder: seed.sortOrder,
        },
      });
    }
  } finally {
    await prisma.$disconnect();
  }

  return seeds;
}

function printDryRun() {
  const seeds = flattenSeeds();
  validateSelectableTemplateMetadata(seeds);
  const groups = seeds.filter((entry) => entry.dimension === 'template' && entry.kind === 'template_group');
  const selectable = seeds.filter((entry) => entry.isActive && entry.dimension === 'template' && entry.kind === 'tag');
  const dataStructures = seeds.filter((entry) => entry.isActive && entry.dimension === 'data_structure');

  console.log(
    `Pattern tag dry run: ${groups.length} parent groups, ${selectable.length} selectable canonical template tags, ${dataStructures.length} data structure tags.`,
  );
  for (const group of groups) {
    const childCount = seeds.filter((entry) => entry.parentKey === group.key).length;
    console.log(`- ${group.key}: ${childCount} selectable templates`);
  }
}

async function main() {
  if (process.argv.includes('--dry-run')) {
    printDryRun();
    return;
  }

  const seeds = await seedPatternTags();
  const parentCount = seeds.filter((entry) => entry.dimension === 'template' && entry.kind === 'template_group').length;
  const selectableCount = seeds.filter((entry) => entry.isActive && entry.dimension === 'template' && entry.kind === 'tag').length;
  const dataStructureCount = seeds.filter((entry) => entry.isActive && entry.dimension === 'data_structure').length;

  console.log(
    `Seeded ${parentCount} parent template groups, ${selectableCount} selectable canonical template tags, and ${dataStructureCount} data structure tags.`,
  );
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
