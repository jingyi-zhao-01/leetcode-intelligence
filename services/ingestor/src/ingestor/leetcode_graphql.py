"""
LeetCode GraphQL API client for fetching all problems.
"""

import os
import json
import time
import requests
from typing import Dict, List, Any, Tuple
from pathlib import Path
from dotenv import load_dotenv
import logging

from .model.problems import Question
from .common.log_decorator import log_function_calls

logger = logging.getLogger(__name__)


load_dotenv()


MAX_INTAKE_QUESTIONS_ENV = os.getenv("MAX_INTAKE_QUESTIONS")
MAX_INTAKE_QUESTIONS = (
    int(MAX_INTAKE_QUESTIONS_ENV) if MAX_INTAKE_QUESTIONS_ENV is not None else 0
)

SAVE_JSON = False


class LeetCodeGraphQLClient:
    """Simple client for fetching all LeetCode problems."""

    LEETCODE_GRAPHQL_URL = "https://leetcode.com/graphql"
    BATCH_SIZE = 10

    def __init__(self):
        self.session = requests.Session()

        # Get cookie from environment variable
        leetcode_cookie = os.getenv("LEETCODE_COOKIE")

        self.session.headers.update(
            {
                "Content-Type": "application/json",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                "Cookie": leetcode_cookie if leetcode_cookie else "",
            }
        )

    @log_function_calls
    def fetch_similar_questions(self, title_slug: str) -> List[Dict[str, Any]]:
        """
        Fetch similar questions for a given question using its titleSlug.

        Args:
            title_slug: The titleSlug of the question to find similar questions for

        Returns:
            List of similar question dictionaries
        """
        query = """
        query SimilarQuestions($titleSlug: String!) {
          question(titleSlug: $titleSlug) {
            similarQuestionList {
              difficulty
              titleSlug
              title
              translatedTitle
              isPaidOnly
            }
          }
        }
        """

        variables = {"titleSlug": title_slug}

        payload = {
            "query": query,
            "variables": variables,
            "operationName": "SimilarQuestions",
        }

        try:
            response = self.session.post(
                self.LEETCODE_GRAPHQL_URL,
                json=payload,
                timeout=30,
            )
            response.raise_for_status()
            data = response.json()

            if "data" not in data or "question" not in data["data"]:
                return []

            question_data = data["data"]["question"]
            if not question_data or "similarQuestionList" not in question_data:
                return []

            return question_data["similarQuestionList"] or []

        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching similar questions for {title_slug}: {e}")
            return []

    @log_function_calls
    def fetch_question_content(self, title_slug: str) -> str | None:
        """
        Fetch the content of a single question.
        """
        query = """
            query questionContent($titleSlug: String!) {
              question(titleSlug: $titleSlug) {
                content
              }
            }
        """
        variables = {"titleSlug": title_slug}
        payload = {
            "query": query,
            "variables": variables,
            "operationName": "questionContent",
        }

        try:
            response = self.session.post(
                self.LEETCODE_GRAPHQL_URL,
                json=payload,
                timeout=30,
            )
            response.raise_for_status()
            data = response.json()

            if "data" not in data or "question" not in data["data"]:
                return None

            question_data = data["data"]["question"]
            if not question_data or "content" not in question_data:
                return None

            return question_data["content"]

        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching question content for {title_slug}: {e}")
            return None

    @log_function_calls
    def fetch_all_questions_with_similar(
        self,
        output_file: str = "data/leetcode_questions_with_similar.json",
        delay: float = 1.0,
        max_questions: int = MAX_INTAKE_QUESTIONS,
    ) -> List[Question]:
        """
        Fetch LeetCode questions and their similar questions using GraphQL API with rate limiting.
        Combines all data into a single output file with simplified format.

        Args:
            output_file: Path to save the JSON file
            delay: Delay between requests in seconds to avoid rate limiting
            max_questions: Maximum number of questions to fetch (for testing/limiting)

        Returns:
            List of question objects with similar questions included
        """
        logger.info(
            f"Starting to fetch LeetCode questions with {delay}s delay between requests..."
        )
        logger.info(f"Maximum questions to fetch: {max_questions}")

        # Step 1: Fetch all questions
        all_questions = self._fetch_paginated_questions(delay, max_questions)

        # Step 2: Enrich with similar questions
        self._enrich_questions_with_similar(all_questions, delay)

        # Enrich with content
        self._enrich_questions_with_content(all_questions, delay)

        # Step 3: Save the final data
        if SAVE_JSON:
            self._save_questions_to_file(all_questions, output_file)

        return all_questions

    @log_function_calls
    def _fetch_paginated_questions(
        self, delay: float, max_questions: int
    ) -> List[Question]:
        """Helper to fetch questions in paginated batches."""
        all_questions: List[Question] = []
        skip = 0
        batch_size = self.BATCH_SIZE
        request_count = 0

        while len(all_questions) < max_questions:
            if request_count > 0:
                time.sleep(delay)

            should_continue = self._fetch_and_process_batch(
                skip, batch_size, all_questions, max_questions
            )
            request_count += 1

            if not should_continue:
                break

            skip += batch_size

        return all_questions[:max_questions]

    def _fetch_question_batch(
        self, skip: int, batch_size: int
    ) -> Tuple[List[Dict[str, Any]], int]:
        """Fetches a single batch of questions."""
        query = """
        query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {
          problemsetQuestionList: questionList(
            categorySlug: $categorySlug
            limit: $limit
            skip: $skip
            filters: $filters
          ) {
            total: totalNum
            questions: data {
              difficulty
              freqBar
              title
              titleSlug
              topicTags { slug }
            }
          }
        }
        """
        variables = {
            "categorySlug": "all-code-essentials",
            "skip": skip,
            "limit": batch_size,
            "filters": {},
        }
        payload = {
            "query": query,
            "variables": variables,
            "operationName": "problemsetQuestionList",
        }

        response = self.session.post(
            self.LEETCODE_GRAPHQL_URL, json=payload, timeout=30
        )
        response.raise_for_status()
        data = response.json()

        if "data" not in data or "problemsetQuestionList" not in data["data"]:
            return [], 0

        problems_data = data["data"]["problemsetQuestionList"]

        # The raw topic tags are dicts, so we extract the 'slug'
        questions_raw = problems_data.get("questions", [])
        for q in questions_raw:
            q["topicTags"] = [tag["slug"] for tag in q.get("topicTags", [])]

        return questions_raw, problems_data.get("total", 0)

    @log_function_calls
    def _fetch_and_process_batch(
        self,
        skip: int,
        batch_size: int,
        all_questions: List[Question],
        max_questions: int,
    ) -> bool:
        """Fetches and processes a single batch of questions, returning True if fetching should continue."""
        try:
            questions_data, total = self._fetch_question_batch(skip, batch_size)

            if not questions_data:
                return False

            if any(q.get("freqBar") is None for q in questions_data):
                raise RuntimeError("LEETCODE_COOKIE has expired. Please refresh it.")

            # Parse dictionaries into Question objects
            questions = [Question.model_validate(q) for q in questions_data]

            all_questions.extend(questions)

            return len(all_questions) < max_questions and len(all_questions) < total

        except requests.exceptions.Timeout:
            logger.warning("Request timed out, retrying in 5 seconds...")
            time.sleep(5)
            return True  # Continue fetching
        except requests.exceptions.RequestException as e:
            logger.error(f"Request error: {e}")
            if "429" in str(e) or "rate" in str(e).lower():
                logger.warning("Rate limited! Waiting 10 seconds before retry...")
                time.sleep(10)
                return True  # Continue fetching
            else:
                raise RuntimeError(f"Failed to fetch questions from LeetCode API: {e}")

    @log_function_calls
    def _enrich_questions_with_similar(self, questions: List[Question], delay: float):
        """Enriches each question with a list of similar questions."""
        for i, question in enumerate(questions, 1):
            if i > 1:
                time.sleep(delay)

            similar_questions = self.fetch_similar_questions(question.title_slug)
            question.related_problems = [sq["titleSlug"] for sq in similar_questions]

    @log_function_calls
    def _enrich_questions_with_content(self, questions: List[Question], delay: float):
        """Enriches each question with its content."""
        for i, question in enumerate(questions, 1):
            if i > 1:
                time.sleep(delay)
            content = self.fetch_question_content(question.title_slug)
            if content:
                question.content = content

    @log_function_calls
    def _save_questions_to_file(self, questions: List[Question], output_file: str):
        """Saves the list of questions to a JSON file."""
        try:
            output_path = Path(output_file)
            output_path.parent.mkdir(parents=True, exist_ok=True)

            # Convert Question objects to dictionaries for JSON serialization
            questions_dict = [q.model_dump(by_alias=True) for q in questions]

            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(questions_dict, f, indent=2, ensure_ascii=False)
        except Exception as e:
            logger.error(f"Error saving to file: {e}")
