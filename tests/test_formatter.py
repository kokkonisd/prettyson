import subprocess
import os
import sys

from prettyson.format import format_files
from prettyson.definitions import color_message

TEST_DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")


def test_cli_calls():
    # Call the tool from the command line
    res = subprocess.run([sys.executable, "-m", "prettyson"])
    assert res.returncode == 2

    res = subprocess.run([sys.executable, "-m", "prettyson", "--help"])
    assert res.returncode == 0


def test_format_invalid_file(capsys):
    f = os.path.join(TEST_DATA_DIR, "invalid.json")
    expected_output = (
        f"{color_message('1 files contain invalid JSON:', color='red')}\n"
        f"{color_message(f'- {f}', color='red')}\n"
    )

    res = format_files(files=[f], dry_run=True)
    assert not res

    captured = capsys.readouterr()
    assert captured.out == expected_output


def test_format_correctly_formatted_file(capsys):
    f = os.path.join(TEST_DATA_DIR, "correct.json")
    expected_output = (
        f"{color_message('All good, no files have changed!', color='green')}\n"
    )

    res = format_files(files=[f], dry_run=True)
    assert res

    captured = capsys.readouterr()
    assert captured.out == expected_output


def test_format_incorrectly_formatted_file(capsys):
    f = os.path.join(TEST_DATA_DIR, "incorrect.json")
    expected_output = (
        f"{color_message('1 files would be reformatted:', color='yellow')}\n"
        f"{color_message(f'- {f}', color='yellow')}\n"
    )

    res = format_files(files=[f], dry_run=True)
    assert not res

    captured = capsys.readouterr()
    assert captured.out == expected_output


def test_overwrite_file(capsys):
    f = os.path.join(TEST_DATA_DIR, "incorrect_tmp.json")
    res = subprocess.run(
        [
            "cp",
            os.path.join(TEST_DATA_DIR, "incorrect.json"),
            f,
        ]
    )
    assert res.returncode == 0

    # File should be reformatted
    res = format_files(files=[f], dry_run=False)
    assert not res

    # File should now be formatted
    res = format_files(files=[f], dry_run=False)
    assert res

    expected_output = (
        f"{color_message('1 files have been reformatted:', color='yellow')}\n"
        f"{color_message(f'- {f}', color='yellow')}\n"
        f"{color_message('All good, no files have changed!', color='green')}\n"
    )
    captured = capsys.readouterr()
    assert captured.out == expected_output

    # Remove dummy file
    res = subprocess.run(["rm", f])
    assert res.returncode == 0


def test_format_correctly_formatted_2_spaces_file(capsys):
    f = os.path.join(TEST_DATA_DIR, "correct_2_spaces.json")
    expected_output = (
        f"{color_message('All good, no files have changed!', color='green')}\n"
    )

    res = format_files(files=[f], dry_run=True, indent=2)
    assert res

    captured = capsys.readouterr()
    assert captured.out == expected_output


def test_format_correctly_formatted_tabs_file(capsys):
    f = os.path.join(TEST_DATA_DIR, "correct_tabs.json")
    expected_output = (
        f"{color_message('All good, no files have changed!', color='green')}\n"
    )

    res = format_files(files=[f], dry_run=True, indent=1, tabs=True)
    assert res

    captured = capsys.readouterr()
    assert captured.out == expected_output
