"""Eusy kubernetes manifests generation libraries. Build script."""

import setuptools

with open("README.md", "r") as readme_file:
    long_description = readme_file.read()

with open("eusy_cdktf/_version.py", "r") as version_file:
    contents = version_file.read()
    package_version = contents.strip().split('"')[-2]

setuptools.setup(
    name="_cdktf",
    version=package_version,
    author="devops",
    author_email="vsevolod.suzdaltsev@gmail.com",
    description="Arranger libraries for generating terraform modules.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="meta.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX :: LINUX",
    ],
    python_requires=">=3.11",
    include_package_data=True,
    install_requires=[
        "cdktf==0.20.2",
        "constructs==10.0.130",
    ],
)
