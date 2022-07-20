terraform {
  #configurações diversas / configs básicas
  #Declarar versão do terraform
  required_version = "~> 1.1.0" # 1.1.0 até 1.1.n
    
    required_providers {
      #provides que podem ser usados
      aws = {
        version = ">= 3.50.0"
        source = "hashicorp/aws"
      }
      #pode-se colocar varios providers
    }

    backend "s3" {
      #neste caso eu guardaria dentro de um bbuckt s3
    }
}

provider "aws" {
    #confi nescessária pelo provider
}

resource "aws_instance" "Nome-autoexplicativo" {
  
}

data "aws_ami" "ami" {
  #puxa dados de fora da estrutura terraform
}

module "nome-explicativo" {
  #só config internas muda
}

variable "ip" {
  #declaração de variavel
}

output "vm1_ip" {
  #pegar informação de dentro do código terraform e utilizarr para outro recurso
}

locals {
  #serve paar pegar funções/expressões utilizadas muitas vezes, para poder chamala mais tarde invés de escrever tudo de uma vez
}