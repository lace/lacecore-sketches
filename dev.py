#!/usr/bin/env python

import os
import click
from executor import execute


def python_source_files():
    import glob

    include_paths = glob.glob("*.py") + glob.glob("lacecore/*.py") + ["doc/"]

    # TODO: Use flake8; argh.
    exclude_paths = ["lacecore/__init__.py"]

    return [x for x in include_paths if x not in exclude_paths]


@click.group()
def cli():
    pass


@cli.command()
def init():
    execute("pip install --upgrade -r requirements_dev.txt")


@cli.command()
def test():
    execute("nose2")


@cli.command()
def test_both():
    execute("python2 -m nose2")
    execute("python3 -m nose2")


@cli.command()
def lint():
    execute("pyflakes", *python_source_files())


@cli.command()
def black():
    execute("black", *python_source_files())


@cli.command()
def black_check():
    execute("black", "--check", *python_source_files())


@cli.command()
def doc():
    execute("rm -rf build/ doc/build/ doc/api/")
    execute("sphinx-build -b singlehtml doc doc/build")


@cli.command()
def doc_open():
    execute("open doc/build/index.html")


@cli.command()
def upload():
    execute("rm -rf dist/")
    execute("python setup.py sdist")
    execute("twine upload dist/*")


if __name__ == "__main__":
    os.chdir(os.path.abspath(os.path.dirname(__file__)))
    cli()
