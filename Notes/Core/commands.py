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

    def build_data(self, dicts_from_file: list):
        db = {}
        for d in dicts_from_file:
            db.update({d['ID']: Note(d['Заголовок'], d['Заметка'], last_change=d['Дата'], note_id=d['ID'])})
        if len(db) > 0:
            Note.id_count = int(max(db.keys())) + 1
        return db

    def save_notes(self):
        """
        :return: возвращает флаг False только для not_saved в контроллере, единственный "обратный" метод
        """
        try:
            self.f.write_notes_csv(self.notes)
            return False
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
            self.out.com_success()
            return True
        except KeyError:
            self.out.com_error("ключ не найден")
            return False
        except TypeError:
            self.out.com_error("ключ должен быть строковым типом")
            return False


    def show_entry(self, keyid: str):
        try:
            self.out.display(self.notes[keyid])
        except KeyError:
            self.out.com_error("ключ не найден")
        except TypeError:
            self.out.com_error("ключ должен быть строковым типом")

    def show_all(self):
        self.out.display(self.notes)

    def sort_by_date(self, filtered: dict):
        """
        сортировка по возрастанию даты, достигается за счет перегрузки сравнения в объекте Note
        :return:
        """

        sorted_dict = dict(sorted(filtered.items(), key=lambda x: x[1]))
        self.out.display(sorted_dict)

    def filter_by_date(self, start_date=None, to_date=None):
        if start_date is not None and to_date is not None:
            filtered_d = {k: v for (k, v) in self.notes.items() if
                          start_date <= datetime.datetime.strptime(v.last_change, "%Y-%m-%d %H:%M:%S").date() <= to_date
                          }
        else:
            filtered_d = self.notes
        self.sort_by_date(filtered_d)
