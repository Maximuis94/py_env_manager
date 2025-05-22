#!/usr/bin/env python
# setup.py

import setuptools
from pathlib import Path

here = Path(__file__).parent
long_description = (here / "README.md").read_text(encoding="utf-8")

setuptools.setup(
    name="py_env_manager",
    version="0.1.0",
    author="Maximuis94",
    author_email="",  # add your email here
    description="Manager for setting up and accessing environmental variables per project without exposing any values",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Maximuis94/py_env_manager",
    license="MIT",
    
    packages=[
        "py_env_manager",
        "py_env_manager.src",
    ],
    package_dir={
        "py_env_manager": ".",
        "py_env_manager.src": "src",
    },
    
    install_requires=[
        "python-dotenv>=0.19.0",
        "pyperclip>=1.8.0",
    ],
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
