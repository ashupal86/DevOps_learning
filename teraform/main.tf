# main.tf

terraform {
    required_providers {
        aws = {
            source  = "hashicorp/aws"
            version = "~> 5.0"
        }
    }
    required_version = ">= 1.0.0"
}

provider "aws" {
    region = "ap-south-1"
}

resource "aws_instance" "terraform" {
    instance_type="t2.micro"
    ami = "ami-0f918f7e67a3323f0"
    tags={
        Name = "Terarform Example"
    }
}