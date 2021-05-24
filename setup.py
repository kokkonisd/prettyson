import setuptools

from prettyson.definitions import __version__, __author__

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="prettyson",
    version=__version__,
    author=__author__,
    author_email="kokkonisd@gmail.com",
    description="A Python-based JSON file formatter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kokkonisd/prettyson",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    install_requires=[],
    package_data={"prettyson": []},
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "prettyson = prettyson.__main__:main",
        ],
    },
    python_requires=">=3.6",
)
