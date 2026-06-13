# LeetCode Intelligence
<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/53115064-eff5-4274-bac8-5a579335febd" />

## WHY

a systematic way to handle leetcode solving to manage the entire life cycle:

- How to get immediate feedback to understand which part of the code block is wrong ? is the reason due to not adequately understanding the problem or inproficiency of the syntax ?
- How to persistently store my submissions overtime so i can understand the full evlution of a specific problem or a specific type of problem ?
- How to manage frictionless refresh of my understanding on solved problem ?
- How to identify weak spot and plan triage on specific topics ?

- Sample Experience :D on Discord
  <img width="3641" height="1910" alt="image" src="https://github.com/user-attachments/assets/1794016f-1d2a-4851-bf7c-5054fb3a1c3d" />

- Sample LLM base static check on failure Experience on Nvim
  <img width="3727" height="1848" alt="image" src="https://github.com/user-attachments/assets/8381bdd6-b4ce-47ac-8f75-84364f8ce378" />

## Overview

an AIO solution for tracking LeetCode submissions, analyzing problem-solving evolution, and receiving rule based recommendations (GenAI optional).

![System architecture](./docs/architecture/architecture-v1.svg)

D2 source: [`docs/architecture/architecture-v1.d2`](./docs/architecture/architecture-v1.d2)

All architecture docs and diagrams live under [`docs/architecture/`](./docs/architecture/README.md).

## Services

| Service                  | Ports         | Protocol        | Description                                                  |
| ------------------------ | ------------- | --------------- | ------------------------------------------------------------ |
| **Submission Service**   | 3000, 8000    | TCP, HTTP       | Submission tracking & analytics API                          |
| **Intelligence Service** | HTTP, Discord | HTTP            | Prompt scoring & recommendations                             |
| **Ingestor**             | CLI           | Python          | ETL for LeetCode problem ingestion                           |

Service docs:

- System Architecture: [docs/architecture/README.md](./docs/architecture/README.md)
- Intelligence Service: [services/leetcode-intelligence-service/README.md](./services/leetcode-intelligence-service/README.md)
