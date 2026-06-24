#!/usr/bin/env python3
"""Generate benchmark fixtures from kamyu104 LeetCode Python solutions."""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
import re
import tarfile
import urllib.request
from datetime import datetime, timezone
from io import BytesIO
from pathlib import Path
from typing import Any, Dict


DEFAULT_REPO_TARBALL_URL = "https://github.com/kamyu104/LeetCode-Solutions/archive/refs/heads/master.tar.gz"
DEFAULT_OUTPUT_DIR = Path(__file__).resolve().parent / "fixtures" / "corpus"
""
SOLUTION_CLASS_PATTERN = re.compile(r"^Solution\d*$")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate local benchmark fixtures from a public corpus.")
    parser.add_argument(
        "--repo-tarball",
        default=DEFAULT_REPO_TARBALL_URL,
        help="Source tarball URL for a LeetCode solution repo.",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Deterministic seed for fixture fingerprinting.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help="Directory to write fixture .py files and manifest.json.",
    )
    parser.add_argument("--manifest-name", default="manifest.json", help="Manifest filename.")
    return parser.parse_args()


def fetch_repo_targz(url: str) -> bytes:
    with urllib.request.urlopen(url) as response:
        return response.read()


def stable_submit_seed(repo: str, seed: int, idx: int, problem_id: str) -> int:
    seed_text = f"{repo}|{seed}|{idx}|{problem_id}"
    return int(hashlib.sha1(seed_text.encode("utf-8")).hexdigest()[:8], 16)


def extract_solution_classes(code: str) -> tuple[list[tuple[str, int, int, str]], int]:
    """Extract top-level Solution-like class chunks and the first class start line.

    Returns:
        (classes, prelude_end_line)
    """
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return [], 0

    lines = code.splitlines()
    candidates: list[tuple[ast.ClassDef, int]] = []
    for node in tree.body:
        if isinstance(node, ast.ClassDef) and SOLUTION_CLASS_PATTERN.match(node.name):
            end_line = node.end_lineno or len(lines)
            candidates.append((node, end_line))

    if not candidates:
        return [], 0

    candidates = sorted(candidates, key=lambda pair: pair[0].lineno)
    results: list[tuple[str, int, int, str]] = []
    for node, end_line in candidates:
        start = node.lineno
        end = end_line
        class_code = "\n".join(lines[start - 1 : end])
        if class_code:
            results.append((node.name, start, end, class_code))
    prelude_end_line = candidates[0][0].lineno - 1
    return results, prelude_end_line


def collect_python_members(tar: tarfile.TarFile) -> list[tarfile.TarInfo]:
    members = []
    for info in tar.getmembers():
        if not info.isfile():
            continue
        parts = Path(info.name).parts
        if len(parts) < 2:
            continue
        if parts[-2] != "Python" or not parts[-1].endswith(".py"):
            continue
        members.append(info)
    return members


def main() -> None:
    args = parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    tar_bytes = fetch_repo_targz(args.repo_tarball)
    with tarfile.open(fileobj=BytesIO(tar_bytes), mode="r:gz") as tar:
        members = collect_python_members(tar)

    if not members:
        raise RuntimeError("No Python files found in repo tarball under Python/.")

    # Remove stale fixtures from previous runs, then write a deterministic full snapshot.
    for old_file in args.output_dir.glob("*.py"):
        old_file.unlink()

    members = sorted(members, key=lambda info: Path(info.name).name)

    manifest_items: list[Dict[str, Any]] = []

    with tarfile.open(fileobj=BytesIO(tar_bytes), mode="r:gz") as tar:
        for idx, member in enumerate(members, start=1):
            file_obj = tar.extractfile(member)
            if file_obj is None:
                continue

            raw_code = file_obj.read()
            code = raw_code.decode("utf-8", errors="replace")
            problem_id = Path(member.name).name.removesuffix(".py")
            lines = code.splitlines()

            solution_variants, prelude_end_line = extract_solution_classes(code)
            variant_suffixes: list[str] = []
            prelude = "\n".join(lines[:prelude_end_line]).rstrip("\n")
            prelude = f"{prelude}\n\n" if prelude else ""

            for variant_idx, (class_name, _, _, solution_code) in enumerate(solution_variants, start=1):
                variant = (
                    f".{class_name.lower()}"
                    if class_name != "Solution"
                    else f".solution{variant_idx}"
                )
                variant_suffixes.append(variant)
                target_name = f"{idx:03d}-{problem_id}{variant}.py"

                snippet_hash = hashlib.sha1(solution_code.encode("utf-8")).hexdigest()
                submit_seed = stable_submit_seed(
                    args.repo_tarball,
                    args.seed,
                    idx,
                    f"{problem_id}|{class_name}",
                )

                header = (
                    "# Source: https://github.com/kamyu104/LeetCode-Solutions\n"
                    f"# problem_id: {problem_id}\n"
                    f"# source_path: {member.name}\n"
                    f"# solution_class: {class_name}\n"
                    f"# submission_id: {snippet_hash}\n"
                    f"# seed: {submit_seed}\n\n"
                )

                (args.output_dir / target_name).write_text(header + prelude + solution_code, encoding="utf-8")
                manifest_items.append(
                    {
                        "problem_id": problem_id,
                        "source_path": member.name,
                        "solution_class": class_name,
                        "fixture_file": target_name,
                        "code_hash": snippet_hash,
                        "submission_seed": submit_seed,
                        "language": "python",
                    }
                )

            if not variant_suffixes:
                # Fallback: preserve full source if parsing failed or no class matches.
                variant = ".solution1"
                snippet_hash = hashlib.sha1(raw_code).hexdigest()
                submit_seed = stable_submit_seed(args.repo_tarball, args.seed, idx, problem_id)
                target_name = f"{idx:03d}-{problem_id}{variant}.py"
                header = (
                    "# Source: https://github.com/kamyu104/LeetCode-Solutions\n"
                    f"# problem_id: {problem_id}\n"
                    f"# source_path: {member.name}\n"
                    "# solution_class: Solution\n"
                    f"# submission_id: {snippet_hash}\n"
                    f"# seed: {submit_seed}\n\n"
                )
                (args.output_dir / target_name).write_text(header + code, encoding="utf-8")
                manifest_items.append(
                    {
                        "problem_id": problem_id,
                        "source_path": member.name,
                        "solution_class": "Solution",
                        "fixture_file": target_name,
                        "code_hash": snippet_hash,
                        "submission_seed": submit_seed,
                        "language": "python",
                    }
                )

    manifest = {
        "generated_at": datetime.now(tz=timezone.utc).isoformat(),
        "repo": args.repo_tarball,
        "seed": args.seed,
        "total_files": len(members),
        "count": len(manifest_items),
        "items": manifest_items,
    }
    (args.output_dir / args.manifest_name).write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
