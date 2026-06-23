


#!/usr/bin/env python3
from __future__ import annotations

import argparse
import ast
import json
import math
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Fingerprint:
    path: str
    features: Counter[str]


METHODS = {
    "append", "appendleft", "pop", "popleft", "add", "remove", "discard",
    "get", "sort", "reverse", "items", "keys", "values",
}

FUNCS = {
    "len", "range", "enumerate", "zip", "sorted", "reversed", "sum", "max", "min",
    "heappush", "heappop", "heapify", "bisect_left", "bisect_right",
}

INIT_CALLS = {"list", "dict", "set", "deque", "defaultdict", "Counter"}


def name_of(node: ast.AST | None) -> str | None:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        base = name_of(node.value)
        return f"{base}.{node.attr}" if base else node.attr
    if isinstance(node, ast.Subscript):
        return name_of(node.value)
    return None


def call_name(node: ast.AST) -> str:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        base = name_of(node.value)
        return f"{base}.{node.attr}" if base else node.attr
    return type(node).__name__


def shape(node: ast.AST | None, depth: int = 0) -> str:
    if node is None:
        return "None"
    if depth >= 3:
        return type(node).__name__

    if isinstance(node, ast.Name):
        return "Name"
    if isinstance(node, ast.Constant):
        return "Const"
    if isinstance(node, ast.Subscript):
        return f"Subscript({shape(node.value, depth + 1)})"
    if isinstance(node, ast.Call):
        n = call_name(node.func)
        short = n.split(".")[-1]
        if short in FUNCS or short in INIT_CALLS or n.startswith("heapq.") or n.startswith("bisect."):
            return f"Call:{n}"
        return "Call"
    if isinstance(node, ast.BinOp):
        return f"BinOp:{type(node.op).__name__}"
    if isinstance(node, ast.BoolOp):
        return f"BoolOp:{type(node.op).__name__}"
    if isinstance(node, ast.UnaryOp):
        return f"UnaryOp:{type(node.op).__name__}"
    if isinstance(node, ast.Compare):
        ops = "+".join(type(op).__name__ for op in node.ops)
        return f"Compare:{ops}"
    if isinstance(node, ast.List):
        return "List"
    if isinstance(node, ast.Dict):
        return "Dict"
    if isinstance(node, ast.Set):
        return "Set"
    if isinstance(node, ast.Tuple):
        return "Tuple"
    if isinstance(node, ast.ListComp):
        return "ListComp"
    if isinstance(node, ast.DictComp):
        return "DictComp"
    if isinstance(node, ast.SetComp):
        return "SetComp"

    return type(node).__name__


def stmt_shape(stmt: ast.stmt) -> str:
    if isinstance(stmt, ast.Assign):
        t = stmt.targets[0] if stmt.targets else None
        return f"Assign:{shape(t)}={shape(stmt.value)}"
    if isinstance(stmt, ast.AugAssign):
        return f"AugAssign:{shape(stmt.target)}:{type(stmt.op).__name__}"
    if isinstance(stmt, ast.For):
        return f"For:{shape(stmt.iter)}"
    if isinstance(stmt, ast.While):
        return f"While:{shape(stmt.test)}"
    if isinstance(stmt, ast.If):
        return f"If:{shape(stmt.test)}"
    if isinstance(stmt, ast.Return):
        return f"Return:{shape(stmt.value)}"
    if isinstance(stmt, ast.Expr) and isinstance(stmt.value, ast.Call):
        return f"ExprCall:{call_name(stmt.value.func)}"
    return type(stmt).__name__


def ngrams(xs: list[str], n: int):
    for i in range(len(xs) - n + 1):
        yield tuple(xs[i:i + n])


class Extractor(ast.NodeVisitor):
    def __init__(self) -> None:
        self.f: Counter[str] = Counter()
        self.ctx: list[str] = []
        self.fn_stack: list[str] = []
        self.var_ops: dict[str, Counter[str]] = defaultdict(Counter)

    def add(self, key: str, n: float = 1.0) -> None:
        self.f[key] += n

    def ctx_name(self) -> str:
        return ">".join(self.ctx[-3:]) if self.ctx else "top"

    def add_body_seq(self, prefix: str, body: list[ast.stmt]) -> None:
        ss = [stmt_shape(s) for s in body]

        for s in ss:
            self.add(f"seq1:{prefix}:{s}")

        for a, b in ngrams(ss, 2):
            self.add(f"seq2:{prefix}:{a} -> {b}")

        for a, b, c in ngrams(ss, 3):
            self.add(f"seq3:{prefix}:{a} -> {b} -> {c}")

    def visit_Import(self, node: ast.Import) -> None:
        for x in node.names:
            self.add(f"import:{x.name}")
        self.generic_visit(node)

    def visit_ImportFrom(self, node: ast.ImportFrom) -> None:
        mod = node.module or ""
        for x in node.names:
            self.add(f"import_from:{mod}.{x.name}")
        self.generic_visit(node)

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        self.add("ctrl:function")
        self.add_body_seq("function", node.body)

        self.fn_stack.append(node.name)
        self.ctx.append("function")
        self.generic_visit(node)
        self.ctx.pop()
        self.fn_stack.pop()

    def visit_For(self, node: ast.For) -> None:
        self.add("ctrl:for")
        self.add(f"ctx:{self.ctx_name()}:for")
        self.add(f"loop:for_iter:{shape(node.iter)}")
        self.add_body_seq("for_body", node.body)

        if any(isinstance(x, ast.While) for s in node.body for x in ast.walk(s)):
            self.add("motif:for_body_contains_while", 3.0)

        if any(isinstance(x, ast.If) for s in node.body for x in ast.walk(s)):
            self.add("motif:for_body_contains_if", 1.5)

        self.ctx.append("for")
        self.generic_visit(node)
        self.ctx.pop()

    def visit_While(self, node: ast.While) -> None:
        self.add("ctrl:while")
        self.add(f"ctx:{self.ctx_name()}:while")
        self.add(f"loop:while_test:{shape(node.test)}")
        self.add_body_seq("while_body", node.body)

        if "for" in self.ctx:
            self.add("motif:while_inside_for", 3.0)

        if any(isinstance(x, ast.Call) for s in node.body for x in ast.walk(s)):
            self.add("motif:while_body_contains_call", 1.0)

        self.ctx.append("while")
        self.generic_visit(node)
        self.ctx.pop()

    def visit_If(self, node: ast.If) -> None:
        self.add("ctrl:if")
        self.add(f"ctx:{self.ctx_name()}:if")
        self.add(f"branch:test:{shape(node.test)}")
        self.add_body_seq("if_body", node.body)

        self.ctx.append("if")
        self.generic_visit(node)
        self.ctx.pop()

    def visit_Call(self, node: ast.Call) -> None:
        n = call_name(node.func)
        short = n.split(".")[-1]

        if short in FUNCS or n.startswith("heapq.") or n.startswith("bisect."):
            self.add(f"call:{n}")
            self.add(f"ctxcall:{self.ctx_name()}:{n}")

        if isinstance(node.func, ast.Attribute):
            method = node.func.attr
            owner = name_of(node.func.value)

            if method in METHODS:
                self.add(f"method:{method}")
                self.add(f"ctxmethod:{self.ctx_name()}:{method}")

                if owner:
                    self.var_ops[owner][method] += 1

        elif short in {"heappush", "heappop", "heapify"} and node.args:
            owner = name_of(node.args[0])
            if owner:
                self.var_ops[owner][short] += 1

        if self.fn_stack and isinstance(node.func, ast.Name) and node.func.id == self.fn_stack[-1]:
            self.add("control_fact:direct_recursion", 5.0)
            self.add(f"ctxcall:{self.ctx_name()}:self_recursion", 3.0)

        self.generic_visit(node)

    def visit_Assign(self, node: ast.Assign) -> None:
        target = node.targets[0] if node.targets else None

        self.add(f"assign:{shape(target)}={shape(node.value)}")
        self.add(f"ctxassign:{self.ctx_name()}:{shape(target)}={shape(node.value)}")

        for t in node.targets:
            self.record_write(t)

            owner = name_of(t)
            value_shape = shape(node.value)

            if owner and value_shape in {"List", "Dict", "Set", "Tuple"}:
                self.var_ops[owner][f"init:{value_shape}"] += 1

            if owner and value_shape.startswith("Call:"):
                self.var_ops[owner][f"init:{value_shape}"] += 1

        self.generic_visit(node)

    def visit_AugAssign(self, node: ast.AugAssign) -> None:
        self.add(f"augassign:{shape(node.target)}:{type(node.op).__name__}")
        self.add(f"ctxaug:{self.ctx_name()}:{shape(node.target)}:{type(node.op).__name__}")

        self.record_write(node.target)

        owner = name_of(node.target)
        if owner:
            self.var_ops[owner][f"aug:{type(node.op).__name__}"] += 1

        self.generic_visit(node)

    def visit_Subscript(self, node: ast.Subscript) -> None:
        owner = name_of(node.value)

        if owner:
            self.var_ops[owner]["subscript_read"] += 1
            self.add(f"subscript_read_ctx:{self.ctx_name()}")

        self.generic_visit(node)

    def visit_Return(self, node: ast.Return) -> None:
        self.add(f"return:{shape(node.value)}")
        self.add(f"ctxreturn:{self.ctx_name()}:{shape(node.value)}")
        self.generic_visit(node)

    def record_write(self, t: ast.AST) -> None:
        if isinstance(t, ast.Name):
            self.var_ops[t.id]["write_name"] += 1

        elif isinstance(t, ast.Subscript):
            owner = name_of(t.value)

            if owner:
                self.var_ops[owner]["subscript_write"] += 1
                self.add(f"subscript_write_ctx:{self.ctx_name()}")

        elif isinstance(t, (ast.Tuple, ast.List)):
            for x in t.elts:
                self.record_write(x)

    def finalize(self) -> Counter[str]:
        for _, ops in self.var_ops.items():
            keys = set(ops)

            for k in keys:
                if k not in {"write_name", "subscript_read"}:
                    self.add(f"var_op:{k}")

            if {"append", "pop"} <= keys:
                self.add("role:append_and_pop_same_var", 3.0)

            if {"append", "popleft"} <= keys or {"appendleft", "pop"} <= keys:
                self.add("role:opposite_end_queue_ops", 3.0)

            if keys & {"heappush", "heappop", "heapify"}:
                self.add("role:priority_queue_ops", 3.0)

            if "subscript_write" in keys and "subscript_read" in keys:
                self.add("role:indexed_state_read_write", 2.0)

            if any(k.startswith("aug:") for k in keys):
                self.add("role:incremental_state", 1.5)

            if any(k.startswith("init:") for k in keys):
                self.add("role:explicit_state_init", 1.0)

        return self.f


def parse_file(path: Path) -> Fingerprint | None:
    try:
        src = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        src = path.read_text(errors="ignore")

    try:
        tree = ast.parse(src, filename=str(path))
    except SyntaxError as e:
        print(f"SKIP {path}: {e}")
        return None

    ex = Extractor()
    ex.visit(tree)

    return Fingerprint(str(path), ex.finalize())


def weight(k: str) -> float:
    if k.startswith(("motif:", "role:", "control_fact:")):
        return 3.0

    if k.startswith(("ctxmethod:", "ctxcall:", "ctxaug:", "ctxassign:")):
        return 2.4

    if k.startswith(("method:", "call:", "import:", "import_from:")):
        return 2.2

    if k.startswith(("seq2:", "seq3:", "loop:", "branch:", "return:")):
        return 1.6

    if k.startswith(("ctrl:", "assign:", "augassign:", "var_op:")):
        return 1.2

    return 0.8


def vector(c: Counter[str]) -> dict[str, float]:
    return {k: min(v, 3.0) * weight(k) for k, v in c.items()}


def sim(a: Counter[str], b: Counter[str]) -> float:
    va = vector(a)
    vb = vector(b)
    keys = set(va) | set(vb)

    if not keys:
        return 0.0

    num = sum(min(va.get(k, 0.0), vb.get(k, 0.0)) for k in keys)
    den = sum(max(va.get(k, 0.0), vb.get(k, 0.0)) for k in keys)

    return num / den if den else 0.0


class DSU:
    def __init__(self, n: int) -> None:
        self.p = list(range(n))

    def find(self, x: int) -> int:
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]

        return x

    def union(self, a: int, b: int) -> None:
        ra = self.find(a)
        rb = self.find(b)

        if ra != rb:
            self.p[rb] = ra


def files_under(path: Path) -> list[Path]:
    if path.is_file():
        return [path]

    return sorted(x for x in path.rglob("*.py") if not x.name.startswith("__"))


def shared_features(fps: list[Fingerprint], group: list[int], top: int) -> list[tuple[str, int, float]]:
    presence = Counter()
    strength = Counter()

    for i in group:
        for k, v in fps[i].features.items():
            presence[k] += 1
            strength[k] += min(v, 3.0) * weight(k)

    need = 1 if len(group) == 1 else max(2, math.ceil(len(group) * 0.50))

    rows = [
        (k, presence[k], strength[k])
        for k in presence
        if presence[k] >= need
    ]

    rows.sort(key=lambda x: (-x[1], -x[2], x[0]))

    return rows[:top]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--threshold", type=float, default=0.34)
    ap.add_argument("--top", type=int, default=12)
    ap.add_argument("--dump-features", type=Path)
    args = ap.parse_args()

    fps = [
        fp
        for p in files_under(Path(args.path))
        if (fp := parse_file(p))
    ]

    print(f"loaded={len(fps)}")

    if args.dump_features:
        with args.dump_features.open("w", encoding="utf-8") as f:
            for fp in fps:
                f.write(json.dumps(
                    {"path": fp.path, "features": dict(fp.features)},
                    ensure_ascii=False,
                    sort_keys=True,
                ) + "\n")

        print(f"features={args.dump_features}")

    dsu = DSU(len(fps))
    pairs = []

    for i in range(len(fps)):
        for j in range(i + 1, len(fps)):
            s = sim(fps[i].features, fps[j].features)

            if s >= args.threshold:
                dsu.union(i, j)
                pairs.append((s, i, j))

    groups: dict[int, list[int]] = defaultdict(list)

    for i in range(len(fps)):
        groups[dsu.find(i)].append(i)

    clusters = sorted(
        groups.values(),
        key=lambda g: (-len(g), min(fps[i].path for i in g)),
    )

    print("\npairs:")

    for s, i, j in sorted(pairs, reverse=True)[:50]:
        print(f"  {s:.3f}  {Path(fps[i].path).name} <-> {Path(fps[j].path).name}")

    print("\nclusters:")

    for n, g in enumerate(clusters, 1):
        print(f"\ncluster_{n:03d} size={len(g)}")

        for i in g:
            print(f"  - {fps[i].path}")

        print("  evidence:")

        for k, present, score in shared_features(fps, g, args.top):
            print(f"    {present}/{len(g)}  {score:.1f}  {k}")

    print("\nnext:")
    print("  size>=3: generate template note from evidence")
    print("  size<3: keep pending, collect more submissions")
    print("  no fixed labels used during clustering")


if __name__ == "__main__":
    main()