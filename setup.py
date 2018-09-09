from setuptools import setup

with open('README.md') as fp:
    readme = fp.read()

setup(
    name='ginteract',
    packages=['ginteract'],
    version='0.2.2',
    description='An interactive Git client!',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Jacob Smith',
    author_email='jacob.smith@unb.ca',
    url='https://github.com/jsmith/ginteract',
    license='MIT',
    install_requires=[
        'GitPython',
        'inquirer',
        'click'
    ],
    entry_points={
        'console_scripts': ['ginteract=ginteract.main:main']
    }
)

