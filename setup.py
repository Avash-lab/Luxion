"""
Setup script for Luxion Voice Assistant
"""

from setuptools import setup, find_packages
import os

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read().splitlines()

setup(
    name="luxion-assistant",
    version="1.0.0",
    author="Tej",
    author_email="",
    description="Intelligent Voice Assistant for Desktop",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/luxion",
    packages=find_packages(),
    package_data={
        '': ['*.db', '*.ico', '*.mp3', '*.css', '*.js', '*.html'],
    },
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Desktop Environment",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "luxion=luxion:main",
        ],
        "gui_scripts": [
            "luxion-gui=luxion:main",
        ]
    },
)