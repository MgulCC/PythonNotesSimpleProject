import json
import os
from models.Note import Note

class NoteBook:
    FILE_PATH = "storage/notes.json"  # Definir la ruta del archivo JSON

    @staticmethod
    def load_notes():
        """Carga las notas desde el archivo JSON y las devuelve como un diccionario."""
        if not os.path.exists(NoteBook.FILE_PATH):
            return {}
        with open(NoteBook.FILE_PATH, "r") as file:
            data = json.load(file)
            return {title: Note(note_data["title"], note_data["content"]) for title, note_data in data.items()}

    @staticmethod
    def display_notes(notes):
        """Muestra todas las notas pasadas como argumento."""
        if not notes:
            print("No hay notas disponibles.")
            return
        for note in notes.values():
            print(note)
