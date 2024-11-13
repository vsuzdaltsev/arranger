<h1 align="center">Arranger</h1>
<h3 align="center">The CDKTF & CDK8S Well-Architected Framework</h3>

<p>
<strong>Arranger</strong> is designed to address the common challenges faced by developers using the Cloud Development Kit for Terraform, providing a seamless experience that truly embodies IaaC as it should be prepared.
</p>

<h2>Key Features</h2>

<ul>  
  <li><strong>Simplified Code Organization:</strong> One of the biggest hurdles with CDKTF is understanding how to organize code effectively. Arranger provides clear guidelines and best practices for structuring your CDKTF code into logical packages, making it easier to manage and scale your projects.</li>
  
  <li><strong>Effortless Multi-Environment Management:</strong> Managing multiple environments can be daunting, but our framework simplifies this process. With CDKTF stacks, you can easily define and manage different environments, such as development, staging, and production, ensuring consistency and reducing the risk of errors.</li>
  
  <li><strong>Global Data Accessibility:</strong> Our framework addresses the challenge of working with data that needs to be accessible across multiple stacks. By leveraging Python’s object-oriented features, you can create a centralized data management system that ensures all stacks have access to the necessary information without redundancy.</li>
  
  <li><strong>Beyond Git-Commited Configurations:</strong> Arranger offers an object-oriented representation of your infrastructure, utilizing Python’s powerful features like inheritance and polymorphism. This approach not only enhances maintainability but also allows for the creation of reusable components, simplifying complex configurations.</li>
  
<li><strong>Comprehensive Toolkit and CLI:</strong>
    <ul>
      <li>A toolkit designed for managing infrastructure described as an object model using Python.</li>
      <li>Includes a Dockerized environment with most necessary tools for development and testing.</li>
      <li>Utilizes the PyInvoke library to create a CLI interface, enabling efficient management of shell-oriented subprocesses and organizing executable Python code into tasks.</li>
      <li>Employs CDKTF and CDK8s for creating and managing infrastructure, in conjunction with the SDK.</li>
      <li>Docker image is intended for use in both CI tools and local development, facilitating a consistent environment across different stages of the development lifecycle.</li>
    </ul>
    </li>
</ul>


[FAQ](doc/arranger/FAQ.md)

[How to start](doc/arranger/PREPARE_ENVIRONMENT.md)

[How to create a new Infrastructure Stack using CDKTF and Arranger](doc/arranger/HOW_TO_CREATE_A_NEW_STACK.md)

[Authorization](doc/arranger/AUTHORIZATION.md)
