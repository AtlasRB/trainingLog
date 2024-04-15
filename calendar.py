#Imports
import tkinter as tk
from tkinter import *
from tkcalendar import *
from dates import dates1, dates2, dates3


#Set up initial screen
root = Tk()
root.title('Test')
root.geometry('800x1000')

cal = Calendar(root, selectmode='day', date_pattern="d/m/yy", background="black")
cal.grid(column=0, row=0)

#Makes dates turn colour when there is data for that date
for i in dates1.keys():
    dt = Calendar.datetime.strptime(i, "%d/%m/%y").date() #Turns dd/mm/yy format into yyyy-mm-dd format
    cal.calevent_create(date=dt, text='Hello World', tags= "Message")
    cal.tag_config("Message", background='green') #Select the colour to turn background into.

#Button to show date
def grab_date():
    if cal.get_date() in dates1: #cal.get_date() is a function that gives the selected data as a str in dd/mm/yy format.
        date = dates1[cal.get_date()] #Finds the data frame in list format of the selected date.
        my_date.config(text='\n'+str(cal.get_date())+'\n')
        my_label.config(text='\n\n'.join(map(str, date))) #Outputs the data frames on the GUI.
        if cal.get_date() in dates2: #cal.get_date() is a function that gives the selected data as a str in dd/mm/yy format.
            date = dates2[cal.get_date()] #Finds the data frame in list format of the selected date.
            my_label2.config(text='\n\n'.join(map(str, date))) #Outputs the data frames on the GUI.
            if cal.get_date() in dates3: #cal.get_date() is a function that gives the selected data as a str in dd/mm/yy format.
                date = dates3[cal.get_date()] #Finds the data frame in list format of the selected date.
                my_label3.config(text='\n\n'.join(map(str, date))) #Outputs the data frames on the GUI.
            else:
                my_label3.config(text='')
        else:
            my_label2.config(text='')
    else: 
        my_label.config(text='No data available for this date')
        my_label2.config(text='')
        my_label3.config(text='')
    
my_button = Button(root, text='Show Data', command = grab_date).grid(column=0, row=1)

my_date = Label(root, text='')
my_date.grid(column=0, row=2)

my_label = Label(root, text='')
my_label.grid(column=0, row=3, sticky=tk.N)

my_label2 = Label(root, text='')
my_label2.grid(column=1, row=3, sticky=tk.N)

my_label3 = Label(root, text='')
my_label3.grid(column=2, row=3, sticky=tk.N)

root.mainloop()