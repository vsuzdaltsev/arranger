# Build and Run Application on AWS
Practical example of a layered infrastructure setup.  
With this approach the application will have several layers of resources:

* VPC + Subnets + NAT GW + Internet GW + Route tables
* Security Groups
* API Gateway
* Elastic Kubernetes Service
* ECR
* Istio service mesh
* K8s manifests

## AWS Resources Diagram

![eks-demo-application](../diagrams/eks-demo-application.png)
