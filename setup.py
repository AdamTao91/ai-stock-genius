#!/usr/bin/env python3
"""
AI Stock Genius Setup
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="ai-stock-genius",
    version="1.0.0",
    author="Adam Tao",
    author_email="hello@opensa.cn",
    description="AI-powered stock analysis tool for Chinese investors",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AdamTao91/ai-stock-genius",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Financial and Insurance Industry",
        "Topic :: Office/Business :: Financial",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.10",
    install_requires=[
        "akshare>=1.12.0",
        "yfinance>=0.2.0",
    ],
    entry_points={
        "console_scripts": [
            "stock-genius=stock_genius.analyzer:main",
        ],
    },
)
