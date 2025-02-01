# © 2025 SuRec Contributors. All Rights Reserved.
# Distributed under the terms of the Apache License 2.0.
# For more details, visit: https://www.apache.org/licenses/LICENSE-2.0

from setuptools import setup, find_packages

setup(
    name="surec",
    version="0.1.0",
    description="A description of your library",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/zzakjista/surec",
    author="zzakjista",
    author_email="gnsdl09@naver.com",
    license="Apache-2.0",
    packages=find_packages(),
    install_requires=open("requirements.txt").read().splitlines(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
