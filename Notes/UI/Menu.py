from Notes.Core.Note import Note


class Menu:
    def __init__(self):
        pass

    def intro(self):
        print("Вы открыли утилиту заметок")
        self.help()

    def help(self):
        print("Доступны следующие команды:")
        print('\t help - вывод данной справки')
        print('\t exit - завершение программы')
        print('\t add  - добавить новую заметку')
        print('\t edit - редактировать заметку')
        print('\t del  - удалить заметку')
        print('\t list - вывод полного списка заметок')
        print('\t show - вывод одной заметки')
        print('\t filter - фильтрация вывода по дате')

    def com_success(self):
        print("Команда выполнена успешно")

    def com_error(self, error):
        print(f"Команду не удалось выполнить, {error}")

    def display(self, entry_list :dict):
        print("===================================================================")
        if isinstance(entry_list, Note):
            print(str(entry_list))
        else:
            for e in entry_list.values():
                print(str(e))
                print("------------------------------------------")
        print("\n")


    def unknown(self):
        print('Команда не опознана. Для подсказки наберите help')

    def outro(self):
        print("Программа завершена. Спасибо за использование!")

    def getTitle(self):
        return input('Введите заголовок:\n')

    def getBody(self):
        return input('Введите текст заметки:\n')

    def getId(self):
        return input('Введите ID заметки: ')