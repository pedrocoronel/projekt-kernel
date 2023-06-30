import os
import subprocess
from main import clear

def abrir_arquivos():
	while True:
		pasta = input("Digite o caminho da pasta: ")
		arquivos = os.listdir(pasta)
		print("Arquivos na pasta:")
		for arquivo in arquivos:
			print(arquivo)

	arquivo_selecionado = input("Digite o nome do arquivo que deseja abrir: ")
	caminho_arquivo = os.path.join(pasta, arquivo_selecionado)

	if os.path.isfile(caminho_arquivo):
		print("Opções:")
		print("1. Visualizar com o comando 'cat'")
		print("2. Editar com o comando 'nano'")
		escolha_opcao = input("Escolha a opção: ")

		if escolha_opcao == "1":
			subprocess.call(["cat", caminho_arquivo])
		elif escolha_opcao == "2":
			subprocess.call(["nano", caminho_arquivo])
		else:
			print("Opção inválida.")
	else:
		print("Arquivo não encontrado.")
		input("Pressione Enter para continuar...")


