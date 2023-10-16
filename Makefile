SHELL = /bin/bash
VENV_NAME = venv
PYTHON_VERSION := $(shell cat .python-version)

clean_py:
	@find . -iname "*.pyc" -delete
	@echo "Cleaned *.pyc files"

python: venv

virtualenv:
	@if [ ! `pip freeze | grep virtualenv` ]; then pip install virtualenv; else echo "Virtualenv pip is already installed"; fi

venv: virtualenv
	virtualenv --python $$(cat .python-version) ${VENV_NAME}
	@${VENV_NAME}/bin/pip install --upgrade pip
	@${VENV_NAME}/bin/pip install --upgrade -r requirements.txt
	@${VENV_NAME}/bin/pip install --upgrade -r requirements-test.txt
	@echo "Installed Python dependencies"
	@touch ${VENV_NAME}/bin/activate
	@echo "virtualenv prepared, please run 'source ${VENV_NAME}/bin/activate' if you wish to use it in your current shell"

test: clean_py python
	@echo "Running tests..."
	@. ${VENV_NAME}/bin/activate && pytest tests

docker-build:
	docker build -t eegist:latest-python${PYTHON_VERSION} .

docker-run:
	docker run --rm -p 8080:5000 eegist:latest-python${PYTHON_VERSION}