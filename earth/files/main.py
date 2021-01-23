# 파일암호화 - 파일불러와서 바이트코드 얻은후에 0과 1 뒤바꿔서 파일 못읽게만들기 - 0123 2021
# in file, 'R' in 변수 means Reverse. 
#TODO : 바이너리 숫자도 앞뒤뒤집기랑 01뒤집기하기
#--------------------------------------------------------------------
# function define

import os
def byteToBit(d):
    return ''.join('{:08b}'.format(b) for b in d)
def bitToByte(d):
    return int(d, 2).to_bytes(len(d) // 8, byteorder='big')
    
# Reverse Binary Code (0>1 : 1>0)
def Reverse(a):
    b = a.replace('0','2')
    c = b.replace('1','0')
    d = c.replace('2','1')
    d = int(d)
    return d
#--------------------------------------------------------------------
# open (import) file

import tkinter
from tkinter import filedialog

root = tkinter.Tk()
root.withdraw()
dir_path = filedialog.askopenfile(parent=root,initialdir="/",title='Selece File to Convert')
# print("\ndir_path : ", dir_path)
os.system("cls")
print("file selected : " + dir_path.name)
#--------------------------------------------------------------------
path = dir_path.name # get name of file

Rpath = str(path[::-1]) # Reverse Path String

# Cut into Path and Name
Rfilename = Rpath[0:Rpath.find('/')]
filename = str(Rfilename[::-1])

Rfilepath = Rpath[Rpath.find('/')+1:]
filepath = str(Rfilepath[::-1])
#--------------------------------------------------------------------
# open file

f = open(filepath+"/" + filename, 'rb') # if i just try to open file with "dir_path.name" (= path+name), it goes to error. so i used "path + name"
data = f.read()
intdata = byteToBit(data)
#     Other Method to convert
#     # using join() + ord() + format()
#     inputtext = input("input text, to convert String to binary")
#     binary = ''.join(format(ord(i), 'b') for i in inputtext)
f.close()

nRintdata = Reverse(intdata)
nRintdata = str(nRintdata)
RnRintdata = str(nRintdata[::-1])


def SaveOrNot():
    whether_save = input("\n Do you want to save Binary File into .TXT ? \n if then, type 'y' to save >>> ")
    if str(whether_save) == "y":
        # import tkinter
        # from tkinter import filedialog
        # root = tkinter.Tk()
        # root.withdraw()
        # dir_path = filedialog.askdirectory(parent=root,initialdir="/",title='Please select a Directory where to Save File')
        # savename = input("type file name you want to save binary codes. \n please contain '.txt' >>> ")
        # savename = str(savename)
        # savepath = dir_path + "/" + savename

        print("Saving...")
        f = open('Binarrt.txt', 'wt')
        f.write(RnRintdata)
        f.close()
        print("SAVED !")

SaveOrNot()