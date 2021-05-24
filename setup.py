import setuptools

from your_cli_tool.definitions import __version__, __author__

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="your_cli_tool",
    version=__version__,
    author=__author__,
    author_email="john.doe@gmail.com",
    description="A simple Python-based CLI tool template",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://link/to/repo",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    install_requires=[],
    package_data={"your_cli_tool": []},
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "your_cli_tool = your_cli_tool.__main__:your_cli_tool_main",
        ],
    },
    python_requires=">=3.6",
)
