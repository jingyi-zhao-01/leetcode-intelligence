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

## Problem Graph 

```bash
poetry run problem-graph --solved 
# This will generate graph with interrelations only on solved questions, auto convered into svg 
# for problem that is solved, it will color it based on acception rate 
# for every problem, it will have a indication whether it is easy, medium, hard 
```

```bash 
poetry run problem-graph --include-tags "Array" "Two-pointers" 
# This will generate graph with interrelations on ALL problems that contain at least 1 of the tags, while preservering the output from poetry run problem-graph --sovled 
```

```bash
poetry run problem-graph --filter-tags "Array" "Two-pointers"
# This will generate graph with interrelations on ALL problems that must contain all tags, while preserving the output from poetry run problem-graph --solved
```