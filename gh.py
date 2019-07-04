# -*- coding: utf-8 -*-

#########################################
#         Autor: Bruno Eduardo          #
#      Script para Google Hacking       #
#              02/07/2019               #
#                 1.0v                  #
#########################################

from googlesearch import search

dominio = str(input("Insira o Domínio: "))

# Método
email = f'intitle:parceria | intitle:contato | intext:@gmail.com | intext:@contato | intext:@hotmail site:{dominio}'
acesslog = f'inurl:access.log {dominio}'
indexof = f'inurl:“index of” {dominio}'
robotstxt = f'inurl:robots.txt {dominio}'
senha = f'filetype:xls senha | filetype:txt intext:senha site:{dominio}'


def controle():
    presentation = '''
	+-------------------------+-------------------------+
	|        Seja bem-vindo ao GoogleHacking 1.0v       |
	|   Automatizando o seu Pentest com Google Hacking  |
	|           https://github.com/Brunoedu-me          |
	+-------------------------+-------------------------+
            '''
    print(presentation)
    print("0 - Sair")
    print("1 - Procurar por e-mails")
    print("2 - Tentar encontrar ROBOTS")
    print("3 - Tentar encontrar Index OF")
    print("4 - Tentar encontrar Log de Acesso")
    print("5 - Tentar roubar senha")

controle()

while True:
	console = input("Selecione uma opção: ")
	if console == '0':
		print("Até a proxima!")
		break
	elif console == '1':
		with open("ghemails.txt", "w") as stream:
			for url in search(email, stop=28):
				print(url, file=stream)
			print("O processo foi concluído.")
			print("Os e-mails encontrados foram salvos em ghemails.txt")
	elif console == '2':
		with open("ghacesslog.txt", "w") as stream:
			for url in search(acesslog, stop=28):
				print(url, file=stream)
			print("O processo foi concluído.")
			print("Os Acess Log encontrados foram salvos em ghacesslog.txt")
	elif console == '3':
		with open("ghindexof.txt", "w") as stream:
			for url in search(indexof, stop=28):
				print(url, file=stream)
			print("O processo foi concluído.")
			print("Os Index OF encontrados foram gravados em ghindexof.txt")
	elif console == '4':
		with open("ghrobots.txt", "w") as stream:
			for url in search(robotstxt, stop=28):
				print(url, file=stream)
			print("O processo foi concluído.")
			print("Os Robots.txt encontrados foram registrados em ghrobots.txt")
	elif console == '5':
		with open("ghsenhas.txt", "w") as stream:
			for url in search(senha, stop=28):
				print(url, file=stream)
			print("O processo foi concluído.")
			print("As senhas foram transferidas para o arquivo ghsenhas.txt")
	else:
		print("Opção inválida. Tente novamente.")