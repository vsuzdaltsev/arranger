"""Eusy automation libraries. Build script."""

import setuptools

with open("README.md", "r") as readme_file:
    long_description = readme_file.read()

with open("arranger_conf/_version.py", "r") as version_file:
    contents = version_file.read()
    package_version = contents.strip().split('"')[-2]

setuptools.setup(
    name="eusy_conf",
    version=package_version,
    author="devops",
    author_email="vsevolod@velox-solution.com",
    description="Eusy automation configuration.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="meta.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX :: LINUX",
    ],
    python_requires=">=3.8",
    install_requires=[],
)
