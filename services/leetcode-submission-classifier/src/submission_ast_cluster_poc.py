#!/usr/bin/env python3
from __future__ import annotations

import ast
import json
import logging
import math
from datetime import datetime, timezone
import os
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any
from uuid import uuid4
from urllib import error, request

from config import (
    ADVANCED_DS_CONFIDENCE_BOOST,
    ARTIFACTS_DIR,
    BASE_FINGERPRINT_CONFIDENCE,
    CLASS_API_BAG_SCORE,
    CLASS_API_TRANSITION_LABEL,
    CLUSTER_FAMILY_RULES,
    COUNTER_IMPORT_HINTS,
    COUNTER_INIT_BAG_SCORE,
    DEFAULT_ANSWER_TIMING_LABEL,
    DEFAULT_CLUSTER_ARTIFACT_NAME,
    DEFAULT_CLUSTER_FAMILY,
    DEFAULT_DATA_STRUCTURE_LABEL,
    DEFAULT_LABELED_CLUSTER_ARTIFACT_NAME,
    DEFAULT_TRANSITION_LABEL,
    DEFAULTDICT_INIT_BAG_SCORE,
    DEQUE_IMPORT_HINTS,
    DEQUE_INIT_BAG_SCORE,
    DICT_INIT_BAG_SCORE,
    DICT_LIKE_CALL_NAMES,
    DESIGN_CLASS_API_METHOD_NAMES,
    DIRECT_RECURSION_BAG_SCORE,
    DP_ANSWER_TIMING_LABEL,
    DP_STATE_NAMES,
    DP_TRANSITION_LABEL,
    EXPLICIT_STATE_INIT_BAG_SCORE,
    FEATURE_VALUE_CAP,
    FEATURE_WEIGHT_ASSIGN,
    FEATURE_WEIGHT_CALL,
    FEATURE_WEIGHT_CONTROL,
    FEATURE_WEIGHT_FALLBACK,
    FEATURE_WEIGHT_NESTED_LOOP,
    FEATURE_WEIGHT_SOURCE,
    FEATURE_WEIGHT_STRUCTURAL,
    FORMAT_EVIDENCE_TOP_K,
    GRAPH_STATE_BAG_SCORE,
    GRAPH_TRAVERSAL_CALL_NAMES,
    GRAPH_SIGNAL_TOKENS,
    GRID_SIGNAL_TOKENS,
    GRID_STATE_BAG_SCORE,
    HEAP_CALL_NAMES,
    HEAP_IMPORT_HINTS,
    IF_COUNT_FEATURE_CAP,
    ITERATIVE_TREE_BAG_SCORE,
    LEFT_RIGHT_POINTER_NAMES,
    LEFT_RIGHT_WHILE_BAG_SCORE,
    LEXICAL_FALLBACK_BAG_SCORE,
    MIDPOINT_ANSWER_TIMING_LABEL,
    MIDPOINT_BOUNDARY_MOTIF_BAG_SCORE,
    MIDPOINT_CONFIDENCE_BOOST,
    MIDPOINT_TRANSITION_LABEL,
    NEIGHBOR_STATE_NAMES,
    NESTED_COLLECTION_API_NAMES,
    NESTED_LOOP_BAG_SCORE,
    NESTED_LOOP_MIN_DEPTH,
    NESTED_LOOP_MIN_TOTAL_LOOPS,
    NEIGHBOR_SIGNAL_TOKENS,
    PREFIX_LOOKUP_MOTIF_BAG_SCORE,
    PREFIX_TRANSITION_LABEL,
    PRIORITY_QUEUE_BAG_SCORE,
    PREVIEW_CLUSTER_THRESHOLD,
    PREFIX_CONFIDENCE_BOOST,
    PYTHON_LANGUAGE_LIKE_PATTERN,
    QUEUE_GRAPH_CONFIDENCE_BOOST,
    QUEUE_ANSWER_TIMING_LABEL,
    QUEUE_MOTIF_BAG_SCORE,
    QUEUE_TRANSITION_LABEL,
    RECURSION_TRANSITION_LABEL,
    RECURSIVE_GRID_BAG_SCORE,
    RECURSIVE_NESTED_COLLECTION_BAG_SCORE,
    RECURSIVE_TREE_BAG_SCORE,
    SCAN_ANSWER_TIMING_LABEL,
    SET_INIT_BAG_SCORE,
    SHARED_EVIDENCE_MIN_COUNT,
    SHARED_EVIDENCE_MIN_FRACTION,
    SHARED_EVIDENCE_TOP_K,
    SLIDING_WINDOW_ANSWER_TIMING_LABEL,
    SLIDING_WINDOW_MOTIF_BAG_SCORE,
    SLIDING_WINDOW_TRANSITION_LABEL,
    SORT_CALL_NAMES,
    TREE_STATE_BAG_SCORE,
    TWO_POINTER_CONFIDENCE_BOOST,
    UNION_FIND_BAG_SCORE,
    UNION_FIND_CALL_NAMES,
    UNION_FIND_TRANSITION_LABEL,
    UNION_FIND_STATE_NAMES,
    WILSON_INTERVAL_Z,
)

from submission_ast_cluster_inputs import (
    CliOptions,
    SubmissionRow,
    fetch_candidate_submissions,
    language_of,
    load_repo_env,
    parse_args,
    setup_logging,
)

LOGGER = logging.getLogger("submission_ast_cluster_poc")


def has_word_signal(text: str, tokens: tuple[str, ...]) -> bool:
    return any(re.search(rf"\b{re.escape(token.lower())}\b", text) for token in tokens)


def apply_lexical_signals(base: dict[str, Any], code: str) -> None:
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
    base["hasTreeSignal"] = base["hasTreeSignal"] or ("treenode" in lowered or ((".left" in lowered or ".right" in lowered) and ".val" in lowered))
    base["hasGridSignal"] = base["hasGridSignal"] or has_word_signal(lowered, GRID_SIGNAL_TOKENS)
    base["hasGraphSignal"] = base["hasGraphSignal"] or has_word_signal(lowered, GRAPH_SIGNAL_TOKENS)
    base["hasNeighborSignal"] = base["hasNeighborSignal"] or has_word_signal(lowered, NEIGHBOR_SIGNAL_TOKENS)
    base["forCount"] = max(base["forCount"], sum(1 for line in lines if line.startswith("for ")))
    base["whileCount"] = max(base["whileCount"], sum(1 for line in lines if line.startswith("while ")))
    base["ifCount"] = max(base["ifCount"], sum(1 for line in lines if line.startswith("if ")))
    base["hasQueueLoopSignal"] = base["hasQueueLoopSignal"] or (base["hasPopleft"] and "while queue" in lowered)
    function_match = re.search(r"def\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\(", code)
    if function_match:
        function_name = function_match.group(1)
        base["hasRecursion"] = base["hasRecursion"] or code.count(f"{function_name}(") > 1


def extract_features_from_code(code: str) -> dict[str, Any]:
    base: dict[str, Any] = {
        "parseOk": True,
        "syntaxError": None,
        "imports": [],
        "calledFunctions": [],
        "assignedNames": [],
        "attributeNames": [],
        "classCount": 0,
        "functionCount": 0,
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
        "hasDesignApiSignal": False,
        "hasNonSolutionClass": False,
    }

    try:
        tree = ast.parse(code)
    except SyntaxError as exc:
        base["parseOk"] = False
        base["syntaxError"] = f"{exc.msg} at line {exc.lineno}"
        apply_lexical_signals(base, code)
        return base

    imports: set[str] = set()
    called: list[str] = []
    assigned: set[str] = set()
    attrs: set[str] = set()
    current_functions: list[str] = []

    class Visitor(ast.NodeVisitor):
        def __init__(self) -> None:
            self.loop_depth = 0
            self.class_depth = 0

        def visit_ClassDef(self, node: ast.ClassDef) -> None:
            base["classCount"] += 1
            if node.name != "Solution":
                base["hasNonSolutionClass"] = True
            self.class_depth += 1
            self.generic_visit(node)
            self.class_depth -= 1

        def visit_Import(self, node: ast.Import) -> None:
            for alias in node.names:
                imports.add(alias.name.split(".")[0])
            self.generic_visit(node)

        def visit_ImportFrom(self, node: ast.ImportFrom) -> None:
            if node.module:
                imports.add(node.module.split(".")[0])
            for alias in node.names:
                imports.add(alias.name.split(".")[0])
            self.generic_visit(node)

        def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
            base["functionCount"] += 1
            if self.class_depth > 0 and not current_functions and node.name.lower() in DESIGN_CLASS_API_METHOD_NAMES:
                base["hasDesignApiSignal"] = True
            current_functions.append(node.name)
            assigned.add(node.name)
            self.generic_visit(node)
            current_functions.pop()

        def visit_Assign(self, node: ast.Assign) -> None:
            for target in node.targets:
                self._record_target(target)
            self.generic_visit(node)

        def visit_AnnAssign(self, node: ast.AnnAssign) -> None:
            self._record_target(node.target)
            self.generic_visit(node)

        def _record_target(self, target: ast.AST) -> None:
            if isinstance(target, ast.Name):
                assigned.add(target.id)
            elif isinstance(target, (ast.Tuple, ast.List)):
                for element in target.elts:
                    self._record_target(element)

        def visit_For(self, node: ast.For) -> None:
            base["forCount"] += 1
            self.loop_depth += 1
            base["maxLoopDepth"] = max(base["maxLoopDepth"], self.loop_depth)
            self.generic_visit(node)
            self.loop_depth -= 1

        def visit_While(self, node: ast.While) -> None:
            base["whileCount"] += 1
            self.loop_depth += 1
            base["maxLoopDepth"] = max(base["maxLoopDepth"], self.loop_depth)
            self.generic_visit(node)
            self.loop_depth -= 1

        def visit_If(self, node: ast.If) -> None:
            base["ifCount"] += 1
            self.generic_visit(node)

        def visit_ListComp(self, node: ast.ListComp) -> None:
            base["comprehensionCount"] += 1
            self.generic_visit(node)

        visit_SetComp = visit_ListComp
        visit_DictComp = visit_ListComp
        visit_GeneratorExp = visit_ListComp

        def visit_Name(self, node: ast.Name) -> None:
            lowered = node.id.lower()
            if lowered == "visited":
                base["hasVisited"] = True
            if lowered in LEFT_RIGHT_POINTER_NAMES:
                base["hasLeftRightPointers"] = True
            if lowered == "mid":
                base["hasMid"] = True
            if lowered.startswith("prefix"):
                base["hasPrefixSignal"] = True
            if lowered in DP_STATE_NAMES or lowered.startswith("dp"):
                base["hasDpSignal"] = True
            if lowered in UNION_FIND_STATE_NAMES:
                base["hasUnionFindSignal"] = True
            if lowered in GRID_SIGNAL_TOKENS:
                base["hasGridSignal"] = True
            if lowered in GRAPH_SIGNAL_TOKENS:
                base["hasGraphSignal"] = True
            if lowered in NEIGHBOR_STATE_NAMES:
                base["hasNeighborSignal"] = True
            self.generic_visit(node)

        def visit_Call(self, node: ast.Call) -> None:
            func_name: str | None = None
            is_direct_call = False

            if isinstance(node.func, ast.Name):
                func_name = node.func.id
                is_direct_call = True
            elif isinstance(node.func, ast.Attribute):
                func_name = node.func.attr
                attrs.add(node.func.attr)

            if func_name:
                called.append(func_name)
                lowered = func_name.lower()
                if lowered == "set":
                    base["hasSet"] = True
                if lowered in DICT_LIKE_CALL_NAMES:
                    base["hasDict"] = True
                if lowered == "defaultdict":
                    base["hasDefaultdict"] = True
                if lowered == "deque":
                    base["hasDeque"] = True
                if lowered == "counter":
                    base["hasCounter"] = True
                if lowered in HEAP_CALL_NAMES:
                    base["hasHeapq"] = True
                if lowered in SORT_CALL_NAMES:
                    base["hasSortedOrSort"] = True
                if lowered == "popleft":
                    base["hasPopleft"] = True
                if lowered == "appendleft":
                    base["hasAppendleft"] = True
                if is_direct_call and current_functions and lowered == current_functions[-1]:
                    base["hasRecursion"] = True
                if is_direct_call and lowered in UNION_FIND_CALL_NAMES:
                    base["hasUnionFindSignal"] = True
                if lowered in GRAPH_TRAVERSAL_CALL_NAMES:
                    base["hasGraphSignal"] = True
            self.generic_visit(node)

        def visit_Attribute(self, node: ast.Attribute) -> None:
            attrs.add(node.attr)
            lowered = node.attr.lower()
            if lowered == "popleft":
                base["hasPopleft"] = True
            if lowered == "appendleft":
                base["hasAppendleft"] = True
            if lowered in HEAP_CALL_NAMES:
                base["hasHeapq"] = True
            if lowered == "sort":
                base["hasSortedOrSort"] = True
            self.generic_visit(node)

    Visitor().visit(tree)

    base["imports"] = sorted(imports)
    base["calledFunctions"] = called
    base["assignedNames"] = sorted(assigned)
    base["attributeNames"] = sorted(attrs)
    base["hasDeque"] = base["hasDeque"] or any(name in imports for name in DEQUE_IMPORT_HINTS)
    base["hasCounter"] = base["hasCounter"] or any(name in imports for name in COUNTER_IMPORT_HINTS)
    base["hasHeapq"] = base["hasHeapq"] or any(name in imports for name in HEAP_IMPORT_HINTS)
    base["hasTreeSignal"] = base["hasTreeSignal"] or (("left" in attrs or "right" in attrs) and ("val" in attrs or "treenode" in code.lower()))
    base["hasQueueLoopSignal"] = base["hasPopleft"] and base["whileCount"] > 0
    apply_lexical_signals(base, code)
    return base


def build_structured_fingerprint(features: dict[str, Any]) -> dict[str, Any]:
    loops: set[str] = set()
    data_structures: set[str] = set()
    ops: set[str] = set()
    state_vars: set[str] = set()
    transition_order: set[str] = set()

    if features["forCount"] > 0:
        loops.add("for")
    if features["whileCount"] > 0:
        loops.add("while")
    if features["maxLoopDepth"] >= NESTED_LOOP_MIN_DEPTH or features["forCount"] + features["whileCount"] >= NESTED_LOOP_MIN_TOTAL_LOOPS:
        loops.add("nested_loop")

    if features["hasDict"] or features["hasDefaultdict"]:
        data_structures.add("dict")
    if features["hasSet"] or features["hasVisited"]:
        data_structures.add("set")
    if features["hasCounter"]:
        data_structures.add("counter")
    if features["hasDeque"] or features["hasPopleft"] or features["hasAppendleft"]:
        data_structures.add("deque")
    if features["hasHeapq"]:
        data_structures.add("heap")
    if features["hasTreeSignal"]:
        data_structures.add("tree_shape")
    if features["hasGridSignal"]:
        data_structures.add("grid")
    if features["hasGraphSignal"] or features["hasNeighborSignal"]:
        data_structures.add("graph_state")
    if features["hasUnionFindSignal"]:
        data_structures.add("parent_array")
    has_design_api = features["hasNonSolutionClass"] and features["hasDesignApiSignal"] and features["functionCount"] >= 2

    if has_design_api:
        data_structures.add("class_api")
    if not data_structures:
        data_structures.add(DEFAULT_DATA_STRUCTURE_LABEL)

    if features["hasPopleft"]:
        ops.add("popleft")
    if features["hasAppendleft"]:
        ops.add("appendleft")
    if features["hasDeque"]:
        ops.add("append")
    if features["hasCounter"]:
        ops.add("increment_count")
    if features["hasDefaultdict"] or features["hasDict"]:
        ops.add("lookup_update")
    if features["hasSet"] or features["hasVisited"]:
        ops.add("membership_check")
    if features["hasHeapq"]:
        ops.add("priority_pop_push")
    if features["hasSortedOrSort"]:
        ops.add("sort")
    if features["hasMid"]:
        ops.add("mid_compute")
    if "max" in features["calledFunctions"]:
        ops.add("max_update")
    if "min" in features["calledFunctions"]:
        ops.add("min_update")

    if features["hasLeftRightPointers"]:
        state_vars.update({"left", "right"})
    if features["hasVisited"]:
        state_vars.add("visited")
    if features["hasMid"]:
        state_vars.add("mid")
    if features["hasPrefixSignal"]:
        state_vars.add("prefix")
    if features["hasDpSignal"]:
        state_vars.add("dp")
    if features["hasUnionFindSignal"]:
        state_vars.update({"parent", "rank"})
    if has_design_api:
        state_vars.add("object_state")
    if features["hasTreeSignal"]:
        state_vars.add("node_children")
    if features["hasGridSignal"]:
        state_vars.add("grid_coords")

    if features["hasQueueLoopSignal"]:
        transition_order.add(QUEUE_TRANSITION_LABEL)
    if features["hasRecursion"]:
        transition_order.add(RECURSION_TRANSITION_LABEL)
    if features["hasMid"] and features["whileCount"] > 0:
        transition_order.add(MIDPOINT_TRANSITION_LABEL)
    if features["hasLeftRightPointers"] and features["whileCount"] > 0 and (features["hasCounter"] or features["hasDict"] or features["hasSet"]):
        transition_order.add(SLIDING_WINDOW_TRANSITION_LABEL)
    if features["hasPrefixSignal"] and (features["hasDict"] or features["hasCounter"]):
        transition_order.add(PREFIX_TRANSITION_LABEL)
    if features["hasDpSignal"]:
        transition_order.add(DP_TRANSITION_LABEL)
    if features["hasUnionFindSignal"]:
        transition_order.add(UNION_FIND_TRANSITION_LABEL)
    if has_design_api:
        transition_order.add(CLASS_API_TRANSITION_LABEL)
    if not transition_order:
        transition_order.add(DEFAULT_TRANSITION_LABEL)

    answer_update_timing = DEFAULT_ANSWER_TIMING_LABEL
    if features["hasQueueLoopSignal"]:
        answer_update_timing = QUEUE_ANSWER_TIMING_LABEL
    elif features["hasLeftRightPointers"] and features["whileCount"] > 0 and (features["hasCounter"] or features["hasDict"] or features["hasSet"]):
        answer_update_timing = SLIDING_WINDOW_ANSWER_TIMING_LABEL
    elif features["hasMid"] and features["whileCount"] > 0:
        answer_update_timing = MIDPOINT_ANSWER_TIMING_LABEL
    elif features["hasDpSignal"]:
        answer_update_timing = DP_ANSWER_TIMING_LABEL
    elif features["forCount"] > 0 or features["whileCount"] > 0:
        answer_update_timing = SCAN_ANSWER_TIMING_LABEL

    confidence = BASE_FINGERPRINT_CONFIDENCE
    if features["hasQueueLoopSignal"] and (features["hasVisited"] or features["hasGridSignal"] or features["hasGraphSignal"]):
        confidence += QUEUE_GRAPH_CONFIDENCE_BOOST
    if features["hasMid"] and features["whileCount"] > 0:
        confidence += MIDPOINT_CONFIDENCE_BOOST
    if features["hasLeftRightPointers"] and features["whileCount"] > 0:
        confidence += TWO_POINTER_CONFIDENCE_BOOST
    if features["hasPrefixSignal"] and (features["hasDict"] or features["hasCounter"]):
        confidence += PREFIX_CONFIDENCE_BOOST
    if features["hasDpSignal"] or features["hasUnionFindSignal"] or features["hasHeapq"]:
        confidence += ADVANCED_DS_CONFIDENCE_BOOST

    return {
        "loops": sorted(loops),
        "recursion": features["hasRecursion"],
        "dataStructures": sorted(data_structures),
        "ops": sorted(ops),
        "stateVars": sorted(state_vars),
        "transitionOrder": sorted(transition_order),
        "answerUpdateTiming": answer_update_timing,
        "confidence": min(1, round(confidence, 2)),
    }


def build_cluster_key(fingerprint: dict[str, Any]) -> str:
    return "__".join([
        f"loops={'+'.join(fingerprint['loops']) or 'none'}",
        f"rec={'y' if fingerprint['recursion'] else 'n'}",
        f"ds={'+'.join(fingerprint['dataStructures']) or 'none'}",
        f"ops={'+'.join(fingerprint['ops']) or 'none'}",
        f"state={'+'.join(fingerprint['stateVars']) or 'none'}",
        f"transition={'+'.join(fingerprint['transitionOrder']) or 'none'}",
        f"answer={fingerprint['answerUpdateTiming']}",
    ])


def add_feature(bag: dict[str, float], key: str, value: float = 1) -> None:
    bag[key] = bag.get(key, 0) + value


def build_feature_bag(features: dict[str, Any]) -> dict[str, float]:
    bag: dict[str, float] = {}

    if features["forCount"] > 0:
        add_feature(bag, "ctrl:for", features["forCount"])
    if features["whileCount"] > 0:
        add_feature(bag, "ctrl:while", features["whileCount"])
    if features["ifCount"] > 0:
        add_feature(bag, "ctrl:if", min(features["ifCount"], IF_COUNT_FEATURE_CAP))
    if features["maxLoopDepth"] > 1 or features["forCount"] + features["whileCount"] >= 2:
        add_feature(bag, "motif:nested_loop", NESTED_LOOP_BAG_SCORE)
    if features["hasRecursion"]:
        add_feature(bag, "control_fact:direct_recursion", DIRECT_RECURSION_BAG_SCORE)

    if features["hasDeque"]:
        add_feature(bag, "var_op:init:Call:deque", DEQUE_INIT_BAG_SCORE)
    if features["hasCounter"]:
        add_feature(bag, "var_op:init:Call:Counter", COUNTER_INIT_BAG_SCORE)
    if features["hasDefaultdict"]:
        add_feature(bag, "var_op:init:Call:defaultdict", DEFAULTDICT_INIT_BAG_SCORE)
    if features["hasDict"]:
        add_feature(bag, "var_op:init:Dict", DICT_INIT_BAG_SCORE)
    if features["hasSet"] or features["hasVisited"]:
        add_feature(bag, "var_op:init:Set", SET_INIT_BAG_SCORE)
    if features["hasHeapq"]:
        add_feature(bag, "role:priority_queue_ops", PRIORITY_QUEUE_BAG_SCORE)
    if features["hasGridSignal"]:
        add_feature(bag, "role:indexed_grid_state", GRID_STATE_BAG_SCORE)
    if features["hasTreeSignal"]:
        add_feature(bag, "role:node_child_state", TREE_STATE_BAG_SCORE)
    if features["hasGraphSignal"] or features["hasNeighborSignal"]:
        add_feature(bag, "role:graph_state_expansion", GRAPH_STATE_BAG_SCORE)

    if features["hasPopleft"]:
        add_feature(bag, "method:popleft")
    if features["hasAppendleft"]:
        add_feature(bag, "method:appendleft")
    if features["hasDeque"]:
        add_feature(bag, "method:append")
    if features["hasSet"] or features["hasVisited"]:
        add_feature(bag, "method:add")
    if features["hasDict"] or features["hasDefaultdict"]:
        add_feature(bag, "method:get")
    if features["hasSortedOrSort"]:
        add_feature(bag, "call:sorted_or_sort")
    if features["hasMid"]:
        add_feature(bag, "assign:midpoint")
    if features["hasPrefixSignal"]:
        add_feature(bag, "role:prefix_state")
    if features["hasDpSignal"]:
        add_feature(bag, "role:dp_state")
    if features["hasUnionFindSignal"]:
        add_feature(bag, "role:union_find_state", UNION_FIND_BAG_SCORE)
    has_design_api = features["hasNonSolutionClass"] and features["hasDesignApiSignal"] and features["functionCount"] >= 2
    if has_design_api:
        add_feature(bag, "role:class_api_design", CLASS_API_BAG_SCORE)
    if features["hasTreeSignal"] and features["hasRecursion"]:
        add_feature(bag, "role:recursive_tree_descent", RECURSIVE_TREE_BAG_SCORE)
    if features["hasGridSignal"] and features["hasRecursion"]:
        add_feature(bag, "role:recursive_grid_dfs", RECURSIVE_GRID_BAG_SCORE)
    if features["hasRecursion"] and not features["hasTreeSignal"] and not features["hasGridSignal"] and any(name in NESTED_COLLECTION_API_NAMES for name in features["attributeNames"]):
        add_feature(bag, "role:recursive_nested_collection", RECURSIVE_NESTED_COLLECTION_BAG_SCORE)
    if features["hasTreeSignal"] and features["whileCount"] > 0 and not features["hasRecursion"]:
        add_feature(bag, "role:iterative_tree_walk", ITERATIVE_TREE_BAG_SCORE)

    if features["hasQueueLoopSignal"]:
        add_feature(bag, "motif:frontier_pop_then_expand", QUEUE_MOTIF_BAG_SCORE)
    if features["hasLeftRightPointers"] and features["whileCount"] > 0:
        add_feature(bag, "motif:left_right_while", LEFT_RIGHT_WHILE_BAG_SCORE)
    if features["hasLeftRightPointers"] and features["whileCount"] > 0 and (features["hasCounter"] or features["hasDict"] or features["hasSet"]):
        add_feature(bag, "motif:expand_then_shrink_window", SLIDING_WINDOW_MOTIF_BAG_SCORE)
    if features["hasPrefixSignal"] and (features["hasDict"] or features["hasCounter"]):
        add_feature(bag, "motif:accumulate_then_lookup", PREFIX_LOOKUP_MOTIF_BAG_SCORE)
    if features["hasMid"] and features["whileCount"] > 0:
        add_feature(bag, "motif:midpoint_boundary_narrow", MIDPOINT_BOUNDARY_MOTIF_BAG_SCORE)

    if not features["parseOk"]:
        add_feature(bag, "source:lexical_fallback", LEXICAL_FALLBACK_BAG_SCORE)
    if any(key.startswith("var_op:init:") for key in bag):
        add_feature(bag, "role:explicit_state_init", EXPLICIT_STATE_INIT_BAG_SCORE)
    return bag


def cluster_family(bag: dict[str, float]) -> str:
    for family, keys in CLUSTER_FAMILY_RULES:
        if any(bag.get(key) for key in keys):
            return family
    return DEFAULT_CLUSTER_FAMILY


def feature_weight(key: str) -> float:
    if key == "motif:nested_loop":
        return FEATURE_WEIGHT_NESTED_LOOP
    if key.startswith(("motif:", "role:", "control_fact:")):
        return FEATURE_WEIGHT_STRUCTURAL
    if key.startswith(("method:", "call:")):
        return FEATURE_WEIGHT_CALL
    if key.startswith(("assign:", "var_op:")):
        return FEATURE_WEIGHT_ASSIGN
    if key.startswith("ctrl:"):
        return FEATURE_WEIGHT_CONTROL
    if key.startswith("source:"):
        return FEATURE_WEIGHT_SOURCE
    return FEATURE_WEIGHT_FALLBACK


def vectorize(bag: dict[str, float]) -> dict[str, float]:
    return {
        key: min(value, FEATURE_VALUE_CAP) * feature_weight(key)
        for key, value in bag.items()
        if min(value, FEATURE_VALUE_CAP) * feature_weight(key) > 0
    }


def is_structural_signal(key: str) -> bool:
    if key in {"motif:nested_loop", "role:explicit_state_init"}:
        return False
    return bool(re.match(r"^(motif|role|method|call|assign|var_op|control_fact):", key))


def structural_similarity(left: dict[str, float], right: dict[str, float]) -> float:
    left_vector = vectorize(left)
    right_vector = vectorize(right)
    keys = set(left_vector) | set(right_vector)
    if not keys:
        return 0.0

    has_shared_structural_signal = any(is_structural_signal(key) and key in left_vector and key in right_vector for key in keys)
    if not has_shared_structural_signal:
        return 0.0

    numerator = sum(min(left_vector.get(key, 0.0), right_vector.get(key, 0.0)) for key in keys)
    denominator = sum(max(left_vector.get(key, 0.0), right_vector.get(key, 0.0)) for key in keys)
    return 0.0 if denominator == 0 else numerator / denominator


class Dsu:
    def __init__(self, size: int) -> None:
        self.parent = list(range(size))

    def find(self, index: int) -> int:
        while self.parent[index] != index:
            self.parent[index] = self.parent[self.parent[index]]
            index = self.parent[index]
        return index

    def union(self, left: int, right: int) -> None:
        left_root = self.find(left)
        right_root = self.find(right)
        if left_root != right_root:
            self.parent[right_root] = left_root


def can_cluster_together(left: dict[str, Any], right: dict[str, Any]) -> bool:
    return cluster_family(left["featureBag"]) == cluster_family(right["featureBag"])


def cluster_submissions(clustered: list[dict[str, Any]], threshold: float) -> list[list[dict[str, Any]]]:
    LOGGER.info("clustering submissions count=%d threshold=%.3f", len(clustered), threshold)
    dsu = Dsu(len(clustered))
    merge_count = 0
    for left in range(len(clustered)):
        for right in range(left + 1, len(clustered)):
            similarity = structural_similarity(clustered[left]["featureBag"], clustered[right]["featureBag"])
            if similarity >= threshold and can_cluster_together(clustered[left], clustered[right]):
                dsu.union(left, right)
                merge_count += 1

    groups: dict[int, list[dict[str, Any]]] = defaultdict(list)
    for index, item in enumerate(clustered):
        groups[dsu.find(index)].append(item)

    grouped = sorted(groups.values(), key=lambda items: (-len(items), str(items[0]["submission"]["titleSlug"])))
    for items in grouped:
        canonical_key = items[0]["fingerprintKey"]
        for item in items:
            item["assignedClusterKey"] = canonical_key
    LOGGER.info("clustered submissions clusters=%d merges=%d", len(grouped), merge_count)
    return grouped


def shared_evidence(items: list[dict[str, Any]], top: int = SHARED_EVIDENCE_TOP_K) -> list[dict[str, Any]]:
    presence: dict[str, int] = defaultdict(int)
    strength: dict[str, float] = defaultdict(float)
    minimum_presence = 1 if len(items) == 1 else max(SHARED_EVIDENCE_MIN_COUNT, math.ceil(len(items) * SHARED_EVIDENCE_MIN_FRACTION))

    for item in items:
        for key, value in item["featureBag"].items():
            presence[key] += 1
            strength[key] += min(value, FEATURE_VALUE_CAP) * feature_weight(key)

    rows = [
        {
            "feature": key,
            "present": presence[key],
            "score": round(strength[key], 2),
        }
        for key in presence
        if presence[key] >= minimum_presence and strength[key] > 0
    ]
    rows.sort(key=lambda row: (-row["present"], -row["score"], row["feature"]))
    return rows[:top]


def base_artifact_metadata(options: CliOptions, generated_at: str, run_id: str) -> dict[str, Any]:
    return {
        "runId": run_id,
        "generatedAt": generated_at,
        "options": {
            "limit": options.limit,
            "scan": options.scan,
            **({"slug": options.slug} if options.slug else {}),
            "source": options.source,
            **({"corpusDir": str(options.corpus_dir)} if options.source == "corpus" and options.corpus_dir else {}),
            "statuses": options.include_statuses or ["Accepted"],
            "unique": options.unique,
            "threshold": options.threshold,
        },
    }


def problem_slug_count(items: list[dict[str, Any]]) -> int:
    return len({item["submission"]["titleSlug"] for item in items if item["submission"]["titleSlug"]})


def wilson_interval(successes: int, total: int, z: float = WILSON_INTERVAL_Z) -> dict[str, float]:
    if total <= 0:
        return {"low": 0.0, "high": 0.0, "level": 0.95}

    p_hat = successes / total
    z2 = z * z
    denom = 1 + z2 / total
    center = (p_hat + z2 / (2 * total)) / denom
    margin = (z / denom) * math.sqrt((p_hat * (1 - p_hat) / total) + (z2 / (4 * total * total)))
    return {
        "low": round(max(0.0, center - margin), 4),
        "high": round(min(1.0, center + margin), 4),
        "level": 0.95,
    }


def build_cluster_records(clustered: list[dict[str, Any]], threshold: float) -> list[dict[str, Any]]:
    clusters = []
    for items in cluster_submissions(clustered, threshold):
        clusters.append({
            "clusterKey": items[0]["assignedClusterKey"],
            "count": len(items),
            "submissionCount": len(items),
            "problemCount": problem_slug_count(items),
            "fingerprint": items[0]["fingerprint"],
            "evidence": shared_evidence(items),
            "submissions": [
                {
                    "id": item["submission"]["id"],
                    "titleSlug": item["submission"]["titleSlug"],
                    "status": item["submission"]["status"],
                    "lang": item["lang"],
                    "createdAt": item["submission"]["createdAt"],
                    "fingerprintKey": item["fingerprintKey"],
                    "assignedClusterKey": item["assignedClusterKey"],
                    "features": item["features"],
                    "featureBag": item["featureBag"],
                }
                for item in items
            ],
        })
    return clusters


def build_cluster_artifact(clustered: list[dict[str, Any]], options: CliOptions, generated_at: str, run_id: str) -> dict[str, Any]:
    clusters = build_cluster_records(clustered, options.threshold)
    problem_count = len({item["submission"]["titleSlug"] for item in clustered if item["submission"]["titleSlug"]})
    LOGGER.info(
        "built cluster artifact runId=%s submissions=%d problems=%d clusters=%d",
        run_id,
        len(clustered),
        problem_count,
        len(clusters),
    )
    return {
        **base_artifact_metadata(options, generated_at, run_id),
        "summary": {
            "submissionCount": len(clustered),
            "problemCount": problem_count,
            "clusterCount": len(clusters),
        },
        "clusters": clusters,
    }


def normalize_cluster_label(value: Any, fallback_key: str) -> dict[str, Any]:
    parsed = value if isinstance(value, dict) else {}
    label = parsed.get("label") if isinstance(parsed.get("label"), str) and parsed.get("label").strip() else fallback_key
    raw_key = parsed.get("key") if isinstance(parsed.get("key"), str) and parsed.get("key").strip() else label
    key = re.sub(r"(^_+|_+$)", "", re.sub(r"[^a-z0-9]+", "_", raw_key.lower()))
    description = parsed.get("description") if isinstance(parsed.get("description"), str) and parsed.get("description").strip() else "Heuristic structure cluster label."
    raw_confidence = parsed.get("confidence")
    confidence = raw_confidence if isinstance(raw_confidence, (int, float)) else 0.5
    raw_should_split = parsed.get("should_split_by")
    should_split_by = [entry for entry in raw_should_split[:5] if isinstance(entry, str)] if isinstance(raw_should_split, list) else []
    return {
        "label": label[:80],
        "key": (key or fallback_key)[:80],
        "description": description[:240],
        "confidence": max(0, min(1, confidence)),
        "mixedCluster": parsed.get("mixed_cluster") is True,
        "shouldSplitBy": should_split_by,
    }


def label_cluster_with_openrouter(cluster: dict[str, Any], model: str) -> dict[str, Any]:
    api_key = os.environ.get("OPEN_ROUTER_API_KEY")
    if not api_key:
        raise RuntimeError("OPEN_ROUTER_API_KEY is required for --label")

    sample_problems = [submission["titleSlug"] or "unknown" for submission in cluster["submissions"][:8]]
    payload = {
        "model": model,
        "temperature": 0,
        "response_format": {"type": "json_object"},
        "messages": [
            {
                "role": "system",
                "content": "\n".join([
                    "You label LeetCode solution-structure clusters.",
                    'Return JSON only: {"label":"short human label","key":"snake_case_key","description":"one sentence","confidence":0.0,"mixed_cluster":false,"should_split_by":[]}.',
                    "Use classic algorithm taxonomy names when possible.",
                    "If samples/evidence mix unrelated solution families, set mixed_cluster true and fill should_split_by.",
                    "Do not invent problem facts beyond the given fingerprint/evidence/samples.",
                ]),
            },
            {
                "role": "user",
                "content": json.dumps({
                    "clusterKey": cluster["clusterKey"],
                    "count": cluster["submissionCount"],
                    "fingerprint": cluster["fingerprint"],
                    "evidence": cluster["evidence"][:12],
                    "sampleProblems": sample_problems,
                }),
            },
        ],
    }
    req = request.Request(
        "https://openrouter.ai/api/v1/chat/completions",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://github.com/jingyi-zhao-01/leetcode-intelligence",
            "X-Title": "leetcode-submission-classifier",
        },
        method="POST",
    )

    try:
        with request.urlopen(req) as response:
            raw = json.loads(response.read().decode("utf-8"))
    except error.HTTPError as exc:
        raise RuntimeError(f"OpenRouter label request failed: {exc.code} {exc.read().decode('utf-8', errors='ignore')}") from exc

    content = (((raw.get("choices") or [{}])[0].get("message") or {}).get("content")) or "{}"
    try:
        return normalize_cluster_label(json.loads(content), cluster["clusterKey"])
    except json.JSONDecodeError:
        return normalize_cluster_label(None, cluster["clusterKey"])


def build_maybe_labeled_cluster_artifact(clustered: list[dict[str, Any]], options: CliOptions, generated_at: str, run_id: str) -> dict[str, Any]:
    artifact = build_cluster_artifact(clustered, options, generated_at, run_id)
    if not options.label:
        return artifact
    LOGGER.info("labeling clusters model=%s clusterCount=%d", options.label_model, len(artifact["clusters"]))
    labeled_clusters = []
    for index, cluster in enumerate(artifact["clusters"], start=1):
        LOGGER.info(
            "labeling cluster index=%d/%d submissions=%d problems=%d key=%s",
            index,
            len(artifact["clusters"]),
            cluster["submissionCount"],
            cluster["problemCount"],
            cluster["clusterKey"],
        )
        label = label_cluster_with_openrouter(cluster, options.label_model)
        LOGGER.info("labeled cluster index=%d/%d label=%s confidence=%.2f", index, len(artifact["clusters"]), label["key"], label["confidence"])
        labeled_clusters.append({
            **cluster,
            "llmLabel": label,
        })
    artifact["clusters"] = labeled_clusters
    return artifact


def cluster_label_lookup(cluster_artifact: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {
        cluster["clusterKey"]: cluster["llmLabel"]
        for cluster in cluster_artifact["clusters"]
        if cluster.get("llmLabel")
    }


def build_problem_artifact(
    clustered: list[dict[str, Any]],
    cluster_artifact: dict[str, Any],
    options: CliOptions,
    generated_at: str,
    run_id: str,
    log_summary: bool = True,
) -> dict[str, Any]:
    label_by_cluster = cluster_label_lookup(cluster_artifact)
    by_problem: dict[str, list[dict[str, Any]]] = defaultdict(list)

    for item in clustered:
        title_slug = item["submission"]["titleSlug"]
        if title_slug:
            by_problem[title_slug].append(item)

    problems = []
    for title_slug, items in sorted(by_problem.items()):
        total = len(items)
        cluster_counts: dict[str, int] = defaultdict(int)
        for item in items:
            cluster_counts[item["assignedClusterKey"]] += 1

        memberships = []
        for cluster_key, count in sorted(cluster_counts.items(), key=lambda entry: (-entry[1], entry[0])):
            membership = {
                "clusterKey": cluster_key,
                "submissionCount": count,
                "share": round(count / total, 4),
                "confidenceInterval": wilson_interval(count, total),
            }
            if cluster_key in label_by_cluster:
                membership["llmLabel"] = label_by_cluster[cluster_key]
            memberships.append(membership)

        problems.append({
            "titleSlug": title_slug,
            "submissionCount": total,
            "clusterCount": len(memberships),
            "primaryClusterKey": memberships[0]["clusterKey"],
            "clusterMemberships": memberships,
            "multiSolution": len(memberships) > 1,
        })

    if log_summary:
        LOGGER.info(
            "built problem artifact runId=%s problems=%d multiSolutionProblems=%d",
            run_id,
            len(problems),
            sum(1 for problem in problems if problem["multiSolution"]),
        )
    return {
        **base_artifact_metadata(options, generated_at, run_id),
        "summary": {
            "problemCount": len(problems),
            "submissionCount": len(clustered),
            "multiSolutionProblemCount": sum(1 for problem in problems if problem["multiSolution"]),
        },
        "problems": problems,
    }


def build_submission_artifact(clustered: list[dict[str, Any]], cluster_artifact: dict[str, Any], options: CliOptions, generated_at: str, run_id: str) -> dict[str, Any]:
    label_by_cluster = cluster_label_lookup(cluster_artifact)
    problem_membership_by_slug: dict[str, dict[str, Any]] = {}
    for problem in build_problem_artifact(clustered, cluster_artifact, options, generated_at, run_id, log_summary=False)["problems"]:
        problem_membership_by_slug[problem["titleSlug"]] = {
            membership["clusterKey"]: membership
            for membership in problem["clusterMemberships"]
        }

    submissions = []
    for item in clustered:
        title_slug = item["submission"]["titleSlug"]
        cluster_key = item["assignedClusterKey"]
        entry = {
            "id": item["submission"]["id"],
            "titleSlug": title_slug,
            "status": item["submission"]["status"],
            "lang": item["lang"],
            "createdAt": item["submission"]["createdAt"],
            "fingerprintKey": item["fingerprintKey"],
            "assignedClusterKey": cluster_key,
            "fingerprint": item["fingerprint"],
            "features": item["features"],
        }
        if cluster_key in label_by_cluster:
            entry["llmLabel"] = label_by_cluster[cluster_key]
        if title_slug and title_slug in problem_membership_by_slug and cluster_key in problem_membership_by_slug[title_slug]:
            entry["problemClusterMembership"] = problem_membership_by_slug[title_slug][cluster_key]
        submissions.append(entry)

    with_membership = sum(1 for submission in submissions if submission.get("problemClusterMembership"))
    with_label = sum(1 for submission in submissions if submission.get("llmLabel"))
    LOGGER.info(
        "built submission artifact runId=%s submissions=%d withProblemMembership=%d withLlmLabel=%d",
        run_id,
        len(submissions),
        with_membership,
        with_label,
    )
    return {
        **base_artifact_metadata(options, generated_at, run_id),
        "summary": {
            "submissionCount": len(submissions),
            "problemCount": len({item["submission"]["titleSlug"] for item in clustered if item["submission"]["titleSlug"]}),
        },
        "submissions": submissions,
    }


def format_cluster_output(clustered: list[dict[str, Any]]) -> str:
    lines = [f"Scanned {len(clustered)} Python submissions", ""]
    for items in cluster_submissions(clustered, PREVIEW_CLUSTER_THRESHOLD):
        first = items[0]
        lines.append(f"{first['clusterKey']} ({len(items)})")
        lines.append(f"  fingerprint: {json.dumps(first['fingerprint'], ensure_ascii=False)}")
        lines.append("  evidence:")
        for evidence in shared_evidence(items, FORMAT_EVIDENCE_TOP_K):
            lines.append(f"    {evidence['present']}/{len(items)} {evidence['score']:.1f} {evidence['feature']}")
        for sample in items[:5]:
            lines.append(f"  - {sample['submission']['titleSlug'] or 'unknown'} :: {sample['submission']['id'][:8]} :: {sample['submission']['status']}")
        lines.append("")
    return "\n".join(lines)


def format_artifact_output(artifact: dict[str, Any]) -> str:
    lines = [f"Scanned {artifact['summary']['submissionCount']} Python submissions", ""]
    for cluster in artifact["clusters"]:
        label = f" :: {cluster['llmLabel']['label']}" if cluster.get("llmLabel") else ""
        lines.append(f"{cluster['clusterKey']}{label} ({cluster['submissionCount']} submissions, {cluster['problemCount']} problems)")
        if cluster.get("llmLabel"):
            llm_label = cluster["llmLabel"]
            lines.append(f"  label: {llm_label['key']} ({llm_label['confidence']:.2f})")
            if llm_label["mixedCluster"]:
                lines.append(f"  mixed: {', '.join(llm_label['shouldSplitBy']) or 'true'}")
            lines.append(f"  {llm_label['description']}")
        lines.append(f"  fingerprint: {json.dumps(cluster['fingerprint'], ensure_ascii=False)}")
        lines.append("  evidence:")
        for evidence in cluster["evidence"][:FORMAT_EVIDENCE_TOP_K]:
            lines.append(f"    {evidence['present']}/{cluster['submissionCount']} {evidence['score']:.1f} {evidence['feature']}")
        for sample in cluster["submissions"][:5]:
            lines.append(f"  - {sample['titleSlug'] or 'unknown'} :: {sample['id'][:8]} :: {sample['status']}")
        lines.append("")
    return "\n".join(lines)


def write_json_artifact(path: str, artifact: dict[str, Any]) -> None:
    out_path = Path(path).resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(artifact, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    LOGGER.info("wrote artifact path=%s bytes=%d", out_path, out_path.stat().st_size)


def derive_artifact_paths(out_path: str) -> dict[str, Path]:
    cluster_path = Path(out_path).resolve()
    suffix = cluster_path.suffix if cluster_path.suffix else ".json"
    stem = cluster_path.name[:-len(suffix)] if cluster_path.suffix else cluster_path.name
    return {
        "clusters": cluster_path,
        "problems": cluster_path.with_name(f"{stem}.problems{suffix}"),
        "submissions": cluster_path.with_name(f"{stem}.submissions{suffix}"),
    }


def create_run_id(generated_at: str) -> str:
    compact = generated_at.replace("-", "").replace(":", "").replace(".", "").replace("Z", "Z")
    compact = compact.replace("+", "").replace("T", "T")
    return f"{compact}-{uuid4().hex[:8]}"


def default_artifact_path(options: CliOptions, run_id: str) -> Path:
    filename = DEFAULT_LABELED_CLUSTER_ARTIFACT_NAME if options.label else DEFAULT_CLUSTER_ARTIFACT_NAME
    return ARTIFACTS_DIR / run_id / filename


def build_clustered_submissions(submissions: list[SubmissionRow]) -> list[dict[str, Any]]:
    clustered = []
    parse_ok_count = 0
    for submission in submissions:
        features = extract_features_from_code(submission.content)
        if features["parseOk"]:
            parse_ok_count += 1
        fingerprint = build_structured_fingerprint(features)
        feature_bag = build_feature_bag(features)
        clustered.append({
            "submission": {
                "id": submission.id,
                "titleSlug": submission.title_slug,
                "status": submission.status,
                "createdAt": submission.created_at,
            },
            "lang": language_of(submission),
            "features": features,
            "fingerprint": fingerprint,
            "featureBag": feature_bag,
            "fingerprintKey": build_cluster_key(fingerprint),
        })
    LOGGER.info(
        "extracted AST features submissions=%d parseOk=%d parseFailed=%d",
        len(clustered),
        parse_ok_count,
        len(clustered) - parse_ok_count,
    )
    return clustered


def run_self_check() -> None:
    frontier = build_feature_bag(extract_features_from_code(
        "from collections import deque\n"
        "def solve(grid):\n"
        "    queue = deque([(0, 0)])\n"
        "    visited = {(0, 0)}\n"
        "    while queue:\n"
        "        r, c = queue.popleft()\n"
        "        for nr, nc in ((r + 1, c),):\n"
        "            if (nr, nc) not in visited:\n"
        "                visited.add((nr, nc))\n"
        "                queue.append((nr, nc))\n"
    ))
    midpoint = build_feature_bag(extract_features_from_code(
        "def search(nums, target):\n"
        "    left, right = 0, len(nums) - 1\n"
        "    while left <= right:\n"
        "        mid = (left + right) // 2\n"
        "        if nums[mid] < target:\n"
        "            left = mid + 1\n"
        "        else:\n"
        "            right = mid - 1\n"
    ))
    assert frontier["motif:frontier_pop_then_expand"] == 3
    assert structural_similarity(frontier, frontier) > structural_similarity(frontier, midpoint)

    clustered = [
        {
            "submission": {"id": "a", "titleSlug": "two-sum", "status": "Accepted", "createdAt": "2026-06-24T00:00:00Z"},
            "lang": "python3",
            "features": extract_features_from_code("def solve(nums, target):\n    return 0\n"),
            "fingerprint": {"loops": ["for"], "recursion": False, "dataStructures": ["array"], "ops": [], "stateVars": [], "transitionOrder": ["sequential_scan"], "answerUpdateTiming": "inside_scan", "confidence": 0.35},
            "featureBag": {"ctrl:for": 1},
            "fingerprintKey": "cluster-a",
            "assignedClusterKey": "cluster-a",
        },
        {
            "submission": {"id": "b", "titleSlug": "two-sum", "status": "Accepted", "createdAt": "2026-06-24T00:00:00Z"},
            "lang": "python3",
            "features": extract_features_from_code("def solve(nums, target):\n    return 1\n"),
            "fingerprint": {"loops": ["while"], "recursion": False, "dataStructures": ["dict"], "ops": [], "stateVars": [], "transitionOrder": ["sequential_scan"], "answerUpdateTiming": "inside_scan", "confidence": 0.35},
            "featureBag": {"ctrl:while": 1},
            "fingerprintKey": "cluster-b",
            "assignedClusterKey": "cluster-b",
        },
    ]
    cluster_artifact = {
        "clusters": [
            {"clusterKey": "cluster-a", "submissionCount": 1},
            {"clusterKey": "cluster-b", "submissionCount": 1},
        ]
    }
    problem_artifact = build_problem_artifact(
        clustered,
        cluster_artifact,
        CliOptions(),
        "2026-06-24T00:00:00Z",
        "self-check",
        log_summary=False,
    )
    assert problem_artifact["summary"]["multiSolutionProblemCount"] == 1
    assert len(problem_artifact["problems"][0]["clusterMemberships"]) == 2
    assert problem_artifact["problems"][0]["clusterMemberships"][0]["confidenceInterval"]["high"] >= 0.5


def main(argv: list[str]) -> int:
    load_repo_env()
    options = parse_args(argv)
    setup_logging(options.verbose)
    LOGGER.info(
        "starting submission AST cluster run limit=%s scan=%s source=%s unique=%s threshold=%.3f label=%s labelModel=%s json=%s",
        options.limit,
        options.scan,
        options.source,
        options.unique,
        options.threshold,
        options.label,
        options.label_model,
        options.json,
    )
    run_self_check()
    LOGGER.debug("self-check passed")

    submissions = fetch_candidate_submissions(options)
    clustered = build_clustered_submissions(submissions)

    if options.json:
        LOGGER.info("writing clustered submissions JSON to stdout submissions=%d", len(clustered))
        print(json.dumps(clustered, indent=2, ensure_ascii=False))
        return 0

    generated_at = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    run_id = create_run_id(generated_at)
    out_path = options.out or str(default_artifact_path(options, run_id))
    LOGGER.info("artifact output runId=%s basePath=%s", run_id, out_path)

    cluster_artifact = build_maybe_labeled_cluster_artifact(clustered, options, generated_at, run_id)
    problem_artifact = build_problem_artifact(clustered, cluster_artifact, options, generated_at, run_id)
    submission_artifact = build_submission_artifact(clustered, cluster_artifact, options, generated_at, run_id)
    paths = derive_artifact_paths(out_path)
    write_json_artifact(str(paths["clusters"]), cluster_artifact)
    write_json_artifact(str(paths["problems"]), problem_artifact)
    write_json_artifact(str(paths["submissions"]), submission_artifact)
    print(f"Wrote cluster artifact: {paths['clusters']}")
    print(f"Wrote problem artifact: {paths['problems']}")
    print(f"Wrote submission artifact: {paths['submissions']}")
    return 0


def cli() -> int:
    return main(sys.argv[1:])


if __name__ == "__main__":
    try:
        raise SystemExit(cli())
    except KeyboardInterrupt:
        raise SystemExit(130)
