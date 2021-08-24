from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import random
import tkinter.ttk

from subprocess import call
import course_admin

import pymysql
import mysql.connector

class University:
    def __init__(self, root):
        self.root = root
        self.root.title("University Management System")
        self.root.configure(background = 'gainsboro')


        MainFrame = Frame (self.root, bd = 10, width = 1450, height = 700, bg='black', relief = RIDGE)
        MainFrame.grid()

        OutterFrame = Frame(MainFrame, bd=7, width=1340, height=500, bg='lightgray', relief=RIDGE)
        OutterFrame.grid(row = 0, column = 0)



        InnerSecondFrame = Frame(OutterFrame, bd=5, width=700, height=500, padx=0, relief=RIDGE)
        InnerSecondFrame.grid(row=0, column=1)

        Records_Frame = Frame(InnerSecondFrame, bd=4, width=800, height=400, relief=RIDGE)
        Records_Frame.grid()



        BottomInnerFrame = Frame(MainFrame, bd=7, width=1340, height=300, bg='lightgray', relief=RIDGE)
        BottomInnerFrame.grid(row=2, column=0)

        InnerFrame = Frame(BottomInnerFrame, bd=5, width=600, height=500, padx=0, relief=RIDGE)
        InnerFrame.grid(row=0, column=1)

        GuidanceFrame = Frame(BottomInnerFrame, bd=5, width=400, height=250, padx=4, pady=4, bg='gainsboro',
                              relief=RIDGE)
        GuidanceFrame.grid(row=0, column=2)

        ButtonsFrame = Frame(BottomInnerFrame, bd=5, width=200, height=250, padx=4, pady=4, bg='gainsboro',
                             relief=RIDGE)
        ButtonsFrame.grid(row=0, column=3)


        #========================================Variables=======================================================
        self.StudentID = StringVar()
        self.Firstname = StringVar()
        self.Surname = StringVar()
        self.NIDNumber = StringVar()
        self.Gender  = StringVar()
        self.DOB  = StringVar()
        self.Mobile  = StringVar()
        self.Email  = StringVar()
        self.Address = StringVar()
        #For Subject Area 1================================
        self.DBMS  = StringVar()
        self.DataStructure  = StringVar()
        self.DS_Sessional  = StringVar()
        self.DBMS_Sessional  = StringVar()
        self.Algebra  = StringVar()
        self.Python_Programming  = StringVar()
        self.Django_Framework  = StringVar()
        self.Data_Science  = StringVar()
        #For Subject Area 2=====================
        self.English  = StringVar()
        self.Linear_Algebra  = StringVar()
        self.Physics  = StringVar()
        self.Chemistry  = StringVar()
        self.Differential_Equation  = StringVar()
        self.Calculas  = StringVar()
        self.History  = StringVar()
        self.Political_Science  = StringVar()
        #For Guidance==========================
        self.ParentGuidance = StringVar()
        self.pgFirstname = StringVar()
        self.pgSurname = StringVar()
        self.pgNID = StringVar()
        self.pgPhone_Number = StringVar()



        #========================================Student Details=======================================================

        DisplayFrame = Frame(InnerFrame, bd=5, width=700, height=300, bg='lightblue', relief=RIDGE)
        DisplayFrame.grid()

        self.lblStudentID = Label(DisplayFrame, font = ('arial', 12, 'bold'), text = 'Student ID', bd = 7)
        self.lblStudentID.grid(row=0, column=0, sticky = W, padx=5, pady=5)
        self.txtStudentID = Entry(DisplayFrame, font=('arial', 12, 'bold'), bd=5, width = 29, textvariable = self.StudentID)
        self.txtStudentID.grid(row=0, column=1)

        self.lblFirstname = Label(DisplayFrame, font=('arial', 12, 'bold'), text='First Name', bd=7)
        self.lblFirstname.grid(row=1, column=0, sticky = W, padx=5, pady=5)
        self.txtFirstname = Entry(DisplayFrame, font=('arial', 12, 'bold'), bd=5, width=29, textvariable = self.Firstname)
        self.txtFirstname.grid(row=1, column=1)

        self.lblSurname = Label(DisplayFrame, font=('arial', 12, 'bold'), text='Last Name', bd=7)
        self.lblSurname.grid(row=2, column=0, sticky = W, padx=5, pady=5)
        self.txtSurname = Entry(DisplayFrame, font=('arial', 12, 'bold'), bd=5, width=29, textvariable = self.Surname)
        self.txtSurname.grid(row=2, column=1)

        self.lblNID = Label(DisplayFrame, font=('arial', 12, 'bold'), text='NID Number', bd=7)
        self.lblNID.grid(row=3, column=0, sticky = W, padx=5, pady=5)
        self.txtNID = Entry(DisplayFrame, font=('arial', 12, 'bold'), bd=5, width=29, textvariable = self.NIDNumber)
        self.txtNID.grid(row=3, column=1)

        self.lblGender = Label(DisplayFrame, font=('arial', 12, 'bold'), text='Gender', bd=7)
        self.lblGender.grid(row=4, column=0, sticky = W, padx=5, pady=5)
        self.cboGender = ttk.Combobox(DisplayFrame, width=27, font=('arial', 12, 'bold'), state = 'readonly', textvariable = self.Gender)
        self.cboGender['values'] = ('', 'Female','Male')
        self.cboGender.current(0)
        self.cboGender.grid(row=4, column=1)

        self.lblDOB = Label(DisplayFrame, font=('arial', 12, 'bold'), text='DOB', bd=7)
        self.lblDOB.grid(row=5, column=0, sticky=W, padx=5, pady=5)
        self.txtDOB = Entry(DisplayFrame, font=('arial', 12, 'bold'), bd=5, width=29, textvariable = self.DOB)
        self.txtDOB.grid(row=5, column=1)

        self.lblMobile = Label(DisplayFrame, font=('arial', 12, 'bold'), text='Mobile', bd=7)
        self.lblMobile.grid(row=6, column=0, sticky=W, padx=5, pady=5)
        self.txtMobile = Entry(DisplayFrame, font=('arial', 12, 'bold'), bd=5, width=29, textvariable = self.Mobile)
        self.txtMobile.grid(row=6, column=1)

        self.lblEmail = Label(DisplayFrame, font=('arial', 12, 'bold'), text='Email', bd=7)
        self.lblEmail.grid(row=7, column=0, sticky=W, padx=5, pady=5)
        self.txtEmail = Entry(DisplayFrame, font=('arial', 12, 'bold'), bd=5, width=29, textvariable = self.Email)
        self.txtEmail.grid(row=7, column=1)

        self.lblAddress = Label(DisplayFrame, font=('arial', 12, 'bold'), text='Address', bd=7)
        self.lblAddress.grid(row=8, column=0, sticky=W, padx=5, pady=5)
        self.txtAddress = Entry(DisplayFrame, font=('arial', 12, 'bold'), bd=5, width=29, textvariable = self.Address)
        self.txtAddress.grid(row=8, column=1)


        #=====================================Student Record=============================================================
        scroll_x = Scrollbar(Records_Frame, orient = HORIZONTAL)

        scroll_x.pack(side=BOTTOM, fill=X)

        #, "ParentGuidance", 'pgfirstname', 'pgsurname', 'pgNID', 'pgPhone'
        self.student_records = ttk.Treeview(Records_Frame,  columns = ("studentid", "firstname", "surname", "nidnumber", "gender", "dob", "mobile", "email", "address"), xscrollcommand = scroll_x.set)

        self.student_records.heading("studentid", text = "StudentID")
        self.student_records.heading("firstname", text = "Firstname")
        self.student_records.heading("surname", text = "Surname")
        self.student_records.heading("nidnumber", text = "NIDnumber")
        self.student_records.heading("gender", text = "Gender")
        self.student_records.heading("dob", text = "DOB")
        self.student_records.heading("mobile", text = "Mobile")
        self.student_records.heading("email", text = "Email")
        self.student_records.heading("address", text="Address")
        # self.student_records.heading("ParentGuidance", text="Parent or Guidance")
        # self.student_records.heading("pgfirstname", text="pgFirstname")
        # self.student_records.heading("pgsurname", text="pgSurname")
        # self.student_records.heading("pgNID", text="pgNID")
        # self.student_records.heading("pgPhone", text="pgPhone_Number")


        self.student_records['show'] ='headings'

        self.student_records.column("studentid", width=75)
        self.student_records.column("firstname", width=100)
        self.student_records.column("surname", width=70)
        self.student_records.column("nidnumber", width=80)
        self.student_records.column("gender", width=70)
        self.student_records.column("dob", width=80)
        self.student_records.column("mobile", width=120)
        self.student_records.column("email", width=160)
        self.student_records.column("address", width=120)
        # self.student_records.column("ParentGuidance", width=120)
        # self.student_records.column("pgfirstname", width=80)
        # self.student_records.column("pgsurname", width=80)
        # self.student_records.column("pgNID", width=80)
        # self.student_records.column("pgPhone", width=80)

        self.student_records.pack(fill=BOTH, expand=1)
        self.student_records.bind("<ButtonRelease-1>",self.LearnersInfo)


        self.view_data()


        #=================================================Parents Details: =============================================

        self.lblGuidance = Label(GuidanceFrame, font=('arial', 12, 'bold'), text='Parent or Guidance', bd=7, bg='gainsboro')
        self.lblGuidance.grid(row=0, column=0, sticky=W, padx=5, pady=5)
        self.cboGuidance = ttk.Combobox(GuidanceFrame, width=27, font=('arial', 12, 'bold'), state='readonly', textvariable = self.ParentGuidance)
        self.cboGuidance['values'] = ('Father', 'Mother', 'Brother', 'Sister', 'Guidance')
        self.cboGuidance.current(0)
        self.cboGuidance.grid(row=0, column=1)

        self.lblFirstname = Label(GuidanceFrame, font=('arial', 12, 'bold'), text='First Name', bd=7, bg='gainsboro')
        self.lblFirstname.grid(row=1, column=0, sticky=W, padx=5, pady=5)
        self.txtFirstname = Entry(GuidanceFrame, font=('arial', 12, 'bold'), bd=5, width=29, textvariable = self.pgFirstname)
        self.txtFirstname.grid(row=1, column=1)

        self.lblSurname = Label(GuidanceFrame, font=('arial', 12, 'bold'), text='Last Name', bd=7, bg='gainsboro')
        self.lblSurname.grid(row=2, column=0, sticky=W, padx=5, pady=5)
        self.txtSurname = Entry(GuidanceFrame, font=('arial', 12, 'bold'), bd=5, width=29, textvariable = self.pgSurname)
        self.txtSurname.grid(row=2, column=1)

        self.lblNID = Label(GuidanceFrame, font=('arial', 12, 'bold'), text='NID Number', bd=7, bg='gainsboro')
        self.lblNID.grid(row=3, column=0, sticky=W, padx=5, pady=5)
        self.txtNID = Entry(GuidanceFrame, font=('arial', 12, 'bold'), bd=5, width=29, textvariable = self.pgNID)
        self.txtNID.grid(row=3, column=1)

        self.lblPhone_Number = Label(GuidanceFrame, font=('arial', 12, 'bold'), text='Phone Number', bd=7, bg='gainsboro')
        self.lblPhone_Number.grid(row=5, column=0, sticky=W, padx=5, pady=5)
        self.txtPhone_Number = Entry(GuidanceFrame, font=('arial', 12, 'bold'), bd=5, width=29, textvariable = self.pgPhone_Number)
        self.txtPhone_Number.grid(row=5, column=1)

        #=========================================Button===================================================================
        self.btnAddNew = Button(ButtonsFrame, pady=1, padx=24, bd=4, font=('arial', 16, 'bold'), width=9, text = 'Add New', command = self.add_student)
        self.btnAddNew.grid(row=0, column = 0)

        self.btnCourseDetails = Button(ButtonsFrame, pady=1, padx=24, bd=4, font=('arial', 16, 'bold'), width=9,
                                text='Course Details', command=self.course_details)
        self.btnCourseDetails.grid(row=1, column=0)

        self.btnUpdate = Button(ButtonsFrame, pady=1, padx=24, bd=4, font=('arial', 16, 'bold'), width=9,
                                text='Update', command = self.update)
        self.btnUpdate.grid(row=2, column=0)

        self.btnDelete = Button(ButtonsFrame, pady=1, padx=24, bd=4, font=('arial', 16, 'bold'), width=9,
                                text='Delete', command = self.deleteDB)
        self.btnDelete.grid(row=3, column=0)

        self.btnReset = Button(ButtonsFrame, pady=1, padx=24, bd=4, font=('arial', 16, 'bold'), width=9,
                                text='Reset', command = self.Reset)
        self.btnReset.grid(row=4, column=0)

        self.btnLogin_Page = Button(ButtonsFrame, pady=1, padx=24, bd=4, font=('arial', 16, 'bold'), width=9,
                                    text='Log Out', command=self.Login_Page)
        self.btnLogin_Page.grid(row=5, column=0)

        self.btnExit = Button(ButtonsFrame, pady=1, padx=24, bd=4, font=('arial', 16, 'bold'), width=9,
                                text='Exit', command = self.iExit)
        self.btnExit.grid(row=6, column=0)



    # ========================================Funtions=======================================================
    def add_student(self):
        if self.StudentID.get() =="" or self.Firstname.get() =='' or self.Surname.get()=="" :
            tkinter.messagebox.showerror("Enter correct student details")
        else:
            sqlCon = pymysql.connect(host="localhost", user='root', password='6638', database='university_db')
            cur =sqlCon.cursor()
            cur.execute("insert into add_new_student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (self.StudentID.get(),
                                                                                                                                                          self.Firstname.get(),
                                                                                                                                                          self.Surname.get(),
                                                                                                                                                          self.NIDNumber.get(),
                                                                                                                                                          self.Gender.get(),
                                                                                                                                                          self.DOB.get(),
                                                                                                                                                          self.Mobile.get(),
                                                                                                                                                          self.Email.get(),
                                                                                                                                                          self.Address.get(),
                                                                                                                                                          self.DBMS.get(),
                                                                                                                                                          self.DataStructure.get(),
                                                                                                                                                          self.DS_Sessional.get(),
                                                                                                                                                          self.DBMS_Sessional.get(),
                                                                                                                                                          self.Algebra.get(),
                                                                                                                                                          self.Python_Programming.get(),
                                                                                                                                                          self.Django_Framework.get(),
                                                                                                                                                          self.Data_Science.get(),
                                                                                                                                                          self.English.get(),
                                                                                                                                                          self.Linear_Algebra.get(),
                                                                                                                                                          self.Physics.get(),
                                                                                                                                                          self.Chemistry.get(),
                                                                                                                                                          self.Differential_Equation.get(),
                                                                                                                                                          self.Calculas.get(),
                                                                                                                                                          self.History.get(),
                                                                                                                                                          self.Political_Science.get(),
                                                                                                                                                          self.ParentGuidance.get(),
                                                                                                                                                          self.pgFirstname.get(),
                                                                                                                                                          self.pgSurname.get(),
                                                                                                                                                          self.pgNID.get(),
                                                                                                                                                          self.pgPhone_Number.get()
                                                                                                                                                          )
                        )
            sqlCon.commit()
            sqlCon.close()
            self.view_data()
            tkinter.messagebox.askyesno("SMS", "Record Entered Successfully")

    def view_data(self):
        sqlCon = pymysql.connect(host="localhost", user='root', password='6638', database='university_db')
        cur = sqlCon.cursor()
        cur.execute("select * from add_new_student")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.student_records.delete(*self.student_records.get_children())
            for row in rows:
                self.student_records.insert('', END, values = row)
            sqlCon.commit()
        sqlCon.close()

    def LearnersInfo(self, ev):
        viewInfo = self.student_records.focus()
        learnerData = self.student_records.item(viewInfo)
        row = learnerData['values']
        self.StudentID.set(row[0])
        self.Firstname.set(row[1])
        self.Surname.set(row[2])
        self.NIDNumber.set(row[3])
        self.Gender.set(row[4])
        self.DOB.set(row[5])
        self.Mobile.set(row[6])
        self.Email.set(row[7])
        self.Address.set(row[8])
        self.ParentGuidance.set(row[25])
        self.pgFirstname.set(row[26])
        self.pgSurname.set(row[27])
        self.pgNID.set(row[28])
        self.pgPhone_Number.set(row[29])

    def course_details(self):
        root.withdraw()
        call(["python", "course_admin.py"])





    def update(self):
        sqlCon = pymysql.connect(host="localhost", user='root', password='6638', database='university_db')
        cur = sqlCon.cursor()
        cur.execute("update add_new_student set Firstname = %s, Surname = %s, NIDNumber = %s, Gender = %s, DOB = %s, Mobile = %s, Email = %s, Address = %s, ParentGuidance = %s, pgFirstname = %s, pgSurname = %s, pgNID = %s, pgPhone_Number = %s  where StudentID = %s",(
        self.Firstname.get(),
        self.Surname.get(),
        self.NIDNumber.get(),
        self.Gender.get(),
        self.DOB.get(),
        self.Mobile.get(),
        self.Email.get(),
        self.Address.get(),
        self.ParentGuidance.get(),
        self.pgFirstname.get(),
        self.pgSurname.get(),
        self.pgNID.get(),
        self.pgPhone_Number.get(),
        self.StudentID.get()))

        sqlCon.commit()
        self.view_data()
        sqlCon.close()
        #self.Reset()
        tkinter.messagebox.showinfo("Success", "Record Successfully Updated")

    def deleteDB(self):
        sqlCon = pymysql.connect(host="localhost", user='root', password='6638', database='university_db')
        cur = sqlCon.cursor()
        cur.execute("delete from add_new_student where StudentID = %s", self.StudentID.get())

        sqlCon.commit()
        self.view_data()
        sqlCon.close()
        #self.Reset()
        tkinter.messagebox.showinfo("Delete", "Record Deleted Successfully")

    def Reset(self):
        self.StudentID.set("")
        self.Firstname.set("")
        self.Surname.set("")
        self.NIDNumber.set("")
        self.Gender.set("")
        self.DOB.set("")
        self.Mobile.set("")
        self.Email.set("")
        self.Address.set("")
        #For Subject Area 1====================
        self.DBMS.set("Core Unit")
        self.DataStructure.set("Core Unit")
        self.DS_Sessional.set("Core Unit")
        self.DBMS_Sessional.set("Core Unit")
        self.Algebra.set("Core Unit")
        self.Python_Programming.set("Core Unit")
        self.Django_Framework.set("Core Unit")
        self.Data_Science.set("Core Unit")
        #For Subject Area 2===================
        self.English.set("Core Unit")
        self.Linear_Algebra.set("Core Unit")
        self.Physics.set("Core Unit")
        self.Chemistry.set("Core Unit")
        self.Differential_Equation.set("Core Unit")
        self.Calculas.set("Core Unit")
        self.History.set("Core Unit")
        self.Political_Science.set("Core Unit")
        #For Guidance===============
        self.ParentGuidance.set("Mother")
        self.pgFirstname.set("")
        self.pgSurname.set("")
        self.pgNID.set("")
        self.pgPhone_Number.set("")

    def Login_Page(self):
        root.withdraw()
        call(["python", "Login.py"])

    def iExit(self):
        iExit = tkinter.messagebox.askyesno("School Management System", "Confirm if you want to exit")
        if iExit > 0:
            root.destroy()
            return



if __name__=='__main__':
    root = Tk()
    application = University(root)
    root.mainloop()
