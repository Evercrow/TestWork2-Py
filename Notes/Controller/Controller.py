from Notes.UI.Menu import Menu
from Notes.Core import commands


class Controller:
    def __init__(self):
        self.ui = Menu()
        self.core = commands.Core()

    def run(self):
        self.ui.intro()
        not_saved = False
        while True:
            inp = input('Введите команду: ')
            match inp.lower():
                case 'exit':
                    break
                case 'help':
                    self.ui.help()
                case 'add':
                    not_saved = self.adding_note()
                case 'edit':
                    not_saved = self.editing_note()
                case 'del':
                    not_saved = self.core.remove_note(self.ui.getId())
                case 'show':
                    self.showing_note()
                case 'filter':
                    self.filtering()
                case 'list':
                    self.core.show_all()
                case 'save':
                    not_saved = self.core.save_notes()
                case 'sort':
                    self.core.sort_by_date(self.core.notes)
                case _:
                    self.ui.unknown()
        while not_saved:
            answer = input("Желаете сохранить изменения? (y/n)\n")
            if answer == 'y':
                self.core.save_notes()
                break
            elif answer == 'n':
                print("Файл заметок остался без изменений")
                break
            else:
                print("Повторите ввод")
        self.ui.outro()

    def adding_note(self):
        return self.core.add_note(self.ui.getTitle(), self.ui.getBody())

    def editing_note(self):
        nid = self.ui.getId()
        print(" \nВы редактируете следующую запись:")
        self.core.show_entry(nid)
        return self.core.edit_note(nid)

    def showing_note(self):
        self.core.show_entry(input('Введите ID заметки: '))

    def filtering(self):
        print("Введите начальную дату")
        start = self.ui.getDate()
        print("Введите конечную дату")
        end = self.ui.getDate()
        self.core.filter_by_date(start, end)
