from colorama import init, Fore, Style

init()

def main():
    while True:
        print(Fore.GREEN + "=" * 20)
        print(Fore.CYAN + "======= Menu =======")
        print(Fore.GREEN + "=" * 20)
        print(Fore.GREEN + "1." + Fore.GREEN + " Nueva nota")
        print(Fore.GREEN + "2." + Fore.GREEN + " Muestra todas las notas")
        print(Fore.GREEN + "3." + Fore.GREEN + " Busca nota por título")
        print(Fore.GREEN + "4." + Fore.GREEN + " Muestra nota por contenido")
        print(Fore.GREEN + "5." + Fore.GREEN + " Actualiza nota")
        print(Fore.GREEN + "6." + Fore.GREEN + " Elimina nota ")
        print(Fore.GREEN + "0." + Fore.GREEN + " Salir")
        print(Fore.GREEN + "=" * 20)

        choice = input(Fore.CYAN + "[+] Elige una tarea: " + Fore.WHITE)

        if choice == "0":
            print(Fore.RED + "Salir del programa ... Cerrando" + Style.RESET_ALL)
            break
        else:
            print(Fore.CYAN + f"As elegido la opción {choice}" + Style.RESET_ALL)


if __name__ == "__main__":
    main()
