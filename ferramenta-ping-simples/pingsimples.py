import os ##Importa o módulo ou biblioteca OS (integrar programas e recursos)

print("#" * 60) ##Imprimindo #60 vezes

ip_ou_host = input("Digite o IP ou HOST a ser verificado: ") ##Criamos uma variáel que vai receber do usuário um IP

print("-" * 60) ##Imprimindo -60 vezes

os.system('ping -n 6 {}'.format(ip_ou_host)) ##Comando para chamar systema da biblioteca os - comando ping
# sendo 6 o número de pacotes a serem testados

print("-" * 60) ##Imprimindo -60 vezes
