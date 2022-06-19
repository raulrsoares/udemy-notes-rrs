"""
PEP8 - Python Enhancement Proposals

São propostas de melhorias para a linguagem Python

The Zen of Python

-----

import this

The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

"""

"""
Ideia da PEP8 é que possamos escrever códigos python em forma pythônica.

1º Utilizar Camel Case para nomes de classes:

class Calculadora:
    pass


class CalculadoraCientifica:
    pass

2º Utilizar nomes em minsculos, separados por underline para funções ou váriaveis:

def soma():
    pass


def soma_dois():
    pass


numero = 4

numero_impar = 3

3º Utilizar 4 espaços para identação [NÃO USAR TABS]

if 'a' in 'banana':
    print('tem')
    
4º Linhas em Branco
    - Separar funções e definições de classe com duas linhas em branco;
    - Métodos detro de ma classe devem ser separados com uma úica linha em branco.

class Calculadora:
    pass


class CalculadoraCientifica:
    pass
    
5º Imports
    - Imports sempre devem ser feitos em linhas separadas

# Import Errado

import sys, os

# Import Certo

import sys
import os

# Não há problemas em utilizar:

from types import StringType, ListType

# Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:

from types import (
    StringType,
    ListType,
    SetTye,
    OutroType
)

# Imports devem ser colocados no topo do arquivo, logo depois de quaisquer comentários ou docstrings 
# e antes de constantes ou variáveis globais

6º Espaços em expressóes e instuções

# Não fazer:

funcao( algo[ 1 ], { outro: 2 } )

# Faça:

funcao(algo[1], {outro: 2})

# Não faça:

algo (1)

# Faça:

algo(1)

# Não faça:

dict ['chave'] = lista [indice]

# Faça:

dict['chave'] = lista[indice]

# Não faça:

x              = 1
y              = 3
variavel_longa = 5

# Faça:

x = 1
y = 2
variavel_longa = 5

7º Termine sempre uma instrução com uma nova linha (Redomendavel sempre deixar uma linha em branco ao final do documento)
"""
import this
