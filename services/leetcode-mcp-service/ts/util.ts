export function extractComments(code: string): string[] {
  return code
    .split("\n")
    .map((line) => line.trim())
    .filter((line) => line.startsWith("#"))
    .map((line) => line.slice(1).trim());
}

export function analyzeCommentThemes(comments: string[]): Record<string, number> {
  const themes = {
    algorithmic_thinking: 0,
    optimization: 0,
    edge_cases: 0,
    complexity_analysis: 0,
    debugging: 0,
  };

  for (const comment of comments) {
    const lower = comment.toLowerCase();
    if (["algorithm", "approach", "strategy", "method"].some((w) => lower.includes(w))) {
      themes.algorithmic_thinking += 1;
    }
    if (["optimize", "faster", "better", "improve"].some((w) => lower.includes(w))) {
      themes.optimization += 1;
    }
    if (["edge", "corner", "special", "boundary"].some((w) => lower.includes(w))) {
      themes.edge_cases += 1;
    }
    if (["time", "space", "complexity", "o(", "big o"].some((w) => lower.includes(w))) {
      themes.complexity_analysis += 1;
    }
    if (["debug", "fix", "error", "bug", "issue"].some((w) => lower.includes(w))) {
      themes.debugging += 1;
    }
  }

  return themes;
}

export function countComplexityMentions(comments: string[]): Record<string, number> {
  const counts = { time_complexity: 0, space_complexity: 0 };
  for (const comment of comments) {
    const lower = comment.toLowerCase();
    if (lower.includes("time") && (lower.includes("complexity") || lower.includes("o("))) {
      counts.time_complexity += 1;
    }
    if (lower.includes("space") && (lower.includes("complexity") || lower.includes("o("))) {
      counts.space_complexity += 1;
    }
  }
  return counts;
}

export function analyzeOverallProgression(commentEvolution: Array<Record<string, unknown>>) {
  if (commentEvolution.length === 0) {
    return {};
  }

  const firstThemes = (commentEvolution[0].comment_themes as Record<string, number>) ?? {};
  const lastThemes = (commentEvolution[commentEvolution.length - 1].comment_themes as Record<string, number>) ?? {};

  const themeDevelopment: Record<string, number> = {};
  for (const key of Object.keys(firstThemes)) {
    themeDevelopment[key] = (lastThemes[key] ?? 0) - (firstThemes[key] ?? 0);
  }

  const commentDensityTrend = commentEvolution.map((item) => Number(item.comments_count ?? 0));
  const complexityAwarenessGrowth = commentEvolution.reduce((sum, item) => {
    const mentions = (item.complexity_mentions as Record<string, number>) ?? {};
    return sum + (mentions.time_complexity ?? 0) + (mentions.space_complexity ?? 0);
  }, 0);

  return {
    theme_development: themeDevelopment,
    comment_density_trend: commentDensityTrend,
    complexity_awareness_growth: complexityAwarenessGrowth,
  };
}
