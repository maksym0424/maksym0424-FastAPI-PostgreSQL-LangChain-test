.PHONY: docker-build
docker-build:	## Build project with compose
	docker compose build

.PHONY: docker-up
docker-up:	## Run project with compose
	docker compose up --remove-orphans

.PHONY: docker-pull
docker-pull:	## Run project with compose
	docker compose pull

.PHONY: docker-down
docker-down:	## Run project with compose
	docker compose down

.PHONY: alembic-upgrade
alembic-upgrade:	## Run project with compose
	docker compose run --rm --entrypoint alembic backend upgrade head

.PHONY: alembic-revision
alembic-revision:	## Run project with compose
	docker compose run --rm --entrypoint alembic backend revision --autogenerate -m "revision"

.PHONY: alembic-downgrade
alembic-downgrade:	## Run project with compose
	docker compose run --rm --entrypoint alembic backend downgrade -1
