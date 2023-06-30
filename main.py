import time
import os
from opcao1 import abrir_arquivos

kernel = '''
  _  _ ____ ____  _   _ ____ _
 | |/ |  __|  _ \| \ | |  __| |
 |   /|  _|| |_) |   | |  _|| |
 |   \| |__|  _ <| |\  | |__| |__
 |_|\_|____|_| \_|_| \_|____|____| v2.1

'''
def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

def logo():
	print(kernel)
	time.sleep(1)

def menu():
	print("Selecione uma opção:")
	print("[1] Intruções")
	print("[2] ?")
	print("[0] Sair")
	escolha = input("Escolha: ")
	return escolha

def main():
	while True:
		clear()
		logo()
		escolha = menu()

		if escolha == "1":
			clear()
			logo()
			abrir_arquivos()
			time.sleep(2)

		elif escolha == "2":
			clear()
			logo()
			print("Executando ação para a Opção 2...")
			time.sleep(2)

		elif escolha == "0":
			clear()
			logo()
			print("Saindo do programa...")
			time.sleep(2)
			break

		else:
			clear()
			logo()
			print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
	main()
