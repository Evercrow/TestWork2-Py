import datetime


class Note:
    note_id = 0

    def __init__(self, body="---", title="Untitled", last_change=datetime.datetime.now()):
        """
        :param title: заголовок заметки
        :param body: тело заметки
        :param last_change: дата создания/изменения
        """
        self.note_id += 1
        self.title = title
        self.body = body
        self.last_change = last_change

    def __str__(self):
        return "{0} : {1}\n{2}\nПоследнее изменение {3}".format(self.note_id, self.title, self.body, self.last_change)

    def __lt__(self, other):
        return self.last_change < other.last_change

    def __len__(self):
        return 1
