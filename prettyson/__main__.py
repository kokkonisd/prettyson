#!/usr/bin/env python3

import argparse
import sys

from prettyson.definitions import DEFAULT_INDENT
from prettyson.format import format_files


def main():
    arg_parser = argparse.ArgumentParser(
        prog="prettyson",
        description="Check that JSON files are properly formatted.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    arg_parser.add_argument(
        "-d",
        "--dry-run",
        help="check files without modifying them",
        action="store_true",
    )
    arg_parser.add_argument(
        "-q",
        "--quiet",
        help="do not output any messages",
        action="store_true",
    )
    indentation_args = arg_parser.add_mutually_exclusive_group()
    indentation_args.add_argument(
        "-i",
        "--indent",
        help="number of spaces to indent by",
        default=DEFAULT_INDENT,
        type=int,
    )
    indentation_args.add_argument(
        "-t",
        "--use-tabs",
        help="use tabs for indentation",
        action="store_true",
    )
    arg_parser.add_argument("files", help="the JSON files to format", nargs="+")
    args = arg_parser.parse_args()

    res = format_files(
        files=args.files,
        indent=args.indent if not args.use_tabs else 1,
        tabs=args.use_tabs,
        dry_run=args.dry_run,
        quiet=args.quiet,
    )
    return 0 if res else 1


if __name__ == "__main__":
    sys.exit(main())
