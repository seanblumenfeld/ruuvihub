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

.PHONY: services
watch-sensor-events:
	python services/ruuvitags/watch_sensor_events.py
