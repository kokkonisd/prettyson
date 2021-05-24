# Template for CLI tools in Python

This is a basic template for a CLI tool made with Python. It contains all the necessary
tools for unit testing and code coverage.

## Dependencies

You will need to install the packages specified in `requirements.txt`. You can do that
by running:

```text
$ python3 -m pip install -r requirements.txt
```

## Setup

Once the [dependencies](#dependencies) are installed, you can set up your environment
locally by starting with the pre-commit checks. In the repo of your project, run:

```text
$ pre-commit install
```

This should install a pre-commit hook that will check that the files of your project
are correctly formatted before any commit.

Once that is done, you should perform the following changes:

- Change the directory `your_cli_tool` to the name of your tool
- Change the name in `your_cli_tool/__init__.py` to the name of your tool
- Change the name of the `your_cli_tool_main` function in `your_cli_tool/__main__.py`
  to the name of your CLI tool (plus `_main`, probably)
- Change the `__author__` in `your_cli_tool/definitions.py`
- Replace `your_cli_tool` with the name of the module (the `your_cli_tool` directory
  you renamed just before) in `tox.ini`
- Replace the placeholder info with your real info in `setup.py`
- Replace the `tests/test_placeholder.py` file with real tests

Once that is all done, then you can start using your project! To test and measure code
coverage, you can run:

```text
$ tox
```
