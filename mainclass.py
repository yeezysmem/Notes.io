import time

import sqlite3

from prettytable import PrettyTable

from PIL import Image

notes = []

def sqlite3_create_db():
    con = sqlite3.connect("./DataBaseForNotes.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS")


class Note_Container():
    def __init__(self, name):
        self.name = name
        self.objects = []

    def add_object(self, object):
        self.objects.append(object)




class Note():
    def __init__(self, name, data):
        self.name = name
        self.data = data
        self.time = time.time()

    def set_name(self, name):
        self.name = name

    def get_time(self):
        return time.ctime(self.time)

    def set_data(self, data):
        self.data = data

    def save_note(self):
        arr = [self.name, self.data, self.time]
        notes.append(arr)

    def get_data_and_time(self):
        for i in range(len(notes)):
            temp = notes[i]
            if self.name == temp[0]:
                return self.data, self.get_time()

    def print(self):
        print(self.data)

class Text_Note(Note):
    def __init__(self, name, text):
        Note.__init__(self, name, text)


class Table_Note(Note):
    def __init__(self, name, table = None):
        Note.__init__(self, name, table)

    def create_table(self):
        self.table = PrettyTable()
        return self.table

    def insert_field_names(self, names):
        self.table.field_names = names

    def insert_rows(self, rows):
        self.table.add_row(rows)

    def insert_column(self, new_table):
        column = input().split()
        new_table.add_column(column)

    def print(self):
        print(self.table)


class List_Note(Note):
    def __init__(self, name, list_heading = None, listt = None):
        Note.__init__(self, name, listt)
        self.list_heading = list_heading
        self.listt = []

    def create_list_heading(self, heading):
        self.list_heading = heading

    def add_element(self, string):
        self.listt.append(string)

    def print(self):
        print(self.list_heading)
        for i in range(len(self.listt)):
            print(i+1,".", self.listt[i])


class Task_List_Note(Note):
    def __init__(self, name, list): #need to add priorities
        Note.__init__(self, name, list)

class Image_Note(Note):
    def __init__(self, name, image = None):
        Note.__init__(self, name, image)

    def choose_img(self, path):
        self.image = Image.open(path)
        return self.image

    def print(self):
        self.image.show()

class File_Note(Note):
    def __init__(self, name, file):
        Note.__init__(self, name, file)

class Link_Note(Note):
    def __init__(self, name, link):
        Note.__init__(self, name, link)


if __name__ == "__main__":
    print("What do you want to do: 1 - create new note, 2 - show list of existing notes, 3 - show note, 4 - edit note")
    type1 = int(input())
    if type1 == 1:
        print("Enter a name for new note:")
        name = input()
        print("Select a note type number from the following pool: 1 - text, 2 - list, 3 - task list,"
              " 4 - table, 5 - image, 6 - file, 7 - link, ")
        type2 = int(input())
        if type2 == 1:
            print("Enter the text of your note:")
            text = input().split()
            New_Note = Text_Note(name, text)
            New_Note.save_note()
            New_Note.print()

        if type2 == 2:
            New_Note = List_Note(name)
            print("Enter the heading of your list")
            heading = input()
            New_Note.create_list_heading(heading)
            print("How many elements will be in your list?:")
            quantity = int(input())
            for i in range(quantity):
                print("Enter the element of your list with number", i+1)
                stringg = input()
                New_Note.add_element(stringg)
            print("Your list is:")
            New_Note.print()

        if type2 == 4:
            New_Note = Table_Note(name)
            New_Note.create_table()
            print("Enter the fields names for your table:")
            field_names = input().split()
            New_Note.insert_field_names(field_names)
            print("Enter the rows of you table")
            rows = input().split()
            New_Note.insert_rows(rows)
            print("Your table is:")
            New_Note.print()

        if type2 == 5:
            print("Enter the path to your image:")
            img_path = input()
            New_Note = Image_Note(name)
            New_Note.choose_img(img_path)
            New_Note.print()
            print("Your image is currently displaying on your screen")


