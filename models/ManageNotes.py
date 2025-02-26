import json
import os
from models.Note import Note
from models.NoteBook import NoteBook

class ManageNotes:
    # Declarada la ruta de la carpeta donde se encuentra el JSON con las notas
    FILE_PATH = "storage/notes.json"

    def save_notes(notes):
        try:
            # Intenta crear el directorio si no existe
            os.makedirs("storage")
        except FileExistsError:
            pass  # La carpeta ya existe, no es un problema
        except Exception as e:
            print(f"Error al crear la carpeta 'storage': {e}")
            return  # Salir de la función si hay un error la crear una carpeta

        try:
            # Intenta guardar las notas en un archivo JSON, podria dar el error por permisos de archivo o almacenamiento
            with open(ManageNotes.FILE_PATH, "w") as file:
                # el obejeto note lo guarda como diccionario y lo añade al JSON
                json.dump({title: note.__dict__ for title, note in notes.items()}, file, indent=4)
        except Exception as e:
            print(f"Error al guardar las notas: {e}")

    @staticmethod
    def create_note(title, content):
        # Trae todas las notas y promero comprueba que no existe una con el mismo titulo
        notes = NoteBook.load_notes()
        if title in notes:
            print("La nota con este título ya existe.")
        else:
            notes[title] = Note(title, content)
            ManageNotes.save_notes(notes) #llama a la función anterior para guardar la nota

    @staticmethod
    def update_note(title, update_content):
        notes = NoteBook.load_notes()
        # Comprueba si la nota existe o no para poder actualizarla
        if title not in notes:
            print("No se encontró la nota.")
        else:
            notes[title].content = update_content
            ManageNotes.save_notes(notes)
            print("Nota actualizada correctamente.")

    @staticmethod
    def delete_note(title):
        # Se obtienen todas las notas
        notes = NoteBook.load_notes()
        if title in notes:
            # Si coinciden con el titulo dado es eliminada
            del notes[title]
            ManageNotes.save_notes(notes)
            print("Nota eliminada correctamente.")
        else:
            print("No se encontró la nota.")