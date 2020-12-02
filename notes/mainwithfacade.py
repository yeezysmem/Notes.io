import time

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

    def create_note(self,type1,name,type2,text):
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
                print(New_Note.get_data_and_time())

class Text_Note(Note):
    def __init__(self, name, text):
        Note.__init__(self, name, text)
        pass

    def create_table(self):
        pass

class Table_Note(object):
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
    def __init__(self, name, file):
        Note.__init__(self, name, file)

class Link_Note(Note):
    def __init__(self, name, link):
        Note.__init__(self, name, link)

# фасад
class Facade:
    def __init__(self):
        self._note = Note(name=self,data=self)
        self._text_note = Text_Note(name=self,text=self)
        self._table_note = Table_Note(name=self,table=self)
        # self._list_note = List_Note()
        # self._task_list_note = Task_List_Note()
        # self._image_note = Image_Note()
        # self._file_note = File_Note()
        # self._link_note = Link_Note()
    def explore(self):
        self._note.create_note(type1=self,name=self,type2=self,text=self)
    


    def operation_z(type1,name,type2,text):
        pass



if __name__ == "__main__":
    facade = Facade()
    facade.explore()
