from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import List, Dict, Any, Iterable, Optional


@dataclass
class Submission:
    id: int
    problem_id: int
    title: str
    tags: List[str]
    knowledge: List[str]
    status: str
    language: str
    error_parts: List[str]
    notes: str
    difficulty: str

    @property
    def is_wrong(self) -> bool:
        return self.status in {"Wrong Answer", "Time Limit Exceeded", "Runtime Error"}


class Submissions:
    def __init__(self, items: List[Submission]):
        self.items = items

    @classmethod
    def load(cls, path: str | Path) -> "Submissions":
        data = json.loads(Path(path).read_text())
        items = [Submission(**x) for x in data]
        return cls(items)

    def stats(self) -> Dict[str, Any]:
        total = len(self.items)
        wrong = sum(s.is_wrong for s in self.items)
        accepted = sum(1 for s in self.items if s.status == "Accepted")
        by_status: Dict[str, int] = {}
        for s in self.items:
            by_status[s.status] = by_status.get(s.status, 0) + 1
        return {
            "total": total,
            "wrong": wrong,
            "accepted": accepted,
            "by_status": by_status,
        }

    def wrong_details(self) -> List[Dict[str, Any]]:
        out = []
        for s in self.items:
            if s.is_wrong:
                out.append({
                    "id": s.id,
                    "problem_id": s.problem_id,
                    "title": s.title,
                    "error_parts": s.error_parts,
                    "knowledge": s.knowledge,
                    "tags": s.tags,
                    "notes": s.notes,
                })
        return out

    def related_by_knowledge(self, knowledge_gaps: Iterable[str], limit: int = 5) -> List[Submission]:
        gaps = set(k.lower() for k in knowledge_gaps)
        scored: List[tuple[int, Submission]] = []
        for s in self.items:
            know = set(k.lower() for k in s.knowledge)
            score = len(gaps & know)
            if score:
                scored.append((score, s))
        scored.sort(key=lambda t: (-t[0], t[1].difficulty, t[1].title))
        return [s for _, s in scored[:limit]]


# CLI

def main(argv: Optional[List[str]] = None) -> None:
    import argparse

    p = argparse.ArgumentParser(description="Submission mentor: summarize and suggest related problems")
    p.add_argument("question", help="Your current question/problem title (free text)")
    p.add_argument("--subs", default=str(Path(__file__).resolve().parents[2] / "data" / "submissions.json"), help="Path to submissions JSON")
    p.add_argument("--show", choices=["summary", "wrong", "related"], default="summary")
    args = p.parse_args(argv)

    subs = Submissions.load(args.subs)

    # Naive extraction of knowledge gaps from question by keyword mapping
    keywords_to_knowledge = {
        "stock": ["prefix minima", "state tracking"],
        "merge": ["pointer manipulation", "null pointer handling"],
        "islands": ["mark visited", "bounds checks"],
        "substring": ["window shrink on duplicate"],
        "coin": ["bottom-up dp", "unbounded knapsack pattern"],
        "lru": ["doubly linked list", "O(1) operations"],
        "two sum": ["hash map lookup"],
        "binary search": ["two-pointer search", "mid computation"],
    }

    q_lower = args.question.lower()
    gaps: List[str] = []
    for k, v in keywords_to_knowledge.items():
        if k in q_lower:
            gaps.extend(v)

    if args.show == "summary":
        s = subs.stats()
        print(f"Total submissions: {s['total']}\nAccepted: {s['accepted']}\nWrong: {s['wrong']}\nBy status: {s['by_status']}")
    elif args.show == "wrong":
        for d in subs.wrong_details():
            print(f"- {d['title']} (id={d['id']}): errors={d['error_parts']} knowledge={d['knowledge']}")
    else:  # related
        related = subs.related_by_knowledge(gaps or ["hash map lookup", "two-pointer search"])  # fallback
        print("Related problems leveraging the missing knowledge:")
        for s in related:
            print(f"- {s.title} (id={s.id}, status={s.status}, knowledge={s.knowledge})")


if __name__ == "__main__":
    main()
