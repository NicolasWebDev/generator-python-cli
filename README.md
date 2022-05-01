# Generator Python CLI

A [copier](https://github.com/copier-org/copier) generator for creating cli tools with python.

## USAGE

Install the dependencies: `poetry install`

Run the tests: `poetry run task test`
*Note:* the tests are run taking into account non-committed files as well as committed files.

Generate a project: `poetry run task copier <path_of_new_project>`
*Note:* when generating a project, only committed files are taken into account, so I need to create dev branches and commit there to try out my changes.

## REMARKS

I use the internal `_folder_name`, which is set to the basename of the destination passed when generating the template, as the project name.

## UPDATE PYTHON VERSION IN GENERATED PROJECTS

I just have to change the python version in `template/pyproject.toml.tmpl`.

## TODO

- use the latest version of python automatically (maybe looking at https://github.com/pawamoy/copier-poetry)
- add more tools (mypy, pylint)
- if prompted, create a project of the same name (but with "-" instead of "−") on my github, push to it
- install the package in development mode using `sudo pip install -e .` or the equivalent setuptools command
- fix the ptw notifications icons so that it may work for other people as well (try to include an svg directly somehow)
- ~~update to python 3.10 (and document the process to update both this project dependencies and the created project dependencies as well)~~
    - I cannot update to python 3.10 in my copier pyproject.toml, because it is not supported by copier 5.1
