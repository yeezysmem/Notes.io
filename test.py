import time

from prettytable import PrettyTable

from PIL import Image

import numpy as np

import PIL.Image, PIL.ImageTk

import tkinter

import cv2

import webbrowser

from sqlalchemy import create_engine

from sqlalchemy.orm.session import sessionmaker

import subprocess, platform


engine = create_engine('sqlite:///DataBaseForNotes.db' , echo=False)

from sqlalchemy import Column, Integer, ForeignKey, String
# from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

import ast

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

class Text_Note(Note):
    __tablename__ = "textnote"
    id = Column(Integer, ForeignKey('note.id'), primary_key=True)

    def set_type(self):
        self.type = "text"


class List_Note(Note):
    __tablename__ = "listnote"
    id = Column(Integer, ForeignKey('note.id'), primary_key=True)

    def set_type(self):
        self.type = "list"
        self.data = []


    def add_element(self, number):
        string = input()
        num = str(number) + '.'
        element = str(num + string)
        self.data.append(element)


    def print(self):
        print(self.data)


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



class File_Note(Note):
    __tablename__ = "filenote"
    id = Column(Integer, ForeignKey('note.id'), primary_key=True)
    # path = Column(String)

    def set_type(self):
        self.type = "file"

    def save_file_path(self):
        self.data = input()

    # def import_file_binary(self):
    #     f = open(self.path, "rb")
    #     file_binary = f.read()
    #     self.data = file_binary



class Link_Note(Note):
    __tablename__ = "linknote"
    id = Column(Integer, ForeignKey('note.id'), primary_key=True)

    def set_type(self):
        self.type = "link"

    def new_URL(self):
        self.data = input()

    def follow_the_link(self):
        webbrowser.open_new(self.data)


base.metadata.create_all(engine)


def create_tablenote():
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

def create_textnote():
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

def create_listnote():
    print("Enter a name for new note:")
    name = input()
    session = sessionmaker(bind=engine)()
    New_Note = List_Note()
    New_Note.name = name
    New_Note.set_type()
    New_Note.get_time()
    print("Enter the amount of items in list:")
    num = int(input())
    for i in range(num):
        print("Enter the list element:")
        New_Note.add_element(i+1)
    New_Note.data = str(New_Note.data)
    session.add(New_Note)
    session.commit()

def create_imagenote():
    print("Enter a name for new note:")
    name = input()
    session = sessionmaker(bind=engine)()
    New_Note = Image_Note()
    New_Note.name = name
    New_Note.set_type()
    New_Note.get_time()
    print("Enter the path to your image:")
    New_Note.set_path()
    New_Note.import_pict_binary()
    session.add(New_Note)
    session.commit()


def create_filenote():
    print("Enter a name for new note:")
    name = input()
    session = sessionmaker(bind=engine)()
    New_Note = File_Note()
    New_Note.name = name
    New_Note.set_type()
    New_Note.get_time()
    print("Enter the path to your file:")
    New_Note.save_file_path()
    session.add(New_Note)
    session.commit()


def create_linknote():
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


def delete_note():
    session = sessionmaker(bind=engine)()
    print("Enter the name of note you want to delete:")
    title = input()
    q = session.query(Note).filter_by(name=title).first()
    session.delete(q)
    session.commit()

# def show_all_notes():
#     session = sessionmaker(bind=engine)()
#     q = session.query(Note).all()
#     for i in range(len(q)):
#

def edit_note():
    pass


def show_tablenote():
    session = sessionmaker(bind=engine)()
    print("Enter the name of table you want to show:")
    title = input()
    q = session.query(Table_Note).filter_by(name=title)
    other_note = q.first()
    other_note.print()


def show_listnote():
    session = sessionmaker(bind=engine)()
    print("Enter the name of list you want to show:")
    title = input()
    q = session.query(List_Note).filter_by(name=title)
    other_note = q.first()
    string = other_note.data
    arr = ast.literal_eval(string)
    arr = [n.strip() for n in arr]
    for i in arr:
        print(i)


def show_imagenote():
    session = sessionmaker(bind=engine)()
    print("Enter the name of image note you want to show:")
    title = input()
    q = session.query(Image_Note).filter_by(name=title)
    other_note = q.first()
    image = other_note.data
    nparr = np.fromstring(image, np.uint8)
    cv_img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    window = tkinter.Tk()
    height, width, no_channels = cv_img.shape
    canvas = tkinter.Canvas(window, width=width, height=height)
    canvas.pack()
    photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
    canvas.create_image(0, 0, image=photo, anchor=tkinter.NW)
    window.mainloop()


def show_filenote():
    session = sessionmaker(bind=engine)()
    print("Enter the name of file note you want to show and open:")
    title = input()
    q = session.query(File_Note).filter_by(name=title)
    other_note = q.first()
    file_path = other_note.data
    if platform.system() == 'Darwin':  # macOS
        subprocess.call(('open', file_path))
    # elif platform.system() == 'Windows':  # Windows
    #     os.startfile(file_path)
    else:  # linux variants
        subprocess.call(('xdg-open', file_path))


def show_textnote():
    session = sessionmaker(bind=engine)()
    print("Enter the name of text note you want to show:")
    title = input()
    q = session.query(Text_Note).filter_by(name=title)
    other_note = q.first()
    print(other_note.data)


def show_linknote():
    session = sessionmaker(bind=engine)()
    print("Enter the name of link note you want to show:")
    title = input()
    q = session.query(Link_Note).filter_by(name=title)
    other_note = q.first()
    other_note.follow_the_link()






# /Users/vadimarko/Desktop/Exams.png
# /Users/vadimarko/Desktop/studying/Essay.docx





create_tablenote()
show_tablenote()

create_textnote()
show_textnote()
#
create_linknote()
show_linknote()
#
create_imagenote()
show_imagenote()

create_filenote()
show_filenote()

create_listnote()
show_listnote()


# class Note_Container():
# #     def __init__(self, name):
# #         self.name = name
# #         self.objects = []
# #
# #     def add_object(self, object):
# #         self.objects.append(object)



