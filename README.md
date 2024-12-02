# Arranger

[![Open Source](https://img.shields.io/badge/Open-Source-brightgreen)](https://opensource.org/)
![Active](http://img.shields.io/badge/Status-Active-green.svg)
[![GitHub Commit](https://img.shields.io/github/commit-activity/m/vsuzdaltsev/arranger/main)](https://github.com/vsuzdaltsev/arranger) 


## The Well-Architected Framework for Infrastructure as Code (IaC)

<p>
<strong>Arranger</strong> is designed to address the common challenges faced by developers using the Cloud Development Kit for Terraform/AWS/K8s, providing a seamless experience that truly embodies IaC as it should be prepared.
</p>

## Scenario Examples

* [**Run Application on AWS**](examples/aws/eks-demo-application.md)  
Use Arranger to build and deploy an infrastructure on AWS

* [**Automate Bare Metal Cloud**](doc/arranger)  
Private cloud automation

## Key Features

<ul>
  <li><strong>Everything as a CLI:</strong>
    We believe that every action performed on the infrastructure should have its own dedicated CLI command and corresponding code representation.
  </li>

  <li><strong>Simplified Code Organization:</strong> Arranger provides clear guidelines and best practices for structuring your CDKTF code into logical packages, making it easier to manage and scale your projects.</li>
  
  <li><strong>Effortless Multi-Environment Management:</strong> With CDKTF stacks, you can easily define and manage different environments, such as development, staging, and production, ensuring consistency and reducing the risk of errors.</li>
  
  <li><strong>Global Data Accessibility:</strong> By leveraging object-oriented features, you can have a centralized data management system that ensures all stacks have access to the necessary information without redundancy.</li>
</ul>

## Documentation

The documentation is located in [Arranger](doc/arranger) folder.

Read [Prepare Environment](doc/arranger/PREPARE_ENVIRONMENT.md) section for a quick start.

In order to create your first Infrastructure stack with Arranger and CDKTF read the [How To](doc/arranger/HOW_TO_CREATE_A_NEW_STACK.md)

## Contributing

Contributions are welcome and always appreciated!

To begin working on an issue, simply leave a comment indicating that you're taking it on. There's no need to be officially assigned to the issue before you start.
