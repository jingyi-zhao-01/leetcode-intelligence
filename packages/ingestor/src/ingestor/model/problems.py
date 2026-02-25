from pydantic import BaseModel, Field
from typing import List, Optional


class Question(BaseModel):
    """Represents a LeetCode question."""

    difficulty: str
    title: str
    title_slug: str = Field(..., alias="titleSlug")
    freq_bar: Optional[float] = Field(None, alias="freqBar")
    topic_tags: List[str] = Field(default_factory=list, alias="topicTags")
    related_problems: List[str] = Field(default_factory=list, alias="relatedProblems")
    content: Optional[str] = None

    class Config:
        populate_by_name = True
