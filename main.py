from colorama import init, Fore, Style
from models.NoteBook import NoteBook
from models.ManageNotes import ManageNotes
from models.Note import Note

init()

def main():
    while True:
        print(Fore.GREEN + "=" * 20)
        print(Fore.CYAN + "=" * 8 + "Menu Principal" + "=" * 8)
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

        if choice == "1":
            create_note_submenu()

        elif choice == "2":
            notes = NoteBook.load_notes()
            print(Fore.YELLOW + "\nMostrando todas las notas:\n" + Style.RESET_ALL)
            NoteBook.display_notes(notes)


        elif choice == "3":
            title = input(Fore.CYAN + "Inserte el título para buscar: " + Fore.WHITE)
            # Validar si el título está vacío
            if not title.strip():
                print(Fore.RED + "El título no puede estar vacío." + Style.RESET_ALL)
            else:
                notes = NoteBook.load_notes()
                found_notes = [note for note in notes.values() if note.matches_title(title)]
                if found_notes:
                    print(Fore.YELLOW + "\nNotas encontradas:\n" + Style.RESET_ALL)
                    for note in found_notes:
                        print(note)
                else:
                    print(Fore.RED + "No se encontró ninguna nota con ese título." + Style.RESET_ALL)

        elif choice == "4":
            content = input(Fore.CYAN + "Inserte el contenido a buscar: " + Fore.WHITE)
            # Validar si el contenido está vacío
            if not content.strip():
                print(Fore.RED + "El contenido no puede estar vacío." + Style.RESET_ALL)
            else:
                notes = NoteBook.load_notes()
                found_notes = [note for note in notes.values() if note.matches_content(content)]
                if found_notes:
                    print(Fore.YELLOW + "\nNotas encontradas:\n" + Style.RESET_ALL)
                    for note in found_notes:
                        print(note)
                else:
                    print(Fore.RED + "No se encontraron notas con ese contenido." + Style.RESET_ALL)

        elif choice == "5":
            update_note_submenu()

        elif choice == "6":
            delete_note_submenu()

        elif choice == "0":
            print(Fore.BLUE + "Salir del programa ... Cerrando" + Style.RESET_ALL)
            break

        else:
            print(Fore.RED + "Opción no válida. Inténtelo de nuevo." + Style.RESET_ALL)

# submenu para crear
def create_note_submenu():
    while True:
        print(Fore.GREEN + "=" * 20)
        print(Fore.CYAN + "=" * 8 + "Crear nueva nota" + "=" * 8)
        print(Fore.GREEN + "=" * 20)
        print(Fore.GREEN + "1." + Fore.GREEN + " Crear nota")
        print(Fore.GREEN + "0." + Fore.GREEN + " Volver al menú principal")
        print(Fore.GREEN + "=" * 20)

        choice = input(Fore.CYAN + "[+] Elige una tarea: " + Fore.WHITE)

        if choice == "1":
            title = input(Fore.CYAN + "Inserte el título de la nota: " + Fore.WHITE)
            content = input(Fore.CYAN + "Inserte el contenido: " + Fore.WHITE)
            ManageNotes.create_note(title, content)
            print(Fore.GREEN + "Nota creada exitosamente" + Style.RESET_ALL)

        elif choice == "0":
            break

        else:
            print(Fore.RED + "Opción no válida. Inténtelo de nuevo." + Style.RESET_ALL)

# submenu para actualizar
def update_note_submenu():
    while True:
        print(Fore.GREEN + "=" * 20)
        print(Fore.CYAN + "=" * 8 + "Actualizar nota" + "=" * 8)
        print(Fore.GREEN + "=" * 20)
        print(Fore.GREEN + "1." + Fore.GREEN + " Actualizar nota")
        print(Fore.GREEN + "0." + Fore.GREEN + " Volver al menú principal")
        print(Fore.GREEN + "=" * 20)

        choice = input(Fore.CYAN + "[+] Elige una tarea: " + Fore.WHITE)

        if choice == "1":
            title = input(Fore.CYAN + "Inserte el título de la nota a actualizar: " + Fore.WHITE)
            update_content = input(Fore.CYAN + "Ingrese el nuevo contenido: " + Fore.WHITE)
            ManageNotes.update_note(title, update_content)

        elif choice == "0":
            break

        else:
            print(Fore.RED + "Opción no válida. Inténtelo de nuevo." + Style.RESET_ALL)

# submenu para eliminar
def delete_note_submenu():
    while True:
        print(Fore.GREEN + "=" * 20)
        print(Fore.CYAN + "=" * 8 + "Eliminar nota" + "=" * 8)
        print(Fore.GREEN + "=" * 20)
        print(Fore.GREEN + "1." + Fore.GREEN + " Eliminar nota")
        print(Fore.GREEN + "0." + Fore.GREEN + " Volver al menú principal")
        print(Fore.GREEN + "=" * 20)

        choice = input(Fore.CYAN + "[+] Elige una tarea: " + Fore.WHITE)

        if choice == "1":
            title = input(Fore.CYAN + "Inserte el título de la nota a eliminar: " + Fore.WHITE)
            ManageNotes.delete_note(title)

        elif choice == "0":
            break

        else:
            print(Fore.RED + "Opción no válida. Inténtelo de nuevo." + Style.RESET_ALL)


if __name__ == "__main__":
    main()