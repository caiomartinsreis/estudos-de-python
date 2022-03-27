# Ferramenta criada em atividade de aula

import os ##Importa o módulo ou biblioteca OS (integrar programas e recursos)
import time ##Importa o módulo time (definir quantidade de vezes)

with open('hosts.txt') as file:
    dump = file.read()
    dump = dump.splitlines()

    for ip in dump:
        print('Verificando o IP: ', ip)
        print('-'*60)
        os.system('ping -n 2 {}'.format(ip))
        print('-' * 60)
        time.sleep(5)

# Tool created in class activity

import os ##Imports OS module or library (integrate programs and resources)
import time ##Import the time module or library (to set the number of times)

with open('hosts.txt') as file: ##Run file with sample hosts for testing
    dump = file.read()
    dump = dump.splitlines()

    for ip in dump:
        print('Verificando o IP: ', ip)
        print('-'*60) ##Printing #60 times
        os.system('ping -n 2 {}'.format(ip))
        print('-' * 60) ##Printing #60 times
        time.sleep(5)
