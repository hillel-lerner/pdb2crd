from setuptools import setup, find_packages

setup(
    name="pdb2crd",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'pdb2crd=pdb2crd.cli:main',
        ],
    },
    author="Your Name",
    author_email="hlerner47@gmail.com",
    description="Convert PDB coordinate files to CRD format",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/hillel-lerner/pdb2crd",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)