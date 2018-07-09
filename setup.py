from setuptools import setup

setup(
    name='gitcheckout',
    packages=['gitcheckout'],
    version='0.2',
    include_package_data=True,
    description='A utility to reduce the amount of time it takes to checkout git branches!',
    author='Jacob Smith',
    author_email='jacob.smith@unb.ca',
    url='http://github.com/jacsmith21/gitcheckout',
    install_requires=[
        'GitPython',
        'inquirer', 'click'
    ],
    entry_points={
        'console_scripts': ['gitcheckout=gitcheckout.main:main']
    }
)

