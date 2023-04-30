import csv
import os.path
import pathlib


class FileDock:
    csv.register_dialect("notes_dialect", delimiter=";", skipinitialspace=True)
    filepath = os.path.join(pathlib.Path().resolve(), r'storage\notes.csv')

    def __init__(self):
        self.fieldnames = ['ID', 'Заголовок', 'Заметка', 'Дата']

    def open_notes_csv(self):
        """
        возвращает построчный список из рабочего файла
        :return:
        """
        if os.path.isfile(self.filepath):
            with open(self.filepath , mode='r') as csv_file:

                csv_reader = csv.DictReader(csv_file, dialect="notes_dialect")
                return list(csv_reader)
        else:
            return []

    def write_notes_csv(self, entry_dict:dict):
        """
        :param entry_dict: рабочий словарь с заметками
        :return:
        """
        with open('./storage/notes.csv', mode='w') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=self.fieldnames, dialect="notes_dialect")

            writer.writeheader()
            for en in entry_dict.values():
                writer.writerow({self.fieldnames[0]: en.note_id,
                                 self.fieldnames[1]: en.title,
                                 self.fieldnames[2]: en.body,
                                 self.fieldnames[3]: en.last_change})


