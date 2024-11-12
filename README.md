# Arranger

## Infrastructure orchestration framework

### About

A toolkit designed for managing infrastructure described as an object model using Python. It is a Dockerized environment
that includes most of the necessary tools for development and testing. The PyInvoke library is utilized to create the
CLI interface, allowing for efficient management of shell-oriented subprocesses and organizing executable Python code
into tasks. For creating and managing infrastructure, CDKTF and CDK8s are primarily used in conjunction with the SDK.
The Docker image is intended for use in both CI tools and local development, facilitating a consistent environment
across different stages of the development lifecycle.

[How to start](doc/arranger/PREPARE_ENVIRONMENT.md)

[How to create a new Infrastructure Stack using CDKTF and Arranger](doc/arranger/HOW_TO_CREATE_A_NEW_STACK.md)

[FAQ](doc/arranger/FAQ.md)