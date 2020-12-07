import setuptools, os, pathlib

BASE_DIR = pathlib.Path(__file__).parent
README = BASE_DIR / 'README.md'
LICENSE = BASE_DIR / 'LICENSE'

setuptools.setup(
    name = "PythonicSwitch",
    version = "1.0.0,",
    author = "DrSparky-2007",
    author_email = "adityaiyer2007@gmail.com",
    description = "A pythonic way to implement switch-case",
    long_description = README.read_text(),
    long_description_content_type = "text/markdown",
    packages = setuptools.find_packages(),
    url = "https://github.com/DrSparky-2007/PythonicSwitchCase",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
