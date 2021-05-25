import subprocess
import os
import sys

from prettyson.definitions import __version__

TEST_DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")


def test_empty_cli_calls():
    res = subprocess.run([sys.executable, "-m", "prettyson"])
    assert res.returncode == 2

    res = subprocess.run([sys.executable, "-m", "prettyson", "--help"])
    assert res.returncode == 0


def test_version_cli_call():
    res = subprocess.run([sys.executable, "-m", "prettyson", "-v"], capture_output=True)
    assert res.returncode == 0

    assert res.stdout.decode("ascii") == f"prettyson {__version__}\n"


def test_correctly_formatted_cli_call():
    f = os.path.join(TEST_DATA_DIR, "correct.json")
    res = subprocess.run([sys.executable, "-m", "prettyson", "-d", f])
    assert res.returncode == 0


def test_incorrectly_formatted_cli_call():
    f = os.path.join(TEST_DATA_DIR, "incorrect.json")
    res = subprocess.run([sys.executable, "-m", "prettyson", "-d", f])
    assert res.returncode == 1
