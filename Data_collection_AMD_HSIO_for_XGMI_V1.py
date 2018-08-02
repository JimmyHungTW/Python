
# split_value function start
def split_value(string):
    B=str(string)
    C = B[2:-4]
    D = C.split()
    return D
# split_value function end

import time
import os
import tkinter.filedialog as tkfile
original_path=os.getcwd()

runtime1= (time.strftime("%Y%m%d")+' '+ time.strftime("%I_%M_%S"))
runtime=str(runtime1)


os.chdir(tkfile.askdirectory())
import glob
files = glob.glob('.\*\*\*\PKG*XGMI*.txt') + glob.glob('.\*\*\PKG*XGMI*.txt') + glob.glob('.\*\PKG*XGMI*.txt') + glob.glob('.\PKG*XGMI*.txt')

writing_counter = 0
for file in files:
    Data_R=open(file,'r')
    Raw_data = Data_R.readlines()
    Eye_center_width=(Raw_data[1:2])
    Eye_center_height=(Raw_data[2:3])
    Eye_opening_area=(Raw_data[3:4])
    Eye_max_width=(Raw_data[4:5])
    Eye_max_height=(Raw_data[5:6])
    Pass_fail_criteria= (Raw_data[6:7])
    Eye_center_width = split_value(Eye_center_width)
    Eye_center_height = split_value(Eye_center_height)
    Eye_opening_area = split_value(Eye_opening_area)
    Eye_max_width = split_value(Eye_max_width)
    Eye_max_height = split_value(Eye_max_height)
    Pass_fail_criteria = split_value(Pass_fail_criteria)
    B_Eye_center_width_1= (Eye_center_width[3])
    B_Eye_center_width_2= (Eye_center_width[5])
    B_Eye_center_height = (Eye_center_height[3])
    B_Eye_opening_area = (Eye_opening_area[3])
    B_Eye_max_width_1 = (Eye_max_width[3])
    B_Eye_max_width_2 = (Eye_max_width[5])
    B_Eye_max_height = (Eye_max_height[3])
    B_Pass_fail_criteria = (Pass_fail_criteria[2])

    Write_result = open(original_path + '.\AMD_XGMI_Margin_Result_' + runtime + '.csv', 'a+')
    if writing_counter==0:
        Write_result.write('File name'+ ',' +'Eye center width (units)'+ ',' +'Eye center width (UI)'+ ',' +'Eye center heigh (units)'+ ',' +'Eye opening are (units'+ ',' +'Eye max width (units)'+ ',' +'Eye max width (UI)'+ ',' +'Eye max height (units)'+ ',' +'Criteria')
        Write_result.write('\n')
        writing_counter = writing_counter + 1
    else: pass
    Write_result.write( file+ ',' + B_Eye_center_width_1 + ',' + B_Eye_center_width_2 + ',' + B_Eye_center_height + ',' + B_Eye_opening_area + ',' + B_Eye_max_width_1 + ',' + B_Eye_max_width_2 + ',' + B_Eye_max_height + ',' + (B_Pass_fail_criteria))
    Write_result.write('\n')
