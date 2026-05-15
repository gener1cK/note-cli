import json

class NotesList:

    def __init__(self):
        self.notes = []

    def

    def show_notes(self):
        for index, note in enumerate(self.notes, start=1):
            print(f'{index}: {note}')

    def add_note(self, new_note):
        self.notes.append(new_note)

    def delete_note(self, note_index):
        try:
            self.notes.pop(note_index - 1)
        except IndexError:
            print('Index out of range!')

    def change_note(self, note_index, new_note):
        try:
            self.notes[note_index - 1] = new_note
        except IndexError:
            print('Index out of range!')
            return False

note_list = NotesList()

while True:
    try:
        script_selection = int(input('''Выберите сценарий:
        \n1 - просмотреть заметки 
        \n2 - пополнить заметки 
        \n3 - удалить заметку 
        \n4 - изменить заметку 
        \n0 - завершить работу
        \nВаш сценарий -  '''))
    except ValueError:
        print('Введите число!')
        continue

    if script_selection == 1:
        note_list.show_notes()

    elif script_selection == 2:
        get_note = input('Введите заметку: ')
        note_list.add_note(get_note)
        note_list.show_notes()

    elif script_selection == 3:
        note_list.show_notes()
        print('Удаление заметки')

        while True:
            try:
                get_index = int(input('Введите номер удаляемой заметки: '))
                note_list.delete_note(get_index)
                note_list.show_notes()
                break

            except ValueError:
                print('Введите число!')
                continue

    elif script_selection == 4:
        note_list.show_notes()
        print('Изменение заметки!')

        while True:
            try:
                get_index = int(input('Введи номер изменяемой заметки: '))
                break
            except ValueError:
                print('Введите число!')

        get_note = input('Введите новую заметку: ')
        note_list.change_note(get_index, get_note)
        note_list.show_notes()

    else:
        break