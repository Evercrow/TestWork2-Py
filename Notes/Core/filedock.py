import csv
import os.path
import pathlib


from Notes.Core.Note import Note


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
        with open(self.filepath , mode='a+') as csv_file:

            csv_reader = csv.reader(csv_file, dialect="notes_dialect")
            print(type(csv_reader))
            print(csv_reader)
            return list(csv_reader)

    def write_notes_csv(self, entry_dict:dict):
        """
        :param entry_dict: рабочий словарь с заметками
        :return:
        """
        with open('./storage/notes.csv', mode='w') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=self.fieldnames)

            writer.writeheader()
            # if len(entry) <= 1:
            #     writer.writerow({self.fieldnames[0]: entry.note_id,
            #                      self.fieldnames[1]: entry.title,
            #                      self.fieldnames[2]: entry.body,
            #                      self.fieldnames[3]: entry.last_change})
            # else:
            for en in entry_dict.values():
                writer.writerow({self.fieldnames[0]: en.note_id,
                                 self.fieldnames[1]: en.title,
                                 self.fieldnames[2]: en.body,
                                 self.fieldnames[3]: en.last_change})


