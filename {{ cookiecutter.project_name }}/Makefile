#################################################################################
# GLOBALS                                                                       #
#################################################################################

## Project variables
PROJECT_NAME = {{ cookiecutter.package_slug }}
PYTHON_INTERPRETER = {{ cookiecutter.python_interpreter }}

## Environment variables
NOTEBOOK_HOME = /home/jovyan
IMAGE_NAME = {{ cookiecutter.docker_image_name }}
CONTAINER_NAME = {{ cookiecutter.docker_container_name }}
CONTAINER_PORT = {{ cookiecutter.docker_container_port }}
CONTAINER_RUNNING := $(shell docker inspect -f '{% raw %}{{.State.Running}}{% endraw %}' $(CONTAINER_NAME))

## Command variables
COMMAND = {{ cookiecutter.application_cli_name }}
DATA_URL = https://www.stats.govt.nz/assets/Uploads/International-travel/International-travel-June-2019/Download-data/new-zealand-resident-arrivals-by-area-of-residence-csv.csv
DATA_LOCATION = /home/jovyan/data/nz-population.csv

#################################################################################
# COMMANDS                                                                      #
#################################################################################

## Install Python Dependencies
install:
	@$(PYTHON_INTERPRETER) -m pip install -U pip setuptools wheel
	@$(PYTHON_INTERPRETER) -m pip install -r requirements.txt

## Upgrade Python Dependencies
upgrade:
	@$(PYTHON_INTERPRETER) -m pip install --upgrade -r requirements.txt

## Package project
package:
	@$(PYTHON_INTERPRETER) -m pip install -e .

## Build environment
environment-build:
	@rm -rf $(PROJECT_NAME).egg-info
	@mkdir -p $(PROJECT_NAME).egg-info
	@chmod -R 777 $(PROJECT_NAME).egg-info
	@chmod -R 777 data
	@chmod -R 777 notebooks
	@chmod -R 777 scripts
	@docker build -t $(IMAGE_NAME) . && echo "\nEnvironment is built! A Docker image was created: $(IMAGE_NAME)"

## Start environment
environment-start:
ifeq ($(CONTAINER_RUNNING),true)
	@echo "Environment is already running and notebooks interface is available at http://localhost:$(CONTAINER_PORT)."
else
	@docker run --rm -d -v $(shell pwd):/data \
 		-h $(PROJECT_NAME) \
 		-v $(shell pwd)/notebooks:$(NOTEBOOK_HOME)/notebooks \
 		-v $(shell pwd)/scripts:$(NOTEBOOK_HOME)/scripts \
 		-v $(shell pwd)/data:$(NOTEBOOK_HOME)/data \
 		-p $(CONTAINER_PORT):8888 --name $(CONTAINER_NAME) $(IMAGE_NAME) && echo "Environment is running!\nNotebooks interface is available at http://localhost:$(CONTAINER_PORT)"
endif

## Shutdown environment
environment-stop:
ifeq ($(CONTAINER_RUNNING),true)
	@docker rm -f $(CONTAINER_NAME) && echo "Environment has shutdown!"
else
	@echo "Environment is not running."
endif

## Restart environment
environment-restart:
ifeq ($(CONTAINER_RUNNING),true)
	@docker restart $(CONTAINER_NAME) && echo "Environment has restarted!"
else
	@echo "Environment is not running."
endif

## Load environment command line interface
environment-shell:
ifeq ($(CONTAINER_RUNNING),true)
	@docker exec -it -w $(NOTEBOOK_HOME) $(CONTAINER_NAME) bash
else
	@echo "Environment is not running."
endif

## Load data intio environment
environment-data:
ifeq ($(CONTAINER_RUNNING),true)
	@docker exec -it -w $(NOTEBOOK_HOME) $(CONTAINER_NAME) $(COMMAND) data $(DATA_URL) $(DATA_LOCATION)
else
	@echo "Environment is not running."
endif

## Environment status
environment-status:
ifeq ($(CONTAINER_RUNNING),true)
	@echo "Notebooks interface is available at http://localhost:$(CONTAINER_PORT)"
else
	@echo "Environment is not running."
endif

## Delete all compiled Python files
clean:
	@find . -type f -name "*.py[co]" -delete
	@find . -type d -name "__pycache__" -delete
	@find "docs/build" -delete

## Check code styling with Flake8
lint:
ifeq ($(CONTAINER_RUNNING),true)
	@docker exec -it -w /data $(CONTAINER_NAME) flake8
else
	@echo "Environment is not running."
endif

## Run unit tests
test:
ifeq ($(CONTAINER_RUNNING),true)
	@docker exec -it -w /data $(CONTAINER_NAME) coverage run --source=$(PROJECT_NAME) -m pytest
else
	@echo "Environment is not running."
endif

## Show code coverage
coverage:
ifeq ($(CONTAINER_RUNNING),true)
	@docker exec -it -w /data $(CONTAINER_NAME) coverage report -m
else
	@echo "Environment is not running."
endif