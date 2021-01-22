from os.path import abspath, join, dirname

from setuptools import setup, find_packages

requirements = list(open(abspath(join(dirname(__file__), 'requirements.txt'))))
setup(
    name='{{cookiecutter.project_slug}}',
    version='{{cookiecutter.version}}',
    packages=find_packages(),
    # add dependencies here.
    install_requires=requirements,
)
