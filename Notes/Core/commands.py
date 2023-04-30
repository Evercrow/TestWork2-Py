import datetime

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
        self.notes.update({str(entry.note_id): entry})
        self.out.display(entry)
        return True

    def build_data(self, dicts_from_file :list):
        db = {}
        print(dicts_from_file)
        for d in dicts_from_file:
            db.update({d['ID']: Note(d['Заголовок'], d['Заметка'], last_change=d['Дата'], note_id=d['ID'])})
        if len(db) > 0:
            Note.id_count = int(max(db.keys())) + 1
        return db

    def save_notes(self):
        try:
            self.f.write_notes_csv(self.notes)
        except OSError:
            self.out.com_error("не удалось записать в файл")
        return True

    def edit_note(self, keyid: str):
        entry = Note(self.out.getTitle(), self.out.getBody(),
                     note_id=keyid, last_change=datetime.datetime.now())
        self.notes.update({keyid: entry})
        self.out.display(entry)
        return True

    def remove_note(self, keyid: str):
        try:
            self.notes.pop(keyid)
            return True
        except KeyError:
            self.out.com_error("ключ не найден")
            return False
        except TypeError:
            self.out.com_error("ключ должен быть строковым типом")
            return False

    def filter_notes(self):
        pass

    def show_entry(self, keyid: str):
        try:
            self.out.display(self.notes[keyid])
        except KeyError:
            self.out.com_error("ключ не найден")
        except TypeError:
            self.out.com_error("ключ должен быть строковым типом")

    def show_all(self):
        self.out.display(self.notes)
