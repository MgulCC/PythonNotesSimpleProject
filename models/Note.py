class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __str__(self):
        # devuelve el contenido y el título de una nota como texto
        return f"{'=' * 30}\nTítulo: {self.title}\nContenido: {self.content}\n{'=' * 30}"

    def matches_title(self, search_title):
        # verificado de si el titulo coincide con el título o palabra del título dentro de una nota
        return search_title.lower() in self.title.lower()

    def matches_content(self, search_content):
        # verificado de si el contenido coincide con el contenido
        return search_content.lower() in self.content.lower()