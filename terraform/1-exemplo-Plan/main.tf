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
  access_key = "my-access-key"
  secret_key = "my-secret-key"

  region = "us-east-2"

  default_tags {
    tags = {
      Owner      = "raul.soares"
      managed-by = "terraform"
    }
  }
}
