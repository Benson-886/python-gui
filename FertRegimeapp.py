from tkinter import *
import collections
from collections import Counter
collections.Callable = collections.abc.Callable
import Pmw
import time
from PIL import Image,ImageTk
root = Tk()
from tkinter import messagebox
root.option_readfile('optionDB.txt')
Pmw.initialise()
root.title("Fertigation ppm app")
root.iconbitmap(default='myapp.ico')
from tkinter import simpledialog
import threading
import re
import PyPDF2
from tkinter import filedialog
import glob
from tkPDFViewer import tkPDFViewer as pdf
from tkinter import ttk
from tkinter.filedialog import asksaveasfile
from tkinter import ttk
import calendar
from tkcalendar import Calendar
balloon = Pmw.Balloon(root)
import numpy
import pandas as pd
import io
import subprocess
import pdfrw
from reportlab.pdfgen import canvas
import os

from pdfrw import PdfReader
from pdfrw.buildxobj import pagexobj
from pdfrw.toreportlab import makerl
from reportlab.lib.units import inch, cm
from reportlab.pdfbase import pdfdoc

### convert png to ico file
##from PIL import Image
##
##filename = r'myapp.png'
##img = Image.open(filename)
##
##img.save('myapp.ico',format = 'ICO', sizes=[(32,32)])
##


root.geometry("1250x700")
root.minsize(width=1100, height=700)

my_menu = Menu(root)
root.config(menu=my_menu)

frame = Frame(root)
text = Text(frame)
text2 = Text(text)
frame2 = Frame(frame)
label = Label(text)
label2 = Label(root)
frame3 = Frame(root)
frame4 = Frame(text)

frame = Frame(root, height=455, width=550)
frame.pack(expand=True, fill=BOTH)

#Validate entry

def digits_only(*args):
    global text1, text2, text3, text4, text5, text6, text7
    global text8, text9, text10, text11, text12, text13, text14, text15, text16
    
    global last_string1, last_string2, last_string3, last_string4
    global last_string5, last_string6, last_string7, last_string8
    global last_string9, last_string10, last_string11, last_string12
    global last_string13, last_string14, last_string15, last_string16
    string1 = text1.get()
    string2 = text2.get()
    string3 = text3.get()
    string4 = text4.get()
    string5 = text5.get()
    string6 = text6.get()
    string7 = text7.get()
    string8 = text8.get()
    string9 = text9.get()
    string10 = text10.get()
    string11 = text11.get()
    string12 = text12.get()
    string13 = text13.get()
    string14 = text14.get()
    string15 = text15.get()
    string16 = text16.get()
    if string1.replace('.', '').replace('', '0').replace('-', '').isdigit():  # Field's content is valid.
        last_string1 = string1
        if string2.replace('.', '').replace('', '0').replace('-', '').isdigit(): # Field's content is valid.
            last_string2 = string2
            if string3.replace('.', '').replace('', '0').replace('-', '').isdigit():  # Field's content is valid.
                last_string3 = string3
                if string4.replace('.', '').replace('', '0').replace('-', '').isdigit():  # Field's content is valid.
                    last_string4 = string4
                    if string5.replace('.', '').replace('', '0').replace('-', '').isdigit():  # Field's content is valid.
                        last_string5 = string5
                        if string6.replace('.', '').replace('', '0').replace('-', '').isdigit():  # Field's content is valid.
                            last_string6 = string6
                            if string7.replace('.', '').replace('', '0').replace('-', '').isdigit():  # Field's content is valid.
                                last_string7 = string7
                                if string8.replace('.', '').replace('', '0').replace('-', '').isdigit():  # Field's content is valid.
                                    last_string8 = string8
                                    if string9.replace('.', '').replace('', '0').replace('-', '').isdigit():  # Field's content is valid.
                                        last_string9 = string9
                                        if string10.replace('.', '').replace('', '0').replace('-', '').isdigit():  # Field's content is valid.
                                            last_string10 = string10
                                            if string11.replace('.', '').replace('', '0').replace('-', '').isdigit(): # Field's content is valid.
                                                last_string11 = string11
                                                if string12.replace('.', '').replace('', '0').replace('-', '').isdigit():  # Field's content is valid.
                                                    last_string12 = string12
                                                    if string13.replace('.', '').replace('', '0').replace('-', '').isdigit():  # Field's content is valid.
                                                        last_string13 = string13
                                                        if string14.replace('.', '').replace('', '0').replace('-', '').isdigit():  # Field's content is valid.
                                                            last_string14 = string14
                                                            if string15.replace('.', '').replace('', '0').replace('-', '').isdigit():  # Field's content is valid.
                                                                last_string15 = string15
                                                                if string16.replace('.', '').replace('', '0').replace('-', '').isdigit():  # Field's content is valid.
                                                                    last_string16 = string16
                                                                else:
                                                                    text16.set(last_string16)
                                                            else:
                                                                text15.set(last_string15)
                                                        else:
                                                            text14.set(last_string14)
                                                    else:
                                                        text13.set(last_string13)
                                                else:
                                                    text12.set(last_string12)
                                            else:
                                                text11.set(last_string11)
                                        else:
                                            text10.set(last_string10)
                                    else:
                                        text9.set(last_string9)
                                else:
                                    text8.set(last_string8)
                            else:
                                text7.set(last_string7)
                        else:
                            text6.set(last_string6)
                    else:
                        text5.set(last_string5)
                else:
                    text4.set(last_string4)
            else:
                text3.set(last_string3)                        
        else:
            text2.set(last_string2)
    else:
        text1.set(last_string1)



last_string1 = ''
text1 = StringVar()
text1.set(last_string1)
text1.trace('w', digits_only)
last_string2 = ''
text2 = StringVar()
text2.set(last_string2)
text2.trace('w', digits_only)
last_string3 = ''
text3 = StringVar()
text3.set(last_string3)
text3.trace('w', digits_only)
last_string4 = ''
text4 = StringVar()
text4.set(last_string4)
text4.trace('w', digits_only)
last_string5 = ''
text5 = StringVar()
text5.set(last_string5)
text5.trace('w', digits_only)
last_string6 = ''
text6 = StringVar()
text6.set(last_string6)
text6.trace('w', digits_only)
last_string7 = ''
text7 = StringVar()
text7.set(last_string7)
text7.trace('w', digits_only)
last_string8 = ''
text8 = StringVar()
text8.set(last_string8)
text8.trace('w', digits_only)
last_string9 = ''
text9 = StringVar()
text9.set(last_string9)
text9.trace('w', digits_only)
last_string10 = ''
text10 = StringVar()
text10.set(last_string10)
text10.trace('w', digits_only)
last_string11 = ''
text11 = StringVar()
text11.set(last_string11)
text11.trace('w', digits_only)
last_string12 = ''
text12 = StringVar()
text12.set(last_string12)
text12.trace('w', digits_only)
last_string13 = ''
text13 = StringVar()
text13.set(last_string13)
text13.trace('w', digits_only)
last_string14 = ''
text14 = StringVar()
text14.set(last_string14)
text14.trace('w', digits_only)
last_string15 = ''
text15 = StringVar()
text15.set(last_string15)
text15.trace('w', digits_only)
last_string16 = ''
text16 = StringVar()
text16.set(last_string16)
text16.trace('w', digits_only)

def copyL(event=None):  
    frame4.clipboard_clear()
    frame4.clipboard_append(Label)
    frame4.update()

labels = [child for child in frame4.winfo_children() if isinstance(child, Label)]


#copy on root
def copy(event=None):#assign this function to any button or any actions
    root.clipboard_clear()
    root.clipboard_append(entry.get())   #get anything from the entry widget.

entries = [child for child in frame.winfo_children() if isinstance(child, Entry)]

# right click mouse on text
  
def do_popup(event):
    try:
        mf4.tk_popup(event.x_root, event.y_root)
    finally:
        mf4.grab_release()


mf4 = Menu(root, tearoff = 0)
mf4.add_command(label ="Cut")
mf4.add_command(label ="Copy", command=copy)
mf4.add_command(label ="Paste")
mf4.add_command(label ="Refresh")
mf4.add_command(label ="select all")
mf4.add_separator()
mf4.add_command(label ="Rename")

#select entry on focus
def select_on_focus(event):
    event.widget.select_range(0, END) # Select all the text in the widget.

  
#Calculate regime

def cal_sum():
    global label
    global frame4
    frame4=Frame(text, bg='#FFFEFC',height=800, width=803)
    frame4.place(x = -3, y = 0)
    frame4.bind("<Button-3>",do_popup)
  
    #fertilizers
    
    try:
        t1=float(Calcium_NitrateE.get())
        t2=float(Potassium_NitrateE.get())
        t3=float(Magnesium_NitrateE.get())
        t4=float(FerillineE.get())
        t5=float(BoraxE.get())
        t6=float(Magnesium_sulphateE.get())
        t7=float(Mono_p_phosphateE.get())
        t8=float(Potassium_sulphateE.get())
        t9=float(Ammonium_sulphateE.get())
        t10=float(Sodium_MolyE.get())
        t11=float(Mn_chellateE.get())
        t12=float(Zn_chellateE.get())
        t13=float(Cu_chellateE.get())
        t14=float(Nitric_acidE.get())
        t15=float(Phosphoric_acidE.get())
        t16=float(Water_cubicME.get())
        
        # Logic ppm

        #Fertilizers in grams

        Convert_to_grams = 1000
        g1 = t1 * Convert_to_grams
        g2 = t2 * Convert_to_grams
        g3 = t3 * Convert_to_grams
        g4 = t4 * Convert_to_grams
        g5 = t5 * Convert_to_grams
        g6 = t6 * Convert_to_grams
        g7 = t7 * Convert_to_grams
        g8 = t8 * Convert_to_grams
        g9 = t9 * Convert_to_grams
        g10 = t10 * Convert_to_grams
        g11 = t11 * Convert_to_grams
        g12 = t12 * Convert_to_grams
        g13 = t13 * Convert_to_grams
        g14 = t14 * Convert_to_grams
        g15 = t15 * Convert_to_grams

        #Fertilizers grams per m3

        gm1 = g1/t16
        gm2 = g2/t16
        gm3 = g3/t16
        gm4 = g4/t16
        gm5 = g5/t16
        gm6 = g6/t16
        gm7 = g7/t16
        gm8 = g8/t16
        gm9 = g9/t16
        gm10 = g10/t16
        gm11 = g11/t16
        gm12 = g12/t16
        gm13 = g13/t16
        gm14 = g14/t16
        gm15 = g15/t16

        #ppm calculation label

        NitrateL=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=30,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        NitrateL.place(x = 2, y = 75)
        NitrateL.bind("<Button-3>",do_popup)
        separator = ttk.Separator(frame4, orient='vertical')
        separator.place(x=350, y=40, relwidth=0, relheight=1)

        phosphateL =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=30,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        phosphateL.place(x = 2, y = 100)
        phosphateL.bind("<Button-3>",do_popup)

        PotassiumL =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=30,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        PotassiumL.place(x = 2, y = 125)
        PotassiumL.bind("<Button-3>",do_popup)
        
        CalciumL=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=30,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        CalciumL.place(x = 2, y = 150)
        CalciumL.bind("<Button-3>",do_popup)

        MagnesiumL=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=30,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        MagnesiumL.place(x = 2, y = 175)
        MagnesiumL.bind("<Button-3>",do_popup)


        sulphateL=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=30,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        sulphateL.place(x = 2, y = 200)
        sulphateL.bind("<Button-3>",do_popup)

        FerillineL=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=30,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        FerillineL.place(x = 2, y = 225)
        FerillineL.bind("<Button-3>",do_popup)


        Mn_chellateL =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=30,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        Mn_chellateL.place(x = 2, y = 250)
        Mn_chellateL.bind("<Button-3>",do_popup)


        Cu_chellateL =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=30,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        Cu_chellateL.place(x = 2, y = 275)
        Cu_chellateL.bind("<Button-3>",do_popup)


        BoraxL=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=30,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        BoraxL.place(x = 2, y = 300)
        BoraxL.bind("<Button-3>",do_popup)


        Zn_chellateL =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=30,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        Zn_chellateL.place(x = 2, y = 325)
        Zn_chellateL.bind("<Button-3>",do_popup)

        
        Sodium_MolyL =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=30,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        Sodium_MolyL.place(x = 2, y = 350)
        Sodium_MolyL.bind("<Button-3>",do_popup)


        AmmoniumL =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=30,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        AmmoniumL.place(x = 2, y = 375)
        AmmoniumL.bind("<Button-3>",do_popup)


        ECL =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=30,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        ECL.place(x = 2, y = 400)
        ECL.bind("<Button-3>",do_popup)

        pHL =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=30,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        pHL.place(x = 2, y = 425)
        pHL.bind("<Button-3>",do_popup)

        #fertilizers entered

        Calcium_NitrateLF=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=30,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        Calcium_NitrateLF.place(x = 600, y = 75)
        Calcium_NitrateLF.insert('end', t1)
        Calcium_NitrateLF.config(state='readonly')
        Calcium_NitrateLF.bind("<Button-3>",do_popup)
        
        Potassium_NitrateLF=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=30,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        Potassium_NitrateLF.place(x = 600, y = 100)
        Potassium_NitrateLF.insert('end', t2)
        Potassium_NitrateLF.config(state='readonly')
        Potassium_NitrateLF.bind("<Button-3>",do_popup)

        Magnesium_NitrateLF=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=30,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        Magnesium_NitrateLF.place(x = 600, y = 125)
        Magnesium_NitrateLF.insert('end', t3)
        Magnesium_NitrateLF.config(state='readonly')
        Magnesium_NitrateLF.bind("<Button-3>",do_popup)

        FerillineLF=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=30,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        FerillineLF.place(x = 600, y = 150)
        FerillineLF.insert('end', t4)
        FerillineLF.config(state='readonly')
        FerillineLF.bind("<Button-3>",do_popup)
        

        BoraxLF=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=30,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        BoraxLF.place(x = 600, y = 175)
        BoraxLF.insert('end', t5)
        BoraxLF.config(state='readonly')
        BoraxLF.bind("<Button-3>",do_popup)

        Magnesium_sulphateLF=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=30,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        Magnesium_sulphateLF.place(x = 600, y = 200)
        Magnesium_sulphateLF.insert('end', t6)
        Magnesium_sulphateLF.config(state='readonly')
        Magnesium_sulphateLF.bind("<Button-3>",do_popup)

        Mono_p_phosphateLF =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=30,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times"))
        Mono_p_phosphateLF.place(x = 600, y = 225)
        Mono_p_phosphateLF.insert('end', t7)
        Mono_p_phosphateLF.config(state='readonly')
        Mono_p_phosphateLF.bind("<Button-3>",do_popup)
        
        Potassium_sulphateLF =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=30,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        Potassium_sulphateLF.place(x = 600, y = 250)
        Potassium_sulphateLF.insert('end', t8)
        Potassium_sulphateLF.config(state='readonly')
        Potassium_sulphateLF.bind("<Button-3>",do_popup)

        Ammonium_sulphateLF =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=30,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        Ammonium_sulphateLF.place(x = 600, y = 275)
        Ammonium_sulphateLF.insert('end', t9)
        Ammonium_sulphateLF.config(state='readonly')
        Ammonium_sulphateLF.bind("<Button-3>",do_popup)

        Sodium_MolyLF =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=30,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        Sodium_MolyLF.place(x = 600, y = 300)
        Sodium_MolyLF.insert('end', t10)
        Sodium_MolyLF.config(state='readonly')
        Sodium_MolyLF.bind("<Button-3>",do_popup)

        Mn_chellateLF =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=30,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        Mn_chellateLF.place(x = 600, y = 325)
        Mn_chellateLF.insert('end', t11)
        Mn_chellateLF.config(state='readonly')
        Mn_chellateLF.bind("<Button-3>",do_popup)

        Zn_chellateLF =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=30,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        Zn_chellateLF.place(x = 600, y = 350)
        Zn_chellateLF.insert('end', t12)
        Zn_chellateLF.config(state='readonly')
        Zn_chellateLF.bind("<Button-3>",do_popup)

        Cu_chellateLF =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=30,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        Cu_chellateLF.place(x = 600, y = 375)
        Cu_chellateLF.insert('end', t13)
        Cu_chellateLF.config(state='readonly')
        Cu_chellateLF.bind("<Button-3>",do_popup)

        Nitric_acidLF =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=30,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        Nitric_acidLF.place(x = 600, y = 400)
        Nitric_acidLF.insert('end', t14)
        Nitric_acidLF.config(state='readonly')
        Nitric_acidLF.bind("<Button-3>",do_popup)

        Phosphoric_acidLF =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=30,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        Phosphoric_acidLF.place(x = 600, y = 425)
        Phosphoric_acidLF.insert('end', t15)
        Phosphoric_acidLF.config(state='readonly')
        Phosphoric_acidLF.bind("<Button-3>",do_popup)

        #Dictionary map
        
        CalciumS = []
        Calcium_Nitrate = {'Ca':19, 'No3':15.5, 'N-NH4':1.1}
        for key, value in Calcium_Nitrate.items():
            if key == 'Ca':
                data1 = "4.", key, ':', round(value * gm1 /100,2)
                sdata1 = '4. Ca: ' + str(round(value * gm1 /100,2))
                for i in data1:
                    CalciumS.append(i)
                    CalciumL.insert('end', data1)
                    CalciumL.config(state='readonly')
            elif key == 'No3':
                data2 = (value * gm1 /100)

            elif key == 'N-NH4':
                data3 = value * gm1 /100


        NitrateS = []
        Potassium_Nitrate = {'K':38, 'No3':13}
        for key, value in Potassium_Nitrate.items():
            if key == 'No3':
                data4 = (value * gm2 /100)

            elif key == 'K':
                data5 = value * gm2 /100

            
        MagnesiumS = []
        Magnesium_Nitrate = { 'No3':11, 'Mg':9.5}
        for key, value in Magnesium_Nitrate.items():
            if key == 'Mg':
                data6 = value * gm3 /100

            elif key == 'No3':
                data7 = (value * gm3 /100)

        FerillineS = []
        Ferilline = {'Fe':6}
        for key, value in Ferilline.items():
            data10 = "7.", key, ':', round(value * gm4 /100,2)
            sdata2 = '7. Fe: ' + str(round(value * gm4 /100,2))
            for i in data10:
                    FerillineS.append(i)
                    FerillineL.insert('end', data10)
                    FerillineL.config(state='readonly')
            
        BoraxS = []    
        Borax = {'B':11}
        for key, value in Borax.items():
            data11 = "10.", key, ':', round(value * gm5 /100,2)
            sdata3 = '10. B: ' + str(round(value * gm5 /100,2))
            for i in data11:
                    BoraxS.append(i)
                    BoraxL.insert('end', data11)
                    BoraxL.config(state='readonly')
            
        sulphateS = []    
        Magnesium_sulphate = {'S':14,'Mg':9.1}
        for key, value in Magnesium_sulphate.items():
            if key == 'S':
                data12 = value * gm6 /100
            elif key == 'Mg':
                data13 = (value * gm6 /100)
                data14 = round((data13 + data6),2)
                data15 = "5.", key, ':', data14
                sdata4 = '5. Mg: ' + str(data14)
                for i in data15:
                    MagnesiumS.append(i)
                    MagnesiumL.insert('end', data15)
                    MagnesiumL.config(state='readonly')

        phosphateS = []    
        Mono_p_phosphate = {'K':28, 'P':22.5}
        for key, value in Mono_p_phosphate.items():
            if key == 'P':
                data16 = value * gm7 /100
            elif key == 'K':
                data17 = (value * gm7 /100)

        PotassiumS = []    
        Potassium_sulphate = {'K':43, 'S':18}
        for key, value in Potassium_sulphate.items():
            if key == 'S':
                data18 = value * gm8 /100
            elif key == 'K':
                data19 = (value * gm8 /100)
                data20 = round((data5 + data17 + data19),2)
                data21 = "3.", key, ':', data20
                sdata5 = '3. K: ' + str(data20)
                for i in data21:
                    PotassiumS.append(i)
                    PotassiumL.insert('end', data21)
                    PotassiumL.config(state='readonly')
                    
        AmmoniumS = []
        Ammonium_sulphate = {'S':24, 'N-NH4':21}
        for key, value in Ammonium_sulphate.items():
            if key == 'S':
                data22 = value * gm9 /100
                data23 = round((data12 + data22 + data18),2)
                data24 = "6.", key, ':', data23
                sdata6 = '6. S: ' + str(data23)
                for i in data24:
                    sulphateS.append(i)
                    sulphateL.config(text=sulphateS)
                    sulphateL.insert('end', data24)
                    sulphateL.config(state='readonly')
            elif key == 'N-NH4':
                data25 = value * gm9 /100
                data26 = round((data3),2)
                data27 = "13.", key, ':', data26
                sdata7 = '13. N-NH4: ' + str(data26)
                for i in data27:
                    AmmoniumS.append(i)
                    AmmoniumL.insert('end', data27)
                    AmmoniumL.config(state='readonly')

        Sodium_MolyS = []    
        Sodium_Moly = {'Mo':39}
        for key, value in Sodium_Moly.items():
            data28 = "12.", key, ':', round((value*gm10/100),2)
            sdata8 = '12. Mo: ' + str(round(value*gm10/100,2))
            for i in data28:
                Sodium_MolyS.append(i)
                Sodium_MolyL.insert('end', data28)
                Sodium_MolyL.config(state='readonly')

        Mn_chellateS = []    
        Mn_chellate = {'Mn':13}
        for key, value in Mn_chellate.items():
            data29 = "8.", key, ':', round(value * gm11 /100,2)
            sdata9 = '8. Mn: ' + str(round(value * gm11 /100,2))
            for i in data29:
                Mn_chellateS.append(i)
                Mn_chellateL.insert('end', data29)
                Mn_chellateL.config(state='readonly')


        Cu_chellateS = []    
        Cu_chellate = {'Cu':14}
        for key, value in Cu_chellate.items():
            data30 = "9.", key, ':', round((value * gm13 /100),2)
            sdata10 = '9. Cu: ' + str(round(value * gm13 /100,2))
            for i in data30:
                Cu_chellateS.append(i)
                Cu_chellateL.insert('end', data30)
                Cu_chellateL.config(state='readonly')

        Zn_chellateS = []    
        Zn_chellate = {'Zn':15}
        for key, value in Zn_chellate.items():
            data31 = "11.", key, ':', round(value * gm12 /100,2)
            sdata11 = '11. Zn: ' + str(round(value * gm12 /100,2))
            for i in data31:
                Zn_chellateS.append(i)
                Zn_chellateL.insert('end', data31)
                Zn_chellateL.config(state='readonly')
        
        Nitric_acid = {'No3':0}
        for key, value in Nitric_acid.items():
            if key == 'No3':
                data32 = (value * gm14 /100)
                data33 = round((data2 + data4 + data7+ data32+data25),2)
                data34 = "1.", key, ':', data33
                sdata12 = '1. No3: ' + str(data33)
                for i in data34:
                    NitrateS.append(i)
                    NitrateL.insert('end', data34)
                    NitrateL.config(state='readonly')
                    
                    
        Phosphoric_acid = {'P':31.608}
        for key, value in Phosphoric_acid.items():
            if key == 'P':
                data35 = value * gm15 /100
                data36 = round((data16 + data35),2)
                data37 = "2.", key, ':', data36
                sdata13 = '2. P: ' + str(data36)
                for i in data37:
                    phosphateS.append(i)
                    phosphateL.insert('end', data37)
                    phosphateL.config(state='readonly')
                    

        Nitric_acidS = []                    
        pH = {'pH':5.5}
        for key, value in pH.items():
            data38 = value
            data39 = "15.", key, ':', data38
            sdata14 = '15. pH: ' + str(data38)
            for i in data39:
                Nitric_acidS.append(i)
                pHL.insert('end', data39)
                pHL.config(state='readonly')

                
        Phosphoric_acidS = []
        EC = {'EC':1.2}
        for key, value in EC.items():
            data40 = value
            data41 = "14.", key, ':', data40
            sdata15 = '14. EC: ' + str(data40)
            for i in data41:
                Phosphoric_acidS.append(i)
                ECL.insert('end', data41)
                ECL.config(state='readonly')
        
        if menu.get() == "HYDRO":
            pdf = canvas.Canvas('Fertilizer Hyroponics regime [Date].pdf')
            sdate2= "Regime Date: " + str(cal.get_date())
            pdf.drawString(x=150, y=805,text=sdate2)
            hydro_phase = "HYDRONICS"
            pdf.drawString(x=150, y=785,text=hydro_phase)
            pdf.setFont('Times-Roman', 11)
            pdf.drawString(x=2, y=770,text="Elements in ppm")
            pdf.drawString(x=2, y=755,text=sdata12)
            pdf.drawString(x=2, y=740, text=sdata13)
            pdf.drawString(x=2, y=725, text=sdata5)
            pdf.drawString(x=2, y=710, text=sdata1)
            pdf.drawString(x=2, y=695, text=sdata4)
            pdf.drawString(x=2, y=680, text=sdata6)
            pdf.drawString(x=2, y=665, text=sdata2)
            pdf.drawString(x=2, y=650, text=sdata9)
            pdf.drawString(x=2, y=635, text=sdata10)
            pdf.drawString(x=2, y=620, text=sdata3)
            pdf.drawString(x=2, y=605, text=sdata11)
            pdf.drawString(x=2, y=590, text=sdata8)
            pdf.drawString(x=2, y=575, text=sdata7)
            pdf.drawString(x=2, y=560, text=sdata15)
            pdf.drawString(x=2, y=545, text=sdata14)


            pdf.drawString(x=200, y=770,text='Fertilizers')
            pdf.drawString(x=200, y=755,text='Calcium Nitrate')
            pdf.drawString(x=200, y=740, text='Potassium Nitrate')
            pdf.drawString(x=200, y=725, text='Magnesium Nitrate')
            pdf.drawString(x=200, y=710, text='Ferilline')
            pdf.drawString(x=200, y=695, text='Borax')
            pdf.drawString(x=200, y=680, text='Magnesium Sulphate')
            pdf.drawString(x=200, y=665, text='Mono p phosphate')
            pdf.drawString(x=200, y=650, text='Potassium Sulphate')
            pdf.drawString(x=200, y=635, text='Ammonium Sulphate')
            pdf.drawString(x=200, y=620, text='Sodium Molybdate')
            pdf.drawString(x=200, y=605, text='Mn chellate')
            pdf.drawString(x=200, y=590, text='Zn chellate')
            pdf.drawString(x=200, y=575, text='Cu chellate')
            pdf.drawString(x=200, y=560, text='Nitric acid')
            pdf.drawString(x=200, y=545, text='Phosphoric acid')

            pdf.drawString(x=350, y=770,text="Amount in kg/ltr")
            pdf.drawString(x=350, y=755,text=str(t1))
            pdf.drawString(x=350, y=740, text=str(t2))
            pdf.drawString(x=350, y=725, text=str(t3))
            pdf.drawString(x=350, y=710, text=str(t4))
            pdf.drawString(x=350, y=695, text=str(t5))
            pdf.drawString(x=350, y=680, text=str(t6))
            pdf.drawString(x=350, y=665, text=str(t7))
            pdf.drawString(x=350, y=650, text=str(t8))
            pdf.drawString(x=350, y=635, text=str(t9))
            pdf.drawString(x=350, y=620, text=str(t10))
            pdf.drawString(x=350, y=605, text=str(t11))
            pdf.drawString(x=350, y=590, text=str(t12))
            pdf.drawString(x=350, y=575, text=str(t13))
            pdf.drawString(x=350, y=560, text=str(t14))
            pdf.drawString(x=350, y=545, text=str(t15))
            pdf.save()
        
        if menu.get() == "SOIL":
            pdf = canvas.Canvas('Fertilizer Soil regime [Date].pdf')
            sdate2= "Regime Date: " + str(cal.get_date())
            pdf.drawString(x=150, y=805,text=sdate2)
            soil_phase = "SOIL"
            pdf.drawString(x=150, y=785,text=soil_phase)
            pdf.setFont('Times-Roman', 11)
            pdf.drawString(x=2, y=770,text="Elements in ppm")
            pdf.drawString(x=2, y=755,text=sdata12)
            pdf.drawString(x=2, y=740, text=sdata13)
            pdf.drawString(x=2, y=725, text=sdata5)
            pdf.drawString(x=2, y=710, text=sdata1)
            pdf.drawString(x=2, y=695, text=sdata4)
            pdf.drawString(x=2, y=680, text=sdata6)
            pdf.drawString(x=2, y=665, text=sdata2)
            pdf.drawString(x=2, y=650, text=sdata9)
            pdf.drawString(x=2, y=635, text=sdata10)
            pdf.drawString(x=2, y=620, text=sdata3)
            pdf.drawString(x=2, y=605, text=sdata11)
            pdf.drawString(x=2, y=590, text=sdata8)
            pdf.drawString(x=2, y=575, text=sdata7)
            pdf.drawString(x=2, y=560, text=sdata15)
            pdf.drawString(x=2, y=545, text=sdata14)


            pdf.drawString(x=200, y=770,text='Fertilizers')
            pdf.drawString(x=200, y=755,text='Calcium Nitrate')
            pdf.drawString(x=200, y=740, text='Potassium Nitrate')
            pdf.drawString(x=200, y=725, text='Magnesium Nitrate')
            pdf.drawString(x=200, y=710, text='Ferilline')
            pdf.drawString(x=200, y=695, text='Borax')
            pdf.drawString(x=200, y=680, text='Magnesium Sulphate')
            pdf.drawString(x=200, y=665, text='Mono p phosphate')
            pdf.drawString(x=200, y=650, text='Potassium Sulphate')
            pdf.drawString(x=200, y=635, text='Ammonium Sulphate')
            pdf.drawString(x=200, y=620, text='Sodium Molybdate')
            pdf.drawString(x=200, y=605, text='Mn chellate')
            pdf.drawString(x=200, y=590, text='Zn chellate')
            pdf.drawString(x=200, y=575, text='Cu chellate')
            pdf.drawString(x=200, y=560, text='Nitric acid')
            pdf.drawString(x=200, y=545, text='Phosphoric acid')

            pdf.drawString(x=350, y=770,text="Amount in kg/ltr")
            pdf.drawString(x=350, y=755,text=str(t1))
            pdf.drawString(x=350, y=740, text=str(t2))
            pdf.drawString(x=350, y=725, text=str(t3))
            pdf.drawString(x=350, y=710, text=str(t4))
            pdf.drawString(x=350, y=695, text=str(t5))
            pdf.drawString(x=350, y=680, text=str(t6))
            pdf.drawString(x=350, y=665, text=str(t7))
            pdf.drawString(x=350, y=650, text=str(t8))
            pdf.drawString(x=350, y=635, text=str(t9))
            pdf.drawString(x=350, y=620, text=str(t10))
            pdf.drawString(x=350, y=605, text=str(t11))
            pdf.drawString(x=350, y=590, text=str(t12))
            pdf.drawString(x=350, y=575, text=str(t13))
            pdf.drawString(x=350, y=560, text=str(t14))
            pdf.drawString(x=350, y=545, text=str(t15))

            pdf.save()
            
##        if menu.get() == "HYDRO PPM":
##            hydro_ppm_phase = "HYDRONICS PPM REGIME"
##     
##        if menu.get() == "SOIL PPM":
##            soil_ppm_phase = "SOIL PPM REGIME"

        #pdf.save()

        # Fertilizers entered label

        Fertilizers =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=30,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13,"bold"))
        Fertilizers.place(x = 2, y = 45)
        Fertilizers.insert('end', 'Elements in ppm')
        Fertilizers.config(state='readonly')
        Fertilizers.bind("<Button-3>",do_popup)
        

        Fertilizers =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=30,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13,"bold"))
        Fertilizers.place(x = 380, y = 45)
        Fertilizers.insert('end', 'Fertilizers')
        Fertilizers.config(state='readonly')
        Fertilizers.bind("<Button-3>",do_popup)

        Amount =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=30,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13,"bold"))
        Amount.place(x = 600, y = 45)
        Amount.insert('end', 'Amount in kg/ltr')
        Amount.config(state='readonly')
        Amount.bind("<Button-3>",do_popup)

        Calcim_Nitrate=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        Calcim_Nitrate.place(x = 380, y = 75)
        Calcim_Nitrate.insert('end', 'Calcium Nitrate')
        Calcim_Nitrate.config(state='readonly')
        Calcim_Nitrate.bind("<Button-3>",do_popup)

        Potassium_Nitrate=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        Potassium_Nitrate.place(x = 380, y = 100)
        Potassium_Nitrate.insert('end', 'Potassium Nitrate')
        Potassium_Nitrate.config(state='readonly')
        Potassium_Nitrate.bind("<Button-3>",do_popup)

        Magnesium_Nitrate=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        Magnesium_Nitrate.place(x = 380, y = 125)
        Magnesium_Nitrate.insert('end', 'Magnesium Nitrate')
        Magnesium_Nitrate.config(state='readonly')
        Magnesium_Nitrate.bind("<Button-3>",do_popup)

        Ferilline=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        Ferilline.place(x = 380, y = 150)
        Ferilline.insert('end', 'Ferilline')
        Ferilline.config(state='readonly')
        Ferilline.bind("<Button-3>",do_popup)

        Borax=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        Borax.place(x = 380, y = 175)
        Borax.insert('end', 'Borax')
        Borax.config(state='readonly')
        Borax.bind("<Button-3>",do_popup)

        Magnesium_sulphate=Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        Magnesium_sulphate.place(x = 380, y = 200)
        Magnesium_sulphate.insert('end', 'Magnesium Sulphate')
        Magnesium_sulphate.config(state='readonly')
        Magnesium_sulphate.bind("<Button-3>",do_popup)

        Mono_p_phosphate =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        Mono_p_phosphate.place(x = 380, y = 225)
        Mono_p_phosphate.insert('end', 'Mono p phosphate')
        Mono_p_phosphate.config(state='readonly')
        Mono_p_phosphate.bind("<Button-3>",do_popup)

        Potassium_sulphate =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        Potassium_sulphate.place(x = 380, y = 250)
        Potassium_sulphate.insert('end', 'Potassium Sulphate')
        Potassium_sulphate.config(state='readonly')
        Potassium_sulphate.bind("<Button-3>",do_popup)

        Ammonium_sulphate =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        Ammonium_sulphate.place(x = 380, y = 275)
        Ammonium_sulphate.insert('end', 'Ammonium Sulphate')
        Ammonium_sulphate.config(state='readonly')
        Ammonium_sulphate.bind("<Button-3>",do_popup)

        Sodium_Moly =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        Sodium_Moly.place(x = 380, y = 300)
        Sodium_Moly.insert('end', 'Sodium Molybdate')
        Sodium_Moly.config(state='readonly')
        Sodium_Moly.bind("<Button-3>",do_popup)

        Mn_chellate =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        Mn_chellate.place(x = 380, y = 325)
        Mn_chellate.insert('end', 'Mn chellate')
        Mn_chellate.config(state='readonly')
        Mn_chellate.bind("<Button-3>",do_popup)

        Zn_chellate =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        Zn_chellate.place(x = 380, y = 350)
        Zn_chellate.insert('end', 'Zn chellate')
        Zn_chellate.config(state='readonly')
        Zn_chellate.bind("<Button-3>",do_popup)

        Cu_chellate =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        Cu_chellate.place(x = 380, y = 375)
        Cu_chellate.insert('end', 'Cu chellate')
        Cu_chellate.config(state='readonly')
        Cu_chellate.bind("<Button-3>",do_popup)

        Nitric_acid =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        Nitric_acid.place(x = 380, y = 400)
        Nitric_acid.insert('end', 'Nitric acid')
        Nitric_acid.config(state='readonly')
        Nitric_acid.bind("<Button-3>",do_popup)

        Phosphoric_acid =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=17,bg='skyblue',borderwidth=1, fg='black',
                            font=("Times",13))
        Phosphoric_acid.place(x = 380, y = 425)
        Phosphoric_acid.insert('end', 'Phosphoric acid')
        Phosphoric_acid.config(state='readonly')
        Phosphoric_acid.bind("<Button-3>",do_popup)
        grad_date2()
        
        
        

    except ValueError:

        Error_label = Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=30,bg='skyblue',borderwidth=1, fg='red',
                            font=("Times",13,"bold"))
        Error_label.place(x = 3, y = 125)
        Error_label.bind("<Button-3>",do_popup)
        Error_label.insert('end', 'Please input a valid Value!')
        Error_label.config(state='readonly')

        separator = ttk.Separator(frame4, orient='vertical')
        separator.place(x=350, y=40, relwidth=0, relheight=1)
    
        Error_labelF =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=30,bg='skyblue',borderwidth=1, fg='red',
                            font=("Times",13,"bold"))
        Error_labelF.place(x = 404, y = 125)
        Error_labelF.bind("<Button-3>",do_popup)
        Error_labelF.insert('end', 'Please input a valid Value!')
        Error_labelF.config(state='readonly')
    

        
        FertilizersER =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=30,bg='skyblue',borderwidth=1, fg='red',
                            font=("Times",13,"bold"))
        FertilizersER.place(x = 30, y = 45)
        FertilizersER.insert('end', 'Elements in PPM')
        FertilizersER.config(state='readonly')
        FertilizersER.bind("<Button-3>",do_popup)
        FertilizersER.bind_all('<Control-c>', lambda x: copyL())

        FertilizersER =Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=30,bg='skyblue',borderwidth=1, fg='red',
                            font=("Times",13,"bold"))
        FertilizersER.place(x = 430, y = 45)
        FertilizersER.insert('end', 'Fertilizers')
        FertilizersER.config(state='readonly')
        FertilizersER.bind("<Button-3>",do_popup)
        
        grad_date2()


def Open_Hyrom():
    
    header_text = 'Fetilizers regime'
    footer_text = 'PPM for plants requirement'
    footer_text3= "Issued by:"
    footer_text4 = "Authorized by:"
    image='myapp.png'
    #image='fleur.png'
    app_image='myapp.ico'
    # read pdf using pdfrw
    reader = PdfReader('Fertilizer Hyroponics regime [Date].pdf')
    pages = [pagexobj(p) for p in reader.pages]
    # Compose new pdf
    pdf = canvas.Canvas('Fertilizer hyroponics regime [Date].pdf')
    for page_num, page in enumerate(pages, start=1):
        footer_text2 = "Page %s of %s" % (page_num, len(pages))
        x = 128
        # Add page with the page size
        # Here BBox denotes a bounding box
        pdf.setPageSize((page.BBox[2], page.BBox[3]))
        
        # make a report lab object
        pdf.doForm(makerl(pdf, page))
        # Draw footer
        pdf.saveState()
        pdf.setFont('Times-Roman', 10)
        pdf.setStrokeColorRGB(0, 0, 1)
        
        # add text in the x,y coordinates of interest
        pdf.drawString(0, 816, header_text)
        pdf.drawString(0, 10, footer_text)
        pdf.drawString(230, 25, footer_text3)
        pdf.drawString(405, 25, footer_text4)
        pdf.drawString(page.BBox[2]-x, 10, footer_text2)
        pdf.setLineWidth(0.5)
        #pdf.line(20, 12, page.BBox[2] - 0, 12)
        pdf.line(390, 25, page.BBox[2] - 320, 25)
        pdf.line(580, 25, page.BBox[2] - 125, 25)
        pdf.drawImage(image,0,826,70,20)
        pdf.drawImage(app_image,0,20,40,10)
        pdf.restoreState()
        pdf.showPage()
    pdf.save()
    subprocess.Popen('Fertilizer hyroponics regime [Date].pdf', shell=True)

def Open_Soilm():
    header_text = 'Fetilizers regime'
    footer_text = 'PPM for plants requirement'
    footer_text3= "Issued by:"
    footer_text4 = "Authorized by:"
    image='myapp.ico'
    #image='fleur.png'
    app_image='myapp.ico'
    # read pdf using pdfrw
    reader = PdfReader('Fertilizer Soil regime [Date].pdf')
    pages = [pagexobj(p) for p in reader.pages]
    # Compose new pdf
    pdf = canvas.Canvas('Fertilizer soil regime [Date].pdf')
    for page_num, page in enumerate(pages, start=1):
        footer_text2 = "Page %s of %s" % (page_num, len(pages))
        x = 128
        # Add page with the page size
        # Here BBox denotes a bounding box
        pdf.setPageSize((page.BBox[2], page.BBox[3]))
        
        # make a report lab object
        pdf.doForm(makerl(pdf, page))
        # Draw footer
        pdf.saveState()
        pdf.setFont('Times-Roman', 10)
        pdf.setStrokeColorRGB(0, 0, 1)
        
        # add text in the x,y coordinates of interest
        pdf.drawString(0, 816, header_text)
        pdf.drawString(0, 10, footer_text)
        pdf.drawString(230, 25, footer_text3)
        pdf.drawString(405, 25, footer_text4)
        pdf.drawString(page.BBox[2]-x, 10, footer_text2)
        pdf.setLineWidth(0.5)
        #pdf.line(20, 12, page.BBox[2] - 0, 12)
        pdf.line(390, 25, page.BBox[2] - 320, 25)
        pdf.line(580, 25, page.BBox[2] - 125, 25)
        pdf.drawImage(image,0,826,70,20)
        pdf.drawImage(app_image,0,20,40,10)
        pdf.restoreState()
        pdf.showPage()
    pdf.save()
    subprocess.Popen('Fertilizer soil regime [Date].pdf', shell=True)
    
def Open_bothm():

    pdf1File = open('Fertilizer hyroponics regime [Date].pdf', 'rb')
    pdf2File = open('Fertilizer soil regime [Date].pdf', 'rb')
     
    # Read the files that you have opened
    pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
    pdf2Reader = PyPDF2.PdfFileReader(pdf2File)
     
    # Create a new PdfFileWriter object which represents a blank PDF document
    pdfWriter = PyPDF2.PdfFileWriter()
     
    # Loop through all the pagenumbers for the first document
    for pageNum in range(pdf1Reader.numPages):
        pageObj = pdf1Reader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
     
    # Loop through all the pagenumbers for the second document
    for pageNum in range(pdf2Reader.numPages):
        pageObj = pdf2Reader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
     
    # Now that you have copied all the pages in both the documents, write them into the a new document
    pdfOutputFile = open('Fertilizer regime [Date].pdf', 'wb')
    pdfWriter.write(pdfOutputFile)
     
    # Close all the files - Created as well as opened
    pdfOutputFile.close()
    pdf1File.close()
    pdf2File.close()
    subprocess.Popen('Fertilizer regime [Date].pdf', shell=True)

    
def grad_date2(event=None):
    global cal
    global button
    global date
    frame4=Frame(text, bg='skyblue',height=25, width=180)
    frame4.place(x = 230, y = 2)
    date2 = Entry(frame4,relief='flat',bd=0,takefocus=0,highlightthickness=0,width=30,bg='skyblue',borderwidth=1, fg='red',
                            font=("Times",13,"bold"))
    date2.insert('end',"Regime Date: " + cal.get_date())
    date2.config(state='readonly')
    date2.place(x = 0, y = 0)
    date2.bind("<Button-3>",do_popup)


#Calendar

cal = Calendar(frame, selectmode = 'day',
               year = 2022, month = 3,
               day = 7)
def grad_date(event=None):
    global cal
    global button
    global date
    date.config(text = "Selected Date is: " + cal.get_date(), bg='yellow', font=("Times",13, 'bold'))
    cal.place(x = 10, y = 490)
    button.place(x = 10, y = 455)
    date.place(x = 160, y = 0)
         
button = Button(frame, text = "Get Date",
    command = lambda: [grad_date2(),grad_date()], bg='skyblue', fg='black',
       font=("Times",12,"bold"), activebackground='skyblue')
date = Label(frame, text = "")

button.bind('<Return>', grad_date)
grad_date()


# clear results
def Clear_get():
    global frame4
    frame4=Frame(text, bg='#FFFEFC',height=800, width=802)
    frame4.place(x = -3, y = 0)
    frame4.pack_forget()
    frame4.bind("<Button-3>",do_popup)

#Hydroponics interface
    
def Hydroponics():
    Header_hydro =Label(frame, text="HYDRO REGIME                           ", font=("Times",17,"bold"), fg="blue")
    Header_hydro.place(x = 130, y = 25)

    Fertilizers =Label(frame, text="Fertilizers", font=("Times",13,"bold"))
    Fertilizers.place(x = 10, y = 50)

    Amount =Label(frame, text="Amount kgs/lts", font=("Times",13,"bold"))
    Amount.place(x = 160, y = 50)

    Water_volume =Label(frame, text="Water M3", font=("Times",13,"bold"))
    Water_volume.place(x = 300, y = 50)

    Calcim_Nitrate=Label(frame, text="Calcium Nitrate", font=("Times",13))
    Calcim_Nitrate.place(x = 10, y = 75)

    Potassium_Nitrate=Label(frame, text="Potassium Nitrate", font=("Times",13))
    Potassium_Nitrate.place(x = 10, y = 100)

    Magnesium_Nitrate=Label(frame, text="Magnesium Nitrate", font=("Times",13))
    Magnesium_Nitrate.place(x = 10, y = 125)

    Ferilline=Label(frame, text="Ferilline", font=("Times",13))
    Ferilline.place(x = 10, y = 150)

    Borax=Label(frame, text="Borax", font=("Times",13))
    Borax.place(x = 10, y = 175)

    Magnesium_sulphate=Label(frame, text="Magnesium Sulphate", font=("Times",13))
    Magnesium_sulphate.place(x = 10, y = 200)

    Mono_p_phosphate =Label(frame, text="Mono p phosphate", font=("Times",13))
    Mono_p_phosphate.place(x = 10, y = 225)

    Potassium_sulphate =Label(frame, text="Potassium Sulphate", font=("Times",13))
    Potassium_sulphate.place(x = 10, y = 250)

    Ammonium_sulphate =Label(frame, text="Ammonium sulphate", font=("Times",13))
    Ammonium_sulphate.place(x = 10, y = 275)

    Sodium_Moly =Label(frame, text="Sodium Molybdate", font=("Times",13))
    Sodium_Moly.place(x = 10, y = 300)

    Mn_chellate =Label(frame, text="Mn chellate", font=("Times",13))
    Mn_chellate.place(x = 10, y = 325)

    Zn_chellate =Label(frame, text="Zn chellate", font=("Times",12))
    Zn_chellate.place(x = 10, y = 350)

    Cu_chellate =Label(frame, text="Cu chellate", font=("Times",13))
    Cu_chellate.place(x = 10, y = 375)

    Nitric_acid =Label(frame, text="Nitric acid", font=("Times",13))
    Nitric_acid.place(x = 10, y = 400)

    Phosphoric_acid =Label(frame, text="Phosphoric acid", font=("Times",13))
    Phosphoric_acid.place(x = 10, y = 425)

Hydroponics()




#Entries
Calcium_NitrateE=Entry(frame, width=10, textvariable=text1)
Calcium_NitrateE.place(x = 160, y = 75)
Calcium_NitrateE.focus_set()
Calcium_NitrateE.bind("<Button-3>",do_popup)
Calcium_NitrateE.bind('<FocusIn>', select_on_focus)
Potassium_NitrateE=Entry(frame,width = 10, textvariable=text2)
Potassium_NitrateE.place(x = 160, y = 100)
Potassium_NitrateE.bind("<Button-3>",do_popup)
Potassium_NitrateE.bind('<FocusIn>', select_on_focus)
Magnesium_NitrateE = Entry(frame,width = 10, textvariable=text3)
Magnesium_NitrateE.place(x = 160, y = 125)
Magnesium_NitrateE.bind("<Button-3>",do_popup)
Magnesium_NitrateE.bind('<FocusIn>', select_on_focus)
FerillineE = Entry(frame,width = 10, textvariable=text4)
FerillineE.place(x = 160, y = 150)
FerillineE.bind("<Button-3>",do_popup)
FerillineE.bind('<FocusIn>', select_on_focus)
BoraxE = Entry(frame,width = 10, textvariable=text5)
BoraxE.place(x = 160, y = 175)
BoraxE.bind("<Button-3>",do_popup)
BoraxE.bind('<FocusIn>', select_on_focus)
Magnesium_sulphateE = Entry(frame,width = 10, textvariable=text6)
Magnesium_sulphateE.place(x = 160, y = 200)
Magnesium_sulphateE.bind("<Button-3>",do_popup)
Magnesium_sulphateE.bind('<FocusIn>', select_on_focus)
Mono_p_phosphateE = Entry(frame,width = 10, textvariable=text7)
Mono_p_phosphateE.place(x = 160, y = 225)
Mono_p_phosphateE.bind("<Button-3>",do_popup)
Mono_p_phosphateE.bind('<FocusIn>', select_on_focus)
Potassium_sulphateE = Entry(frame,width = 10, textvariable=text8)
Potassium_sulphateE.place(x = 160, y = 250)
Potassium_sulphateE.bind("<Button-3>",do_popup)
Potassium_sulphateE.bind('<FocusIn>', select_on_focus)
Ammonium_sulphateE = Entry(frame,width = 10, textvariable=text9)
Ammonium_sulphateE.place(x = 160, y = 275)
Ammonium_sulphateE.bind("<Button-3>",do_popup)
Ammonium_sulphateE.bind('<FocusIn>', select_on_focus)
Sodium_MolyE = Entry(frame,width = 10, textvariable=text10)
Sodium_MolyE.place(x = 160, y = 300)
Sodium_MolyE.bind("<Button-3>",do_popup)
Sodium_MolyE.bind('<FocusIn>', select_on_focus)
Mn_chellateE = Entry(frame,width = 10, textvariable=text11)
Mn_chellateE.place(x = 160, y = 325)
Mn_chellateE.bind("<Button-3>",do_popup)
Mn_chellateE.bind('<FocusIn>', select_on_focus)
Zn_chellateE = Entry(frame,width = 10, textvariable=text12)
Zn_chellateE.place(x = 160, y = 350)
Zn_chellateE.bind("<Button-3>",do_popup)
Zn_chellateE.bind('<FocusIn>', select_on_focus)
Cu_chellateE = Entry(frame,width = 10, textvariable=text13)
Cu_chellateE.place(x = 160, y = 375)
Cu_chellateE.bind("<Button-3>",do_popup)
Cu_chellateE.bind('<FocusIn>', select_on_focus)
Nitric_acidE = Entry(frame,width = 10, textvariable=text14)
Nitric_acidE.place(x = 160, y = 400)
Nitric_acidE.bind("<Button-3>",do_popup)
Nitric_acidE.bind('<FocusIn>', select_on_focus)
Phosphoric_acidE = Entry(frame,width = 10, textvariable=text15)
Phosphoric_acidE.place(x = 160, y = 425)
Phosphoric_acidE.bind("<Button-3>",do_popup)
Phosphoric_acidE.bind('<FocusIn>', select_on_focus)
Water_cubicME = Entry(frame,width = 10, textvariable=text16)
Water_cubicME.place(x = 300, y = 75)
Water_cubicME.bind("<Button-3>",do_popup)
Water_cubicME.bind('<FocusIn>', select_on_focus)
modify = Entry(frame, width=30)
modify.bind("<Button-3>",do_popup)
modify.bind('<FocusIn>', select_on_focus)



def delete_entries():
  for field in fields:
    field.delete(0,END)

fields = Calcium_NitrateE, Potassium_NitrateE, Magnesium_NitrateE, FerillineE, BoraxE, \
         Magnesium_sulphateE, Mono_p_phosphateE, Potassium_sulphateE, Ammonium_sulphateE,\
         Sodium_MolyE, Mn_chellateE, Zn_chellateE, Cu_chellateE, Nitric_acidE, Phosphoric_acidE,\
         Water_cubicME, modify


def go_to_next_entry(event, entry_list, this_index):
    next_index = (this_index + 1) % len(entry_list)
    entry_list[next_index].focus_set()

entries = [child for child in frame.winfo_children() if isinstance(child, Entry)]
for idx, entry in enumerate(entries):
    entry.bind('<Return>', lambda e, idx=idx: go_to_next_entry(e, entries, idx))


def go_to_back_entry(event, entry_list, this_index):
    next_index = (this_index - 1) % len(entry_list)
    entry_list[next_index].focus_set()

entries = [child for child in frame.winfo_children() if isinstance(child, Entry)]
for idx, entry in enumerate(entries):
    entry.bind('<Shift-Return>', lambda e, idx=idx: go_to_back_entry(e, entries, idx))
    

def go_to_next_entry_arrow(event, entry_list, this_index):
    next_index = (this_index + 1) % len(entry_list)
    entry_list[next_index].focus_set()

entries = [child for child in frame.winfo_children() if isinstance(child, Entry)]
for idx, entry in enumerate(entries):
    entry.bind('<Down>', lambda e, idx=idx: go_to_next_entry_arrow(e, entries, idx))
    

def go_to_back_entry_arrow(event, entry_list, this_index):
    next_index = (this_index - 1) % len(entry_list)
    entry_list[next_index].focus_set()

entries = [child for child in frame.winfo_children() if isinstance(child, Entry)]
for idx, entry in enumerate(entries):
    entry.bind('<Up>', lambda e, idx=idx: go_to_back_entry_arrow(e, entries, idx))

    
#Calculate button
Cbutton = Button(frame, text="Calculate Regime", command=lambda: [update_progress_bar()]
                 ,bg='skyblue', fg='black',
                 font=("Times",12,"bold"), activebackground='skyblue')
Cbutton.place(x = 140, y = 455)


#Entries ballon  
balloon.bind(Cbutton, "Calculate")
balloon.bind(Calcium_NitrateE,"numbers")
balloon.bind(Potassium_NitrateE, "numbers")
balloon.bind(Magnesium_NitrateE, "numbers")
balloon.bind(FerillineE, "numbers")
balloon.bind(BoraxE, "numbers")
balloon.bind(Magnesium_sulphateE, "numbers")
balloon.bind(Mono_p_phosphateE, "numbers")
balloon.bind(Potassium_sulphateE, "numbers")
balloon.bind(Ammonium_sulphateE, "numbers")
balloon.bind(Sodium_MolyE, "numbers")
balloon.bind(Mn_chellateE, "numbers")
balloon.bind(Zn_chellateE, "numbers")
balloon.bind(Cu_chellateE, "numbers")
balloon.bind(Nitric_acidE, "numbers")
balloon.bind(Phosphoric_acidE, "numbers")
balloon.bind(Water_cubicME, "numbers")
balloon.bind(modify, "Search")

#Soil interface
def Soil():
    Header_hydro =Label(frame, text="SOIL REGIME                                          ", font=("Times",16,"bold"), fg="blue")
    Header_hydro.place(x = 130, y = 25)

    Fertilizers =Label(frame, text="Fertilizers", font=("Times",13,"bold"))
    Fertilizers.place(x = 10, y = 50)

    Amount =Label(frame, text="Amount kgs/lts", font=("Times",13,"bold"))
    Amount.place(x = 160, y = 50)

    Calcim_Nitrate=Label(frame, text="Calcium Nitrate", font=("Times",13))
    Calcim_Nitrate.place(x = 10, y = 75)

    Potassium_Nitrate=Label(frame, text="Potassium Nitrate", font=("Times",13))
    Potassium_Nitrate.place(x = 10, y = 100)

    Magnesium_Nitrate=Label(frame, text="Magnesium Nitrate", font=("Times",13))
    Magnesium_Nitrate.place(x = 10, y = 125)

    Ferilline=Label(frame, text="Ferilline", font=("Times",13))
    Ferilline.place(x = 10, y = 150)

    Borax=Label(frame, text="Borax", font=("Times",13))
    Borax.place(x = 10, y = 175)

    Magnesium_sulphate=Label(frame, text="Magnesium Sulphate", font=("Times",13))
    Magnesium_sulphate.place(x = 10, y = 200)

    Mono_p_phosphate =Label(frame, text="Mono p phosphate", font=("Times",13))
    Mono_p_phosphate.place(x = 10, y = 225)

    Potassium_sulphate =Label(frame, text="Potassium Sulphate", font=("Times",13))
    Potassium_sulphate.place(x = 10, y = 250)

    Ammonium_sulphate =Label(frame, text="Ammonium sulphate", font=("Times",13))
    Ammonium_sulphate.place(x = 10, y = 275)

    Sodium_Moly =Label(frame, text="Sodium Molybdate", font=("Times",13))
    Sodium_Moly.place(x = 10, y = 300)

    Mn_chellate =Label(frame, text="Mn chellate", font=("Times",13))
    Mn_chellate.place(x = 10, y = 325)

    Zn_chellate =Label(frame, text="Zn chellate", font=("Times",12))
    Zn_chellate.place(x = 10, y = 350)

    Cu_chellate =Label(frame, text="Cu chellate", font=("Times",13))
    Cu_chellate.place(x = 10, y = 375)

    Nitric_acid =Label(frame, text="Nitric acid", font=("Times",13))
    Nitric_acid.place(x = 10, y = 400)

    Phosphoric_acid =Label(frame, text="Phosphoric acid", font=("Times",13))
    Phosphoric_acid.place(x = 10, y = 425)


def hydro_regime():
    global label
    text.image_create(END, image=photo1)


#loading bar
def update_progress_bar(event=None):
    global barVar
    global bar
    global label2
    global frame4
    label2=Label(text)
    x = barVar.get()
    bar = ttk.Progressbar(text, length=802, style='black.Horizontal.TProgressbar',
                  variable=barVar, mode='indeterminate')
    bar.place(x = 0, y = -15)

    if x < 100:
        barVar.set(x+2)
        label2.after(50, update_progress_bar)
        label2.config(text="{:.0%}".format(x))
        label2.update_idletasks()
    else:
        label2.config(text="{:.0%}".format(x))
        frame4 = Frame(bar, height=22, width=802, bg='white')
        frame4.pack(fill=X)
        cal_sum()

    label2 = Label(text, text='')
    label2.place(x = -10, y = -10)


barVar = DoubleVar()
barVar.set(0)


Cbutton.bind('<Return>', update_progress_bar)

# Hdroponics PPM interface
def Home_Hydro_PPM():
    global frame
    Header_hydro =Label(frame, text="HYDRO REGIME - PPM PROPOSED", font=("Times",16,"bold"), fg="blue")
    Header_hydro.place(x = 130, y = 25)

    Fertilizers =Label(frame, text="Elements      ", font=("Times",13,"bold"))
    Fertilizers.place(x = 10, y = 50)
    
    Amount =Label(frame, text="Amount in ppm", font=("Times",13,"bold"))
    Amount.place(x = 160, y = 50)

    Calcim_Nitrate=Label(frame, text="No3                    ", font=("Times",13))
    Calcim_Nitrate.place(x = 10, y = 75)

    Potassium_Nitrate=Label(frame, text="P                               ", font=("Times",13))
    Potassium_Nitrate.place(x = 10, y = 100)

    Magnesium_Nitrate=Label(frame, text="K                                 ", font=("Times",13))
    Magnesium_Nitrate.place(x = 10, y = 125)
    
    Ferilline=Label(frame, text="Ca                         ", font=("Times",13))
    Ferilline.place(x = 10, y = 150)
    
    Borax=Label(frame, text="Mg                       ", font=("Times",13))
    Borax.place(x = 10, y = 175)

    Magnesium_sulphate=Label(frame, text="S                                 ", font=("Times",13))
    Magnesium_sulphate.place(x = 10, y = 200)
    
    Mono_p_phosphate =Label(frame, text="Fe                             ", font=("Times",13))
    Mono_p_phosphate.place(x = 10, y = 225)
    
    Potassium_sulphate =Label(frame, text="Mn                             ", font=("Times",13))
    Potassium_sulphate.place(x = 10, y = 250)

    Ammonium_sulphate =Label(frame, text="Cu                              ", font=("Times",13))
    Ammonium_sulphate.place(x = 10, y = 275)

    Sodium_Moly =Label(frame, text="B                                ", font=("Times",13))
    Sodium_Moly.place(x = 10, y = 300)

    Mn_chellate =Label(frame, text="Zn                       ", font=("Times",13))
    Mn_chellate.place(x = 10, y = 325)

    Zn_chellate =Label(frame, text="Mo                         ", font=("Times",12))
    Zn_chellate.place(x = 10, y = 350)

    Cu_chellate =Label(frame, text="N-NH4                      ", font=("Times",13))
    Cu_chellate.place(x = 10, y = 375)

    Nitric_acid =Label(frame, text="pH                       ", font=("Times",13))
    Nitric_acid.place(x = 10, y = 400)

    Phosphoric_acid =Label(frame, text="EC                          ", font=("Times",13))
    Phosphoric_acid.place(x = 10, y = 425)

# Soil PPM interface
def Home_Soil_PPM():
    global frame
    Header_hydro =Label(frame, text="SOIL REGIME - PPM PROPOSED     ", font=("Times",16,"bold"), fg="blue")
    Header_hydro.place(x = 130, y = 25)

    Fertilizers =Label(frame, text="Elements      ", font=("Times",13,"bold"))
    Fertilizers.place(x = 10, y = 50)
    
    Amount =Label(frame, text="Amount in ppm", font=("Times",13,"bold"))
    Amount.place(x = 160, y = 50)

    Calcim_Nitrate=Label(frame, text="No3                    ", font=("Times",13))
    Calcim_Nitrate.place(x = 10, y = 75)

    Potassium_Nitrate=Label(frame, text="P                               ", font=("Times",13))
    Potassium_Nitrate.place(x = 10, y = 100)

    Magnesium_Nitrate=Label(frame, text="K                                 ", font=("Times",13))
    Magnesium_Nitrate.place(x = 10, y = 125)
    
    Ferilline=Label(frame, text="Ca                         ", font=("Times",13))
    Ferilline.place(x = 10, y = 150)
    
    Borax=Label(frame, text="Mg                       ", font=("Times",13))
    Borax.place(x = 10, y = 175)

    Magnesium_sulphate=Label(frame, text="S                                 ", font=("Times",13))
    Magnesium_sulphate.place(x = 10, y = 200)
    
    Mono_p_phosphate =Label(frame, text="Fe                             ", font=("Times",13))
    Mono_p_phosphate.place(x = 10, y = 225)
    
    Potassium_sulphate =Label(frame, text="Mn                             ", font=("Times",13))
    Potassium_sulphate.place(x = 10, y = 250)

    Ammonium_sulphate =Label(frame, text="Cu                              ", font=("Times",13))
    Ammonium_sulphate.place(x = 10, y = 275)

    Sodium_Moly =Label(frame, text="B                                ", font=("Times",13))
    Sodium_Moly.place(x = 10, y = 300)

    Mn_chellate =Label(frame, text="Zn                       ", font=("Times",13))
    Mn_chellate.place(x = 10, y = 325)

    Zn_chellate =Label(frame, text="Mo                         ", font=("Times",12))
    Zn_chellate.place(x = 10, y = 350)

    Cu_chellate =Label(frame, text="N-NH4                      ", font=("Times",13))
    Cu_chellate.place(x = 10, y = 375)

    Nitric_acid =Label(frame, text="pH                       ", font=("Times",13))
    Nitric_acid.place(x = 10, y = 400)

    Phosphoric_acid =Label(frame, text="EC                          ", font=("Times",13))
    Phosphoric_acid.place(x = 10, y = 425)

#Save document

def file_save():
    files = [('All Files', '*.*'), 
             ('Python Files', '*.py'),
             ('Text Document', '*.txt'),
             ('Word Document', '*.docx'),
             ('Pdf Document', '*.pdf'),
             ('Photo Document', '*.png'),
             ('Excel Document', '*.xlsx')]
    
    file = asksaveasfile(filetypes = files, defaultextension = files)



# use fuction
label3 = Label(frame,text='Find:')
buttn = Button(frame, text='Find')


def find():
    global modify
    global buttn
    global label3
    label3.place(x=450,y=0)
    modify.pack(side=TOP, expand=YES)
    modify.focus_set()
    buttn.place(x=820,y=0)
	
    text.tag_remove('found', '1.0', END)
    ser = modify.get()
    if ser:
            idx = '1.0'
            while 1:
                    idx = text.search(ser, idx, nocase=1,
                                                    stopindex=END)
                    if not idx: break
                    lastidx = '%s+%dc' % (idx, len(ser))
                    
                    text.tag_add('found', idx, lastidx)
                    idx = lastidx
            text.tag_config('found', foreground='blue', background='yellow')
    modify.focus_set()
buttn.config(command=find)

find()

#Find in app
def take_user_input_for_something(event=None):
    user_input = simpledialog.askstring("Search item!", "Search for item?")
    if user_input != "":
        print(user_input)
        
    
def Edit():
    global frame
    frame.pack_forget()
    

def refresh():
    update_progress_bar()

def Edit_get():
    global frame2
    frame2.pack_forget()

def soil_regime():
    text.image_create(END, image=photo2)
    
def lab_result():
    text.image_create(END, image=photo4)

def insert():
    text.insert(END, '\n')

    
def clear_all():
    global text
    text.delete("1.0","end")



def text_again():
    global label
    global text
    Clear_get()
    text = Text(frame4, height=39, width=98, bg='white', undo=True)

    scroll_h = Scrollbar(frame4, orient = 'horizontal')
    scroll_v = Scrollbar(frame4)
    scroll_h.pack(side=BOTTOM, fill=X)
    scroll_v.pack(side=RIGHT, fill=Y)
    text.configure(xscrollcommand=scroll_h.set,
               yscrollcommand=scroll_v.set )


    text.pack(pady=0, padx=0, side=RIGHT)
    text.bind("<Button-3>",do_popup)
    scroll_h.config(command=text.xview)
    scroll_v.config(command=text.yview)

    
def Exit(event=None):
    answer = messagebox.askyesno("!","Do you want to exit?")
    if answer == True:
        root.destroy()


def about_app():
    Pmw.aboutversion('1.0')
    Pmw.aboutcopyright('Copyright Rainforest 2022\nAll rights reserved')
    Pmw.aboutcontact(
        'For information about this application contact:\n' +
        ' Sales at Benson Mwangi\n' +
        ' Phone: 0742309044\n' +
        ' email: bensonmwangi101@gmail.com'
        )
    about = Pmw.AboutDialog(root, applicationname='FertRegime application')
     

def hydro_description():
    text.insert(END, "\n Overall Regime ppm WITH 30% AFTER UV SOLUTION, Hydropinics")

def soil_description():
    text.insert(END, "\n Overall Regime ppm WITH 50% AFTER UV SOLUTION, Soil") 





# function to open a new window
def openNewWindow():
    newWindow = Toplevel(root)

    # Create an instance of tkinter frame

    # Set the size of the tkinter window
    newWindow.geometry("800x500")

    # Create an object of Style widget
    style = ttk.Style()
    style.theme_use('clam')

    # Create a Frame
    frame = Frame(newWindow)
    frame.pack()
    
    # Define a function for opening the file
    def open_file():
       filename = filedialog.askopenfilename(title="Open a File", filetype=(("xlxs files", ".*xlsx"),
    ("All Files", "*.")))

       if filename:
          try:
             filename = r"{}".format(filename)
             df = pd.read_excel(filename)
          except ValueError:
             label.config(text="File could not be opened")
          except FileNotFoundError:
             label.config(text="File Not Found")

       # Clear all the previous data in tree
       clear_treeview()

       # Add new data in Treeview widget
       tree["column"] = list(df.columns)
       tree["show"] = "headings"

       # For Headings iterate over the columns
       for col in tree["column"]:
          tree.heading(col, text=col)

       # Put Data in Rows
       df_rows = df.to_numpy().tolist()
       for row in df_rows:
          tree.insert("", "end", values=row)

       tree.pack()

    # Clear the Treeview Widget
    def clear_treeview():
       tree.delete(*tree.get_children())

    # Create a Treeview widget
    tree = ttk.Treeview(frame)


    def open_pdf():
        global frame
        frame = Frame(newWindow)
        frame.pack()

        # Grab the filename of the pdf file
        open_file = filedialog.askopenfilename(
            title="Open PDF File",
            filetypes=(
                        ("PDF Files", "*.pdf"),
                        ("All Files", "*.*")))
        v1 = pdf.ShowPdf()
        v2 = v1.pdf_view(frame,
                     pdf_location = open_file,
                         )
        v2.pack(fill=BOTH, expand=YES)


    newWindow.title("Fertigation ppm app")
    def Exit():
        answer = messagebox.askyesno("!","Do you want to exit?")
        if answer == True:
            newWindow.destroy()

    
    my_menu = Menu(newWindow)
    newWindow.config(menu=my_menu)
    
    file_menu = Menu(my_menu, tearoff=0)
    my_menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_separator()
    file_menu.add_command(label='New',command=open_pdf)
    file_menu.add_command(label='Open', command = open_file)
    file_menu.add_command(label='Save as')
    file_menu.add_command(label='Save')
    file_menu.add_command(label='Recent file...')
    file_menu.add_command(label='Exit', command=Exit)

        
    edit_menu = Menu(my_menu,tearoff=0)
    my_menu.add_cascade(label="Edit", menu=edit_menu)
    edit_menu.add_separator()
    edit_menu.add_command(label='Undo')
    edit_menu.add_command(label='Redo')
    edit_menu.add_command(label='Copy')
    edit_menu.add_command(label='paste')
    edit_menu.add_command(label='clear all', command=clear_all)
    edit_menu.add_command(label='Select all')


    text = Text(newWindow)
    photo1=ImageTk.PhotoImage(file='hydro_regime.png')
    photo2=ImageTk.PhotoImage(file='soil_regime.png')
    photo3=ImageTk.PhotoImage(file='loading.png')
    photo4=ImageTk.PhotoImage(file='lab_result.png')
    scroll = Scrollbar(newWindow, command=text.yview)

    text.configure(yscrollcommand=scroll.set)
    text.pack(side=LEFT, fill=BOTH, expand=YES)
    scroll.pack(side=RIGHT, fill=BOTH)

    insert_menu = Menu(my_menu,tearoff=0)
    my_menu.add_cascade(label="Insert", menu=insert_menu)
    insert_menu.add_separator()
    insert_menu.add_command(label='Add charts')
    insert_menu.add_command(label='Tables')
    insert_menu.add_command(label='add pictures')
    insert_menu.add_command(label='Hyperlinks')

    data_menu = Menu(my_menu,tearoff=0)
    my_menu.add_cascade(label="Data", menu=data_menu)
    data_menu.add_separator()
    data_menu.add_command(label='Sort')
    data_menu.add_command(label='Filter')
    data_menu.add_command(label='Remove duplicates')
    data_menu.add_command(label='Data validation')
    data_menu.add_command(label='Reflesh', command=update_progress_bar)

    view_menu = Menu(my_menu,tearoff=0)
    my_menu.add_cascade(label="View", menu=view_menu)
    view_menu.add_separator()
    view_menu.add_command(label='Formulas')
    view_menu.add_command(label='New window', command=openNewWindow)
    view_menu.add_command(label='Arrange all')
    view_menu.add_command(label='Switch windows')

    option_menu = Menu(my_menu,tearoff=0)
    my_menu.add_cascade(label="Option", menu=option_menu)
    option_menu.add_separator()
    option_menu.add_command(label='Load soil', command=soil_regime)
    option_menu.add_command(label='load Hdroponics', command=hydro_regime)
    option_menu.add_command(label='30 % UV water, hydro', command = hydro_description)
    option_menu.add_command(label='50 % UV water, soil', command = soil_description)
    option_menu.add_command(label='Print', command = soil_description)

    help_menu = Menu(my_menu, tearoff=0)
    my_menu.add_cascade(label="Help", menu=help_menu)
    help_menu.add_separator()
    help_menu.add_command(label='about app', command=about_app)
    help_menu.add_command(label='converting ppm')
    help_menu.add_command(label='regime calculation demo')
    help_menu.add_command(label='Recent lab documents', command = lab_result)


#main window

file_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="File", menu=file_menu, underline=0)
file_menu.add_separator()
file_menu.add_command(label='New', underline=0)
file_menu.add_command(label='Open', underline=0)
file_menu.add_command(label='Hydro Home', underline=0, command=lambda : [Hydroponics(), delete_entries(), Clear_get()])
file_menu.add_command(label='Soil Home', underline=3, command=lambda : [Soil(), delete_entries(), Clear_get()])
file_menu.add_command(label='Save as', underline=1, command=file_save)
file_menu.add_command(label='Save', underline=0)

sub_file_menu = Menu(file_menu, tearoff=0)
file_menu.add_cascade(label="Open recent file...", underline=5, menu=sub_file_menu)
for i in range(8):
    number = str(i + 1)
    sub_file_menu.add_command(label=number + ". file.txt", underline=0)
    
file_menu.add_command(label='Exit', underline=0, accelerator="Ctrl-Q", command=Exit)
root.bind_all("<Control-q>", Exit)
    
edit_menu = Menu(my_menu,tearoff=0)
my_menu.add_cascade(label="Edit", underline=0, menu=edit_menu)
edit_menu.add_separator()
edit_menu.add_command(label='Undo',underline=0)
edit_menu.add_command(label='Redo',underline=0)
edit_menu.add_command(label='Copy', underline=0)
edit_menu.add_command(label='Paste', underline=0)
edit_menu.add_command(label='Find', underline=0, accelerator="Ctrl-F",command=take_user_input_for_something)
root.bind_all("<Control-f>", take_user_input_for_something)
edit_menu.add_command(label='Clear all', underline=1, command=lambda : [delete_entries()])
edit_menu.add_command(label='Select all', underline=0)


photo1=ImageTk.PhotoImage(file='hydro_regime.png')
photo2=ImageTk.PhotoImage(file='soil_regime.png')
photo3=ImageTk.PhotoImage(file='loading.png')
photo4=ImageTk.PhotoImage(file='lab_result.png')

text = Text(frame, height=110, width=100, bg='white', undo=True)

scroll_h = Scrollbar(frame, orient = 'horizontal')
scroll_v = Scrollbar(frame)
scroll_h.pack(side=BOTTOM, fill=X)
scroll_v.pack(side=RIGHT, fill=Y)
text.configure(xscrollcommand=scroll_h.set,
               yscrollcommand=scroll_v.set )


text.pack(pady=15, padx=20, side=RIGHT)
scroll_h.config(command=text.xview)
scroll_v.config(command=text.yview)


insert_menu = Menu(my_menu,tearoff=0)
my_menu.add_cascade(label="Insert",underline=0, menu=insert_menu)
insert_menu.add_separator()
insert_menu.add_command(label='Add charts', underline=0)
insert_menu.add_command(label='Tables', underline=0)
insert_menu.add_command(label='add pictures', underline=4)
insert_menu.add_command(label='Hyperlinks', underline=0)

data_menu = Menu(my_menu,tearoff=0)
my_menu.add_cascade(label="Data",underline=0, menu=data_menu)
data_menu.add_separator()
data_menu.add_command(label='Sort', underline=0, command=update_progress_bar)
data_menu.add_command(label='Filter', underline=0)
data_menu.add_command(label='Remove duplicates', underline=0)
data_menu.add_command(label='Data validation', underline=5)
data_menu.add_command(label='Refresh', underline=5, command= lambda : [text_again()])

view_menu = Menu(my_menu,tearoff=0)
my_menu.add_cascade(label="View",underline=0, menu=view_menu)
view_menu.add_separator()
view_menu.add_command(label='Formulas',underline=0)
view_menu.add_command(label='New window',underline=0, command=openNewWindow)
view_menu.add_command(label='Arrange all',underline=0, command= lambda : [Edit()])
view_menu.add_command(label='Switch window', underline=1)
view_menu.add_command(label='Hydro PPM window',underline=0, command=lambda : [Home_Hydro_PPM(),delete_entries(),Clear_get()])
view_menu.add_command(label='Soil PPM window',underline=0, command=lambda : [Home_Soil_PPM(),delete_entries(),Clear_get()])



option_menu = Menu(my_menu,tearoff=0)
my_menu.add_cascade(label="Option",underline=0, menu=option_menu)
option_menu.add_separator()
option_menu.add_command(label='Load Soil',underline=5, command= lambda : [Open_Soilm()])
option_menu.add_command(label='Load Hdroponics',underline=5, command= lambda : [Open_Hyrom()])
option_menu.add_command(label='30 % UV water, hydro',underline=0, command = hydro_description)
option_menu.add_command(label='50 % UV water, soil',underline=0, command = soil_description)
option_menu.add_command(label='Print',underline=0, command= lambda : [Open_bothm()])

help_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Help",underline=0, menu=help_menu)
help_menu.add_separator()
help_menu.add_command(label='about app',underline=0, command=about_app)
help_menu.add_command(label='converting ppm',underline=0)
help_menu.add_command(label='regime calculation demo', underline=0)
help_menu.add_command(label='Recent lab documents', underline=11, command = lab_result)

# right click mouse on frame

frame.bind("<Button-3>", do_popup)

def mediaf(event):
    if menu.get() == "HYDRO":
        Hydroponics()
        delete_entries()
        Clear_get()
    if menu.get() == "SOIL":
        Soil()
        delete_entries()
        Clear_get()
    if menu.get() == "HYDRO PPM":
        Home_Hydro_PPM()
        delete_entries()
        Clear_get()
    if menu.get() == "SOIL PPM":
        Home_Soil_PPM()
        delete_entries()
        Clear_get()

options = ["HYDRO", "SOIL","HYDRO PPM","SOIL PPM"]
#Set the Menu initially
menu= StringVar()
menu.set("MEDIA")

#Create a dropdown Menu
drop= OptionMenu(frame, menu,*options, command=mediaf)
drop.place(x=0,y=0)
drop.bind("<Button-3>", do_popup)


# right click mouse on text
text.bind("<Button-3>", do_popup)


#selcect frame

saved = {}

class SelectArea():
    def __init__(self, master, *args, **kwargs):
        self.master = master
        master.bind("<Button-1>", self.StartSelect)
        master.bind("<B1-Motion>", self.SelectMotion)
        master.bind("<ButtonRelease-1>", self.EndSelection)
        self.SelectFrame = Frame(master, width=0, height=0, highlightbackground="blue", highlightcolor="red", highlightthickness=1)

    def StartSelect(self, event):
        for obj in self.master.winfo_children():
            if str(obj.winfo_name()) != "!frame":
                saved.update({obj:obj["bg"]})
        self.startx = event.x
        self.starty = event.y

    def SelectMotion(self, event):
        self.endx = event.x
        self.endy = event.y
        if self.startx > self.endx and self.starty > self.endy:
            width = ((self.startx-self.endx))
            height = ((self.starty-self.endy))
            self.SelectFrame.place(x=self.endx, y=self.endy)
        elif self.startx > self.endx and self.starty < self.endy:
            width = ((self.startx-self.endx))
            height = ((self.endy-self.starty))
            self.SelectFrame.place(x=self.endx, y=self.starty)
        elif self.startx < self.endx and self.starty > self.endy:
            width = ((self.endx-self.startx))
            height = ((self.starty-self.endy))
            self.SelectFrame.place(x=self.startx, y=self.endy)
        else:
            width = ((self.endx-self.startx))
            height = ((self.endy-self.starty))
            self.SelectFrame.place(x=self.startx, y=self.starty)
        self.SelectFrame["width"] = width
        self.SelectFrame["height"] = height
        self.HoverWidgets()

    def EndSelection(self, event):
        self.SelectFrame.place_forget()
        for obj in self.master.winfo_children():
            if str(obj.winfo_name()) != "!frame":
                obj["bg"] = '#CDCDCD'

    def HoverWidgets(self):
        for obj in self.master.winfo_children():
            if str(obj.winfo_name()) != "!frame":
                if self.endx >= obj.winfo_x() and self.endx <= obj.winfo_x() + obj.winfo_width() and self.endy >= obj.winfo_y() and self.endy <= obj.winfo_y() + obj.winfo_height():
                    obj["bg"] = "light blue"

if __name__=="__main__":
    SelectArea(root)
    SelectArea(frame4)
    SelectArea(drop)


def loading():
    text.image_create(END, image=photo3)
    
loading()

seconds = 1 # Initial time must be the time+1 (now 0+1)
timer = None
def tick ():
    global seconds, timer
    seconds -= 1
    if seconds==0:
        clear_all()
        insert()

        
    timer = threading.Timer(1, tick)
    timer.start()

seconds += 1
tick()
root.mainloop()
