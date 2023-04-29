# TestWork2-Py
утилита для записок в консоли

## Задание
Реализовать консольное приложение заметки, с сохранением, чтением,
добавлением, редактированием и удалением заметок.   
Заметка должна содержать идентификатор, заголовок, тело заметки и дату/время создания или
последнего изменения заметки. Сохранение заметок необходимо сделать в
формате json или csv формат (разделение полей рекомендуется делать через
точку с запятой). Реализацию пользовательского интерфейса студент может
делать как ему удобнее, можно делать как параметры запуска программы
(команда, данные), можно делать как запрос команды с консоли и
последующим вводом данных, как-то ещё, на усмотрение студента.  
Например:

        python notes.py add --title "новая заметка" –msg "тело новой заметки"
Или так:    

        python note.py
        Введите команду: add
        Введите заголовок заметки: новая заметка
        Введите тело заметки: тело новой заметки
        Заметка успешно сохранена
        Введите команду:


При чтении списка заметок реализовать фильтрацию по дате.  
## *Критерии оценки*  
Приложение должно запускаться без ошибок, должно уметь сохранять данные
в файл, уметь читать данные из файла, делать выборку по дате, выводить на
экран выбранную запись, выводить на экран весь список записок, добавлять
записку, редактировать ее и удалять.
