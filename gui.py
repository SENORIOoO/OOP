from tkinter import *
import sqlite3


root = Tk()
root.title('LIBRARY MANAGEMENT SYSTEM')
root.geometry("490x700")
root.config(bg="#f0f8ff") 

conn = sqlite3.connect('login.db')
c = conn.cursor()


title_label = Label(root, text="LIBRARY MANAGEMENT SYSTEM", bg="#f0f8ff", font=("Arial", 22, "bold"))
title_label.grid(row=0, column=0, columnspan=4, pady=20)

def submit():
    conn = sqlite3.connect('login.db')
    c = conn.cursor()
    c.execute("INSERT INTO book VALUES(:id,:Title,:Publication_date,:Author,:Status)", {
        'id': id.get(),
        'Title': Title.get(),
        'Publication_date': Publication_date.get(),
        'Author': Author.get(),
        'Status': Status.get(),
    })
    conn.commit()
    conn.close()

  
    id.delete(0, END)
    Title.delete(0, END)
    Publication_date.delete(0, END)
    Author.delete(0, END)
    Status.delete(0, END)


def query():
    conn = sqlite3.connect('login.db')
    c = conn.cursor()
    c.execute("SELECT *, oid FROM book")
    records = c.fetchall()


    query_frame = Frame(root, bg="#E5E5E2")
    query_frame.grid(row=12, column=0, columnspan=4, pady=20)

 
    Label(query_frame, text="Book ID", font=("Arial", 10, "bold")).grid(row=0, column=0, padx=10)
    Label(query_frame, text="Title", font=("Arial", 10, "bold")).grid(row=0, column=1, padx=10)
    Label(query_frame, text="Publication Date", font=("Arial", 10, "bold")).grid(row=0, column=2, padx=10)
    Label(query_frame, text="Author", font=("Arial", 10, "bold")).grid(row=0, column=3, padx=10)
    Label(query_frame, text="Status", font=("Arial", 10, "bold")).grid(row=0, column=4, padx=10)

  
    for idx, record in enumerate(records):
        Label(query_frame, text=record[0], font=("Arial", 9)).grid(row=idx+1, column=0, padx=10)
        Label(query_frame, text=record[1], font=("Arial", 9)).grid(row=idx+1, column=1, padx=10)
        Label(query_frame, text=record[2], font=("Arial", 9)).grid(row=idx+1, column=2, padx=10)
        Label(query_frame, text=record[3], font=("Arial", 9)).grid(row=idx+1, column=3, padx=10)
        Label(query_frame, text=record[4], font=("Arial", 9)).grid(row=idx+1, column=4, padx=10)

     
        edit_btn = Button(query_frame, text="Edit", command=lambda record_id=record[5]: edit(record_id), bg="#4CAF50", fg="white")
        edit_btn.grid(row=idx+1, column=5, padx=5)

        delete_btn = Button(query_frame, text="Delete", command=lambda record_id=record[5]: delete(record_id), bg="#f44336", fg="white")
        delete_btn.grid(row=idx+1, column=6, padx=5)

    conn.commit()
    conn.close()


def delete(record_id):
    conn = sqlite3.connect('login.db')
    c = conn.cursor()
    c.execute("DELETE FROM book WHERE oid=?", (record_id,))
    conn.commit()
    conn.close()

    query()
    
def update(record_id):
    conn = sqlite3.connect('login.db')
    c = conn.cursor()

    c.execute("""UPDATE book SET
        id=:id,
        Title=:Title,
        Publication_date=:Publication_date,
        Author=:Author,
        Status=:Status
        WHERE oid=:oid""", {
        'id': id_editor.get(),
        'Title': Title_editor.get(),
        'Publication_date': Publication_date_editor.get(),
        'Author': Author_editor.get(),
        'Status': Status_editor.get(),
        'oid': record_id
    })

    conn.commit()
    conn.close()


def edit(record_id):
    editor = Tk()
    editor.title('Update Record')
    editor.geometry("500x500")
    editor.config(bg="#f0f8ff")

    conn = sqlite3.connect('login.db')
    c = conn.cursor()
    c.execute("SELECT * FROM book WHERE oid=?", (record_id,))
    record = c.fetchone()

    global id_editor, Title_editor, Publication_date_editor, Author_editor, Status_editor
    id_editor = Entry(editor, width=30)
    id_editor.grid(row=0, column=1, padx=20, pady=10)
    Title_editor = Entry(editor, width=30)
    Title_editor.grid(row=1, column=1, padx=20)
    Publication_date_editor = Entry(editor, width=30)
    Publication_date_editor.grid(row=2, column=1, padx=20)
    Author_editor = Entry(editor, width=30)
    Author_editor.grid(row=3, column=1, padx=20)
    Status_editor = Entry(editor, width=30)
    Status_editor.grid(row=4, column=1, padx=20)

    id_label = Label(editor, text="Book ID", bg="#f0f8ff")
    id_label.grid(row=0, column=0, pady=10)
    Title_label = Label(editor, text="Title", bg="#f0f8ff")
    Title_label.grid(row=1, column=0, pady=10)
    Publication_date_label = Label(editor, text="Publication Date", bg="#f0f8ff")
    Publication_date_label.grid(row=2, column=0, pady=10)
    Author_label = Label(editor, text="Author", bg="#f0f8ff")
    Author_label.grid(row=3, column=0, pady=10)
    Status_label = Label(editor, text="Status", bg="#f0f8ff")
    Status_label.grid(row=4, column=0, pady=10)

 
    id_editor.insert(0, record[0])
    Title_editor.insert(0, record[1])
    Publication_date_editor.insert(0, record[2])
    Author_editor.insert(0, record[3])
    Status_editor.insert(0, record[4])

    save_btn = Button(editor, text="Save Record", command=lambda: update(record_id), bg="#4CAF50", fg="white")
    save_btn.grid(row=5, column=0, columnspan=2, pady=20, padx=20, ipadx=140)

    conn.commit()
    conn.close()

id_label = Label(root, text="Book ID", bg="#f0f8ff")
id_label.grid(row=1, column=0, pady=10, sticky="nsew")
id = Entry(root, width=30)
id.grid(row=1, column=1, padx=20, sticky="nsew")

Title_label = Label(root, text="Title", bg="#f0f8ff")
Title_label.grid(row=2, column=0, pady=10, sticky="nsew")
Title = Entry(root, width=30)
Title.grid(row=2, column=1, padx=20, sticky="nsew")

Publication_date_label = Label(root, text="Publication Date", bg="#f0f8ff")
Publication_date_label.grid(row=3, column=0, pady=10, sticky="nsew")
Publication_date = Entry(root, width=30)
Publication_date.grid(row=3, column=1, padx=20, sticky="nsew")

Author_label = Label(root, text="Author", bg="#f0f8ff")
Author_label.grid(row=4, column=0, pady=10, sticky="nsew")
Author = Entry(root, width=30)
Author.grid(row=4, column=1, padx=20, sticky="nsew")

Status_label = Label(root, text="Status", bg="#f0f8ff")
Status_label.grid(row=5, column=0, pady=10, sticky="nsew")
Status = Entry(root, width=30)
Status.grid(row=5, column=1, padx=20, sticky="nsew")


submit_btn = Button(root, text="Add Record to Database", command=submit, bg="#4CAF50", fg="white")
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=110)

query_btn = Button(root, text="Show records", command=query, bg="#4CAF50", fg="white")
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

root.mainloop()


