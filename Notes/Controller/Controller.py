from Notes.UI.Menu import Menu
from Notes.Core import commands


class Controller:
    def __init__(self):
        self.ui = Menu()
        self.core = commands.Core()

    def run(self):
        self.ui.intro()
        while True:
            inp = input('Введите команду: ')
            match inp.lower():
                case 'exit':
                    break
                case 'help':
                    self.ui.help()
                case 'add':
                    self.core.add_note(input('Введите заголовок: \n'), input('Введите текст заметки: \n'))
                case 'edit':
                    self.core.edit_note()
                case 'del':
                    self.core.remove_note()
                case 'show':
                    self.core.show_entry(input('Введите ID заметки: \n'))
                case 'filter':
                    self.core.filter_notes()
                case 'list':
                    self.core.show_all()
                case 'save' :
                    self.core.save_notes()
                case _:
                    self._view.print('Команда не опознана. Для подсказки наберите help')