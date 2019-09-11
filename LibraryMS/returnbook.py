__author__ = "ResearchInMotion"

from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox
from PIL import ImageTk , Image


con=sqlite3.connect('/Users/sahilnagpal/Desktop/library.db')
cur=con.cursor()

class ReturnBook(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x750+550+200")
        self.title("Lend Book")
        self.resizable(False,False)

        query="SELECT * FROM books WHERE book_status=1"
        books =cur.execute(query).fetchall()
        book_list=[]
        for book in books:
            book_list.append(str(book[0])+"-"+book[1])

        query2="SELECT * FROM member"
        members = cur.execute(query2).fetchall()
        member_list=[]
        for member in members:
            member_list.append(str(member[0])+"-"+member[1])
        #######################Frames#######################

        # Top Frame
        self.topFrame = Frame(self, height=150, bg='white')
        self.topFrame.pack(fill=X)
        # Bottom Frame
        self.bottomFrame = Frame(self, height=600, bg='#fcc324')
        self.bottomFrame.pack(fill=X)
        # heading, image
        self.top_image = ImageTk.PhotoImage(file='icons/addperson.png')
        top_image_lbl = Label(self.topFrame, image=self.top_image, bg='white')
        top_image_lbl.place(x=120, y=10)
        heading = Label(self.topFrame, text='  Return a Book ', font='arial 22 bold', fg='#003f8a', bg='white')
        heading.place(x=290, y=60)

        ###########################################Entries and Labels########################3

        # member name
        self.book_name = StringVar()
        self.lbl_name = Label(self.bottomFrame, text='Book: ', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_name.place(x=40, y=40)
        self.combo_name = ttk.Combobox(self.bottomFrame,textvariable=self.book_name)
        self.combo_name['values']=book_list
        self.combo_name.place(x=150,y=45)

        # phone
        self.member_name = StringVar()
        self.lbl_phone = Label(self.bottomFrame, text='Member: ', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_phone.place(x=40, y=80)
        self.combo_member = ttk.Combobox(self.bottomFrame, textvariable=self.member_name)
        self.combo_member['values']=member_list
        self.combo_member.place(x=150, y=85)

        # Button
        button = Button(self.bottomFrame, text='Return Book')
        button.place(x=220, y=120)
