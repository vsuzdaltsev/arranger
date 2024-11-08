"""Arranger automation libraries. Build script."""

import setuptools

with open("README.md", "r") as readme_file:
    long_description = readme_file.read()

with open("arranger_automation/_version.py", "r") as version_file:
    contents = version_file.read()
    package_version = contents.strip().split('"')[-2]

setuptools.setup(
    name="arranger_automation",
    version=package_version,
    author="devops",
    author_email="vsevolod.suzdaltsev@gmail.com",
    description="Arranger automation shared libraries.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="meta.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX :: LINUX",
    ],
    python_requires=">=3.11",
    install_requires=[
        "docker==4.4.1",
        "GitPython==3.1.24",
        "hvac==0.11.2",
        "jinja2==3.0.1",
        "kubernetes==12.0.1",
        "pyyaml==5.3.1",
        "requests==2.26.0",
        "slack_sdk==3.10.0",
    ],
)
