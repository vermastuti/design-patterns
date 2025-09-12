# LLD for Google Docs

# This is a simplified version focusing on core functionalities.

# https://www.youtube.com/watch?v=MT9qZFGQXOU&list=PLQEaRBV9gAFvzp6XhcNFpk1WdOcyVo9qT&index=7

class DocumentElement:
    def render(self):
        raise NotImplementedError("Subclasses must implement render method")
    

class TextElement(DocumentElement):
    def __init__(self, text):
        self.text = text

    def render(self):
        return self.text

class ImageElement(DocumentElement):
    def __init__(self, image_path):
        self.image_path = image_path

    def render(self):
        return f"Image: {self.image_path}"


class NewLineElement(DocumentElement):
    def render(self):
        return "\n"
    

class TabSpaceElement(DocumentElement):
    def render(self):
        return "\t"


class Persistence:
    def save(self, document):
        pass


class SaveToFile(Persistence):
    def __init__(self, filename):
        self.filename = filename

    def save(self, document):
        try:
            with open(self.filename, 'w') as f:
                f.write(document)
        except IOError as e:
            print(f"An error occurred while saving to file: {e}")


class SaveToDatabase(Persistence):
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def save(self, document):
        # Simulate saving to a database
        print(f"Saving document to database with connection: {self.connection_string}")
        for element in document.elements:
            print(element.render())


class Document:

    def __init__(self, elements):
        self.elements = elements
        
    def add_element(self, element):
        self.elements.append(element)

    def render(self):
        document = ""
        for element in self.elements:
            document += element.render()
        return document


class DocumentEditor:
    def __init__(self, document, persistence):
        self.document = document
        self.persistence = persistence
        self.rendered_document = ""

    def add_text(self, text):
        self.document.add_element(TextElement(text))

    def add_image(self, image_path):
        self.document.add_element(ImageElement(image_path))

    def add_new_line(self):
        self.document.add_element(NewLineElement())

    def add_tab_space(self):
        self.document.add_element(TabSpaceElement())

    def render_document(self):
        self.rendered_document = self.document.render()
        return self.rendered_document

    def save(self):
        self.persistence.save(self.render_document())


if __name__ == "__main__":

    doc = Document([])
    persistence = SaveToFile("document.txt")
    editor = DocumentEditor(doc, persistence)

    editor.add_text("Hi, this is your LLD for Google Docs")
    editor.add_new_line()
    editor.add_text("You can add text, image, new lines and tab spaces")
    editor.add_new_line()
    editor.add_tab_space()
    editor.add_text("Showing tab space here. ")
    editor.add_text("See, what else you can do. ")
    editor.add_text("Isn't it cool?")
    editor.add_new_line()
    editor.add_image("/Users/stutiverma/Downloads/image.png")
    editor.add_new_line()
    editor.add_text("You can save this document to a file or database")
    editor.add_new_line()
    print(editor.render_document())
    editor.save()
