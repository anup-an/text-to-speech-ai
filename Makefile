compile:
	pip-compile requirements/requirements.in --output-file=requirements/requirements.txt

install: compile
	pip install --no-cache-dir -r requirements/requirements.txt
	rm requirements/requirements.txt
