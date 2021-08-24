import tkinter as tk
from tkinter import *
from tkinter import font
from tkinter.font import BOLD
import tkinter.messagebox as mb
import random
import tkinter.ttk
from PIL import ImageTk,Image
import webbrowser

from subprocess import call
import university_stu_details_admin

import mysql.connector  # mysql connector imported

class StartingPage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Port City International University")
        self.geometry("600x450+482+135")
        self.configure(bg="#000000")

        self.lblHeading = tk.Label(self, text="Welcome to Port City International University", font=("Helvetica", 15), bg="black",
                                   fg="lightblue")

        self.btn_home = tk.Button(self, text="HOME", font=("Helvetica", 16), bg="black", fg="green", command=self.home)
        self.btn_faculty = tk.Button(self, text="Faculty and Department", font=("Helvetica", 16), bg="black", fg="green", command=self.faculty)
        self.btn_lab = tk.Button(self, text="LAB", font=("Helvetica", 16), bg="black", fg="green", command=self.lab)
        self.btn_teachers = tk.Button(self, text="Teacher's List", font=("Helvetica", 16), bg="black", fg="green", command=self.teachers)

        self.btn_login = tk.Button(self, text="Login", font=("Helvetica", 16), bg="black", fg="red", command=self.login_page)
        self.btn_contact = tk.Button(self, text="Contact US", font=("Helvetica", 16), bg="black", fg="red", command = self.contact)
        self.btn_exit = tk.Button(self, text="Exit", font=("Helvetica", 16), bg="black", fg="red", command=self.exit)

        self.lblHeading.place(relx=0.18, rely=0.089, height=50, width=450)

        self.btn_home.place(relx=0.31, rely=0.289, height=30, width=250)
        self.btn_faculty.place(relx=0.31, rely=0.389, height=30, width=250)
        self.btn_lab.place(relx=0.31, rely=0.489, height=30, width=250)
        self.btn_teachers.place(relx=0.31, rely=0.589, height=30, width=250)


        self.btn_login.place(relx=0.31, rely=0.789, height=30, width=250)
        self.btn_contact.place(relx=0.20, rely=0.911, height=24, width=120)
        self.btn_exit.place(relx=0.75, rely=0.911, height=24, width=61)


    def home(self):
        webbrowser.open('http://www.portcity.edu.bd/')

    def faculty(self):
        webbrowser.open('http://www.portcity.edu.bd/HomePage/ListPrimary/8/C/academic-faculty-and-department')

    def lab(self):
        webbrowser.open('http://www.portcity.edu.bd/HomePage/ListPrimary/57/C/facilities-lab')

    def teachers(self):
        webbrowser.open('http://portcity.edu.bd/HomePage/ListPrimary/9/T/view-teacher-list')

    def contact(self):
        webbrowser.open('http://www.portcity.edu.bd/HomePage/SubPageDetailsPara/12/Page/contact-us')

    def login_page(self):
        self.withdraw()
        call(["python", "Login.py"])

    def exit(self):
        MsgBox = mb.askquestion('Exit Application', 'Are you sure you want to exit the application', icon='warning')
        if MsgBox == 'yes':
            self.destroy()

if __name__ == "__main__":
    app = StartingPage()
    app.mainloop()