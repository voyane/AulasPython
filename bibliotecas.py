import math #funcionalidades matematicas
import os #funcionalidades do sistema operativo
import sys #funcionalidades do sistema operativo
import random #é usada para gerar números e escolhas aleatórias.
import datetime #fornece classes para manipular datas e horários.
import collections #fornece tipos de dados especializados, como dicionários ordenados, contadores e tuplas nomeadas.
import json #é usada para codificar e decodificar dados no formato JSON

x = float(input("Digite um numero: "))
raiz = math.sqrt(x)
print("A raiz quadrada de ",x , " e' igual a ", raiz)

angulo = float(input("Digite o  valor do angulo do triangulo: "))
seno = math.sin(angulo)
print("O seno de ", angulo, " e': ", seno)

diretorio = os.getcwd()
print("O directorio corrente de trabalho e': ", diretorio)