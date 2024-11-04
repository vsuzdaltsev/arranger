# Prepare arranger_cli environment

## NB: all the commands are run within the arranger repo root directory
## Table of contents

* [About](#about)
* [Prerequisites](#prerequisites)
* [Setup](#setup)
* [Known limitations](#known-limitations)
* [Maintainers](#maintainers)

## About <div id='about'/>

Automation tasks (command line interface) for orchestrating Eusy application instances.

## Prerequisites <div id='prerequisites'/>

1. [Pyenv](https://github.com/pyenv/pyenv) installed.
2. [Pipenv](https://pypi.org/project/pipenv/) installed.
3. [Docker](https://www.docker.com) running.

## Setup <div id='setup'/>

1. Create Python virtual environment (where '3.9.2' is your installed python3 version, see Pipfile for details):

   ```shell
   $ pyenv install 3.9.2
   $ pyenv local 3.9.2
   $ eval "$(pyenv init --path)"
   $ pipenv --python 3.9.2
   ```

2. Enter the virtual environment's context:

   ```shell
   $ pipenv shell
   ```

3. Install pyInvoke and some related libs:

   ```shell
   $ pip install -r requirements.txt
   ```

4. (**OPTIONAL**) Download all dependencies and install all eusy_automation packages (for some IDEs autocompletion to
   work
   primarily):

   ```shell
   $ pipenv sync
   $ pipenv sync -d
   $ inv python3.build-and-install
   ```

5. List existing invoke tasks:

   ```shell
   $ inv -l
   ```

6. Build container:

   ```shell
   $ inv local.container.build
   ```

7. Run & enter container:

   ```shell
   $ inv local.container.run
   ```

## Known limitations <div id='known-limitations'/>

This setup and all the automation tasks were tested under macOS, but they should also work under Linux (and with obvious
minor changes under Windows as well).

## Maintainers <div id='maintainers'/>

* [vsevolod.suzdaltsev@gmail.com](mailto:vsevolod.suzdaltsev@gmail.com?subject=prepare-meta-cli)
