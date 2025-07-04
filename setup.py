"""Setup configuration for theme_nxn package."""

from setuptools import setup, find_packages

setup(
    name="theme_nxn",
    version="0.1.0",
    description="A custom plotnine theme with harmonious color palette",
    author="theme_nxn",
    packages=find_packages(),
    install_requires=[
        "plotnine>=0.10.0",
    ],
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)