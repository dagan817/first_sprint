from setuptools import setup, find_packages

setup(
    name='dovydas_calculator',
    version='1.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'dovydas_calculator = calculator.calculator:main'
        ]
    },
    install_requires=[],
    author='Dovydas A',
    description='A simple calculator by Dovydas A',
    long_description='A simple calculator program with basic arithmetic operations.',
    url='https://github.com/dagan817/first_sprint/tree/main/calculator',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
