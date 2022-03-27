# Ferramenta criada em atividade de aula

import os ##Importa o módulo ou biblioteca OS (integrar programas e recursos)

print("#" * 60) ##Imprimindo #60 vezes

ip_ou_host = input("Digite o IP ou HOST a ser verificado: ") ##Criamos uma variáel que vai receber do usuário um IP

print("-" * 60) ##Imprimindo -60 vezes

os.system('ping -n 6 {}'.format(ip_ou_host)) ##Comando para chamar systema da biblioteca os - comando ping
# sendo 6 o número de pacotes a serem testados

print("-" * 60) ##Imprimindo -60 vezes

# Tool created in class activity

import os ##Imports OS module or library (integrate programs and resources)

print("#" * 60) ##Printing #60 times

ip_ou_host = input("Digite o IP ou HOST a ser verificado: ") ##
We create a variable that will receive an IP from the user

print("-" * 60) ##IPrinting #60 times

os.system('ping -n 6 {}'.format(ip_ou_host)) ##Command to call systema from os library - ping command
# with 6 being the number of packages to be tested

print("-" * 60) ##Printing #60 times

