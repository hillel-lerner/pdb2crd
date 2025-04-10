from setuptools import setup, find_packages

setup(
    name="pdb2crd",
    version="1.0.0",
    packages=find_packages(),
    entry_points={
        'console_scripts': ['pdb2crd=pdb2crd.cli:main'],
    },
)