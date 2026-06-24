UV ?= uv
SCRIPT ?= submission-ast-cluster-poc
BENCHMARK_SOURCE ?= corpus
RESULT_SOURCE ?= db
CORPUS_DIR ?= benchmark/fixtures/corpus
RUN_ID ?= $(shell date -u +%Y%m%dT%H%M%SZ)
BENCHMARK_LIMIT ?= 4000
RESULT_LIMIT ?= 500
PERSISTENT_SUFFIX ?= .json
OUT_DIR ?= artifacts
BENCHMARK_OUT_PREFIX ?= benchmark
RESULT_OUT_PREFIX ?= my-data
COMMON_ARGS ?=

.PHONY: help benchmark result compile

help:
	@echo "Available targets:"
	@echo "  make benchmark    # run clusterer on local corpus fixtures"
	@echo "  make result       # run clusterer on Neon db submissions"
	@echo "  make compile      # compile project Python entrypoints"
	@echo "Common vars:"
	@echo "  BENCHMARK_LIMIT=<n>      # number of items for benchmark (default: 500)"
	@echo "  RESULT_LIMIT=<n>          # number of items for db run (default: 500)"
	@echo "  CORPUS_DIR=<path>        # corpus directory for benchmark mode"
	@echo "  COMMON_ARGS='--label ...' # pass extra args e.g. --slug xxx --limit ..."

benchmark:
	$(UV) run $(SCRIPT) \
		--source $(BENCHMARK_SOURCE) \
		--corpus-dir $(CORPUS_DIR) \
		--limit $(BENCHMARK_LIMIT) \
		--no-label \
		--out $(OUT_DIR)/$(BENCHMARK_OUT_PREFIX)-$(RUN_ID)$(PERSISTENT_SUFFIX) \
		$(COMMON_ARGS)

result:
	$(UV) run $(SCRIPT) \
		--source $(RESULT_SOURCE) \
		--limit $(RESULT_LIMIT) \
		--out $(OUT_DIR)/$(RESULT_OUT_PREFIX)-$(RUN_ID)$(PERSISTENT_SUFFIX) \
		$(COMMON_ARGS)

compile:
	$(UV) run python -m py_compile src/submission_ast_cluster_poc.py src/submission_ast_cluster_inputs.py
