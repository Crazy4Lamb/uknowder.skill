from setuptools import setup, find_packages
import os

long_description = ""
readme_path = os.path.join(os.path.dirname(__file__), "README.md")
if os.path.exists(readme_path):
    with open(readme_path, encoding="utf-8") as f:
        long_description = f.read()

setup(
    name="uknowder",
    version="1.0.0",
    packages=find_packages(),
    author="Your Name",
    description="你知道个der · 爹味暴躁反击技能",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Crazy4Lamb/uknowder",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)