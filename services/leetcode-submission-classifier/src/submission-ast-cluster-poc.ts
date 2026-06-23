import { mkdirSync, readFileSync, existsSync, writeFileSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { spawnSync } from 'node:child_process';

import { PrismaClient, type Prisma } from '@prisma/client';

type SubmissionRow = {
  id: string;
  titleSlug: string | null;
  status: string;
  content: string;
  createdAt: Date;
  submissionDetails: Prisma.JsonValue | null;
};

export type ExtractedFeatures = {
  parseOk: boolean;
  syntaxError: string | null;
  imports: string[];
  calledFunctions: string[];
  assignedNames: string[];
  attributeNames: string[];
  forCount: number;
  whileCount: number;
  ifCount: number;
  comprehensionCount: number;
  maxLoopDepth: number;
  hasDeque: boolean;
  hasPopleft: boolean;
  hasAppendleft: boolean;
  hasCounter: boolean;
  hasDefaultdict: boolean;
  hasHeapq: boolean;
  hasSet: boolean;
  hasDict: boolean;
  hasSortedOrSort: boolean;
  hasVisited: boolean;
  hasRecursion: boolean;
  hasLeftRightPointers: boolean;
  hasMid: boolean;
  hasPrefixSignal: boolean;
  hasDpSignal: boolean;
  hasUnionFindSignal: boolean;
  hasTreeSignal: boolean;
  hasGridSignal: boolean;
  hasGraphSignal: boolean;
  hasNeighborSignal: boolean;
  hasQueueLoopSignal: boolean;
};

export type StructuredFingerprint = {
  loops: string[];
  recursion: boolean;
  dataStructures: string[];
  ops: string[];
  stateVars: string[];
  transitionOrder: string[];
  answerUpdateTiming: string;
  confidence: number;
};

type ClusteredSubmission = {
  submission: SubmissionRow;
  lang: string | null;
  features: ExtractedFeatures;
  fingerprint: StructuredFingerprint;
  featureBag: Record<string, number>;
  clusterKey: string;
};

export type CliOptions = {
  limit: number;
  scan: number;
  slug?: string;
  includeStatuses?: string[];
  unique: boolean;
  threshold: number;
  out?: string;
  json: boolean;
};

export type ClusterArtifact = {
  generatedAt: string;
  options: {
    limit: number;
    scan: number;
    slug?: string;
    statuses: string[];
    unique: boolean;
  };
  summary: {
    submissionCount: number;
    clusterCount: number;
  };
  clusters: Array<{
    clusterKey: string;
    count: number;
    fingerprint: StructuredFingerprint;
    evidence: Array<{
      feature: string;
      present: number;
      score: number;
    }>;
    submissions: Array<{
      id: string;
      titleSlug: string | null;
      status: string;
      lang: string | null;
      createdAt: string;
      features: ExtractedFeatures;
      featureBag: Record<string, number>;
    }>;
  }>;
};

const PYTHON_EXTRACTOR = String.raw`
import ast, json, re, sys

rows = json.load(sys.stdin)
results = []

def apply_lexical_signals(base, code):
    lowered = code.lower()
    lines = [line.strip().lower() for line in code.splitlines() if line.strip()]
    base["hasDeque"] = base["hasDeque"] or "deque(" in lowered or "import deque" in lowered
    base["hasPopleft"] = base["hasPopleft"] or ".popleft(" in lowered
    base["hasAppendleft"] = base["hasAppendleft"] or ".appendleft(" in lowered
    base["hasCounter"] = base["hasCounter"] or "counter(" in lowered or "import counter" in lowered
    base["hasDefaultdict"] = base["hasDefaultdict"] or "defaultdict(" in lowered
    base["hasHeapq"] = base["hasHeapq"] or "heapq" in lowered or "heappush(" in lowered or "heappop(" in lowered
    base["hasSet"] = base["hasSet"] or "set(" in lowered
    base["hasDict"] = base["hasDict"] or "dict(" in lowered
    base["hasSortedOrSort"] = base["hasSortedOrSort"] or "sorted(" in lowered or ".sort(" in lowered
    base["hasVisited"] = base["hasVisited"] or "visited" in lowered
    base["hasLeftRightPointers"] = base["hasLeftRightPointers"] or bool(re.search(r"\b(left|right|l|r)\b", lowered))
    base["hasMid"] = base["hasMid"] or bool(re.search(r"\bmid\b", lowered))
    base["hasPrefixSignal"] = base["hasPrefixSignal"] or "prefix" in lowered
    base["hasDpSignal"] = base["hasDpSignal"] or bool(re.search(r"\bdp\b|\bmemo\b", lowered))
    base["hasUnionFindSignal"] = base["hasUnionFindSignal"] or ("parent" in lowered and ("find(" in lowered or "union(" in lowered))
    base["hasTreeSignal"] = base["hasTreeSignal"] or ".left" in lowered or ".right" in lowered or "treenode" in lowered
    base["hasGridSignal"] = base["hasGridSignal"] or any(token in lowered for token in ["grid", "mat", "matrix", "board", "image"])
    base["hasGraphSignal"] = base["hasGraphSignal"] or any(token in lowered for token in ["graph", "adj", "adjacency", "edge"])
    base["hasNeighborSignal"] = base["hasNeighborSignal"] or any(token in lowered for token in ["neighbor", "neighbour", "directions", "dirs", "delta"])
    base["forCount"] = max(base["forCount"], sum(1 for line in lines if line.startswith("for ")))
    base["whileCount"] = max(base["whileCount"], sum(1 for line in lines if line.startswith("while ")))
    base["ifCount"] = max(base["ifCount"], sum(1 for line in lines if line.startswith("if ")))
    base["hasQueueLoopSignal"] = base["hasQueueLoopSignal"] or (base["hasPopleft"] and "while queue" in lowered)
    function_match = re.search(r"def\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\(", code)
    if function_match:
        function_name = function_match.group(1)
        base["hasRecursion"] = base["hasRecursion"] or code.count(f"{function_name}(") > 1

for row in rows:
    code = row.get("content", "")
    base = {
        "parseOk": True,
        "syntaxError": None,
        "imports": [],
        "calledFunctions": [],
        "assignedNames": [],
        "attributeNames": [],
        "forCount": 0,
        "whileCount": 0,
        "ifCount": 0,
        "comprehensionCount": 0,
        "maxLoopDepth": 0,
        "hasDeque": False,
        "hasPopleft": False,
        "hasAppendleft": False,
        "hasCounter": False,
        "hasDefaultdict": False,
        "hasHeapq": False,
        "hasSet": False,
        "hasDict": False,
        "hasSortedOrSort": False,
        "hasVisited": False,
        "hasRecursion": False,
        "hasLeftRightPointers": False,
        "hasMid": False,
        "hasPrefixSignal": False,
        "hasDpSignal": False,
        "hasUnionFindSignal": False,
        "hasTreeSignal": False,
        "hasGridSignal": False,
        "hasGraphSignal": False,
        "hasNeighborSignal": False,
        "hasQueueLoopSignal": False,
    }
    try:
        tree = ast.parse(code)
    except SyntaxError as exc:
        base["parseOk"] = False
        base["syntaxError"] = f"{exc.msg} at line {exc.lineno}"
        apply_lexical_signals(base, code)
        results.append(base)
        continue

    imports = set()
    called = []
    assigned = set()
    attrs = set()
    current_functions = []

    class Visitor(ast.NodeVisitor):
        def __init__(self):
            self.loop_depth = 0

        def visit_Import(self, node):
            for alias in node.names:
                imports.add(alias.name.split(".")[0])
            self.generic_visit(node)

        def visit_ImportFrom(self, node):
            if node.module:
                imports.add(node.module.split(".")[0])
            for alias in node.names:
                imports.add(alias.name.split(".")[0])
            self.generic_visit(node)

        def visit_FunctionDef(self, node):
            current_functions.append(node.name)
            assigned.add(node.name)
            self.generic_visit(node)
            current_functions.pop()

        def visit_Assign(self, node):
            for target in node.targets:
                self._record_target(target)
            self.generic_visit(node)

        def visit_AnnAssign(self, node):
            self._record_target(node.target)
            self.generic_visit(node)

        def _record_target(self, target):
            if isinstance(target, ast.Name):
                assigned.add(target.id)
            elif isinstance(target, (ast.Tuple, ast.List)):
                for elt in target.elts:
                    self._record_target(elt)

        def visit_For(self, node):
            base["forCount"] += 1
            self.loop_depth += 1
            base["maxLoopDepth"] = max(base["maxLoopDepth"], self.loop_depth)
            self.generic_visit(node)
            self.loop_depth -= 1

        def visit_While(self, node):
            base["whileCount"] += 1
            self.loop_depth += 1
            base["maxLoopDepth"] = max(base["maxLoopDepth"], self.loop_depth)
            self.generic_visit(node)
            self.loop_depth -= 1

        def visit_If(self, node):
            base["ifCount"] += 1
            self.generic_visit(node)

        def visit_ListComp(self, node):
            base["comprehensionCount"] += 1
            self.generic_visit(node)

        visit_SetComp = visit_ListComp
        visit_DictComp = visit_ListComp
        visit_GeneratorExp = visit_ListComp

        def visit_Name(self, node):
            assigned_name = node.id.lower()
            if assigned_name == "visited":
                base["hasVisited"] = True
            if assigned_name in {"left", "right", "l", "r"}:
                base["hasLeftRightPointers"] = True
            if assigned_name == "mid":
                base["hasMid"] = True
            if assigned_name.startswith("prefix"):
                base["hasPrefixSignal"] = True
            if assigned_name in {"dp", "memo"} or assigned_name.startswith("dp"):
                base["hasDpSignal"] = True
            if assigned_name in {"parent", "rank"}:
                base["hasUnionFindSignal"] = True
            if assigned_name in {"grid", "mat", "matrix", "board", "image"}:
                base["hasGridSignal"] = True
            if assigned_name in {"graph", "adj", "adjacency"}:
                base["hasGraphSignal"] = True
            if assigned_name in {"neighbors", "neighbours", "dirs", "directions"}:
                base["hasNeighborSignal"] = True
            self.generic_visit(node)

        def visit_Call(self, node):
            func_name = None
            if isinstance(node.func, ast.Name):
                func_name = node.func.id
            elif isinstance(node.func, ast.Attribute):
                func_name = node.func.attr
                attrs.add(node.func.attr)
            if func_name:
                called.append(func_name)
                lower = func_name.lower()
                if lower == "set":
                    base["hasSet"] = True
                if lower in {"dict", "defaultdict"}:
                    base["hasDict"] = True
                if lower == "defaultdict":
                    base["hasDefaultdict"] = True
                if lower == "deque":
                    base["hasDeque"] = True
                if lower == "counter":
                    base["hasCounter"] = True
                if lower in {"heappush", "heappop", "heapify"}:
                    base["hasHeapq"] = True
                if lower in {"sorted", "sort"}:
                    base["hasSortedOrSort"] = True
                if lower == "popleft":
                    base["hasPopleft"] = True
                if lower == "appendleft":
                    base["hasAppendleft"] = True
                if current_functions and lower == current_functions[-1]:
                    base["hasRecursion"] = True
                if lower in {"find", "union"}:
                    base["hasUnionFindSignal"] = True
                if lower in {"dfs", "bfs"}:
                    base["hasGraphSignal"] = True
            self.generic_visit(node)

        def visit_Attribute(self, node):
            attrs.add(node.attr)
            lower = node.attr.lower()
            if lower in {"left", "right", "val"}:
                base["hasTreeSignal"] = True
            if lower == "popleft":
                base["hasPopleft"] = True
            if lower == "appendleft":
                base["hasAppendleft"] = True
            if lower in {"heappush", "heappop"}:
                base["hasHeapq"] = True
            if lower in {"sort"}:
                base["hasSortedOrSort"] = True
            self.generic_visit(node)

    Visitor().visit(tree)

    base["imports"] = sorted(imports)
    base["calledFunctions"] = called
    base["assignedNames"] = sorted(assigned)
    base["attributeNames"] = sorted(attrs)
    base["hasDeque"] = base["hasDeque"] or "deque" in imports or "collections" in imports
    base["hasCounter"] = base["hasCounter"] or "Counter" in imports or "collections" in imports
    base["hasHeapq"] = base["hasHeapq"] or "heapq" in imports
    base["hasQueueLoopSignal"] = base["hasPopleft"] and base["whileCount"] > 0
    apply_lexical_signals(base, code)
    results.append(base)

json.dump(results, sys.stdout)
`;

function resolveDatabaseUrl(databaseUrl = process.env.DATABASE_URL): string | undefined {
  if (!databaseUrl) {
    return undefined;
  }

  try {
    const parsed = new URL(databaseUrl);
    if (!parsed.hostname.includes('-pooler.')) {
      return databaseUrl;
    }

    if (!parsed.searchParams.has('pgbouncer')) {
      parsed.searchParams.set('pgbouncer', 'true');
    }
    if (!parsed.searchParams.has('connection_limit')) {
      parsed.searchParams.set('connection_limit', process.env.PRISMA_CONNECTION_LIMIT ?? '1');
    }
    if (!parsed.searchParams.has('pool_timeout')) {
      parsed.searchParams.set('pool_timeout', process.env.PRISMA_POOL_TIMEOUT ?? '30');
    }

    return parsed.toString();
  } catch {
    return databaseUrl;
  }
}

function parseArgs(argv: string[]): CliOptions {
  const options: CliOptions = { limit: 120, scan: 300, unique: false, threshold: 0.55, json: false };

  for (let index = 0; index < argv.length; index += 1) {
    const arg = argv[index];
    const next = argv[index + 1];

    if (arg === '--limit' && next) {
      options.limit = Number(next);
      index += 1;
    } else if (arg === '--scan' && next) {
      options.scan = Number(next);
      index += 1;
    } else if (arg === '--slug' && next) {
      options.slug = next;
      index += 1;
    } else if (arg === '--status' && next) {
      options.includeStatuses = next.split(',').map((value) => value.trim()).filter(Boolean);
      index += 1;
    } else if (arg === '--threshold' && next) {
      options.threshold = Number(next);
      index += 1;
    } else if (arg === '--unique') {
      options.unique = true;
    } else if (arg === '--out' && next) {
      options.out = next;
      index += 1;
    } else if (arg === '--json') {
      options.json = true;
    }
  }

  return options;
}

function loadRepoEnv() {
  if (process.env.DATABASE_URL) {
    return;
  }

  const repoRoot = resolve(dirname(fileURLToPath(import.meta.url)), '../../..');
  const envPath = resolve(repoRoot, '.env');
  if (!existsSync(envPath)) {
    return;
  }

  const contents = readFileSync(envPath, 'utf8');
  for (const rawLine of contents.split(/\r?\n/u)) {
    const line = rawLine.trim();
    if (!line || line.startsWith('#')) {
      continue;
    }

    const equalsIndex = line.indexOf('=');
    if (equalsIndex <= 0) {
      continue;
    }

    const key = line.slice(0, equalsIndex).trim();
    let value = line.slice(equalsIndex + 1).trim();
    if ((value.startsWith('"') && value.endsWith('"')) || (value.startsWith("'") && value.endsWith("'"))) {
      value = value.slice(1, -1);
    }
    if (!(key in process.env)) {
      process.env[key] = value;
    }
  }
}

function languageOf(submission: SubmissionRow): string | null {
  if (!submission.submissionDetails || typeof submission.submissionDetails !== 'object' || Array.isArray(submission.submissionDetails)) {
    return null;
  }
  const details = submission.submissionDetails as Record<string, unknown>;
  const lang = details.lang ?? details.language ?? details.pretty_lang ?? details.langName;
  return typeof lang === 'string' ? lang.toLowerCase() : null;
}

export function buildStructuredFingerprint(features: ExtractedFeatures): StructuredFingerprint {
  const loops = new Set<string>();
  const dataStructures = new Set<string>();
  const ops = new Set<string>();
  const stateVars = new Set<string>();
  const transitionOrder = new Set<string>();

  if (features.forCount > 0) loops.add('for');
  if (features.whileCount > 0) loops.add('while');
  if (features.maxLoopDepth > 1 || features.forCount + features.whileCount >= 2) loops.add('nested_loop');

  if (features.hasDict || features.hasDefaultdict) dataStructures.add('dict');
  if (features.hasSet || features.hasVisited) dataStructures.add('set');
  if (features.hasCounter) dataStructures.add('counter');
  if (features.hasDeque || features.hasPopleft || features.hasAppendleft) dataStructures.add('deque');
  if (features.hasHeapq) dataStructures.add('heap');
  if (features.hasTreeSignal) dataStructures.add('tree_shape');
  if (features.hasGridSignal) dataStructures.add('grid');
  if (features.hasGraphSignal || features.hasNeighborSignal) dataStructures.add('graph_state');
  if (features.hasUnionFindSignal) dataStructures.add('parent_array');
  if (dataStructures.size === 0) dataStructures.add('array');

  if (features.hasPopleft) ops.add('popleft');
  if (features.hasAppendleft) ops.add('appendleft');
  if (features.hasDeque) ops.add('append');
  if (features.hasCounter) ops.add('increment_count');
  if (features.hasDefaultdict || features.hasDict) ops.add('lookup_update');
  if (features.hasSet || features.hasVisited) ops.add('membership_check');
  if (features.hasHeapq) ops.add('priority_pop_push');
  if (features.hasSortedOrSort) ops.add('sort');
  if (features.hasMid) ops.add('mid_compute');
  if (features.calledFunctions.includes('max')) ops.add('max_update');
  if (features.calledFunctions.includes('min')) ops.add('min_update');

  if (features.hasLeftRightPointers) {
    stateVars.add('left');
    stateVars.add('right');
  }
  if (features.hasVisited) stateVars.add('visited');
  if (features.hasMid) stateVars.add('mid');
  if (features.hasPrefixSignal) stateVars.add('prefix');
  if (features.hasDpSignal) stateVars.add('dp');
  if (features.hasUnionFindSignal) {
    stateVars.add('parent');
    stateVars.add('rank');
  }
  if (features.hasTreeSignal) stateVars.add('node_children');
  if (features.hasGridSignal) stateVars.add('grid_coords');

  if (features.hasQueueLoopSignal) transitionOrder.add('frontier_pop_then_expand');
  if (features.hasRecursion) transitionOrder.add('recursive_descent');
  if (features.hasMid && features.whileCount > 0) transitionOrder.add('midpoint_then_boundary_narrow');
  if (features.hasLeftRightPointers && features.whileCount > 0 && (features.hasCounter || features.hasDict || features.hasSet)) {
    transitionOrder.add('expand_then_shrink_window');
  }
  if (features.hasPrefixSignal && (features.hasDict || features.hasCounter)) {
    transitionOrder.add('accumulate_then_lookup');
  }
  if (features.hasDpSignal) transitionOrder.add('state_transition_update');
  if (features.hasUnionFindSignal) transitionOrder.add('find_then_union');
  if (transitionOrder.size === 0) transitionOrder.add('sequential_scan');

  let answerUpdateTiming = 'unknown';
  if (features.hasQueueLoopSignal) {
    answerUpdateTiming = 'on_frontier_hit';
  } else if (features.hasLeftRightPointers && features.whileCount > 0 && (features.hasCounter || features.hasDict || features.hasSet)) {
    answerUpdateTiming = 'after_shrink';
  } else if (features.hasMid && features.whileCount > 0) {
    answerUpdateTiming = 'after_boundary_update';
  } else if (features.hasDpSignal) {
    answerUpdateTiming = 'during_state_transition';
  } else if (features.forCount > 0 || features.whileCount > 0) {
    answerUpdateTiming = 'inside_scan';
  }

  let confidence = 0.35;
  if (features.hasQueueLoopSignal && (features.hasVisited || features.hasGridSignal || features.hasGraphSignal)) confidence += 0.3;
  if (features.hasMid && features.whileCount > 0) confidence += 0.25;
  if (features.hasLeftRightPointers && features.whileCount > 0) confidence += 0.2;
  if (features.hasPrefixSignal && (features.hasDict || features.hasCounter)) confidence += 0.2;
  if (features.hasDpSignal || features.hasUnionFindSignal || features.hasHeapq) confidence += 0.2;
  confidence = Math.min(1, Number(confidence.toFixed(2)));

  return {
    loops: [...loops].sort(),
    recursion: features.hasRecursion,
    dataStructures: [...dataStructures].sort(),
    ops: [...ops].sort(),
    stateVars: [...stateVars].sort(),
    transitionOrder: [...transitionOrder].sort(),
    answerUpdateTiming,
    confidence,
  };
}

export function buildClusterKey(fingerprint: StructuredFingerprint) {
  return [
    `loops=${fingerprint.loops.join('+') || 'none'}`,
    `rec=${fingerprint.recursion ? 'y' : 'n'}`,
    `ds=${fingerprint.dataStructures.join('+') || 'none'}`,
    `ops=${fingerprint.ops.join('+') || 'none'}`,
    `state=${fingerprint.stateVars.join('+') || 'none'}`,
    `transition=${fingerprint.transitionOrder.join('+') || 'none'}`,
    `answer=${fingerprint.answerUpdateTiming}`,
  ].join('__');
}

function addFeature(bag: Record<string, number>, key: string, value = 1) {
  bag[key] = (bag[key] ?? 0) + value;
}

export function buildFeatureBag(features: ExtractedFeatures): Record<string, number> {
  const bag: Record<string, number> = {};

  if (features.forCount > 0) addFeature(bag, 'ctrl:for', features.forCount);
  if (features.whileCount > 0) addFeature(bag, 'ctrl:while', features.whileCount);
  if (features.ifCount > 0) addFeature(bag, 'ctrl:if', Math.min(features.ifCount, 3));
  if (features.maxLoopDepth > 1 || features.forCount + features.whileCount >= 2) addFeature(bag, 'motif:nested_loop', 3);
  if (features.hasRecursion) addFeature(bag, 'control_fact:direct_recursion', 5);

  if (features.hasDeque) addFeature(bag, 'var_op:init:Call:deque', 2);
  if (features.hasCounter) addFeature(bag, 'var_op:init:Call:Counter', 2);
  if (features.hasDefaultdict) addFeature(bag, 'var_op:init:Call:defaultdict', 2);
  if (features.hasDict) addFeature(bag, 'var_op:init:Dict', 1.5);
  if (features.hasSet || features.hasVisited) addFeature(bag, 'var_op:init:Set', 1.5);
  if (features.hasHeapq) addFeature(bag, 'role:priority_queue_ops', 3);
  if (features.hasGridSignal) addFeature(bag, 'role:indexed_grid_state', 2);
  if (features.hasTreeSignal) addFeature(bag, 'role:node_child_state', 2);
  if (features.hasGraphSignal || features.hasNeighborSignal) addFeature(bag, 'role:graph_state_expansion', 2);

  if (features.hasPopleft) addFeature(bag, 'method:popleft');
  if (features.hasAppendleft) addFeature(bag, 'method:appendleft');
  if (features.hasDeque) addFeature(bag, 'method:append');
  if (features.hasSet || features.hasVisited) addFeature(bag, 'method:add');
  if (features.hasDict || features.hasDefaultdict) addFeature(bag, 'method:get');
  if (features.hasSortedOrSort) addFeature(bag, 'call:sorted_or_sort');
  if (features.hasMid) addFeature(bag, 'assign:midpoint');
  if (features.hasPrefixSignal) addFeature(bag, 'role:prefix_state');
  if (features.hasDpSignal) addFeature(bag, 'role:dp_state');
  if (features.hasUnionFindSignal) addFeature(bag, 'role:union_find_state', 3);

  if (features.hasQueueLoopSignal) addFeature(bag, 'motif:frontier_pop_then_expand', 3);
  if (features.hasLeftRightPointers && features.whileCount > 0) addFeature(bag, 'motif:left_right_while', 2);
  if (features.hasLeftRightPointers && features.whileCount > 0 && (features.hasCounter || features.hasDict || features.hasSet)) {
    addFeature(bag, 'motif:expand_then_shrink_window', 3);
  }
  if (features.hasPrefixSignal && (features.hasDict || features.hasCounter)) addFeature(bag, 'motif:accumulate_then_lookup', 3);
  if (features.hasMid && features.whileCount > 0) addFeature(bag, 'motif:midpoint_boundary_narrow', 3);

  if (!features.parseOk) addFeature(bag, 'source:lexical_fallback', 0.5);
  if (Object.keys(bag).some((key) => key.startsWith('var_op:init:'))) addFeature(bag, 'role:explicit_state_init');

  return bag;
}

function featureWeight(key: string): number {
  if (key === 'motif:nested_loop') return 0.6;
  if (key.startsWith('motif:') || key.startsWith('role:') || key.startsWith('control_fact:')) return 3;
  if (key.startsWith('method:') || key.startsWith('call:')) return 2.2;
  if (key.startsWith('assign:') || key.startsWith('var_op:')) return 1.2;
  if (key.startsWith('ctrl:')) return 0.4;
  if (key.startsWith('source:')) return 0;
  return 0.8;
}

function vectorize(bag: Record<string, number>): Record<string, number> {
  return Object.fromEntries(
    Object.entries(bag)
      .map(([key, value]) => [key, Math.min(value, 3) * featureWeight(key)] as const)
      .filter(([, value]) => value > 0),
  );
}

function isStructuralSignal(key: string): boolean {
  if (key === 'motif:nested_loop' || key === 'role:explicit_state_init') return false;
  return /^(motif|role|method|call|assign|var_op|control_fact):/u.test(key);
}

export function structuralSimilarity(left: Record<string, number>, right: Record<string, number>): number {
  const leftVector = vectorize(left);
  const rightVector = vectorize(right);
  const keys = new Set([...Object.keys(leftVector), ...Object.keys(rightVector)]);
  if (keys.size === 0) return 0;

  const hasSharedStructuralSignal = [...keys].some((key) => isStructuralSignal(key) && key in leftVector && key in rightVector);
  if (!hasSharedStructuralSignal) return 0;

  let numerator = 0;
  let denominator = 0;
  for (const key of keys) {
    numerator += Math.min(leftVector[key] ?? 0, rightVector[key] ?? 0);
    denominator += Math.max(leftVector[key] ?? 0, rightVector[key] ?? 0);
  }

  return denominator === 0 ? 0 : numerator / denominator;
}

class Dsu {
  private readonly parent: number[];

  constructor(size: number) {
    this.parent = Array.from({ length: size }, (_, index) => index);
  }

  find(index: number): number {
    while (this.parent[index] !== index) {
      this.parent[index] = this.parent[this.parent[index]];
      index = this.parent[index];
    }
    return index;
  }

  union(left: number, right: number) {
    const leftRoot = this.find(left);
    const rightRoot = this.find(right);
    if (leftRoot !== rightRoot) {
      this.parent[rightRoot] = leftRoot;
    }
  }
}

function clusterSubmissions(clustered: ClusteredSubmission[], threshold: number): ClusteredSubmission[][] {
  const dsu = new Dsu(clustered.length);

  for (let left = 0; left < clustered.length; left += 1) {
    for (let right = left + 1; right < clustered.length; right += 1) {
      const similarity = structuralSimilarity(clustered[left].featureBag, clustered[right].featureBag);
      if (similarity >= threshold) {
        dsu.union(left, right);
      }
    }
  }

  const groups = new Map<number, ClusteredSubmission[]>();
  for (let index = 0; index < clustered.length; index += 1) {
    const root = dsu.find(index);
    const group = groups.get(root) ?? [];
    group.push(clustered[index]);
    groups.set(root, group);
  }

  return [...groups.values()].sort((left, right) => right.length - left.length || String(left[0].submission.titleSlug).localeCompare(String(right[0].submission.titleSlug)));
}

export function sharedEvidence(items: ClusteredSubmission[], top = 12): Array<{ feature: string; present: number; score: number }> {
  const presence = new Map<string, number>();
  const strength = new Map<string, number>();
  const minimumPresence = items.length === 1 ? 1 : Math.max(2, Math.ceil(items.length * 0.5));

  for (const item of items) {
    for (const [key, value] of Object.entries(item.featureBag)) {
      presence.set(key, (presence.get(key) ?? 0) + 1);
      strength.set(key, (strength.get(key) ?? 0) + Math.min(value, 3) * featureWeight(key));
    }
  }

  return [...presence.keys()]
    .filter((key) => (presence.get(key) ?? 0) >= minimumPresence)
    .filter((key) => (strength.get(key) ?? 0) > 0)
    .map((feature) => ({
      feature,
      present: presence.get(feature) ?? 0,
      score: Number((strength.get(feature) ?? 0).toFixed(2)),
    }))
    .sort((left, right) => right.present - left.present || right.score - left.score || left.feature.localeCompare(right.feature))
    .slice(0, top);
}

export function dedupeLatestByTitleSlug(rows: SubmissionRow[], limit: number): SubmissionRow[] {
  const seen = new Set<string>();
  const uniqueRows: SubmissionRow[] = [];

  for (const row of rows) {
    const key = row.titleSlug?.trim();
    if (!key || seen.has(key)) {
      continue;
    }
    seen.add(key);
    uniqueRows.push(row);
    if (uniqueRows.length >= limit) {
      break;
    }
  }

  return uniqueRows;
}

async function fetchCandidateSubmissions(prisma: PrismaClient, options: CliOptions): Promise<SubmissionRow[]> {
  const rows = await prisma.submission.findMany({
    take: options.scan,
    orderBy: { createdAt: 'desc' },
    where: {
      ...(options.slug ? { titleSlug: options.slug } : {}),
      ...(options.includeStatuses?.length ? { status: { in: options.includeStatuses } } : { status: 'Accepted' }),
    },
    select: {
      id: true,
      titleSlug: true,
      status: true,
      content: true,
      createdAt: true,
      submissionDetails: true,
    },
  });

  const pythonRows = rows.filter((row) => languageOf(row)?.includes('python'));

  if (!options.unique) {
    return pythonRows.slice(0, options.limit);
  }

  return dedupeLatestByTitleSlug(pythonRows, options.limit);
}

function extractPythonFeatures(submissions: SubmissionRow[]): ExtractedFeatures[] {
  const payload = submissions.map((submission) => ({ content: submission.content }));
  const result = spawnSync('python3', ['-c', PYTHON_EXTRACTOR], {
    input: JSON.stringify(payload),
    encoding: 'utf8',
    maxBuffer: 10 * 1024 * 1024,
  });

  if (result.status !== 0) {
    throw new Error(result.stderr.trim() || 'python3 AST extractor failed');
  }

  return JSON.parse(result.stdout) as ExtractedFeatures[];
}

function formatClusterOutput(clustered: ClusteredSubmission[]) {
  const sorted = clusterSubmissions(clustered, 0.34);
  const lines = [`Scanned ${clustered.length} Python submissions`, ''];

  for (const items of sorted) {
    const first = items[0];
    lines.push(`${first.clusterKey} (${items.length})`);
    lines.push(`  fingerprint: ${JSON.stringify(first.fingerprint)}`);
    lines.push('  evidence:');
    for (const evidence of sharedEvidence(items, 8)) {
      lines.push(`    ${evidence.present}/${items.length} ${evidence.score.toFixed(1)} ${evidence.feature}`);
    }
    for (const sample of items.slice(0, 5)) {
      lines.push(`  - ${sample.submission.titleSlug ?? 'unknown'} :: ${sample.submission.id.slice(0, 8)} :: ${sample.submission.status}`);
    }
    lines.push('');
  }

  return lines.join('\n');
}

export function buildClusterArtifact(clustered: ClusteredSubmission[], options: CliOptions, generatedAt = new Date().toISOString()): ClusterArtifact {
  const clusters = clusterSubmissions(clustered, options.threshold)
    .map((items) => ({
      clusterKey: items[0].clusterKey,
      count: items.length,
      fingerprint: items[0].fingerprint,
      evidence: sharedEvidence(items),
      submissions: items.map((item) => ({
        id: item.submission.id,
        titleSlug: item.submission.titleSlug,
        status: item.submission.status,
        lang: item.lang,
        createdAt: item.submission.createdAt.toISOString(),
        features: item.features,
        featureBag: item.featureBag,
      })),
    }));

  return {
    generatedAt,
    options: {
      limit: options.limit,
      scan: options.scan,
      ...(options.slug ? { slug: options.slug } : {}),
      statuses: options.includeStatuses ?? ['Accepted'],
      unique: options.unique,
      threshold: options.threshold,
    },
    summary: {
      submissionCount: clustered.length,
      clusterCount: clusters.length,
    },
    clusters,
  };
}

function writeJsonArtifact(path: string, artifact: ClusterArtifact) {
  mkdirSync(dirname(path), { recursive: true });
  writeFileSync(path, `${JSON.stringify(artifact, null, 2)}\n`, 'utf8');
}

async function main() {
  loadRepoEnv();
  const options = parseArgs(process.argv.slice(2));
  const databaseUrl = resolveDatabaseUrl();
  const prisma = databaseUrl ? new PrismaClient({ datasources: { db: { url: databaseUrl } } }) : new PrismaClient();

  try {
    const submissions = await fetchCandidateSubmissions(prisma, options);
    const features = extractPythonFeatures(submissions);
    const clustered = submissions.map((submission, index) => {
      const extracted = features[index];
      const fingerprint = buildStructuredFingerprint(extracted);
      const featureBag = buildFeatureBag(extracted);
      return {
        submission,
        lang: languageOf(submission),
        features: extracted,
        fingerprint,
        featureBag,
        clusterKey: buildClusterKey(fingerprint),
      } satisfies ClusteredSubmission;
    });

    if (options.json) {
      console.log(JSON.stringify(clustered, null, 2));
      return;
    }

    if (options.out) {
      const artifact = buildClusterArtifact(clustered, options);
      const outPath = resolve(process.cwd(), options.out);
      writeJsonArtifact(outPath, artifact);
      console.log(`Wrote cluster artifact: ${outPath}`);
      return;
    }

    console.log(formatClusterOutput(clustered));
  } finally {
    await prisma.$disconnect();
  }
}

if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) {
  main().catch((error) => {
    console.error(error);
    process.exitCode = 1;
  });
}
