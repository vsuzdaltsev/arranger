from typing import Any, Dict

from arranger_cdktf.imports.aws.eip import Eip as AwsEip
from arranger_cdktf.imports.aws.internet_gateway import (
    InternetGateway as AwsInternetGateway,
)
from arranger_cdktf.imports.aws.route_table import (
    RouteTable as AwsRouteTable,
    RouteTableRoute as AwsRouteTableRoute,
)
from arranger_cdktf.imports.aws.vpc import Vpc as AwsVpc
from arranger_cdktf.imports.aws.nat_gateway import NatGateway as AwsNatGateway
from arranger_cdktf.imports.aws.route_table_association import (
    RouteTableAssociation as AwsRouteTableAssociation,
)
from arranger_cdktf.imports.aws.subnet import Subnet as AwsSubnet

from .basic_stack import AwsBasicStack, Construct, TfConf


class VpcStack(AwsBasicStack):
    @property
    def _name_prefix(self) -> str:
        return "vpc"

    def __init__(self, scope: Construct, ns: str, config: TfConf):
        super().__init__(scope, ns, config)

        self.tags = self.stack_tags
        self.aws_provider = self.globals.automation(scope=self)
        self.null_provider = self.globals.null_provider(scope=self)
        self.main_vpc = self._main_vpc()

        self.vpc_internet_gw = self._vpc_internet_gw()

        self.eks_subnet1 = self._eks_subnet1()
        self.eks_subnet2 = self._eks_subnet2()
        self.eks_subnet3 = self._eks_subnet3()
        self.eks_subnet4 = self._eks_subnet4()

        self.eip_eks_subnet1_nat_gw = self._eip_eks_subnet1_nat_gw()
        self.nat_gw_eks_subnet1 = self._nat_gw_eks_subnet1()
        self.eks_subnet1_route_table = self._eks_subnet1_route_table()
        self.eks_subnet1_route_table_association = (
            self._eks_subnet1_route_table_association()
        )

        self.eks_subnet2_route_table = self._eks_subnet2_route_table()
        self.eks_subnet2_route_table_association = (
            self._eks_subnet2_route_table_association()
        )

        self.eks_subnet3_route_table = self._eks_subnet3_route_table()
        self.eks_subnet3_route_table_association = (
            self._eks_subnet3_route_table_association()
        )

        self.eks_subnet4_route_table = self._eks_subnet4_route_table()
        self.eks_subnet4_route_table_association = (
            self._eks_subnet4_route_table_association()
        )

    def _main_vpc(self) -> AwsVpc:
        name = self._name(object_type="main")

        return AwsVpc(
            scope=self,
            id_=name,
            cidr_block=self._vpc_main["cidr"][0],
            tags=self.stack_tags
            | {"Name": name}
            | {f"kubernetes.io/cluster/{self.globals.tenant}": "owned"},
            enable_dns_support=True,
            enable_dns_hostnames=True,
            provider=self.aws_provider,
            lifecycle=self.lifecycle_policy(),
        )

    def _vpc_internet_gw(self) -> AwsInternetGateway:
        name = self._name(object_type="igw-eks-main-eks-vpc")

        return AwsInternetGateway(
            scope=self,
            id_=name,
            vpc_id=self.main_vpc.id,
            tags=self.tags | {"Name": name},
            lifecycle=self.lifecycle_policy(),
            depends_on=[self.main_vpc],
        )

    @property
    def _vpc_main(self) -> Any:
        return self.globals.ip_ranges["vpc-main"]

    @property
    def _vpc_main_subnets(self) -> Dict[str, Any]:
        return self.globals.ip_ranges["vpc-main"]["subnets"]

    @property
    def _subnets_additional_tag(self) -> Dict[str, str]:
        return {"owner": f"vpc-main-eks-{self.globals.tenant}"}

    def _eks_subnet1(self) -> AwsSubnet:
        name = self._name(object_type="main-subnet-1")

        return AwsSubnet(
            scope=self,
            id_=name,
            cidr_block=self._vpc_main_subnets["snet-eks1"]["cidr"][0],
            vpc_id=self.main_vpc.id,
            availability_zone=self._vpc_main_subnets["snet-eks1"]["availability-zone"],
            tags=self.stack_tags
            | self._subnets_additional_tag
            | {"Name": f"{name}-public"}
            | {f"kubernetes.io/cluster/{self.globals.tenant}": "shared"}
            | {"type": "public"},
            provider=self.aws_provider,
            depends_on=[self.main_vpc],
            lifecycle=self.lifecycle_policy(),
        )

    def _eip_eks_subnet1_nat_gw(self) -> AwsEip:
        name = self._name(object_type="eip-nat-gw-eks-subnet1")

        return AwsEip(
            scope=self,
            id_=name,
            tags=self.tags | {"Name": name},
            provider=self.aws_provider,
            lifecycle=self.lifecycle_policy(),
            depends_on=[self.eks_subnet1],
        )

    def _nat_gw_eks_subnet1(self) -> AwsNatGateway:
        name = self._name(object_type="nat-gw-eks-subnet1")

        return AwsNatGateway(
            scope=self,
            id_=name,
            subnet_id=self.eks_subnet1.id,
            allocation_id=self.eip_eks_subnet1_nat_gw.allocation_id,
            connectivity_type="public",
            tags=self.tags | {"Name": name},
            provider=self.aws_provider,
            lifecycle=self.lifecycle_policy(),
            depends_on=[self.eip_eks_subnet1_nat_gw],
        )

    def _eks_subnet1_route_table(self) -> AwsRouteTable:
        name = self._name(object_type=f"eks-subnet1-rt")

        return AwsRouteTable(
            scope=self,
            id_=name,
            vpc_id=self.main_vpc.id,
            route=[
                AwsRouteTableRoute(
                    cidr_block="0.0.0.0/0",
                    gateway_id=self.vpc_internet_gw.id,
                ),
            ],
            tags=self.tags | {"Name": name},
            provider=self.aws_provider,
            lifecycle=self.lifecycle_policy(),
        )

    def _eks_subnet1_route_table_association(self) -> AwsRouteTableAssociation:
        name = self._name(object_type="eks-subnet1-rt-association")

        return AwsRouteTableAssociation(
            scope=self,
            id_=name,
            route_table_id=self.eks_subnet1_route_table.id,
            subnet_id=self.eks_subnet1.id,
        )

    def _eks_subnet2(self) -> AwsSubnet:
        name = self._name(object_type="main-subnet-2")

        return AwsSubnet(
            scope=self,
            id_=name,
            cidr_block=self._vpc_main_subnets["snet-eks2"]["cidr"][0],
            vpc_id=self.main_vpc.id,
            availability_zone=self._vpc_main_subnets["snet-eks2"]["availability-zone"],
            tags=self.stack_tags
            | self._subnets_additional_tag
            | {"Name": f"{name}-private"}
            | {f"kubernetes.io/cluster/{self.globals.tenant}": "shared"}
            | {"type": "private"},
            depends_on=[self.main_vpc],
            lifecycle=self.lifecycle_policy(),
        )

    def _eks_subnet2_route_table(self) -> AwsRouteTable:
        name = self._name(object_type=f"eks-subnet2-rt")

        return AwsRouteTable(
            scope=self,
            id_=name,
            vpc_id=self.main_vpc.id,
            route=[
                AwsRouteTableRoute(
                    cidr_block="0.0.0.0/0",
                    nat_gateway_id=self.nat_gw_eks_subnet1.id,
                ),
            ],
            tags=self.tags | {"Name": name},
            provider=self.aws_provider,
            lifecycle=self.lifecycle_policy(),
        )

    def _eks_subnet2_route_table_association(self) -> AwsRouteTableAssociation:
        name = self._name(object_type="eks-subnet2-rt-association")

        return AwsRouteTableAssociation(
            scope=self,
            id_=name,
            route_table_id=self.eks_subnet2_route_table.id,
            subnet_id=self.eks_subnet2.id,
        )

    def _eks_subnet3(self) -> AwsSubnet:
        name = self._name(object_type="main-subnet-3")

        return AwsSubnet(
            scope=self,
            id_=name,
            cidr_block=self._vpc_main_subnets["snet-eks3"]["cidr"][0],
            vpc_id=self.main_vpc.id,
            availability_zone=self._vpc_main_subnets["snet-eks3"]["availability-zone"],
            tags=self.stack_tags
            | self._subnets_additional_tag
            | {"Name": f"{name}-private"}
            | {f"kubernetes.io/cluster/{self.globals.tenant}": "shared"}
            | {"type": "private"},
            depends_on=[self.main_vpc],
            lifecycle=self.lifecycle_policy(),
        )

    def _eks_subnet3_route_table(self) -> AwsRouteTable:
        name = self._name(object_type=f"eks-subnet3-rt")

        return AwsRouteTable(
            scope=self,
            id_=name,
            vpc_id=self.main_vpc.id,
            route=[
                AwsRouteTableRoute(
                    cidr_block="0.0.0.0/0",
                    nat_gateway_id=self.nat_gw_eks_subnet1.id,
                ),
            ],
            tags=self.tags | {"Name": name},
            provider=self.aws_provider,
            lifecycle=self.lifecycle_policy(),
        )

    def _eks_subnet3_route_table_association(self) -> AwsRouteTableAssociation:
        name = self._name(object_type="eks-subnet3-rt-association")

        return AwsRouteTableAssociation(
            scope=self,
            id_=name,
            route_table_id=self.eks_subnet3_route_table.id,
            subnet_id=self.eks_subnet3.id,
        )

    def _eks_subnet4(self) -> AwsSubnet:
        name = self._name(object_type="main-subnet-4")

        return AwsSubnet(
            scope=self,
            id_=name,
            cidr_block=self._vpc_main_subnets["snet-eks4"]["cidr"][0],
            vpc_id=self.main_vpc.id,
            availability_zone=self._vpc_main_subnets["snet-eks4"]["availability-zone"],
            tags=self.stack_tags
            | self._subnets_additional_tag
            | {"Name": f"{name}-private"}
            | {f"kubernetes.io/cluster/{self.globals.tenant}": "shared"}
            | {"type": "private"},
            depends_on=[self.main_vpc],
            lifecycle=self.lifecycle_policy(),
        )

    def _eks_subnet4_route_table(self) -> AwsRouteTable:
        name = self._name(object_type=f"eks-subnet4-rt")

        return AwsRouteTable(
            scope=self,
            id_=name,
            vpc_id=self.main_vpc.id,
            route=[
                AwsRouteTableRoute(
                    cidr_block="0.0.0.0/0",
                    nat_gateway_id=self.nat_gw_eks_subnet1.id,
                ),
            ],
            tags=self.tags | {"Name": name},
            provider=self.aws_provider,
            lifecycle=self.lifecycle_policy(),
        )

    def _eks_subnet4_route_table_association(self) -> AwsRouteTableAssociation:
        name = self._name(object_type="eks-subnet4-rt-association")

        return AwsRouteTableAssociation(
            scope=self,
            id_=name,
            route_table_id=self.eks_subnet4_route_table.id,
            subnet_id=self.eks_subnet4.id,
        )
