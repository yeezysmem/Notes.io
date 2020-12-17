import time

from heapq import heappush as insert, heappop as extract_maximum

import tkinter as t
from tkinter.filedialog import askopenfilename
import webbrowser


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
    

    def create_note(self,type,name,type2,text,type3,filename,data,link,URL):
        print("What do you want to do: 1 - create new note, 2 - show list of existing notes, 3 - show note, 4 - edit note")
        type = int(input())
        if type == 1:
            print("Enter a name for new note:")
            name = input()
            print("Select a note type number from the following pool: 1 - text, 2 - list, 3 - task list,"
              " 4 - table, 5 - image, 6 - file, 7 - link, ")
            type = int(input())
        if type == 1:
            print("Enter the text of your note:")
            text = input().split()
            New_Note = Text_Note(name, text)
            New_Note.save_note()
            print(New_Note.get_data_and_time())
            print("SSelect a note type number from the following pool: 1 - text, 2 - list, 3 - task list,"
              " 4 - table, 5 - image, 6 - file, 7 - link,")
            type = int(input())
                
        if type == 6:
            print("hi brah")
            New_file = File_Note(filename,data)
            New_file.open_file(filename)
            New_file.save_note()
            print(New_file.get_data_and_time())
        if type == 7:
            print("Enter your link")
            link=input()
            New_Link = Link_Note(URL,link)
            New_Link.new_link(URL,link)
            New_Link.save_note()
            print(New_Link.get_data_and_time())
            

class Text_Note(Note):
    def __init__(self, name, text):
        Note.__init__(self, name, text)
        pass

    def create_table(self):
        pass

class Table_Note(Note):
    def __init__(self, name, table):
        Note.__init__(self, name, table)

class List_Note(Note):
    def __init__(self, name, list):
        Note.__init__(self, name, list)

class Task_List_Note(Note):
    def __init__(self, name, list): #need to add priorities
        Note.__init__(self, name, list)

class Image_Note(Note):
    def __init__(self, name, image):
        Note.__init__(self, name, image)

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
        # self._table_note = Table_Note(name=self,table=self)
        # self._list_note = List_Note()
        # self._task_list_note = Task_List_Note()
        # self._image_note = Image_Note()
        self._file_note = File_Note(filename=self,data=self)
        self._link_note = Link_Note(link=self,name=self)


    def explore(self):
        self._note.create_note(type=self,name=self,type2=self,text=self,type3=self,filename=self,data=self,link=self,URL=self)
    


    def operation_z(type1,name,type2,text):
        pass





# def open_file():
#     global file_name
#     inp = askopenfile(mode='r')
#     if inp is None:
#         return 
#         file_name = inp.name
#     data = inp.read()
#     text.delete('1.0',END)
#     text.insert('1.0',END)

# root = Tk()
# root.title("Заметки")
# root.geometry("400x400")

# text = Text(root,width=400,height=400)
# text.pack()

# menu_bar = Menu(root)
# file_menu = Menu(menu_bar)

# file_menu.add_command(label="New",command=new_file)
# file_menu.add_command(label="Open",command=open_file)
# file_menu.add_command(label="Save as",command=save_as)
# file_menu.add_command(label="Create Note",command=create_note)

# menu_bar.add_cascade(label="Файл", menu=file_menu)

# root.config(menu=menu_bar)

# root.mainloop()    



if __name__ == "__main__":
    facade = Facade()
    facade.explore()
