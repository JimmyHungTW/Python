#The purpose of the py is to collect data for AMD memory-eye

#split_value function explanation:
#import [' 132.6 (Strong Pass)        -132.6 (Strong Pass)\n']
#export 132.6 (Strong Pass)
#export -70.6 (Margin Pass)
def split_value(string):
    global Positive_spec,Negative_spec,Positive_value,Negative_value
    B=str(string)
    C = B[3:-4]
    D = C.split()
    if len(D)==2:
        Positive_spec = 'TBD'
        Negative_spec = 'TBD'
        Positive_value = D[0]
        Negative_value = D[-1]
    elif len(D) == 4:
        Positive_spec = ''.join(D[1])
        Negative_spec = ''.join(D[-1])
        Positive_value = D[0]
        Negative_value = D[-2]
    elif len(D) == 5:
        if D[1]== "(Pass)":
            Positive_spec = ''.join(D[1])
            Negative_spec = ''.join(D[-2]) + ' ' + ''.join(D[-1])
            Positive_value = D[0]
            Negative_value = D[-3]
        elif D[1] == "(Fail)":
            Positive_spec = ''.join(D[1])
            Negative_spec = ''.join(D[-2]) + ' ' + ''.join(D[-1])
            Positive_value = D[0]
            Negative_value = D[-3]
        else:
            Positive_spec = ''.join(D[1]) + ' ' + ''.join(D[2])
            Negative_spec = ''.join(D[-1])
            Positive_value = D[0]
            Negative_value = D[-2]

    elif len(D) == 6:
        Positive_spec = ''.join(D[1]) + ' ' + ''.join(D[2])
        Negative_spec = ''.join(D[-2]) + ' ' + ''.join(D[-1])
        Positive_value = D[0]
        Negative_value = D[-3]
#print(Positive_value, Positive_spec, Negative_value, Negative_spec)
# split_value function end

import time
import os
import tkinter.filedialog as tkfile
original_path=os.getcwd()

runtime1= (time.strftime("%Y%m%d")+' '+ time.strftime("%I_%M_%S"))
runtime=str(runtime1)
DQ_result=open('A_DQ_result_'+runtime+'.csv','w+')
#DQ_result.write("Data Date:"+runtime+'\n')

CPU_result=open('A_CPU_result_'+runtime+'.csv','w+')
#CPU_result.write("Data Date:"+runtime+'\n')

CA_result=open('A_CA_result_'+runtime+'.csv','w+')
#CA_result.write("Data Date:"+runtime+'\n')

os.chdir(tkfile.askdirectory())
import glob
files = glob.glob('.\*\*\*.log') + glob.glob('.\*\*.log') + glob.glob('.\*.log')
for file in files:
    Data_R=open(file,'r')
    Raw_data = Data_R.readlines()
    Data_Category=(Raw_data[-5:-4])
    Data_value=(Raw_data[-1:])
    if Data_Category==['Margining result for DQ\n']:
        Data_Category='DQ_Result'
        Data_value=split_value(Data_value)
        final_data1=(file, Data_Category, Positive_value, Positive_spec , Negative_value, Negative_spec)
        final_data=str(final_data1)
        DQ_result1=open(original_path + '.\A_DQ_result_'+runtime+'.csv','a+')
        DQ_result1.write(final_data)
        DQ_result1.write('\n')
    elif Data_Category==['Margining result for CA\n']:
        Data_Category='CA_Result'
        Data_value=split_value(Data_value)
        final_data1=(file, Data_Category, Positive_value, Positive_spec , Negative_value, Negative_spec)
        final_data=str(final_data1)
        DQ_result1=open(original_path + '.\A_CA_result_'+runtime+'.csv','a+')
        DQ_result1.write(final_data)
        DQ_result1.write('\n')
    else:
        Data_Category = 'CPU_Result'
        Data_value=split_value(Data_value)
        final_data1=(file, Data_Category, Positive_value, Positive_spec , Negative_value, Negative_spec)
        final_data=str(final_data1)
        DQ_result1=open(original_path + '.\A_CPU_result_' + runtime + '.csv','a+')
        DQ_result1.write(final_data)
        DQ_result1.write('\n')






