module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "20.8.4"

  cluster_name    = "microservices-all-eks"
  cluster_version = "1.29"

  subnet_ids = module.vpc.private_subnets
  vpc_id     = module.vpc.vpc_id

  cluster_endpoint_public_access  = true
  cluster_endpoint_private_access = true

  eks_managed_node_groups = {
    ng-1 = {
      instance_types   = ["t3.micro"]
      desired_capacity = 5
      min_capacity     = 1
      max_capacity     = 6
    }
  }

  tags = {
    Environment = "dev"
    ManagedBy   = "Terraform"
  }
}