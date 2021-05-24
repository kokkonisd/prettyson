import subprocess
import sys

from your_cli_tool.__main__ import your_cli_tool_main
from your_cli_tool.definitions import __version__


def test_tool_main():
    # Call your tool's main function
    res = your_cli_tool_main()
    assert res == None


def test_tool_version():
    # Check the tool's version
    assert __version__ == "0.0.1"


def test_cli_calls():
    # Call the tool from the command line
    res = subprocess.run([sys.executable, "-m", "your_cli_tool"])

    assert res.returncode == 0
