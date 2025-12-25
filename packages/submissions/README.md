# LeetCode Submissions Package

A package for managing LeetCode submissions, including tracking, statistics, and problem graph analysis.

## Features

- **Submission Server**: Track and save LeetCode submissions with timer functionality
- **Statistics**: Analyze submission patterns, success rates, and time spent
- **Problem Graph**: Visualize relationships between problems based on tags and patterns

## Installation

```bash
poetry install
```

## Usage

### Start the Submission Server

```bash
poetry run submission-server
```

### View Statistics

```bash
poetry run submission-stats
```

### Generate Problem Graph

```bash
poetry run problem-graph
```

## Development

```bash
poetry install --with dev
poetry run pytest
```
