# デフォルトのfeatureファイル
DEFAULT_FEATURE ?= default

# featureを実行
# デフォルトではdefaultフォルダのfeatureを実行
# 例: make run
# 特定のfeatureを実行
# 例: make run feature=sample
.PHONY: run
run:
ifndef feature
	@echo "Running feature: $(DEFAULT_FEATURE)"
	bash scripts/run.sh $(DEFAULT_FEATURE)
endif
	@echo "Running feature: $(feature)"
	bash scripts/run.sh $(feature)

.PHONY: setup
setup:
	@echo "Setup..."
	bash scripts/setup.sh

.PHONY: serve
serve:
	@echo "Serving..."
	sh scripts/serve.sh

.PHONY: test
test:
	@echo "Testing..."
	bash scripts/test.sh
