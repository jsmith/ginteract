from setuptools import setup

with open('README.md') as fp:
    readme = fp.read()

setup(
    name='ginteract',
    packages=['ginteract'],
    version='0.2.1',
    description='An interactive Git client!',
    long_description=readme,
    author='Jacob Smith',
    author_email='jacob.smith@unb.ca',
    url='http://github.com/jacsmith21/ginteract',
    install_requires=[
        'GitPython',
        'inquirer',
        'click'
    ],
    entry_points={
        'console_scripts': ['ginteract=ginteract.main:main']
    }
)

