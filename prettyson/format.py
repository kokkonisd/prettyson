import json
from typing import List, Union

from prettyson.definitions import DEFAULT_INDENT, success, warning, fail


def format_files(
    files: List[str],
    indent: int = DEFAULT_INDENT,
    tabs: bool = False,
    dry_run: bool = False,
    quiet: bool = False,
) -> bool:
    """Format JSON files.

    :param files: the files to format
    :param indent: the amount of spaces to use as indentation
    :param tabs: use <indent> amount of tabs if True
    :param dry_run: do not change the contents of the files
    :param quiet: do not print any output
    :return: True if successful, False otherwise
    """
    indentation: Union[int, str] = indent if not tabs else "\t" * indent
    files_changed = []
    invalid_files = []
    for f in files:
        # Get the raw data
        with open(f, "r") as raw_file:
            raw_data = raw_file.read()

        # Check if JSON is valid
        try:
            data = json.loads(raw_data)
        except json.decoder.JSONDecodeError:
            invalid_files.append(f)
            continue

        # Format the data and append a newline at the end
        formatted_data = json.dumps(data, indent=indentation) + "\n"
        if raw_data != formatted_data:
            files_changed.append(f)
            # Overwrite file, reformatting it
            if not dry_run:
                with open(f, "w") as raw_file:
                    raw_file.write(formatted_data)

    # All good
    if not files_changed and not invalid_files:
        if not quiet:
            success("All good, no files have changed!")
        return True

    # Some invalid files were found
    if invalid_files and not quiet:
        fail(f"{len(invalid_files)} files contain invalid JSON:")
        for f in invalid_files:
            fail(f"- {f}")

    # Some incorrectly formatted files were found
    if files_changed and not quiet:
        message = "have been" if not dry_run else "would be"
        warning(f"{len(files_changed)} files {message} reformatted:")
        for f in files_changed:
            warning(f"- {f}")

    return False
