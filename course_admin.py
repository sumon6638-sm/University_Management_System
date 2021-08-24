from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import random
import tkinter.ttk

from subprocess import call
import university_stu_details_admin

import pymysql
import mysql.connector

class course:
    def __init__(self, root):
        self.root = root
        self.root.title("University Management System-Student Course")
        self.root.configure(background = 'gainsboro')

        MainFrame = Frame(self.root, bd=10, width=1300, height=700, bg='black', relief=RIDGE)
        MainFrame.grid()

        UpperFrame = Frame(MainFrame, bd=5, width=1300, height=500, padx=0, relief=RIDGE)
        UpperFrame.grid(row=1, column=0)

        Records_Frame = Frame(UpperFrame, bd=4, width=800, height=300, relief=RIDGE)
        Records_Frame.grid(row=0, column=0)

        Button_Frame = Frame(UpperFrame, bd = 4, width=400, height=300, relief=RIDGE)
        Button_Frame.grid(row=0,column=1)

        BoottomFrame = Frame(MainFrame, bd=7, width=1300, height=400, bg='lightgray', relief=RIDGE)
        BoottomFrame.grid(row=0, column=0)

        SubjectFrame1 = Frame(BoottomFrame, bd=5, width=680, height=250, padx=2, bg='gainsboro', relief=RIDGE)
        SubjectFrame1.grid(row=0, column=0)

        SubjectFrame2 = Frame(BoottomFrame, bd=5, width=680, height=250, padx=2, bg='gainsboro', relief=RIDGE)
        SubjectFrame2.grid(row=0, column=1)




        #===============================================Variable====================================================
        self.StudentID = StringVar()
        self.Firstname = StringVar()
        self.Surname = StringVar()

        #For Subject Area 1
        self.DBMS = StringVar()
        self.DataStructure = StringVar()
        self.DS_Sessional = StringVar()
        self.DBMS_Sessional = StringVar()
        self.Algebra = StringVar()
        self.Python_Programming = StringVar()
        self.Django_Framework = StringVar()
        self.Data_Science = StringVar()
        # For Subject Area 2=====================
        self.English = StringVar()
        self.Linear_Algebra = StringVar()
        self.Physics = StringVar()
        self.Chemistry = StringVar()
        self.Differential_Equation = StringVar()
        self.Calculas = StringVar()
        self.History = StringVar()
        self.Political_Science = StringVar()



        # =========================================View Data======================================================================
        self.student_records = ttk.Treeview(Records_Frame, columns=("studentid", "firstname", "surname"))

        self.student_records.heading("studentid", text="StudentID")
        self.student_records.heading("firstname", text="Firstname")
        self.student_records.heading("surname", text="Surname")

        self.student_records['show'] = 'headings'

        self.student_records.column("studentid", width=100)
        self.student_records.column("firstname", width=100)
        self.student_records.column("surname", width=70)

        self.student_records.pack(fill=BOTH, expand=1)
        self.student_records.bind("<ButtonRelease-1>", self.LearnersInfo)

        self.view_data()



        # =========================================Subject Area-1======================================================================
        self.lblDBMS = Label(SubjectFrame1, font=('arial', 12, 'bold'), text='DBMS', bd=7, bg='lightblue')
        self.lblDBMS.grid(row=0, column=0, sticky=W, padx=5, pady=5)

        self.cboDBMS = ttk.Combobox(SubjectFrame1, width=19, font=('arial', 12, 'bold'), state='readonly',
                                    textvariable=self.DBMS)
        self.cboDBMS['values'] = ('Core Unit', 'Yes', 'No', 'Completed')
        self.cboDBMS.current(0)
        self.cboDBMS.grid(row=0, column=1)

        self.lblDataStructure = Label(SubjectFrame1, font=('arial', 12, 'bold'), text='Data Structure', bd=7,
                                      bg='lightblue')
        self.lblDataStructure.grid(row=1, column=0, sticky=W, padx=5, pady=5)

        self.cboDataStructure = ttk.Combobox(SubjectFrame1, width=19, font=('arial', 12, 'bold'), state='readonly',
                                             textvariable=self.DataStructure)
        self.cboDataStructure['values'] = ('Core Unit', 'Yes', 'No', 'Completed')
        self.cboDataStructure.current(0)
        self.cboDataStructure.grid(row=1, column=1)

        self.lblDS_Sessional = Label(SubjectFrame1, font=('arial', 12, 'bold'), text='DS_Sessional', bd=7,
                                     bg='lightblue')
        self.lblDS_Sessional.grid(row=2, column=0, sticky=W, padx=5, pady=5)

        self.cboDS_Sessional = ttk.Combobox(SubjectFrame1, width=19, font=('arial', 12, 'bold'), state='readonly',
                                            textvariable=self.DS_Sessional)
        self.cboDS_Sessional['values'] = ('Core Unit', 'Yes', 'No', 'Completed')
        self.cboDS_Sessional.current(0)
        self.cboDS_Sessional.grid(row=2, column=1)

        self.lblDBMS_Sessional = Label(SubjectFrame1, font=('arial', 12, 'bold'), text='DBMS_Sessional', bd=7,
                                       bg='lightblue')
        self.lblDBMS_Sessional.grid(row=3, column=0, sticky=W, padx=5, pady=5)

        self.cboDBMS_Sessional = ttk.Combobox(SubjectFrame1, width=19, font=('arial', 12, 'bold'), state='readonly',
                                              textvariable=self.DBMS_Sessional)
        self.cboDBMS_Sessional['values'] = ('Core Unit', 'Yes', 'No', 'Completed')
        self.cboDBMS_Sessional.current(0)
        self.cboDBMS_Sessional.grid(row=3, column=1)

        self.lblAlgebra = Label(SubjectFrame1, font=('arial', 12, 'bold'), text='Algebra', bd=7, bg='lightblue')
        self.lblAlgebra.grid(row=4, column=0, sticky=W, padx=5, pady=5)

        self.cboAlgebra = ttk.Combobox(SubjectFrame1, width=19, font=('arial', 12, 'bold'), state='readonly',
                                       textvariable=self.Algebra)
        self.cboAlgebra['values'] = ('Core Unit', 'Yes', 'No', 'Completed')
        self.cboAlgebra.current(0)
        self.cboAlgebra.grid(row=4, column=1)

        self.lblPython_Programming = Label(SubjectFrame1, font=('arial', 12, 'bold'), text='Python_Programming', bd=7,
                                           bg='lightblue')
        self.lblPython_Programming.grid(row=5, column=0, sticky=W, padx=5, pady=5)

        self.cboPython_Programming = ttk.Combobox(SubjectFrame1, width=19, font=('arial', 12, 'bold'), state='readonly',
                                                  textvariable=self.Python_Programming)
        self.cboPython_Programming['values'] = ('Core Unit', 'Yes', 'No', 'Completed')
        self.cboPython_Programming.current(0)
        self.cboPython_Programming.grid(row=5, column=1)

        self.lblDjango_Framework = Label(SubjectFrame1, font=('arial', 12, 'bold'), text='Django_Framework', bd=7,
                                         bg='lightblue')
        self.lblDjango_Framework.grid(row=6, column=0, sticky=W, padx=5, pady=5)

        self.cboDjango_Framework = ttk.Combobox(SubjectFrame1, width=19, font=('arial', 12, 'bold'), state='readonly',
                                                textvariable=self.Django_Framework)
        self.cboDjango_Framework['values'] = ('Core Unit', 'Yes', 'No', 'Completed')
        self.cboDjango_Framework.current(0)
        self.cboDjango_Framework.grid(row=6, column=1)

        self.lblData_Science = Label(SubjectFrame1, font=('arial', 12, 'bold'), text='Data_Science', bd=7,
                                     bg='lightblue')
        self.lblData_Science.grid(row=7, column=0, sticky=W, padx=5, pady=5)

        self.cboData_Science = ttk.Combobox(SubjectFrame1, width=19, font=('arial', 12, 'bold'), state='readonly',
                                            textvariable=self.Data_Science)
        self.cboData_Science['values'] = ('Core Unit', 'Yes', 'No', 'Completed')
        self.cboData_Science.current(0)
        self.cboData_Science.grid(row=7, column=1)

        # =========================================Subject Area-2======================================================================

        self.lblEnglish = Label(SubjectFrame2, font=('arial', 12, 'bold'), text='English', bd=7, bg='lightblue')
        self.lblEnglish.grid(row=0, column=0, sticky=W, padx=5, pady=5)

        self.cboEnglish = ttk.Combobox(SubjectFrame2, width=19, font=('arial', 12, 'bold'), state='readonly',
                                       textvariable=self.English)
        self.cboEnglish['values'] = ('Core Unit', 'Yes', 'No', 'Completed')
        self.cboEnglish.current(0)
        self.cboEnglish.grid(row=0, column=1)

        self.lbLinear_Algebra = Label(SubjectFrame2, font=('arial', 12, 'bold'), text='Linear Algebra', bd=7,
                                      bg='lightblue')
        self.lbLinear_Algebra.grid(row=1, column=0, sticky=W, padx=5, pady=5)

        self.cbLinear_Algebra = ttk.Combobox(SubjectFrame2, width=19, font=('arial', 12, 'bold'), state='readonly',
                                             textvariable=self.Linear_Algebra)
        self.cbLinear_Algebra['values'] = ('Core Unit', 'Yes', 'No', 'Completed')
        self.cbLinear_Algebra.current(0)
        self.cbLinear_Algebra.grid(row=1, column=1)

        self.lblPhysics = Label(SubjectFrame2, font=('arial', 12, 'bold'), text='Physics', bd=7,
                                bg='lightblue')
        self.lblPhysics.grid(row=2, column=0, sticky=W, padx=5, pady=5)

        self.cboPhysics = ttk.Combobox(SubjectFrame2, width=19, font=('arial', 12, 'bold'), state='readonly',
                                       textvariable=self.Physics)
        self.cboPhysics['values'] = ('Core Unit', 'Yes', 'No', 'Completed')
        self.cboPhysics.current(0)
        self.cboPhysics.grid(row=2, column=1)

        self.lblChemistry = Label(SubjectFrame2, font=('arial', 12, 'bold'), text='Chemistry', bd=7,
                                  bg='lightblue')
        self.lblChemistry.grid(row=3, column=0, sticky=W, padx=5, pady=5)

        self.cboChemistry = ttk.Combobox(SubjectFrame2, width=19, font=('arial', 12, 'bold'), state='readonly',
                                         textvariable=self.Chemistry)
        self.cboChemistry['values'] = ('Core Unit', 'Yes', 'No', 'Completed')
        self.cboChemistry.current(0)
        self.cboChemistry.grid(row=3, column=1)

        self.lblDifferential_Equation = Label(SubjectFrame2, font=('arial', 12, 'bold'), text='Differential Equation',
                                              bd=7, bg='lightblue')
        self.lblDifferential_Equation.grid(row=4, column=0, sticky=W, padx=5, pady=5)

        self.cboDifferential_Equation = ttk.Combobox(SubjectFrame2, width=19, font=('arial', 12, 'bold'),
                                                     state='readonly', textvariable=self.Differential_Equation)
        self.cboDifferential_Equation['values'] = ('Core Unit', 'Yes', 'No', 'Completed')
        self.cboDifferential_Equation.current(0)
        self.cboDifferential_Equation.grid(row=4, column=1)

        self.lblCalculas = Label(SubjectFrame2, font=('arial', 12, 'bold'), text='Calculas', bd=7,
                                 bg='lightblue')
        self.lblCalculas.grid(row=5, column=0, sticky=W, padx=5, pady=5)

        self.cboCalculas = ttk.Combobox(SubjectFrame2, width=19, font=('arial', 12, 'bold'), state='readonly',
                                        textvariable=self.Calculas)
        self.cboCalculas['values'] = ('Core Unit', 'Yes', 'No', 'Completed')
        self.cboCalculas.current(0)
        self.cboCalculas.grid(row=5, column=1)

        self.lblHistory = Label(SubjectFrame2, font=('arial', 12, 'bold'), text='History', bd=7,
                                bg='lightblue')
        self.lblHistory.grid(row=6, column=0, sticky=W, padx=5, pady=5)

        self.cboHistory = ttk.Combobox(SubjectFrame2, width=19, font=('arial', 12, 'bold'), state='readonly',
                                       textvariable=self.History)
        self.cboHistory['values'] = ('Core Unit', 'Yes', 'No', 'Completed')
        self.cboHistory.current(0)
        self.cboHistory.grid(row=6, column=1)

        self.lblPolitical_Science = Label(SubjectFrame2, font=('arial', 12, 'bold'), text='Political Science', bd=7,
                                          bg='lightblue')
        self.lblPolitical_Science.grid(row=7, column=0, sticky=W, padx=5, pady=5)

        self.cboPolitical_Science = ttk.Combobox(SubjectFrame2, width=19, font=('arial', 12, 'bold'), state='readonly',
                                                 textvariable=self.Political_Science)
        self.cboPolitical_Science['values'] = ('Core Unit', 'Yes', 'No', 'Completed')
        self.cboPolitical_Science.current(0)
        self.cboPolitical_Science.grid(row=7, column=1)


        #==========================================================ButtonFrame=====================================================

        # self.btnUpdate = Button(Button_Frame, pady=1, padx=24, bd=4, font=('arial', 16, 'bold'), width=9,
        #                         text='Update', command=self.update)
        # self.btnUpdate.grid(row=0, column=0)

        self.btnStudentInfo = Button(Button_Frame, pady=1, padx=24, bd=4, font=('arial', 16, 'bold'), width=9,
                                text='Student Details', command=self.StudentInfo)
        self.btnStudentInfo.grid(row=0, column=0)



        #==================================================Function===================================================


    def view_data(self):
        sqlCon = pymysql.connect(host="localhost", user='root', password='6638', database='university_db')
        cur = sqlCon.cursor()
        cur.execute("select * from add_new_student")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.student_records.delete(*self.student_records.get_children())
            for row in rows:
                self.student_records.insert('', END, values=row)
            sqlCon.commit()
        sqlCon.close()

    def LearnersInfo(self, ev):
        viewInfo = self.student_records.focus()
        learnerData = self.student_records.item(viewInfo)
        row = learnerData['values']
        self.DBMS.set(row[9])
        self.DataStructure.set(row[10])
        self.DS_Sessional.set(row[11])
        self.DBMS_Sessional.set(row[12])
        self.Algebra.set(row[13])
        self.Python_Programming.set(row[14])
        self.Django_Framework.set(row[15])
        self.Data_Science.set(row[16])
        self.English.set(row[17])
        self.Linear_Algebra.set(row[18])
        self.Physics.set(row[19])
        self.Chemistry.set(row[20])
        self.Differential_Equation.set(row[21])
        self.Calculas.set(row[22])
        self.History.set(row[23])
        self.Political_Science.set(row[24])

    # def update(self):
    #     sqlCon = pymysql.connect(host="localhost", user='root', password='6638', database='university_db')
    #     cur = sqlCon.cursor()
    #     cur.execute(
    #         "update add_new_student set DBMS = %s, DataStructure = %s, DS_Sessional = %s, DBMS_Sessional = %s, Algebra = %s, Python_Programming = %s, Django_Framework = %s, Data_Science = %s, English = %s, Linear_Algebra = %s, Physics = %s, Chemistry = %s, Differential_Equation = %s, Calculas = %s, History = %s, Political_Science = %s  where StudentID = %s",
    #         (
    #             self.DBMS.get(),
    #             self.DataStructure.get(),
    #             self.DS_Sessional.get(),
    #             self.DBMS_Sessional.get(),
    #             self.Algebra.get(),
    #             self.Python_Programming.get(),
    #             self.Django_Framework.get(),
    #             self.Data_Science.get(),
    #             self.English.get(),
    #             self.Linear_Algebra.get(),
    #             self.Physics.get(),
    #             self.Chemistry.get(),
    #             self.Differential_Equation.get(),
    #             self.Calculas.get(),
    #             self.History.get(),
    #             self.Political_Science.get(),
    #             self.StudentID.get()))
    #
    #     sqlCon.commit()
    #     self.view_data()
    #     sqlCon.close()
    #     # self.Reset()
    #     tkinter.messagebox.showinfo("Success", "Record Successfully Updated")

    def StudentInfo(self):
        root.withdraw()
        call(["python", "university_stu_details_admin.py"])


if __name__=='__main__':
    root = Tk()
    application = course(root)
    root.mainloop()