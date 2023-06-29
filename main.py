import random
import time

logo1 = '''
  ____  ____  __________  ___
 |  _ \|  _ \| ___/  ___|/ _ \ 
 | |_) | |_) |  _|| |  _| | | |
 |  __/|  _ <| |__| |_| | |_| |
 |_|   |_| \_|____\_____|\___/

  _____  ___   ___  _    ____
 |_   _|/ _ \ / _ \| |  |  __|
   | | | | | | | | | |  |__
   | | | |_| | |_| | |__ __| |
   |_| |\___/ \___/|____|____|

'''

logo2 = logo1


# logo
def print_logo():
	logos = [logo1, logo2]
	logo = random.choice(logos)
	print(logo)
	time.sleep(1)

# menu
def exibir_menu():
	print("Selecione uma opção:")
	print("1. opção")
	print("2. opção")
	print("3. sair")

	escolha = input("Escolha: ")
	return escolha

def main():
	print_logo()
	while True:
		escolha = exibir_menu()

		if escolha == "1":
			print("ação")

		elif escolha == "2":
			print("ação")

		elif escolha == "3":
			print("ação")
			break

		else:
			print("Opção inválida. Tente novamente.")
			print("\n")

if __name__ == "__main__":
	main()

