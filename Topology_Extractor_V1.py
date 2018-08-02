# -*- coding:utf-8 -*-
import tkinter as tk
import tkinter.messagebox
import tkinter.filedialog as tkfile
import numpy as np
import pandas as pd
import pandas._libs.tslibs.np_datetime #無功能，但必須載入才能正常轉Win EXE
import pandas._libs.tslibs.nattype     #無功能，但必須載入才能正常轉Win EXE
import pandas._libs.skiplist           #無功能，但必須載入才能正常轉Win EXE


############# Pandas setting #############
pd.set_option('display.width', None)  # 設定顯示最大寬度
pd.set_option('display.max_rows', None)  # 設定顯示最大行數
############# Pandas setting #############


############# Function #############

def select_html_file():
    filename = tkfile.askopenfilename(filetypes=[("Htm Files",".htm"),("Html Files",".html")])
    var.set(filename)

def select_tpy_file():
    filename = tkfile.askopenfilename(filetypes=[("TPY Files",".tpy")])
    tpy_var.set(filename)


def conventer():
    url = PathName.get()
    data_list = pd.read_html(url)  # 轉html to list
    data = data_list[0]  # 轉list to DataFrame
    data.to_csv(tkfile.asksaveasfilename(defaultextension='.tpy',filetypes=[("TPY Files",".tpy")]))

def searching_location():
    url = Tpy_Name.get()
    data = pd.read_csv(url)  # 轉html to list

    data.columns = ['Number', 'Name', 'Total Net Length', 'Layer', 'Total Layer Length (mils)',
                    'Layer Length % of Total', 'Line Width (mils)', 'Length (mils)',
                    'Contiguous Length % Layer Length', 'Location']
    count = -1
    row_list = []
    keyword = NetName.get()

    info = (data['Location'])
    info1 = info.str.split('(', expand=True)
    infoP1 = info1[1].str.split(')', expand=True)
    infoP2 = info1[2].str.split(')', expand=True)
    infoP1XY = infoP1[0].str.split(' ', expand=True)
    infoP2XY = infoP2[0].str.split(' ', expand=True)

    data['Point1_X'] = pd.DataFrame(infoP1XY[0], dtype=np.float)
    data['Point1_Y'] = pd.DataFrame(infoP1XY[1], dtype=np.float)
    data['Point2_X'] = pd.DataFrame(infoP2XY[0], dtype=np.float)
    data['Point2_Y'] = pd.DataFrame(infoP2XY[1], dtype=np.float)

    for i in (data['Name']):
        count = count + 1
        if keyword == i:
            row_list.append(count)
        else:
            pass

    Line_name = (list(data.loc[row_list, 'Name']))
    Line_layer = (list(data.loc[row_list, 'Layer']))
    Line_width = (list(data.loc[row_list, 'Line Width (mils)']))
    Line_length = (list(data.loc[row_list, 'Length (mils)']))
    Point1_1 = (list(data.loc[row_list, 'Point1_X']))
    Point1_2 = (list(data.loc[row_list, 'Point1_Y']))
    Point2_1 = (list(data.loc[row_list, 'Point2_X']))
    Point2_2 = (list(data.loc[row_list, 'Point2_Y']))

    Data_dict = {"Name": Line_name, "Layer": Line_layer, "Line_width": Line_width, "Length": Line_length,
                 'Point1_1': Point1_1
        , 'Point1_2': Point1_2, 'Point2_1': Point2_1, 'Point2_2': Point2_2}
    Data_df = pd.DataFrame(Data_dict)

    flow = pd.DataFrame(Data_dict)
    flow.drop(flow.index, inplace=True)

    flow.loc[0] = Data_df.loc[0]
    Data_df.drop(0, axis=0, inplace=True)
    Data_df.reset_index(drop=True, inplace=True)

    # 初始化插入方向判斷
    up = False
    down = False

    # 初始化最初必要資訊
    index = 0
    temp = 2
    i = 0
    while True:
        if i >= len(Data_df.Point1_1):
            break

        if (flow.Point1_1[index], flow.Point1_2[index]) == (Data_df.Point1_1[i], Data_df.Point1_2[i]) or \
                (flow.Point1_1[index], flow.Point1_2[index]) == (Data_df.Point2_1[i], Data_df.Point2_2[i]) or \
                (flow.Point2_1[index], flow.Point2_2[index]) == (Data_df.Point1_1[i], Data_df.Point1_2[i]) or \
                (flow.Point2_1[index], flow.Point2_2[index]) == (Data_df.Point2_1[i], Data_df.Point2_2[i]):
            if temp == 2:
                flow.loc[1] = Data_df.loc[i]
                Data_df.drop(i, axis=0, inplace=True)
                Data_df.reset_index(drop=True, inplace=True)

                down = True
                i = 0
                temp -= 1
            elif temp == 1:
                line = Data_df.loc[i:i]
                flow = pd.concat([line, flow.loc[0:]]).reset_index(drop=True)
                Data_df.drop(i, axis=0, inplace=True)
                Data_df.reset_index(drop=True, inplace=True)

                up = True
                break

        i += 1

    while True:
        if up is False and down is False:
            break
        if len(Data_df.Point1_1) <= 0:
            break

        if up is True:
            index = 0
            i = 0
            while True:
                if (flow.Point1_1[index], flow.Point1_2[index]) == (Data_df.Point1_1[i], Data_df.Point1_2[i]) or \
                        (flow.Point1_1[index], flow.Point1_2[index]) == (Data_df.Point2_1[i], Data_df.Point2_2[i]) or \
                        (flow.Point2_1[index], flow.Point2_2[index]) == (Data_df.Point1_1[i], Data_df.Point1_2[i]) or \
                        (flow.Point2_1[index], flow.Point2_2[index]) == (Data_df.Point2_1[i], Data_df.Point2_2[i]):
                    line = Data_df.loc[i:i]
                    flow = pd.concat([line, flow.loc[0:]]).reset_index(drop=True)
                    Data_df.drop(i, axis=0, inplace=True)
                    Data_df.reset_index(drop=True, inplace=True)

                    break
                elif i >= len(Data_df.Point1_1) - 1:
                    up = False
                    break

                i += 1

        if down is True:
            index = len(flow.Point1_1) - 1
            i = 0
            while True:
                if (flow.Point1_1[index], flow.Point1_2[index]) == (Data_df.Point1_1[i], Data_df.Point1_2[i]) or \
                        (flow.Point1_1[index], flow.Point1_2[index]) == (Data_df.Point2_1[i], Data_df.Point2_2[i]) or \
                        (flow.Point2_1[index], flow.Point2_2[index]) == (Data_df.Point1_1[i], Data_df.Point1_2[i]) or \
                        (flow.Point2_1[index], flow.Point2_2[index]) == (Data_df.Point2_1[i], Data_df.Point2_2[i]):
                    flow.loc[index + 1] = Data_df.loc[i]
                    Data_df.drop(i, axis=0, inplace=True)
                    Data_df.reset_index(drop=True, inplace=True)

                    break
                elif i >= len(Data_df.Point1_1) - 1:
                    down = False
                    break

                i += 1

    #print("-----------------------------------------------------------------------")
    #print("flow1 : \n", flow, '\n')
    #print("flow2 : \n", flow.reindex(index=flow.index[::-1]), '\n')
    var_Name.set(flow.iloc[:, 0:1])
    var_Layer.set(flow.iloc[:, 1:2])
    var_Line_width.set(flow.iloc[:, 2:3])
    var_Length.set(flow.iloc[:, 3:4])
    var_Point1_1.set(flow.iloc[:, 4:5])
    var_Point1_2.set(flow.iloc[:, 5:6])
    var_Point2_1.set(flow.iloc[:, 6:7])
    var_Point2_2.set(flow.iloc[:, 7:8])



############# Function #############

################# Main Frame Setting #################
Mwin = tk.Tk()
Mwin.title('Topology Extractor')
Mwin.geometry('900x400')
Mwin.resizable(False,False)

frame1 = tk.Frame(Mwin, width=900, height=300, background="white")
frame2 = tk.Frame(Mwin, width=900, height=500, background="white")

frame1.pack(fill=None, expand=False)
frame2.place(relx=.5, rely=.6, anchor="c")
################# Main Frame Setting #################

################ Menu #############################
def hit_me():
    tk.messagebox._show(title='About Tool', message='The purpose of tool is to help SI engineer to create signal topology more quickly')
def help_me():
    tk.messagebox._show(title='About Tool', message='Questions/Comments: Please contact SI/Jimmy Hung\nExt: 23097 , Email: Hung.Jimmy@inventec.com')
menubar = tk.Menu(Mwin)
filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=filemenu)
#filemenu.add_command(label='Save', command='')
filemenu.add_command(label='Exit', command=Mwin.quit)
editmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='Help', menu=editmenu)
editmenu.add_command(label='About Tool', command=hit_me)
editmenu.add_command(label='Contact me', command=help_me)
Mwin.config(menu=menubar)


################ Menu #############################

################# Label Setting #################
Tool_Name = tk.Label(frame1, text='', width=20)
Tool_Name.grid(row=0,column=0)

Trace_Name = tk.Label(frame1, text='Net Name', width=20)
Trace_Name.grid(row=4,column=0)

################# Label Setting #################


################# Entry Setting #################

NetName = tk.Entry(frame1, width=100)
NetName.grid(row=4,column=1)

var = tk.StringVar()
PathName = tk.Entry(frame1,textvariable=var, width=100)
PathName.grid(row=1,column=1)

tpy_var = tk.StringVar()
Tpy_Name = tk.Entry(frame1,textvariable=tpy_var, width=100)
Tpy_Name.grid(row=3,column=1)

################# Entry Setting #################


################# Button Setting #################
Open_html_button = tk.Button(frame1, width=20, text='Open Html',command=select_html_file)
Open_html_button.grid(row=1,column=0,padx=10,pady=1)

Html2Csv = tk.Button(frame1, width=20, text='Convent to Tpy',command=conventer)
Html2Csv.grid(row=2,column=0,padx=10,pady=1)

Open_tpy_button = tk.Button(frame1, width=20, text='Open Tpy',command=select_tpy_file)
Open_tpy_button.grid(row=3,column=0,padx=10,pady=1)


Searching = tk.Button(frame1, width=20, text='Searching',command=searching_location)
Searching.grid(row=6,column=0,padx=10,pady=1)
################# Button Setting #################


################# Location Result #################

################# Label Setting #################

var_Name = tk.StringVar()
ResultName = tk.Label(frame2,textvariable=var_Name, justify = 'left',  width=25)
ResultName.grid(row=0,column=0)

var_Layer = tk.StringVar()
ResultLayer = tk.Label(frame2,textvariable=var_Layer, justify = 'left',  width=10)
ResultLayer.grid(row=0,column=1)

var_Line_width = tk.StringVar()
ResultLine_width = tk.Label(frame2,textvariable=var_Line_width, justify = 'left',  width=10)
ResultLine_width.grid(row=0,column=2)

var_Length = tk.StringVar()
ResultLength = tk.Label(frame2,textvariable=var_Length, justify = 'left',  width=10)
ResultLength.grid(row=0,column=3)

var_Point1_1 = tk.StringVar()
ResultPoint1_1 = tk.Label(frame2,textvariable=var_Point1_1, justify = 'left',  width=10)
ResultPoint1_1.grid(row=0,column=4)

var_Point1_2 = tk.StringVar()
ResultPoint1_2 = tk.Label(frame2,textvariable=var_Point1_2, justify = 'left',  width=10)
ResultPoint1_2.grid(row=0,column=5)

var_Point2_1 = tk.StringVar()
ResultPoint2_1 = tk.Label(frame2,textvariable=var_Point2_1, justify = 'left',  width=10)
ResultPoint2_1.grid(row=0,column=6)

var_Point2_2 = tk.StringVar()
ResultPoint2_2 = tk.Label(frame2,textvariable=var_Point2_2, justify = 'left',  width=10)
ResultPoint2_2.grid(row=0,column=7)

################# Location Result #################

Mwin.mainloop()













