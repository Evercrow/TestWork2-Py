import datetime


class Note:
    id_count = 0

    def __init__(self, title: str, body: str, last_change=None, note_id=None):
        """
        :param title: заголовок заметки
        :param body: тело заметки
        :param last_change: дата создания/изменения
        """
        if last_change is None:
            self.last_change = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        else:
            self.last_change = last_change
        if note_id is None:
            self.note_id = Note.id_count
            Note.id_count += 1
        else:
            self.note_id = note_id
        self.title = title
        self.body = body

    def __str__(self):
        return "{0} : {1}\n{2}\nПоследнее изменение {3}".format(self.note_id, self.title, self.body, self.last_change)

    def __lt__(self, other):
        return self.last_change < other.last_change

    def __len__(self):
        return 1
