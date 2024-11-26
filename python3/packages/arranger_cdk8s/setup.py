"""Arranger kubernetes manifests generation libraries. Build script."""

import setuptools

with open("README.md", "r") as readme_file:
    long_description = readme_file.read()

with open("arranger_cdk8s/_version.py", "r") as version_file:
    contents = version_file.read()
    package_version = contents.strip().split('"')[-2]

setuptools.setup(
    name="arranger_cdk8s",
    version=package_version,
    author="devops",
    author_email="vsevolod.suzdaltsev@gmail.com",
    description="Arranger libraries for kubernetes manifests generation.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="meta.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX :: LINUX",
    ],
    python_requires=">=3.7",
    include_package_data=True,
    install_requires=["constructs==10.0.130", "cdk8s==2.68.18"],
)
