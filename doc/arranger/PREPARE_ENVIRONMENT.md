# Prepare Arranger environment

## NB: all the commands are to be run within the Arranger repo's root directory

## Table of contents

* [Prerequisites](#prerequisites)
* [Setup](#setup)
* [Known limitations](#known-limitations)
* [Maintainers](#maintainers)

## Prerequisites <div id='prerequisites'/>

1. [Pyenv](https://github.com/pyenv/pyenv) installed.
2. [Pipenv](https://pypi.org/project/pipenv/) installed.
3. [Docker](https://www.docker.com) running.

## Setup <div id='setup'/>


1. Create Python virtual environment (where '3.12' is your python3 version, see Pipfile for the details):

   ```shell
   $ pyenv install 3.12
   $ pyenv local 3.12
   $ eval "$(pyenv init --path)"
   $ pipenv --python 3.12
   ```

2. Enter the virtual environment's context:

   ```shell
   $ pipenv shell
   ```

3. Install pyInvoke and some related libs:
   ```shell
   $ pip install -r requirements.txt
   ```
4. (**OPTIONAL**) Download all dependencies and install all arranger_automation packages (for some IDEs autocompletion
   to
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
8. Observe the list of existing Invoke tasks:

   ```shell
   (arranger) root@cli#  inv -l
   Available tasks:

   local.autocorrect-black      >> Run autocorrection on Python files (using Black).
   local.cleanup-repo           >> Clean the environment from within the Dockerized CLI.
   local.container.build        >> Build the Dockerized environment.
   local.container.clean-repo   >> Clean environment from within the dockerized CLI.
   local.container.enter        >> Enter the Arranger service container shell.
   local.container.run          >> Run the Dockerized environment.
   local.container.stop         >> Stop the Dockerized environment.
   python3.build                >> Build the specified Python package.
   python3.build-and-install    >> Build the specified Python package, install it, and clean up the repository.
   python3.install              >> Install the specified Python package.
   spec.python                  >> Run specifications for the specified Python package.
   ...
   ```

## Known limitations <div id='known-limitations'/>

This setup and all associated automation tasks were tested on macOS; however, they should also function on Linux, with
only minor adjustments needed for Windows.

