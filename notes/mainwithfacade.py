import time

from prettytable import PrettyTable

# from PIL import Image
import tkinter as t
from tkinter.filedialog import askopenfilename
import webbrowser

from sqlalchemy import create_engine

from sqlalchemy.orm.session import sessionmaker

engine = create_engine('sqlite:///DataBaseForNotes.db' , echo=False)

from sqlalchemy import Column, Integer, ForeignKey, String
# from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()

# class Note_Container(base):
#     __tablename__= "notes_container"
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     sub_note = relationship("Note")

class Note(base):
    __tablename__="note"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    data = Column(String)
    type = Column(String)
    time = Column(String)
    # container_id = Column(ForeignKey('notes_container.id'))
    # note = relationship("Note_Container")

    __mapper_args__ = {'polymorphic_identity': 'note'}


    def get_time(self):
         self.time = time.ctime()

    def set_data(self, data):
        self.data = data

    def print(self):
        print(self.data)

    def delete_note(self):
        session = sessionmaker(bind=engine)()
        print("Enter the name of note you want to delete:")
        title = input()
        q = session.query(Note).filter_by(name=title).first()
        session.delete(q)
        session.commit()

class Table_Note(Note):
    __tablename__="tablenote"
    id = Column(Integer, ForeignKey('note.id'), primary_key=True)

    def set_type(self):
        self.type = "table"

    def create_table(self):
        self.data = PrettyTable()
        return self.data

    def insert_field_names(self, names):
        self.data.field_names = names

    def insert_rows(self, rows):
        self.data.add_row(rows)

    def insert_column(self, new_table):
        column = input().split()
        new_table.add_column(column)

    def create_tablenote(self):
        print("Enter a name for new note:")
        name = input()
        session = sessionmaker(bind=engine)()
        New_Note = Table_Note()
        New_Note.name = name
        New_Note.set_type()
        New_Note.create_table()
        New_Note.get_time()
        print("Enter the fields names for your table:")
        field_names = input().split()
        New_Note.insert_field_names(field_names)
        print("Enter the rows of you table")
        rows = input().split()
        New_Note.insert_rows(rows)
        table_string = New_Note.data.get_string()
        New_Note.data = table_string
        session.add(New_Note)
        session.commit()

    def show_tablenote(self):
        session = sessionmaker(bind=engine)()
        print("Enter the name of table you want to show:")
        title = input()
        q = session.query(Table_Note).filter_by(name=title)
        other_note = q.first()
        other_note.print()

class Text_Note(Note):
    __tablename__ = "textnote"
    id = Column(Integer, ForeignKey('note.id'), primary_key=True)

    def set_type(self):
        self.type = "text"
    
    def create_textnote(self):
        print("Enter a name for new note:")
        name = input()
        session = sessionmaker(bind=engine)()
        New_Note = Text_Note()
        New_Note.name = name
        New_Note.set_type()
        New_Note.get_time()
        print("Enter the text of your note:")
        text = input()
        New_Note.set_data(text)
        session.add(New_Note)
        session.commit()


class List_Note(Note):
    __tablename__ = "listnote"
    id = Column(Integer, ForeignKey('note.id'), primary_key=True)
    type = "list"
    list_heading = Column(String)
    listt = Column(String)

    def set_type(self):
        self.type = "list"

    def create_list_heading(self, heading):
        self.list_heading = heading

    def add_element(self, string):
        self.listt.append(string)

    def print(self):
        print(self.list_heading)
        for i in range(len(self.listt)):
            print(i+1,".", self.listt[i])
    
    def create_listnote(self):
        print("Enter a name for new note:")
        name = input()
        session = sessionmaker(bind=engine)()
        New_Note = List_Note()
        New_Note.name = name
        New_Note.set_type()
        New_Note.get_time()
        print("Enter the list heading:")
        heading = input()
        New_Note.create_list_heading(heading)
        print("Enter the amount of items in list:")
        num = int(input())
        for i in range(num):
            print("Enter list item:")
            item = input()
            New_Note.add_element(item)
        session.add(New_Note)
        session.commit()


class Image_Note(Note):
    __tablename__ = "imagenote"
    id = Column(Integer, ForeignKey('note.id'), primary_key=True)
    path = Column(String)


    def set_type(self):
        self.type = "image"

    def set_path(self):
        self.path = input()

    # def print(self):
    #     self.data.show()

    def import_pict_binary(self):
        f = open(self.path, "rb")
        pict_binary = f.read()
        self.data = pict_binary

    def create_imagenote(self):
        print("Enter a name for new note:")
        name = input()
        session = sessionmaker(bind=engine)()
        New_Note = Image_Note()
        New_Note.name = name
        New_Note.set_type()
        New_Note.get_time()
        print("Enter the path to your image:")
        New_Note.import_pict_binary()
        session.add(New_Note)
        session.commit()



class File_Note(Note):
    __tablename__ = "filenote"
    id = Column(Integer, ForeignKey('note.id'), primary_key=True)
    path = Column(String)

    def set_type(self):
        self.type = "file"

    def import_file_binary(self):
        self.path = input()
        f = open(self.path, "rb")
        file_binary = f.read()
        self.data = file_binary

    def create_filenote(self):
        print("Enter a name for new note:")
        name = input()
        session = sessionmaker(bind=engine)()
        New_Note = File_Note()
        New_Note.name = name
        New_Note.set_type()
        New_Note.get_time()
        print("Enter the path to your file:")
        New_Note.import_file_binary()
        session.add(New_Note)
        session.commit()




class Link_Note(Note):
    __tablename__ = "linknote"
    id = Column(Integer, ForeignKey('note.id'), primary_key=True)

    def set_type(self):
        self.type = "link"


    def new_URL(self):
        self.data = input()

    def follow_the_link(self):
        webbrowser.open_new(self.data)
    
    def create_linknote(self):
        print("Enter a name for new note:")
        name = input()
        session = sessionmaker(bind=engine)()
        New_Note = Link_Note()
        New_Note.name = name
        New_Note.set_type()
        New_Note.get_time()
        print("Enter a link to save in note:")
        New_Note.new_URL()
        session.add(New_Note)
        session.commit()



base.metadata.create_all(engine)





















# def show_all_notes():
#     session = sessionmaker(bind=engine)()
#     q = session.query(Note).all()
#     for i in range(len(q)):
#

# def edit_note():
#     pass




class Facade(object):
    def __init__(self):
        self._note = Note()
        self._tablenote = Table_Note()
        self._textnote = Text_Note()
        self._listnote = List_Note()
        self._imagenote = Image_Note()
        self._filenote = File_Note()
        self._linknote = Link_Note()

    def subsystem(self):
        # self._tablenote.create_tablenote()
        # self._textnote.create_textnote()
        # self._listnote.create_listnote()
        # self._imagenote.create_imagenote()
        # self._filenote.create_filenote()
        # self._tablenote.show_tablenote()
        self._linknote.create_linknote()
        self._linknote.new_URL()
        self._linknote.follow_the_link()
        
        
        
        
        
        
        
        

# Клиентская часть
if __name__ == "__main__":
    facade = Facade()
    facade.subsystem()
# /Users/vadimarko/Desktop/Exams.png





# create_tablenote()
# show_tablenote()



# class Note_Container():
# #     def __init__(self, name):
# #         self.name = name
# #         self.objects = []
# #
# #     def add_object(self, object):
# #         self.objects.append(object)



