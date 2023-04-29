from Notes.Core.Note import Note
from Notes.Core.filedock import FileDock
from Notes.UI.Menu import Menu


class Core:
    notes = {}
    out = Menu()
    f = FileDock()

    def __init__(self):
        self.notes = self.build_data(self.f.open_notes_csv())

    def add_note(self, title, body):
        entry = Note(title, body)
        self.notes.update({entry.note_id: entry})
        self.out.display(entry)

    def build_data(self, lines_from_file):
        db = {}
        for l in lines_from_file:
            db.update({l[0]: Note(l[1], l[2], l[3])})
        return db

    def save_notes(self):
        try:
            self.f.write_notes_csv(self.notes)
        except OSError:
            self.out.com_error("Не удалось записать в файл")

    def edit_note(self):
        pass

    def remove_note(self):
        pass

    def filter_notes(self):
        pass

    def show_entry(self):
        pass

    def show_all(self):
        pass
