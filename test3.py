import time

from prettytable import PrettyTable

from PIL import Image

from sqlalchemy import create_engine

from sqlalchemy.orm.session import sessionmaker

engine = create_engine('sqlite:///DataBaseForNotes3.db' , echo=True)

from sqlalchemy import Table, Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()

# class Note_Container(base):
#     __tablename__= "notes_container"
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     sub_note = relationship("Note")

class Note(base):
    __abstract__=True
    # container_id = Column(ForeignKey('notes_container.id'))
    name = Column(String)
    data = Column(String)
    time = Column(String)
    # note = relationship("Note_Container")

    def get_time(self):
         self.time = time.ctime()

    def set_data(self, data):
        self.data = data

    def print(self):
        print(self.data)

class Table_Note(Note):
    __tablename__="tablenote"
    id = Column(Integer, primary_key=True)


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


base.metadata.create_all(engine)

session = sessionmaker(bind=engine)()

print("Enter a name for new note:")
name = input()

New_Note = Table_Note()
New_Note.name = name
New_Note.create_table()
New_Note.get_time()
session.add(New_Note)
print("Enter the fields names for your table:")
field_names = input().split()
New_Note.insert_field_names(field_names)
print("Enter the rows of you table")
rows = input().split()
New_Note.insert_rows(rows)
print("Your table is:")
New_Note.print()
table_string = New_Note.data.get_string()
New_Note.data = table_string
session.commit()
q = session.query(Table_Note).filter_by(name="buba")
other_note = q.first()
other_note.print()