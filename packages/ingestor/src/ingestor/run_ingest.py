"""
This script ingests LeetCode problems into a PostgreSQL database using Prisma.
"""

import asyncio
import logging
from prisma import Prisma
from .leetcode_graphql import LeetCodeGraphQLClient
from .common.logging_config import setup_logging
from .common.log_decorator import log_function_calls

logger = logging.getLogger(__name__)


@log_function_calls
async def main():
    """
    Fetch questions and ingest them into the database.
    """
    setup_logging()
    client = LeetCodeGraphQLClient()
    questions = client.fetch_all_questions_with_similar()

    db = Prisma()
    await db.connect()

    try:
        for q in questions:
            await db.question.upsert(
                where={"titleSlug": q.title_slug},
                data={
                    "create": {
                        "title": q.title,
                        "titleSlug": q.title_slug,
                        "difficulty": q.difficulty,
                        "freqBar": q.freq_bar,
                        "topicTags": q.topic_tags,
                        "relatedProblems": q.related_problems,
                        "content": q.content,
                    },
                    "update": {
                        "difficulty": q.difficulty,
                        "freqBar": q.freq_bar,
                        "topicTags": q.topic_tags,
                        "relatedProblems": q.related_problems,
                        "content": q.content,
                    },
                },
            )
    finally:
        await db.disconnect()


def run():
    """Entry point for poetry script."""
    asyncio.run(main())


if __name__ == "__main__":
    run()
