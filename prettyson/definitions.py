__version_info__ = ("0", "0", "1")
__version__ = ".".join(__version_info__)
__author__ = "Dimitri Kokkonis"

# Default indentation level (spaces)
DEFAULT_INDENT = 4

# A mapping of colors to terminal color codes
TERMINAL_COLORS = {
    "green": "\033[32m{}\033[0m",
    "yellow": "\033[33m{}\033[0m",
    "red": "\033[31m{}\033[0m",
}


def color_message(message: str, color: str) -> str:
    """Color a message.

    :param message: the message to color
    :param color: the color to use
    :return: a colored message string
    """
    if color not in TERMINAL_COLORS:
        return message

    return TERMINAL_COLORS[color].format(message)


def success(message: str, end: str = "\n") -> None:
    r"""Print a success message.

    :param message: the success message to print
    :param end: the end character/string ('\n' by default)
    """
    print(color_message(message=message, color="green"), end=end)


def warning(message: str, end: str = "\n") -> None:
    r"""Print a warning message.

    :param message: the warning message to print
    :param end: the end character/string ('\n' by default)
    """
    print(color_message(message=message, color="yellow"), end=end)


def fail(message: str, end: str = "\n") -> None:
    r"""Print a fail message.

    :param message: the fail message to print
    :param end: the end character/string ('\n' by default)
    """
    print(color_message(message=message, color="red"), end=end)
