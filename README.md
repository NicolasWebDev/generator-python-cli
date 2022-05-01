# Generator Python CLI

A [copier](https://github.com/copier-org/copier) generator for creating cli tools with python.

## USAGE

Install the dependencies: `poetry install`
Generate a project: `poetry run task copier <path_of_new_project>`
Run the tests: `poetry run task test`

## REMARKS

I use the internal `_folder_name`, which is set to the basename of the destination passed when generating the template, as the project name.

## TODO

- use the latest version of python automatically (maybe looking at https://github.com/pawamoy/copier-poetry)
- add more tools (mypy, pylint)
- if prompted, create a project of the same name (but with "-" instead of "−") on my github, push to it
- install the package in development mode using `sudo pip install -e .` or the equivalent setuptools command
- fix the ptw notifications icons so that it may work for other people as well (try to include an svg directly somehow)
- update to python 3.10 (and document the process to update both this project dependencies and the created project dependencies as well)
