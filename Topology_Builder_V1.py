
import random
import tkinter as tk
from PIL import ImageTk, Image
import os, sys
import tkinter.messagebox

################ Import picture #############################
def rc(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)
Img_Transmitter=rc("Transmitter.jpeg")
Img_Receiver=rc("Receiver.jpeg")
Img_Trace=rc("Trace.jpeg")
Img_Via=rc("Via.jpeg")
Img_Conn=rc("Conn.jpeg")
Img_cable=rc("Cable.jpeg")
Img_Capacitor=rc("Capacitor.jpeg")
Img_Resistor=rc("Resistor.jpeg")
Img_Indctor=rc("Inductor.jpeg")
Img_Redrv=rc("ReDrv.jpeg")
################ Import picture #############################

################ Export picture #############################

##還沒找到適合的方案來替代pyHook##

################ Export picture #############################

################# Color Setting #################

ct = [random.randrange(256) for x in range(3)]
brightness = int(round(0.299 * ct[0] + 0.587 * ct[1] + 0.114 * ct[2]))
ct_hex = "%02x%02x%02x" % tuple(ct)
bg_colour = '#' + "".join(ct_hex)
################# Color Setting #################

################# Main Frame Setting #################
Mwin = tk.Tk()
Mwin.title('Topology Builder')
Mwin.geometry('900x400')
Mwin.resizable(True,False)

frame1 = tk.Frame(Mwin, width=900, height=400, background="white")
frame2 = tk.Frame(Mwin, width=900, height=300, background="white")

frame1.pack(fill=None, expand=False)
frame2.place(relx=.5, rely=.8, anchor="c")
################# Main Frame Setting #################

################ Menu #############################
def hit_me():
    print(tk.messagebox._show(title='About Tool', message='The purpose of tool is to help SI engineer to create signal topology more quickly'))
menubar = tk.Menu(Mwin)
filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=filemenu)
#filemenu.add_command(label='Save', command='')
filemenu.add_command(label='Exit', command=Mwin.quit)
editmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='Help', menu=editmenu)
editmenu.add_command(label='About Tool', command=hit_me)
Mwin.config(menu=menubar)
################ Menu #############################


################ Delete Topology #############################
element_count_pic=0
element_count_text=0
element_count_info1=0
element_count_info2=0
dict_pic={}
dict_text1={}
dict_text2={}

def delete_element():
    global dict_pic
    global dict_text
    global element_count_pic
    global element_count_text
    if element_count_pic > 0:
        dict_pic[element_count_pic].destroy()
        dict_text1[element_count_text].destroy()
        dict_text2[element_count_text].destroy()
        element_count_pic = element_count_pic - 1
        element_count_text = element_count_text - 1
        if element_count_pic<0: element_count_pic=0
        print('element_count_pic:',element_count_pic)
        print('element_count_text:',element_count_text)
    else: pass

def clear_element():
    for i in range(element_count_pic):
        delete_element()
        print('clear work')
################ Delete Topology #############################

################ Add an element in Topology #############################
img1 = ImageTk.PhotoImage(Image.open(Img_Trace))
def add_trace():
    global dict_pic
    global dict_text
    global element_count_pic
    global element_count_text
    element_count_pic += 1
    element_count_text += 1
    dict_pic.update({element_count_pic: element_count_pic})
    dict_text1.update({element_count_text: element_count_text})
    dict_text2.update({element_count_text: element_count_text})
    dict_pic[element_count_pic] = tk.Label(frame2, imag=img1)
    dict_pic[element_count_pic].grid(row=0, column=element_count_pic, ipadx=0, ipady=0)
    dict_text1[element_count_text]= tk.Label(frame2,text='Length: '+Input_Trace_Length.get()+' mil')
    dict_text1[element_count_text].grid(row=1, column=element_count_text, ipadx=0, ipady=0)
    dict_text2[element_count_text]= tk.Label(frame2,text='Layer: '+Input_Trace_Layer.get())
    dict_text2[element_count_text].grid(row=2, column=element_count_text, ipadx=0, ipady=0)
    print(element_count_pic)

img2 = ImageTk.PhotoImage(Image.open(Img_Receiver))
def add_Receiver():
    global dict_pic
    global dict_text
    global element_count_pic
    global element_count_text
    element_count_pic += 1
    element_count_text += 1
    dict_pic.update({element_count_pic: element_count_pic})
    dict_text1.update({element_count_text: element_count_text})
    dict_text2.update({element_count_text: element_count_text})
    dict_pic[element_count_pic] = tk.Label(frame2, imag=img2)
    dict_pic[element_count_pic].grid(row=0, column=element_count_pic, ipadx=0, ipady=0)
    dict_text1[element_count_text]= tk.Label(frame2,text='Type: '+Input_IC_Name.get())
    dict_text1[element_count_text].grid(row=1, column=element_count_text, ipadx=0, ipady=0)
    dict_text2[element_count_text]= tk.Label(frame2,text='  ')
    dict_text2[element_count_text].grid(row=2, column=element_count_text, ipadx=0, ipady=0)
    print(element_count_pic)

img3 = ImageTk.PhotoImage(Image.open(Img_Transmitter))
def add_Transmitter():
    global dict_pic
    global dict_text
    global element_count_pic
    global element_count_text
    element_count_pic += 1
    element_count_text += 1
    dict_pic.update({element_count_pic: element_count_pic})
    dict_text1.update({element_count_text: element_count_text})
    dict_text2.update({element_count_text: element_count_text})
    dict_pic[element_count_pic] = tk.Label(frame2, imag=img3)
    dict_pic[element_count_pic].grid(row=0, column=element_count_pic, ipadx=0, ipady=0)
    dict_text1[element_count_text]= tk.Label(frame2,text='Type: '+Input_IC_Name.get())
    dict_text1[element_count_text].grid(row=1, column=element_count_text, ipadx=0, ipady=0)
    dict_text2[element_count_text]= tk.Label(frame2,text='  ')
    dict_text2[element_count_text].grid(row=2, column=element_count_text, ipadx=0, ipady=0)
    print(element_count_pic)

img4 = ImageTk.PhotoImage(Image.open(Img_Via))
def add_Via():
    global dict_pic
    global dict_text
    global element_count_pic
    global element_count_text
    element_count_pic += 1
    element_count_text += 1
    dict_pic.update({element_count_pic: element_count_pic})
    dict_text1.update({element_count_text: element_count_text})
    dict_text2.update({element_count_text: element_count_text})
    dict_pic[element_count_pic] = tk.Label(frame2, imag=img4)
    dict_pic[element_count_pic].grid(row=0, column=element_count_pic, ipadx=0, ipady=0)
    dict_text1[element_count_text]= tk.Label(frame2,text='Stub: '+Input_Via_stub.get()+' mil')
    dict_text1[element_count_text].grid(row=1, column=element_count_text, ipadx=0, ipady=0)
    dict_text2[element_count_text]= tk.Label(frame2,text='  ')
    dict_text2[element_count_text].grid(row=2, column=element_count_text, ipadx=0, ipady=0)
    print(element_count_pic)

img5 = ImageTk.PhotoImage(Image.open(Img_Conn))
def add_Conn():
    global dict_pic
    global dict_text
    global element_count_pic
    global element_count_text
    element_count_pic += 1
    element_count_text += 1
    dict_pic.update({element_count_pic: element_count_pic})
    dict_text1.update({element_count_text: element_count_text})
    dict_text2.update({element_count_text: element_count_text})
    dict_pic[element_count_pic] = tk.Label(frame2, imag=img5)
    dict_pic[element_count_pic].grid(row=0, column=element_count_pic, ipadx=0, ipady=0)
    dict_text1[element_count_text]= tk.Label(frame2,text='Type: '+Input_Conn_type.get())
    dict_text1[element_count_text].grid(row=1, column=element_count_text, ipadx=0, ipady=0)
    dict_text2[element_count_text]= tk.Label(frame2,text='  ')
    dict_text2[element_count_text].grid(row=2, column=element_count_text, ipadx=0, ipady=0)
    print(element_count_pic)

img6 = ImageTk.PhotoImage(Image.open(Img_cable))
def add_Cable():
    global dict_pic
    global dict_text
    global element_count_pic
    global element_count_text
    element_count_pic += 1
    element_count_text += 1
    dict_pic.update({element_count_pic: element_count_pic})
    dict_text1.update({element_count_text: element_count_text})
    dict_text2.update({element_count_text: element_count_text})
    dict_pic[element_count_pic] = tk.Label(frame2, imag=img6)
    dict_pic[element_count_pic].grid(row=0, column=element_count_pic, ipadx=0, ipady=0)
    dict_text1[element_count_text]= tk.Label(frame2,text='AWG Size: '+Input_Cable_AWG.get())
    dict_text1[element_count_text].grid(row=1, column=element_count_text, ipadx=0, ipady=0)
    dict_text2[element_count_text]= tk.Label(frame2,text='Length: '+Input_Cable_Length.get()+' mm')
    dict_text2[element_count_text].grid(row=2, column=element_count_text, ipadx=0, ipady=0)
    print(element_count_pic)

img7 = ImageTk.PhotoImage(Image.open(Img_Resistor))
def add_Res():
    global dict_pic
    global dict_text
    global element_count_pic
    global element_count_text
    element_count_pic += 1
    element_count_text += 1
    dict_pic.update({element_count_pic: element_count_pic})
    dict_text1.update({element_count_text: element_count_text})
    dict_text2.update({element_count_text: element_count_text})
    dict_pic[element_count_pic] = tk.Label(frame2, imag=img7)
    dict_pic[element_count_pic].grid(row=0, column=element_count_pic, ipadx=0, ipady=0)
    dict_text1[element_count_text]= tk.Label(frame2,text='  ')
    dict_text1[element_count_text].grid(row=1, column=element_count_text, ipadx=0, ipady=0)
    dict_text2[element_count_text]= tk.Label(frame2,text='  ')
    dict_text2[element_count_text].grid(row=2, column=element_count_text, ipadx=0, ipady=0)
    print(element_count_pic)

img8 = ImageTk.PhotoImage(Image.open(Img_Capacitor))
def add_Cap():
    global dict_pic
    global dict_text
    global element_count_pic
    global element_count_text
    element_count_pic += 1
    element_count_text += 1
    dict_pic.update({element_count_pic: element_count_pic})
    dict_text1.update({element_count_text: element_count_text})
    dict_text2.update({element_count_text: element_count_text})
    dict_pic[element_count_pic] = tk.Label(frame2, imag=img8)
    dict_pic[element_count_pic].grid(row=0, column=element_count_pic, ipadx=0, ipady=0)
    dict_text1[element_count_text]= tk.Label(frame2,text='  ')
    dict_text1[element_count_text].grid(row=1, column=element_count_text, ipadx=0, ipady=0)
    dict_text2[element_count_text]= tk.Label(frame2,text='  ')
    dict_text2[element_count_text].grid(row=2, column=element_count_text, ipadx=0, ipady=0)
    print(element_count_pic)

img9 = ImageTk.PhotoImage(Image.open(Img_Indctor))
def add_Indctor():
    global dict_pic
    global dict_text
    global element_count_pic
    global element_count_text
    element_count_pic += 1
    element_count_text += 1
    dict_pic.update({element_count_pic: element_count_pic})
    dict_text1.update({element_count_text: element_count_text})
    dict_text2.update({element_count_text: element_count_text})
    dict_pic[element_count_pic] = tk.Label(frame2, imag=img9)
    dict_pic[element_count_pic].grid(row=0, column=element_count_pic, ipadx=0, ipady=0)
    dict_text1[element_count_text]= tk.Label(frame2,text='  ')
    dict_text1[element_count_text].grid(row=1, column=element_count_text, ipadx=0, ipady=0)
    dict_text2[element_count_text]= tk.Label(frame2,text='  ')
    dict_text2[element_count_text].grid(row=2, column=element_count_text, ipadx=0, ipady=0)
    print(element_count_pic)

img10 = ImageTk.PhotoImage(Image.open(Img_Redrv))
def add_Redrv():
    global dict_pic
    global dict_text
    global element_count_pic
    global element_count_text
    element_count_pic += 1
    element_count_text += 1
    dict_pic.update({element_count_pic: element_count_pic})
    dict_text1.update({element_count_text: element_count_text})
    dict_text2.update({element_count_text: element_count_text})
    dict_pic[element_count_pic] = tk.Label(frame2, imag=img10)
    dict_pic[element_count_pic].grid(row=0, column=element_count_pic, ipadx=0, ipady=0)
    dict_text1[element_count_text]= tk.Label(frame2,text='Type: '+Input_IC_Name.get())
    dict_text1[element_count_text].grid(row=1, column=element_count_text, ipadx=0, ipady=0)
    dict_text2[element_count_text]= tk.Label(frame2,text='  ')
    dict_text2[element_count_text].grid(row=2, column=element_count_text, ipadx=0, ipady=0)
    print(element_count_pic)
################ Add an element in Topology #############################




################# Label Setting #################
Tool_Name = tk.Label(frame1, text='', width=10)
Tool_Name.grid(row=0,column=0)

IC_Name = tk.Label(frame1, text='IC Name', width=10)
IC_Name.grid(row=1,column=0)

Trace_Layer_Name = tk.Label(frame1, text='Layer', width=10)
Trace_Layer_Name.grid(row=1,column=1)

Trace_Length_Name = tk.Label(frame1, text='Length (mil)', width=10)
Trace_Length_Name.grid(row=3,column=1)

Via_stub_Name = tk.Label(frame1, text='Via Stub (mil)', width=10)
Via_stub_Name.grid(row=3,column=2)

Connector_Name = tk.Label(frame1, text='Type', width=10)
Connector_Name.grid(row=3,column=3)

Cable_AWG_Name = tk.Label(frame1, text='AWG', width=10)
Cable_AWG_Name.grid(row=1,column=4)

Cable_Length_Name = tk.Label(frame1, text='Length (mm)', width=10)
Cable_Length_Name.grid(row=3,column=4)

Empty1= tk.Label(frame1, text='', width=10)
Empty1.grid(row=2,column=6)

Empty2= tk.Label(frame1, text='', width=10)
Empty2.grid(row=2,column=6)
################# Label Setting #################


################# Entry Setting #################
Input_IC_Name = tk.Entry(frame1, width=10)
Input_IC_Name.grid(row=2,column=0)

Input_Trace_Layer = tk.Entry(frame1, width=10)
Input_Trace_Layer.grid(row=2,column=1)

Input_Trace_Length = tk.Entry(frame1, width=10)
Input_Trace_Length.grid(row=4,column=1)

Input_Via_stub = tk.Entry(frame1, width=10)
Input_Via_stub.grid(row=4,column=2)

Input_Conn_type = tk.Entry(frame1, width=10)
Input_Conn_type.grid(row=4,column=3)

Input_Cable_AWG = tk.Entry(frame1, width=10)
Input_Cable_AWG.grid(row=2,column=4)

Input_Cable_Length = tk.Entry(frame1, width=10)
Input_Cable_Length.grid(row=4,column=4)
################# Entry Setting #################


################# Button Setting #################
Add_transmitter_button = tk.Button(frame1, width=10, text='Transmitter',command=add_Transmitter)
Add_transmitter_button.grid(row=3,column=0,padx=10,pady=1)

Add_receiver_button = tk.Button(frame1, width=10, text='Receiver',command=add_Receiver)
Add_receiver_button.grid(row=4,column=0,padx=10,pady=1)

Add_redrv_button = tk.Button(frame1, width=10, text='Re-Driver',command=add_Redrv)
Add_redrv_button.grid(row=5,column=0,padx=10,pady=1)

Add_Trace_button = tk.Button(frame1, width=10, text='Trace',command=add_trace)
Add_Trace_button.grid(row=5,column=1,padx=10,pady=1)

Add_Via_button = tk.Button(frame1, width=10, text='Via',command=add_Via)
Add_Via_button.grid(row=5,column=2,padx=10,pady=1)

Add_Connector_button = tk.Button(frame1, width=10, text='Connector',command=add_Conn)
Add_Connector_button.grid(row=5,column=3,padx=10,pady=1)

Add_Cable_button = tk.Button(frame1, width=10, text='Cable',command=add_Cable)
Add_Cable_button.grid(row=5,column=4,padx=10,pady=1)

Add_Resistor_button = tk.Button(frame1, width=10, text='Resisotr',command=add_Res)
Add_Resistor_button.grid(row=4,column=5,padx=10,pady=1)

Add_Inductor_button = tk.Button(frame1, width=10, text='Inductor',command=add_Indctor)
Add_Inductor_button.grid(row=3,column=5,padx=10,pady=1)

Add_Capacitor_button = tk.Button(frame1, width=10, text='Capacitor',command=add_Cap)
Add_Capacitor_button.grid(row=5,column=5,padx=10,pady=1)

Add_Delete_button = tk.Button(frame1, width=10, text='Delete',command=delete_element)
Add_Delete_button.grid(row=5,column=7,padx=10,pady=1)

Add_Clear_button = tk.Button(frame1, width=10, text='Clear All',command=clear_element)
Add_Clear_button.grid(row=4,column=7,padx=10,pady=1)

#Add_Save_button = tk.Button(frame1, width=10, text='Save',command=None)
#Add_Save_button.grid(row=5,column=8,padx=10,pady=1)
################# Button Setting #################


########################signature line#######################################
signature_label = tk.Label(frame1,text='Questions/Comments: Please contact SI/Jimmy Hung\nExt: 23097 , Email: Hung.Jimmy@inventec.com',justify='left', font=('Arial', 8), width=50, height=2 )
signature_label.place(x=480,y=000,anchor='nw')
########################signature line#######################################

Mwin.mainloop()













