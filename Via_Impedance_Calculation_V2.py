import tkinter as tk
from PIL import ImageTk, Image
import os, sys
from decimal import *
import tkinter.messagebox

################ Main Window #############################
window = tk.Tk()
window.title('Via Impedance Calculation')
window.geometry('650x600')
window.resizable(False,False)
################ Main Window #############################

################ Menu #############################
def hit_me():
    print(tk.messagebox._show(title='About Tool', message='The theory of tool is based on statistical analysis and 3D solved tool result.'
                                                          '\nThe purpose of this tool is to help SI engineer to find out the via impedance more quickly.'
                                                          '\nEngineer saves a lot of time in the sweeping parameter for via optimization.'))
menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=filemenu)
#filemenu.add_command(label='Save', command='')
filemenu.add_command(label='Exit', command=window.quit)
editmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='Help', menu=editmenu)
editmenu.add_command(label='About Tool', command=hit_me)
window.config(menu=menubar)
################ Menu #############################


################ Import picture #############################
def rc(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)
icon_se=rc("Via_Impedance_Calculation.jpg")

img = ImageTk.PhotoImage(Image.open(icon_se))
img_label = tk.Label(window, imag=img)
img_label.place(x=0,y=0,anchor='nw')
################ Import picture #############################

################ Add menu #############################

################ Add menu #############################


#############################################
AntiPad_label = tk.Label(window, text='Anti-Pad (mil)',  bg='green', font=('Arial', 12), width=18, height=1 )
AntiPad_label.place(x=330,y=50,anchor='nw')

AntiPad1=tk.Entry(window,show='',width=15)
AntiPad1.place(x=500,y=52.5,anchor='nw')

AntiPad2_label = tk.Label(window, text='Suggested value: 30 - 50 mil', font=('Arial', 10), width=20, height=1 )
AntiPad2_label.place(x=400,y=75,anchor='nw')
###############################################################
Pitch_S2G_label = tk.Label(window, text='Pitch S2G (mil)', bg='green', font=('Arial', 12), width=18, height=1 )
Pitch_S2G_label.place(x=330,y=110,anchor='nw')

Pitch_S2G_label2 = tk.Label(window, text='30', font=('Arial', 12), width=2, height=1 )
Pitch_S2G_label2.place(x=500,y=110,anchor='nw')
#Pitch_S2G1=tk.Entry(window,show='',width=15)
#Pitch_S2G1.place(x=580,y=112.5,anchor='nw')

Pitch_S2G2 = tk.Label(window, text='Suggested value: 30 mil only', font=('Arial', 10), width=20, height=1 )
Pitch_S2G2.place(x=400,y=135,anchor='nw')
###############################################################
Pitch_S2S_label = tk.Label(window,text='Pitch S2S (mil)',  bg='green', font=('Arial', 12), width=18, height=1 )
Pitch_S2S_label.place(x=330,y=170,anchor='nw')

Pitch_S2S1=tk.Entry(window,show='',width=15)
Pitch_S2S1.place(x=500,y=172.5,anchor='nw')

Pitch_S2S2 = tk.Label(window, text='Suggested value: 30 - 50 mil', font=('Arial', 10), width=20, height=1 )
Pitch_S2S2.place(x=400,y=195,anchor='nw')
###############################################################
Via_drill_size_label = tk.Label(window, text='Via drill hole size (mil)', bg='green', font=('Arial', 12), width=18, height=1 )

Via_drill_size_label.place(x=330,y=230,anchor='nw')

Via_drill_size1=tk.Entry(window,show='',width=15)
Via_drill_size1.place(x=500,y=232.5,anchor='nw')

Via_drill_size2 = tk.Label(window, text='Suggested value: 8 - 12 mil', font=('Arial', 10), width=20, height=1 )
Via_drill_size2.place(x=400,y=255,anchor='nw')
###############################################################
Via_Stub_label = tk.Label(window,text='Via Stub (mil)', bg='green', font=('Arial', 12), width=18, height=1 )

Via_Stub_label.place(x=330,y=290,anchor='nw')

Via_Stub1=tk.Entry(window,show='',width=15)
Via_Stub1.place(x=500,y=292.5,anchor='nw')

Via_Stub2 = tk.Label(window, text='Suggested value: 0 - 100 mil', font=('Arial', 10), width=20, height=1 )
Via_Stub2.place(x=400,y=315,anchor='nw')
###############################################################
Dk_label = tk.Label(window,text='Dielectric constant',bg='green', font=('Arial', 12), width=18, height=1 )
Dk_label.place(x=330,y=350,anchor='nw')

Dk1=tk.Entry(window,show='',width=15)
Dk1.place(x=500,y=352.5,anchor='nw')

Via_Stub2 = tk.Label(window, text='Suggested value: 3 - 4', font=('Arial', 10), width=20, height=1 )
Via_Stub2.place(x=383,y=375,anchor='nw')
###############################################################
def calculate_impedance():
    AntiPad=float(AntiPad1.get())
    Pitch_S2G= 30 #float(Pitch_S2G1.get())
    Pitch_S2S=float(Pitch_S2S1.get())
    Via_drill_size=float(Via_drill_size1.get())
    Via_Stub=float(Via_Stub1.get())
    Dk=float(Dk1.get())
    global Impedance
    Impedance=  122.165097764585 + 0.6669243276 * AntiPad + 0 * Pitch_S2G + 0.408009044554444 * Pitch_S2S + -2.86707168392499 * Via_drill_size + -0.421655484423005 * Via_Stub + -9.48190542720001 * Dk + (AntiPad - 40) * (AntiPad - 40) * -0.00931903607746035 + (AntiPad - 40) * (Pitch_S2G - 30) * 0 + (Pitch_S2G - 30) * (Pitch_S2G - 30) * 0 + (AntiPad - 40) * (Pitch_S2S - 40) * 0.0149472969765555 + (Pitch_S2G - 30) * (Pitch_S2S - 40) * 0 + (Pitch_S2S - 40) * (Pitch_S2S - 40) * -0.0107933589420635 + (AntiPad - 40) * (Via_drill_size - 10) * 0.00905564440416666 + (Pitch_S2G - 30) * (Via_drill_size - 10) * 0 + (Pitch_S2S - 40) * (Via_drill_size - 10) * 0.00145920316083333 + (Via_drill_size - 10) * (Via_drill_size - 10) * 0.0431208266208342 + (AntiPad - 40) * (Via_Stub - 36.7000000000001) * -0.00294866125531205 + (Pitch_S2G - 30) * (Via_Stub - 36.7000000000001) * 0 + (Pitch_S2S - 40) * (Via_Stub - 36.7000000000001) * -0.00529701848811238 + (Via_drill_size - 10) * (Via_Stub - 36.7000000000001) * 0.0409881412144616 + (Via_Stub - 36.7000000000001) * (Via_Stub - 36.7000000000001) * -0.00113916931248867 + (AntiPad - 40) * (Dk - 3.5) * 0.0025310173800001 + (Pitch_S2G - 30) * (Dk - 3.5) * 0 + (Pitch_S2S - 40) * (Dk - 3.5) * -0.00539003818333315 + (Via_drill_size - 10) * (Dk - 3.5) * 0.0168599270250014 + (Via_Stub - 36.7000000000001) * (Dk - 3.5) * 0.0134229620750737 + (Dk - 3.5) * (Dk - 3.5) * 1.87390095813333
    showimp.delete(0.0,tk.END)
    showimp.insert('insert',Decimal(Impedance).quantize(Decimal('0.00')))

Cal=tk.Button(window,text='Calculate',font=('Arial', 20), width=19,height=1,command=calculate_impedance)
Cal.place(x=330,y=410,anchor='nw')
###############################################################

###############################################################
result_label = tk.Label(window,text='Impedance (ohm)', bg='green', font=('Arial', 12), width=18, height=1 )
result_label.place(x=330,y=480,anchor='nw')

showimp=tk.Text(window,height=1 ,width=15 ,font=('Arial', 12))
showimp.place(x=500,y=480,anchor='nw')

########################signature line#######################################
signature_label = tk.Label(window,text='Questions/Comments: Please contact SI/Jimmy Hung\nExt: 23097 , Email: Hung.Jimmy@inventec.com',justify='left', font=('Arial', 10), width=39, height=2 )
signature_label.place(x=330,y=560,anchor='nw')

########################signature line#######################################

window.mainloop()