terraform {
    required_version = ">= 1.0.0"

    required_providers {
        azurerem = {
            source = "hashicorp/azurerem"
            version = "2.94.0"
        }
    }
}

provider "azurerem" {
  features {}
}