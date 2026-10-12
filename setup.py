from pathlib import Path
from setuptools import find_packages, setup

setup(
    name='uknowder',
    version="1.1.0",
    packages=find_packages(),
    description='Uknowder: Push Back on Patronizing Talk',
    long_description=Path(__file__).with_name("README.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    url="https://github.com/Crazy4Lamb/uknowder.skill",
    python_requires=">=3.9",
    entry_points={"console_scripts": ["uknowder=uknowder.main:main"]},
    classifiers=["Programming Language :: Python :: 3", "License :: OSI Approved :: MIT License"],
)
