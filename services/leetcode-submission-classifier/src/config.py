from __future__ import annotations

from pathlib import Path

import yaml

# Artifact output root. Each run creates a unique subdirectory under here.
ARTIFACTS_DIR = Path(__file__).resolve().parents[1] / "artifacts"
CLUSTERING_RULES_PATH = Path(__file__).resolve().parents[1] / "clustering_rules.yaml"
# Local Python fixture corpus used for benchmark mode.
CORPUS_FIXTURES_DIR = Path(__file__).resolve().parents[1] / "benchmark" / "fixtures" / "corpus"
DEFAULT_CLUSTER_ARTIFACT_NAME = "latest-structure-clusters.json"
DEFAULT_LABELED_CLUSTER_ARTIFACT_NAME = "latest-structure-clusters-labeled.json"
DEFAULT_SUBMISSION_LIMIT = 500

# Default clustering threshold for weighted structural similarity.
# Higher values make clusters stricter and create more singletons.
DEFAULT_CLUSTER_THRESHOLD = 0.55

# Console preview threshold. Kept looser than the persisted clustering threshold
# so ad-hoc local inspection can still show near-neighbor structure families.
PREVIEW_CLUSTER_THRESHOLD = 0.34

# Default model for optional cluster labeling. Keep this as the label-specific
# source of truth so the CLI doesn't need to duplicate model fallback logic.
DEFAULT_LABEL_MODEL = "qwen/qwen3-coder-next"

# Language filter used at the SQL layer to keep the classifier scoped to Python submissions.
PYTHON_LANGUAGE_LIKE_PATTERN = "%python%"

def load_clustering_rules() -> dict:
    return yaml.safe_load(CLUSTERING_RULES_PATH.read_text(encoding="utf-8"))


CLUSTERING_RULES = load_clustering_rules()


def rule_tuple(section: str, key: str) -> tuple[str, ...]:
    return tuple(CLUSTERING_RULES[section][key])


def rule_value(section: str, key: str) -> str:
    return str(CLUSTERING_RULES[section][key])


# Lexical signal tokens and family gates live in YAML so tuning cluster behavior
# does not require editing Python code.
GRID_SIGNAL_TOKENS = rule_tuple("signals", "grid")
GRAPH_SIGNAL_TOKENS = rule_tuple("signals", "graph")
NEIGHBOR_SIGNAL_TOKENS = rule_tuple("signals", "neighbor")
LEFT_RIGHT_POINTER_NAMES = rule_tuple("signals", "left_right_pointers")
UNION_FIND_STATE_NAMES = rule_tuple("signals", "union_find_states")
NEIGHBOR_STATE_NAMES = rule_tuple("signals", "neighbor_states")
NESTED_COLLECTION_API_NAMES = rule_tuple("signals", "nested_collection_api_names")
DP_STATE_NAMES = rule_tuple("signals", "dp_states")
DICT_LIKE_CALL_NAMES = rule_tuple("signals", "dict_like_call_names")
HEAP_CALL_NAMES = rule_tuple("signals", "heap_call_names")
SORT_CALL_NAMES = rule_tuple("signals", "sort_call_names")
UNION_FIND_CALL_NAMES = rule_tuple("signals", "union_find_call_names")
GRAPH_TRAVERSAL_CALL_NAMES = rule_tuple("signals", "graph_traversal_call_names")
DESIGN_CLASS_API_METHOD_NAMES = tuple(name.lower() for name in rule_tuple("signals", "design_class_api_methods"))
DEQUE_IMPORT_HINTS = rule_tuple("signals", "deque_import_hints")
COUNTER_IMPORT_HINTS = rule_tuple("signals", "counter_import_hints")
HEAP_IMPORT_HINTS = rule_tuple("signals", "heap_import_hints")

# Confidence scoring knobs for the heuristic fingerprint. These do not affect
# raw feature extraction; they only tune how strongly a pattern "looks like"
# a recognizable solution family.
BASE_FINGERPRINT_CONFIDENCE = 0.35
QUEUE_GRAPH_CONFIDENCE_BOOST = 0.3
MIDPOINT_CONFIDENCE_BOOST = 0.25
TWO_POINTER_CONFIDENCE_BOOST = 0.2
PREFIX_CONFIDENCE_BOOST = 0.2
ADVANCED_DS_CONFIDENCE_BOOST = 0.2

# Wilson interval z-score for problem->cluster membership confidence intervals.
WILSON_INTERVAL_Z = 1.96

# Fingerprint construction caps. These limit how strongly generic control-flow
# signals can dominate the final structure signature.
NESTED_LOOP_MIN_DEPTH = 2
NESTED_LOOP_MIN_TOTAL_LOOPS = 2
IF_COUNT_FEATURE_CAP = 3
FEATURE_VALUE_CAP = 3.0
SHARED_EVIDENCE_TOP_K = 12
FORMAT_EVIDENCE_TOP_K = 8
SHARED_EVIDENCE_MIN_FRACTION = 0.5
SHARED_EVIDENCE_MIN_COUNT = 2

# Canonical fingerprint labels also live in YAML because they are cluster
# vocabulary, not classifier control flow.
DEFAULT_DATA_STRUCTURE_LABEL = rule_value("labels", "default_data_structure")
DEFAULT_TRANSITION_LABEL = rule_value("labels", "default_transition")
DEFAULT_ANSWER_TIMING_LABEL = rule_value("labels", "default_answer_timing")
QUEUE_TRANSITION_LABEL = rule_value("labels", "queue_transition")
RECURSION_TRANSITION_LABEL = rule_value("labels", "recursion_transition")
MIDPOINT_TRANSITION_LABEL = rule_value("labels", "midpoint_transition")
SLIDING_WINDOW_TRANSITION_LABEL = rule_value("labels", "sliding_window_transition")
PREFIX_TRANSITION_LABEL = rule_value("labels", "prefix_transition")
DP_TRANSITION_LABEL = rule_value("labels", "dp_transition")
UNION_FIND_TRANSITION_LABEL = rule_value("labels", "union_find_transition")
CLASS_API_TRANSITION_LABEL = rule_value("labels", "class_api_transition")
QUEUE_ANSWER_TIMING_LABEL = rule_value("labels", "queue_answer_timing")
SLIDING_WINDOW_ANSWER_TIMING_LABEL = rule_value("labels", "sliding_window_answer_timing")
MIDPOINT_ANSWER_TIMING_LABEL = rule_value("labels", "midpoint_answer_timing")
DP_ANSWER_TIMING_LABEL = rule_value("labels", "dp_answer_timing")
SCAN_ANSWER_TIMING_LABEL = rule_value("labels", "scan_answer_timing")

# Feature-bag scoring weights. These are the main knobs for deciding which
# concrete implementation details should dominate clustering.
NESTED_LOOP_BAG_SCORE = 3.0
DIRECT_RECURSION_BAG_SCORE = 5.0
DEQUE_INIT_BAG_SCORE = 2.0
COUNTER_INIT_BAG_SCORE = 2.0
DEFAULTDICT_INIT_BAG_SCORE = 2.0
DICT_INIT_BAG_SCORE = 1.5
SET_INIT_BAG_SCORE = 1.5
PRIORITY_QUEUE_BAG_SCORE = 3.0
GRID_STATE_BAG_SCORE = 2.0
TREE_STATE_BAG_SCORE = 2.0
GRAPH_STATE_BAG_SCORE = 2.0
UNION_FIND_BAG_SCORE = 3.0
CLASS_API_BAG_SCORE = 5.0
RECURSIVE_TREE_BAG_SCORE = 5.0
RECURSIVE_GRID_BAG_SCORE = 5.0
RECURSIVE_NESTED_COLLECTION_BAG_SCORE = 5.0
ITERATIVE_TREE_BAG_SCORE = 5.0
QUEUE_MOTIF_BAG_SCORE = 3.0
LEFT_RIGHT_WHILE_BAG_SCORE = 2.0
SLIDING_WINDOW_MOTIF_BAG_SCORE = 3.0
PREFIX_LOOKUP_MOTIF_BAG_SCORE = 3.0
MIDPOINT_BOUNDARY_MOTIF_BAG_SCORE = 3.0
LEXICAL_FALLBACK_BAG_SCORE = 0.5
EXPLICIT_STATE_INIT_BAG_SCORE = 0.0

# Weighted-Jaccard feature weights. These tune how much each feature namespace
# matters when deciding whether two submissions are structurally similar.
FEATURE_WEIGHT_NESTED_LOOP = 0.6
FEATURE_WEIGHT_STRUCTURAL = 3.0
FEATURE_WEIGHT_CALL = 2.2
FEATURE_WEIGHT_ASSIGN = 1.2
FEATURE_WEIGHT_CONTROL = 0.4
FEATURE_WEIGHT_SOURCE = 0.0
FEATURE_WEIGHT_FALLBACK = 0.8

# Family gate ordering for DSU clustering. Earlier matches win.
CLUSTER_FAMILY_RULES = tuple(
    (str(rule["family"]), tuple(rule["keys"]))
    for rule in CLUSTERING_RULES["cluster_families"]["rules"]
)
DEFAULT_CLUSTER_FAMILY = rule_value("cluster_families", "default")
