"""
NaMIx setup script.

See license in LICENSE
"""

from setuptools import setup


def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name="namix",
    version="0.2.0",
    author="Serra Yosmaoglu",
    author_email="Serra.Yosmaoglu@dlr.de",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/DLR-VF/NaMIx",
    packages=["namix"],
    include_package_data=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: GIS",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: Eclipse Public License 2.0 (EPL-2.0)",
    ],
)
