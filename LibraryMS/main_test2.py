__author__ = "ResearchInMotion"

from tkinter import *
from tkinter import ttk
from tkinter import font
from PIL import ImageTk , Image
import addbook,addmember,givebook,returnbook
from tkinter import messagebox
import tkinter.messagebox as tm


import sqlite3


con=sqlite3.connect('/Users/sahilnagpal/Desktop/library.db')
cur=con.cursor()



class Main(object):
    def __init__(self,master):
        self.master = master

        def displayStatistics(evt):
            count_books = cur.execute("SELECT count(book_id) FROM books").fetchall()
            count_members = cur.execute("SELECT count(member_id) FROM member").fetchall()
            taken_books = cur.execute("SELECT count(book_status) FROM books WHERE book_status=1").fetchall()
            print(count_books)
            self.lbl_book_count.config(text='Total :' + str(count_books[0][0]) + ' books in library')
            self.lbl_member_count.config(text="Total member : " + str(count_members[0][0]))
            self.lbl_taken_count.config(text="Taken books :" + str(taken_books[0][0]))
            displayBooks(self)

        def displayBooks(self):
            books = cur.execute("SELECT * FROM books").fetchall()
            count = 0

            self.list_books.delete(0, END)
            for book in books:
                print(book)
                self.list_books.insert(count, str(book[0]) + "-" + book[1])
                count += 1

                def bookInfo(evt):
                    value = str(self.list_books.get(self.list_books.curselection()))
                    id = value.split('-')[0]
                    book = cur.execute("SELECT * FROM books WHERE book_id=?", (id,))
                    book_info = book.fetchall()
                    print(book_info)
                    self.list_details.delete(0, 'end')
                    self.list_details.insert(0, "Book Name : " + book_info[0][1])
                    self.list_details.insert(1, "Author : " + book_info[0][2])
                    self.list_details.insert(2, "Page : " + book_info[0][3])
                    self.list_details.insert(3, "Language : " + book_info[0][4])
                    if book_info[0][5] == 0:
                        self.list_details.insert(4, "Status : Avaiable")
                    else:
                        self.list_details.insert(4, "Status : Not Avaiable")

                def doubleClick(evt):
                    global given_id
                    value = str(self.list_books.get(self.list_books.curselection()))
                    given_id = value.split('-')[0]
                    give_book = GiveBook()

                self.list_books.bind('<<ListboxSelect>>', bookInfo)
                self.tabs.bind('<<NotebookTabChanged>>', displayStatistics)
                self.list_books.bind('<Double-Button-1>', doubleClick)


        # Creating the Frame
        mainFrame = Frame(self.master)
        mainFrame.pack()

        # Top Frame
        topFrame = Frame(mainFrame,width=1350, height=70, bg = '#f8f8f8' ,padx = 20 , relief = SUNKEN ,
                         borderwidth = 2)
        topFrame.pack(side = TOP,fill= X)

        # centre Frame
        centreFrame = Frame(mainFrame,width = 1350,relief = RIDGE,bg = '#e0f0f0',height = 680)
        centreFrame.pack(side = TOP )

        # centre Left Frame
        centreLeftFrame = Frame(centreFrame,width= 900,height = 700,bg ='#e0f0f0',borderwidth = 2, relief = SUNKEN)
        centreLeftFrame.pack(side = LEFT)

        # centre Right Frame
        centreRightFrame = Frame(centreFrame, width=450, height=700, bg='#e0f0f0', borderwidth=2, relief=SUNKEN)
        centreRightFrame.pack(side=LEFT)

        # search bar
        search_bar = LabelFrame(centreRightFrame,width = 440 , height = 75 , text = 'Search Box' , bg = '#9bc9ff')
        search_bar.pack(fill = BOTH)
        self.lbl_search = Label(search_bar, text='Search :', font='arial 12 bold', bg='#9bc9ff', fg='white')
        self.lbl_search.grid(row=0, column=0, padx=20, pady=10)
        self.ent_search = Entry(search_bar, width=30, bd=10)
        self.ent_search.grid(row=0, column=1, columnspan=3, padx=10, pady=10)
        self.btn_search = Button(search_bar, text='Search', font='arial 12', bg='#fcc324', fg='white',
                                 command=self.searchBooks)
        self.btn_search.grid(row=0, column=4, padx=20, pady=10)

        # list bar
        list_bar = LabelFrame(centreRightFrame, width=440, height=175, text='List Box', bg='#fcc324')
        list_bar.pack(fill=BOTH)
        lbl_list = Label(list_bar, text='Sort By', font='times 16 bold', fg='#2488ff', bg='#fcc324')
        lbl_list.grid(row=0, column=2)
        self.listChoice = IntVar()
        rb1 = Radiobutton(list_bar, text='All Books', var=self.listChoice, value=1, bg='#fcc324')
        rb2 = Radiobutton(list_bar, text='In Library', var=self.listChoice, value=2, bg='#fcc324')
        rb3 = Radiobutton(list_bar, text='Borrowed Books', var=self.listChoice, value=3, bg='#fcc324')
        rb1.grid(row=1, column=0)
        rb2.grid(row=1, column=1)
        rb3.grid(row=1, column=2)
        btn_list = Button(list_bar, text='List Books', bg='#2488ff', fg='white', font='arial 12',command=self.listBooks)
        btn_list.grid(row=1, column=3, padx=40, pady=10)

        # title and image
        image_bar = Frame(centreRightFrame, width=440, height=350)
        image_bar.pack(fill=BOTH)
        self.title_right = Label(image_bar, text='Welcome to our Library', font='arial 16 bold')
        self.title_right.grid(row=0)
        self.img_library = ImageTk.PhotoImage(file='icons/library.png')
        self.lblImg = Label(image_bar, image=self.img_library)
        self.lblImg.grid(row=1)





        #### Add Book ####

        self.iconbook = ImageTk.PhotoImage(file='icons/add_book.png')
        self.btnbook = Button(topFrame, text='Add Book', image=self.iconbook, compound=LEFT,
                              font='arial 12 bold',command=self.addBook)
        self.btnbook.pack(side=LEFT, padx=10)

        #### Add Member ####

        self.iconmember = ImageTk.PhotoImage(file='icons/users.png')
        self.btnmember = Button(topFrame, text='Add Member', font='arial 12 bold', padx=10,command=self.addMember)
        self.btnmember.configure(image=self.iconmember, compound=LEFT)
        self.btnmember.pack(side=LEFT)

        #### Give Book ####

        self.icongive = ImageTk.PhotoImage(file='icons/givebook.png')
        self.btngive = Button(topFrame, text='Give Book', font='arial 12 bold', padx=10,
                              image=self.icongive, compound=LEFT,command=self.giveBook)
        self.btngive.pack(side=LEFT)

        #### Return Book ####

        self.iconreturn = ImageTk.PhotoImage(file='icons/give_book.png')
        self.btnreturn = Button(topFrame, text='Return Book', font='arial 12 bold', padx=10,
                              image=self.iconreturn, compound=LEFT,command = self.returnbook)
        self.btnreturn.pack(side=LEFT)

######################################Tabs#########################################

                  ###############tab1###############################

        self.tabs = ttk.Notebook(centreLeftFrame,width=800,height=600)
        self.tabs.pack()
        self.tab1_icon = ImageTk.PhotoImage(file='icons/books.png')
        self.tab2_icon = ImageTk.PhotoImage(file='icons/members.png')
        self.tab1 = ttk.Frame(self.tabs)
        self.tab2 = ttk.Frame(self.tabs)
        self.tabs.add(self.tab1, text='Library Management', image=self.tab1_icon, compound=LEFT)
        self.tabs.add(self.tab2, text='Statistics', image=self.tab2_icon, compound=LEFT)

        # list books
        self.list_books = Listbox(self.tab1, width=40, height=30, bd=5, font='times 12 bold')
        self.sb = Scrollbar(self.tab1, orient=VERTICAL)
        self.list_books.grid(row=0, column=0, padx=(10, 0), pady=10, sticky=N)
        self.sb.config(command=self.list_books.yview)
        self.list_books.config(yscrollcommand=self.sb.set)
        self.sb.grid(row=0, column=0, sticky=N + S + E)

        # list details
        self.list_details = Listbox(self.tab1, width=80, height=30, bd=5, font='times 12 bold')
        self.list_details.grid(row=0, column=1, padx=(10, 0), pady=10, sticky=N)

        ##########################tab2####################################

        # statistics
        self.lbl_book_count = Label(self.tab2, text="adfafs", pady=20, font='verdana 14 bold')
        self.lbl_book_count.grid(row=0)
        self.lbl_member_count = Label(self.tab2, text="asdfadsf", pady=20, font='verdana 14 bold')
        self.lbl_member_count.grid(row=1, sticky=W)
        self.lbl_taken_count = Label(self.tab2, text="asdfdafd", pady=20, font='verdana 14 bold')
        self.lbl_taken_count.grid(row=2, sticky=W)

        # functions
        displayBooks(self)
        displayStatistics(self)

    def addBook(self):
        add = addbook.AddBook()

    def addMember(self):
        member = addmember.AddMember()

    def searchBooks(self):
        value = self.ent_search.get()
        search = cur.execute("SELECT * FROM books WHERE book_name LIKE ?", ('%' + value + '%',)).fetchall()
        print(search)
        self.list_books.delete(0, END)
        count = 0
        for book in search:
            self.list_books.insert(count, str(book[0]) + "-" + book[1])
            count += 1

    def listBooks(self):
        value = self.listChoice.get()
        if value == 1:
            allbooks = cur.execute("SELECT * FROM books").fetchall()
            self.list_books.delete(0, END)

            count = 0
            for book in allbooks:
                self.list_books.insert(count, str(book[0]) + "-" + book[1])
                count += 1

        elif value == 2:
            books_in_library = cur.execute("SELECT * FROM books WHERE book_status =?", (0,)).fetchall()
            self.list_books.delete(0, END)

            count = 0
            for book in books_in_library:
                self.list_books.insert(count, str(book[0]) + "-" + book[1])
                count += 1
        else:
            taken_books = cur.execute("SELECT * FROM books WHERE book_status =?", (1,)).fetchall()
            self.list_books.delete(0, END)

            count = 0
            for book in taken_books:
                self.list_books.insert(count, str(book[0]) + "-" + book[1])

                count += 1

    def giveBook(self):
        give_book = givebook.GiveBook()

    def returnbook(self):
        return_book = returnbook.ReturnBook()




class GiveBook(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x750+550+200")
        self.title("Lend Book")
        self.resizable(False, False)
        global given_id
        self.book_id = int(given_id)
        query = "SELECT * FROM books"
        books = cur.execute(query).fetchall()
        book_list = []
        for book in books:
            book_list.append(str(book[0]) + "-" + book[1])

        query2 = "SELECT * FROM member"
        members = cur.execute(query2).fetchall()
        member_list = []
        for member in members:
            member_list.append(str(member[0]) + "-" + member[1])
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
        heading = Label(self.topFrame, text='  Add Person ', font='arial 22 bold', fg='#003f8a', bg='white')
        heading.place(x=290, y=60)

        ###########################################Entries and Labels########################3

        # member name
        self.book_name = StringVar()
        self.lbl_name = Label(self.bottomFrame, text='Book: ', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_name.place(x=40, y=40)
        self.combo_name = ttk.Combobox(self.bottomFrame, textvariable=self.book_name)
        self.combo_name['values'] = book_list
        self.combo_name.current(self.book_id - 1)
        self.combo_name.place(x=150, y=45)

        # phone
        self.member_name = StringVar()
        self.lbl_phone = Label(self.bottomFrame, text='Member: ', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_phone.place(x=40, y=80)
        self.combo_member = ttk.Combobox(self.bottomFrame, textvariable=self.member_name)
        self.combo_member['values'] = member_list
        self.combo_member.place(x=150, y=85)

        # Button
        button = Button(self.bottomFrame, text='Lend Book', command=self.lendBook)
        button.place(x=220, y=120)

    def lendBook(self):
        book_name = self.book_name.get()
        member_name = self.member_name.get()

        if (book_name and member_name != ""):
            try:
                query = "INSERT INTO 'borrows' (bbook_id,bmember_id) VALUES(?,?)"
                cur.execute(query, (book_name, member_name))
                con.commit()
                messagebox.showinfo("Success", "Successfully added to database!", icon='info')
                cur.execute("UPDATE books SET book_status =? WHERE book_id=?", (1, self.book_id))
                con.commit()
            except:
                messagebox.showerror("Error", "Cant add to database", icon='warning')

        else:
            messagebox.showerror("Error", "Fields cant be empty", icon='warning')


class ReturnBook(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x750+550+200")
        self.title("Lend Book")
        self.resizable(False, False)
        global given_id
        self.book_id = int(given_id)
        query = "SELECT * FROM books"
        books = cur.execute(query).fetchall()
        book_list = []
        for book in books:
            book_list.append(str(book[0]) + "-" + book[1])

        query2 = "SELECT * FROM member"
        members = cur.execute(query2).fetchall()
        member_list = []
        for member in members:
            member_list.append(str(member[0]) + "-" + member[1])
        #######################Frames#######################

        # Top Frame
        self.topFrame = Frame(self, height=150, bg='white')
        self.topFrame.pack(fill=X)
        # Bottom Frame
        self.bottomFrame = Frame(self, height=600, bg='#fcc324')
        self.bottomFrame.pack(fill=X)
        # heading, image
        self.top_image = ImageTk.PhotoImage(file='icons/add_person.png')
        top_image_lbl = Label(self.topFrame, image=self.top_image, bg='white')
        top_image_lbl.place(x=120, y=10)
        heading = Label(self.topFrame, text='  Add Person ', font='arial 22 bold', fg='#003f8a', bg='white')
        heading.place(x=290, y=60)

        ###########################################Entries and Labels########################3

        # member name
        self.book_name = StringVar()
        self.lbl_name = Label(self.bottomFrame, text='Book: ', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_name.place(x=40, y=40)
        self.combo_name = ttk.Combobox(self.bottomFrame, textvariable=self.book_name)
        self.combo_name['values'] = book_list
        self.combo_name.current(self.book_id - 1)
        self.combo_name.place(x=150, y=45)

        # phone
        self.member_name = StringVar()
        self.lbl_phone = Label(self.bottomFrame, text='Member: ', font='arial 15 bold', fg='white', bg='#fcc324')
        self.lbl_phone.place(x=40, y=80)
        self.combo_member = ttk.Combobox(self.bottomFrame, textvariable=self.member_name)
        self.combo_member['values'] = member_list
        self.combo_member.place(x=150, y=85)

        # Button
        button = Button(self.bottomFrame, text='Lend Book')
        button.place(x=220, y=120)

    def returnbook(self):
        book_name=self.book_name.get()
        updated_book_name = "'%s'" % book_name
        self.book_id=book_name.split('-')[0]

        if(book_name !=""):
            try:
                cur.execute("DELETE FROM `borrows` WHERE bbook_id = ?",(updated_book_name,))
                con.commit()
                messagebox.showinfo("Success","Successfully added to database!",icon='info')
                cur.execute("UPDATE books SET book_status =? WHERE book_id=?",(0,self.book_id))
                con.commit()
                con.close()
            except:
                messagebox.showerror("Error", "Cant add to database", icon='warning')

        else:
            messagebox.showerror("Error","Fields cant be empty",icon='warning')




class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.label_username = Label(self, text="Username")
        self.label_password = Label(self, text="Password")

        self.entry_username = Entry(self)
        self.entry_password = Entry(self, show="*")

        self.label_username.grid(row=0, sticky=E)
        self.label_password.grid(row=1, sticky=E)
        self.entry_username.grid(row=0, column=1)
        self.entry_password.grid(row=1, column=1)

        self.checkbox = Checkbutton(self, text="Keep me logged in")
        self.checkbox.grid(columnspan=2)

        self.logbtn = Button(self, text="Login", command=self._login_btn_clicked)
        self.logbtn.grid(columnspan=2)

        self.pack()








def main():
    root = Tk()

    top = Toplevel()
    entry1 = Entry(top)  # Username entry
    entry2 = Entry(top)  # Password entry
    button1 = Button(top, text="Login", command=lambda: command1())  # Login button
    button2 = Button(top, text="Cancel", command=lambda: command2())  # Cancel button

    def command1():
        if entry1.get() == "user" and entry2.get() == "password":  # Checks whether username and password are correct
            messagebox.showinfo("Success", "Successfully Logged in!", icon='info')
            root.deiconify()  # Unhides the root window
            top.destroy()  # Removes the toplevel window

        else:
            messagebox.showerror("Not a Success", "Unsuccessfull Login!", icon='warning')

    def command2():
        top.destroy()  # Removes the toplevel window
        root.destroy()  # Removes the hidden root window
        sys.exit()

    entry1.pack()  # These pack the elements, this includes the items for the main window
    entry2.pack()
    button1.pack()
    button2.pack()
    font.nametofont("TkDefaultFont").actual()
    app = Main(root)
    root.title("Library Management System")
    root.geometry("1350x750+350+200")
    root.iconbitmap('icons/icon.icns')
    root.withdraw()
    root.mainloop()

if __name__ == '__main__':
    main()
