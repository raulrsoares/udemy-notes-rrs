terraform {
  required_version = ">= 1.1.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "4.22.0"
    }
  }
}

provider "aws" {
  region = "eu-east-2"

  default_tags {
    tags = {
      Owner      = "raul.soares"
      managed-by = "terraform"
    }
  }
}
