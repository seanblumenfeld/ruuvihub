.PHONY: help
help:
	@echo "Available commands:"
	@echo "\tclean - stop the running containers and remove pycache folders"
	@echo "\tcreate-env-files - Create local env files"
	@echo "\tbuild - build application"
	@echo "\tup - start program"
	@echo "\tup-detached - start program in background"
	@echo "\tdown - stop program"

.PHONY: clean
clean:
	-find . -type d -name '__pycache__' -exec rm -rf {} ';'

# TODO: remove?
.PHONY: create-env-file
create-env-files:
ifeq ("$(wildcard .dev.env)","")
	@echo "POSTGRES_DB=app" > .env
	@echo "POSTGRES_USER=app" >> .env
	@echo "POSTGRES_PASSWORD=CHANGEME" >> .env
	@echo "POSTGRES_HOST=postgres" >> .env
	@echo "POSTGRES_DB=app" >> .env
endif
