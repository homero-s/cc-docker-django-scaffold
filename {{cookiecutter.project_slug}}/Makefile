# ---- Config (override with: make up PROFILES="dev db") -----------------------
DOCKER_COMPOSE ?= docker compose
PROFILES        ?= dev             # common: dev | prod | "dev db" | "prod db proxy"
WEB             ?= web
DB              ?= db
ENV_FILE        ?= .env
PORT            ?= 8000

# Compose command with profiles applied
CMD = $(DOCKER_COMPOSE) $(foreach p,$(PROFILES),--profile $(p))

# Colors
CINFO = \033[1;34m
CEND  = \033[0m

.PHONY: help init up up-build up-prod stop restart down ps logs shell manage \
        migrate makemigrations superuser collectstatic test test-ci \
        fmt lint env-copy dbshell db-backup db-restore health

help:
	@echo "$(CINFO)Targets$(CEND)"
	@echo "  make init                 - Bootstrap with init.sh (creates .env, builds, migrates, optional superuser)"
	@echo "  make up [PROFILES=...]    - Start stack (default PROFILES=\"$(PROFILES)\")"
	@echo "  make up-build             - Start with rebuild"
	@echo "  make up-prod              - Start production stack (PROFILES=prod [db proxy])"
	@echo "  make stop|restart|down    - Stop / restart / stop & remove"
	@echo "  make ps|logs              - Show services / follow logs"
	@echo "  make shell                - Shell into $(WEB)"
	@echo "  make manage ARGS='...'    - Run manage.py command in $(WEB)"
	@echo "  make migrate|makemigrations|superuser|collectstatic|test"
	@echo "  make fmt|lint             - Run pre-commit (host) across repo"
	@echo "  make env-copy             - Copy .env.example -> .env if missing"
	@echo "  make dbshell              - psql into Postgres (if db profile)"
	@echo "  make db-backup FILE=...   - pg_dump to FILE (if db profile)"
	@echo "  make db-restore FILE=...  - restore FILE into current DB (if db profile)"
	@echo "  make health               - curl healthcheck http://127.0.0.1:$(PORT)/healthz/"

# --- Bootstrap ---------------------------------------------------------------
init:
	@test -x ./init.sh || (echo "init.sh not found or not executable" && exit 1)
	./init.sh --noninteractive --profiles "$(PROFILES)"

env-copy:
	@[ -f $(ENV_FILE) ] && echo "$(ENV_FILE) already exists" || (cp .env.example $(ENV_FILE) && echo "Created $(ENV_FILE)")

# --- Lifecycle ---------------------------------------------------------------
up:
	$(CMD) up -d

up-build:
	$(CMD) up -d --build

# Uses recursive make so PROFILES override applies only to this target
up-prod:
	@$(MAKE) up-build PROFILES="prod db proxy"

stop:
	$(CMD) stop

restart:
	$(CMD) restart

down:
	$(CMD) down -v

ps:
	$(CMD) ps

logs:
	$(CMD) logs -f --tail=200

# --- Development ergonomics --------------------------------------------------
shell:
	$(CMD) exec -it $(WEB) bash

manage:
	@if [ -z "$(ARGS)" ]; then echo "Usage: make manage ARGS='createsuperuser'"; exit 2; fi
	$(CMD) exec -T $(WEB) python manage.py $(ARGS)

migrate:
	$(CMD) exec -T $(WEB) python manage.py migrate

makemigrations:
	$(CMD) exec -T $(WEB) python manage.py makemigrations

superuser:
	# Interactive superuser; for CI, set DJANGO_SUPERUSER_* in env and call init.sh
	-$(CMD) exec -it $(WEB) python manage.py createsuperuser

collectstatic:
	$(CMD) exec -T $(WEB) python manage.py collectstatic --noinput

test:
	$(CMD) exec -T $(WEB) python manage.py test

# CI-friendly: fail fast, no TTY
test-ci:
	$(CMD) exec -T $(WEB) python manage.py test -v 2

fmt:
	# Run formatting hooks on host; install with: pip install pre-commit && pre-commit install
	-pre-commit run --all-files

lint:
	-pre-commit run --all-files

health:
	@which curl >/dev/null 2>&1 || (echo "curl not installed"; exit 1)
	@curl -fsS "http://127.0.0.1:$(PORT)/healthz/" && echo "\nOK" || (echo "\nNot healthy yet"; exit 1)

# --- Database helpers (Postgres profile) -------------------------------------
dbshell:
	@if ! $(CMD) ps $(DB) >/dev/null 2>&1; then echo "No '$(DB)' service (enable db profile)"; exit 2; fi
	$(CMD) exec -it $(DB) psql -U $$POSTGRES_USER -d $$POSTGRES_DB

# Usage: make db-backup FILE=backup.sql
db-backup:
	@if [ -z "$(FILE)" ]; then echo "Usage: make db-backup FILE=backup.sql"; exit 2; fi
	@if ! $(CMD) ps $(DB) >/dev/null 2>&1; then echo "No '$(DB)' service (enable db profile)"; exit 2; fi
	# Expand $$POSTGRES_* inside the container; stream dump to host file
	$(CMD) exec -T $(DB) sh -lc 'pg_dump -U "$$POSTGRES_USER" "$$POSTGRES_DB"' > "$(FILE)"
	@echo "Wrote $(FILE)"

# Usage: make db-restore FILE=backup.sql
db-restore:
	@if [ -z "$(FILE)" ]; then echo "Usage: make db-restore FILE=backup.sql"; exit 2; fi
	@if ! $(CMD) ps $(DB) >/devnull 2>&1; then echo "No '$(DB)' service (enable db profile)"; exit 2; fi
	# Feed host file into psql inside the container
	cat "$(FILE)" | $(CMD) exec -T $(DB) sh -lc 'psql -U "$$POSTGRES_USER" "$$POSTGRES_DB"'
