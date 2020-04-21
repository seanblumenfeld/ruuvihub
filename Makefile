.PHONY: help
help:
	@echo "Available commands:"
	@echo "\tclean - stop the running containers and remove pycache folders"
	@echo "\tcreate-env-files - Create local env files"
	@echo "\tbuild - build application"
	@echo "\tup - start program"
	@echo "\tup-detached - start program in background"
	@echo "\tdown - stop program"
	@echo "\ttest - run tests"
	@echo "\tlint - run lint"

.PHONY: clean
clean:
	-find . -type d -name '__pycache__' -exec rm -rf {} ';'

.PHONY: create-env-file
create-env-files:
ifeq ("$(wildcard .env)","")
	@echo "POSTGRES_DB=app" > .env
	@echo "POSTGRES_USER=app" >> .env
	@echo "POSTGRES_PASSWORD=CHANGEME" >> .env
	@echo "POSTGRES_HOST=postgres" >> .env
	@echo "POSTGRES_DB=app" >> .env
endif

.PHONY: build
build: create-env-files clean
	docker-compose build

.PHONY: up
up: build
	@$(MAKE) down
	docker-compose up

.PHONY: up-detached
up-detached: build
	@$(MAKE) down
	docker-compose up -d
	@echo "TODO: implement a service readiness check here"
	@echo "sleeping for 7 seconds..."
	@sleep 7

.PHONY: down
down:
	docker-compose down

.PHONY: make-migrations
make-migrations:
	docker-compose run web bash -c "python manage.py makemigrations"

.PHONY: test
test:
	docker-compose run web bash -c "pytest"

.PHONY: lint
lint:
	docker-compose run web flake8
