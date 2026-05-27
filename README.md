
# LeetCode Intelligence

## WHY
a systematic way to handle leetcode solving to manage the entire life cycle:
- How to get immediate feedback to understand which part of the code block is wrong ? is the reason due to not adequately understanding the problem or inproficiency of the syntax ? 
- How to persistently store my submissions overtime so i can understand the full evlution of a specific problem or a specific type of problem ?
- How to manage frictionless refresh of my understanding on solved problem ? 
- How to identify weak spot and plan triage on specific topics ?



## Overview

an AIO solution for tracking LeetCode submissions, analyzing problem-solving evolution, and receiving rule based recommendations (GenAI optional).

![System architecture](./architecture.svg)

## Services

| Service | Ports | Protocol | Description |
|---------|------|----------|-------------|
| **Submission Service** | 3000, 8000 | TCP, HTTP | Submission tracking & analytics API |
| **Intelligence Service** | HTTP, Discord | HTTP | Prompt scoring & recommendations |
| **Ingestor** | CLI | Python | ETL for LeetCode problem ingestion |

Service docs:

- Submission Service: [services/leetcode-submission-service/ARCHITECTURE.md](./services/leetcode-submission-service/ARCHITECTURE.md)
- Intelligence Service: [services/leetcode-intelligence-service/README.md](./services/leetcode-intelligence-service/README.md)


