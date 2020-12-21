import time

from heapq import heappush as insert, heappop as extract_maximum

import tkinter as t
from tkinter.filedialog import askopenfilename
import webbrowser

from prettytable import PrettyTable

from PIL import Image


notes = []

class Note:
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

    def create_note(type,name,type2,text,filename,data,link,URL,img_path):
        print("What do you want to do: 1 - create new note, 2 - show list of existing notes, 3 - show note, 4 - edit note")
        type = int(input())
        if type == 1:
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
            
        if type2 == 6:
            print("hi brah")
            New_file = File_Note(filename,data)
            New_file.open_file(filename)
            New_file.save_note()
            New_file.print()
            print(New_file.get_data_and_time())
            
        if type2 == 7:
            print("Enter your link")
            link=input()
            New_Link = Link_Note(URL,link)
            New_Link.new_link(URL,link)
            New_Link.save_note()
            New_Link.print()
            print(New_Link.get_data_and_time())
            

class Text_Note(Note):
    def __init__(self, name, text):
        Note.__init__(self, name, text)
        pass

    def create_table(self):
        pass

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
    def __init__(self, filename,data):
        Note.__init__(self, filename,data)
        
    
    def open_file(self,filename):
        self.filename = filename
        filename = askopenfilename() 
        print(filename)

class Link_Note(Note):
    def __init__(self, name, link):
        Note.__init__(self, name, link)

    def new_link(self,URL,link):
        self.link = link
        self.URL = webbrowser.open_new(self.link) 
        
        
        

        
        



# фасад
class Facade:
    def __init__(self):
        self._note = Note(name=self,data=self)
        self._text_note = Text_Note(name=self,text=self)
        self._table_note = Table_Note(name=self,table=None)
        self._list_note = List_Note(name=self,list_heading = None, listt = None)
        # self._task_list_note = Task_List_Note()
        self._image_note = Image_Note(name=self,image=None)
        self._file_note = File_Note(filename=self,data=self)
        self._link_note = Link_Note(link=self,name=self)


    def explore(self):
        self._note.create_note(name=self,type2=self,text=self,filename=self,data=self,link=self,URL=self,img_path=self)
    


    def operation_z(type1,name,type2,text):
        pass



if __name__ == "__main__":
    facade = Facade()
    facade.explore()

