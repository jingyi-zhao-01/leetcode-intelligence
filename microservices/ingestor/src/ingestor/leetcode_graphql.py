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
