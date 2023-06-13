from setuptools import setup, find_packages

setup(
    name='dovydas_calculator',
    version='1.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'dovydas_calculator = dovydas_calculator.calculator:main',
        ],
    },
    install_requires=[
        'pytest',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
