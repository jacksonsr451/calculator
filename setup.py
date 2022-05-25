from importlib.metadata import entry_points
from setuptools import find_packages
from setuptools import setup

setup(
    name='Calculator',
    version='1.0.0',
    description='A simple calculator',
    author='Jackson Severino da Rocha',
    author_email='jacksonsr45@gmail.com',
    url='https://github.com/jacksonsr45/calculator',
    install_requires=[
        ],
    packages=find_packages(exclude=['*__tests__*', ]),
    entry_points={
            'console_scripts': [
                'calculator-cli = app.main:main'
            ]
        },
)