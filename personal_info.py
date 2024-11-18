from tkinter import*
import sqlite3

root=Tk()
root.title('MY PROJECT')
root.geometry("500x500")

conn=sqlite3.connect('personal_info.db')
c=conn.cursor()




def submit():
    conn=sqlite3.connect('D:/paylz_ni_maryana/OOP/personal_info.db')
    c=conn.cursor()
    c.execute ("INSERT INTO student_info VALUES(:first_name,:last_name,:age,:address,:email)",
               {
                   'first_name':first_name.get(),
                   'last_name':last_name.get(),
                   'age':age.get(),
                   'address':address.get(),
                   'email':email.get(),
                   })
    conn.commit()
    conn.close()

    first_name.delete(0,END)
    last_name.delete(0,END)
    age.delete(0,END)
    address.delete(0,END)
    email.delete(0,END)

def query():
    conn=sqlite3.connect('D:/paylz_ni_maryana/OOP/personal_info.db')
    c=conn.cursor()
    c.execute("SELECT *,oid FROM student_info")
    records=c.fetchall()

    print_records=''
    for record in records:
        print_records+=str(record[0])+" "+str(record[1])+" "+str(record[2])+" "+str(record[3])+" "+str(record[4])+" "+"\t"+str(record[5])+"\n\n"
        query_label=Label(root,text=print_records)
        query_label.grid(row=15,column=0,columnspan=2)

    conn.commit()
    conn.close()


                   
def delete():
    conn=sqlite3.connect('D:/paylz_ni_maryana/OOP/personal_info.db')
    c=conn.cursor()
    c.execute ("DELETE from student_info WHERE oid="+delete_box.get())

    delete_box.delete(0,END)

    conn.commit()
    conn.close()

def update():
    conn=sqlite3.connect('D:/paylz_ni_maryana/OOP/personal_info.db')
    c=conn.cursor()
    
    record_id=delete_box.get()
    c.execute(""" UPDATE student_info SET
        first_name=:first,
        last_name=:last,
        age=:age,
        address=:address,
        email=:email

        WHERE oid=:oid""",
              {
                  'first':first_name_editor.get(),
                  'last':last_name_editor.get(),
                  'age':age_editor.get(),
                  'address':address_editor.get(),
                  'email':email_editor.get(),
                  'oid':record_id
                  })
        
    conn.commit()
    conn.close()         
    

def edit():
    editor=Tk()
    editor.title('Update Record from database')
    editor.geometry("500x500")

    conn=sqlite3.connect('D:/paylz_ni_maryana/OOP/personal_info.db')
    c=conn.cursor()

    record_id=delete_box.get()
    c.execute("SELECT * FROM student_info WHERE oid="+record_id)
    records=c.fetchall()

    global first_name_editor
    global last_name_editor
    global age_editor
    global address_editor
    global email_editor


    first_name_editor=Entry(editor,width=30)
    first_name_editor.grid(row=0,column=1,padx=20,pady=(10,0))
    last_name_editor=Entry(editor,width=30)
    last_name_editor.grid(row=1,column=1,padx=20)
    age_editor=Entry(editor,width=30)
    age_editor.grid(row=2,column=1,padx=20)
    address_editor=Entry(editor,width=30)
    address_editor.grid(row=3,column=1,padx=20)
    email_editor=Entry(editor,width=30)
    email_editor.grid(row=4,column=1,padx=20)

    first_name_label=Label(editor,text="First Name")
    first_name_label.grid(row=0,column=0,pady=(10,0))
    last_name_label=Label(editor,text="Last Name")
    last_name_label.grid(row=1,column=0)
    age_label=Label(editor,text="Age")
    age_label.grid(row=2,column=0)
    address_label=Label(editor,text="Address")
    address_label.grid(row=3,column=0)
    email_label=Label(editor,text="Email")
    email_label.grid(row=4,column=0)
   

    for record in records:
        first_name_editor.insert(0,record[0])
        last_name_editor.insert(0,record[1])
        age_editor.insert(0,record[2])
        address_editor.insert(0,record[3])
        email_editor.insert(0,record[4])

    save_btn=Button(editor,text="Save Record",command=update)
    save_btn.grid(row=14,column=0,columnspan=2,pady=10,padx=10,ipadx=140)
    
    
    conn.commit()
    conn.close()

                

'''
c.execute("""CREATE TABLE "student_info" (
	"first_name"	TEXT,
	"last_name"	TEXT,
	"age"	INTEGER,
	"address"	TEXT,
	"email"	TEXT
)""")
'''




first_name=Entry(root,width=30)
first_name.grid(row=0,column=1,padx=20)
last_name=Entry(root,width=30)
last_name.grid(row=1,column=1,padx=20)
age=Entry(root,width=30)
age.grid(row=2,column=1,padx=20)
address=Entry(root,width=30)
address.grid(row=3,column=1,padx=20)
email=Entry(root,width=30)
email.grid(row=4,column=1,padx=20)

first_name_label=Label(root,text="First Name")
first_name_label.grid(row=0,column=0)
last_name_label=Label(root,text="Last Name")
last_name_label.grid(row=1,column=0)
age_label=Label(root,text="Age")
age_label.grid(row=2,column=0)
address_label=Label(root,text="Address")
address_label.grid(row=3,column=0)
email_label=Label(root,text="Email")
email_label.grid(row=4,column=0)

submit_btn=Button(root,text="Add Record to Database",command=submit)
submit_btn.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=110)

query_btn=Button(root,text="Show records",command=query)
query_btn.grid(row=7,column=0,columnspan=2,pady=10,padx=10,ipadx=137)

query_btn=Button(root,text="Delete Record",command=delete)
query_btn.grid(row=12,column=0,columnspan=2,pady=2,padx=10,ipadx=136)

update_btn=Button(root,text="Edit Record",command=edit)
update_btn.grid(row=8,column=0,columnspan=2,pady=2,padx=10,ipadx=136)


delete_box=Entry(root,width=30)
delete_box.grid(row=10,column=1,padx=30)

delete_box_label=Label(root,text="Select ID No.")
delete_box_label.grid(row=10,column=0)



root.mainloop()
