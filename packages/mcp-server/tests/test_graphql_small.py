#!/usr/bin/env python3
"""
Small test for GraphQL client to fetch just a few questions.
"""

from problems.leetcode_graphql import LeetCodeGraphQLClient
import json
import os


def test_small_fetch():
    """Test fetching just a few questions."""
    client = LeetCodeGraphQLClient()

    try:
        print("Testing small fetch (first 10 questions)...")

        # Fetch just the first 10 questions for testing
        questions = []
        offset = 0
        limit = 10  # Just fetch 10 for testing

        print(f"Fetching questions {offset + 1}-{offset + limit}...")
        response = client.fetch_questions(offset=offset, limit=limit)

        if (
            response
            and "data" in response
            and "problemsetQuestionList" in response["data"]
        ):
            batch_questions = response["data"]["problemsetQuestionList"]["questions"]
            questions.extend(batch_questions)
            print(f"Fetched {len(batch_questions)} questions")

        # Save to test JSON file
        test_file = "test_questions.json"
        with open(test_file, "w", encoding="utf-8") as f:
            json.dump(questions, f, indent=2, ensure_ascii=False)

        print(f"\nSaved {len(questions)} questions to {test_file}")
        print(f"File size: {os.path.getsize(test_file)} bytes")

        # Display first few questions
        print("\nFirst 3 questions:")
        for i, question in enumerate(questions[:3], 1):
            tags = [tag["slug"] for tag in question.get("topicTags", [])]
            tags_str = ", ".join(tags[:3]) + ("..." if len(tags) > 3 else "")

            print(
                f"{i}. {question['titleSlug']} | {question['title']} "
                f"({question['difficulty']}) | Freq: {question.get('freqBar', 0)} | Tags: {tags_str}"
            )

        return True

    except Exception as e:
        print(f"Error: {e}")
        return False


if __name__ == "__main__":
    test_small_fetch()
