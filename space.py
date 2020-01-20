#!/usr/bin/python
# -*- coding: UTF-8 -*-
 

from tkinter import * 
#import tkMessageBox
import dns.resolver
import os
from tkinter import filedialog
from tkinter import messagebox


def mxrecord():
    messagebox.showinfo("提示","正在mx查询中。。。耐心等待。。。结束有提示^-^。。。")
    f=open(fileselect1,'r')
    lines = f.readlines()
    for line in lines:
        #print("1")
        #print(line.strip())
        #mxrecord(line.strip())
        #domain=line.strip()
        try:
            mx=dns.resolver.query(line.strip(),'MX')
            f=open("MX.csv","a")
            for i in mx.response.answer:
                for j in i:
                    record = line.strip() + str(j)
                    #f.write(str(record.split("\n"))+"\n")
                    print(j)
                    f.write(line.strip()+" ")
                    f.write(str(j)+"\n")
        except:
                        f=open("MX.csv","a")
                        f.write(line.strip())
                        f.write("找不到解析\n")
                        f.close()
    f.close()
    messagebox.showinfo("提示","查询结束^-^")

def cnamerecord():
    messagebox.showinfo("提示","正在cname查询中。。。耐心等待。。。结束有提示^-^。。。")
    f=open(fileselect2,'r')
    lines = f.readlines()
    for line in lines:
        #print("1")
        print(line.strip())
        #mxrecord(line.strip())
        #domain=line.strip()
        try:
            cname=dns.resolver.query(line.strip(),'CNAME')
            f=open("CNAME.csv","a")
            for i in cname.response.answer:
                cnamerecord = line.strip() + str(i)
                print(cnamerecord)
                f.write(line.strip()+" ")
                f.write(str(j)+"\n")
                
              #  record = line.strip() + str(j)
                #f.write(str(record.split("\n"))+"\n")
               
        except:
                        f=open("CNAME.csv","a")
                        f.write(line.strip())
                        f.write("找不到解析\n")
                        f.close()
    f.close()
    messagebox.showinfo("提示","查询结束^-^")

    

if __name__ == '__main__':
    def selectFile1():
        global fileselect1
        fileselect1=filedialog.askopenfilename(title="选择txt文件",filetypes=[("txt","*.txt"),("All Files","*")])
        print(fileselect1)
        mmxen.insert(INSERT,fileselect1)
        return fileselect1
    def selectFile2():
        global fileselect2
        fileselect2=filedialog.askopenfilename(title="选择txt文件",filetypes=[("txt","*.txt"),("All Files","*")])
        print(fileselect2)
        mcnen.insert(INSERT,fileselect2)
        return fileselect2
        
        
    review=Tk()
    review.title("批量查询DNS")
    review.geometry("550x200")
    #多个域名的MX
    mmx=Label(review,text="mx查询")
    mmx.pack()
    mmxen=Entry(review,bd=5)
    mmxen.pack()
    mxb=Button(review,text="选择文件路径",command=selectFile1)
    mxb.pack()
    mxb1=Button(review,text="查询",command=mxrecord)
    mxb1.pack()
    mmx.place(x=40,y=30)
    mmxen.place(x=120,y=30)
    mxb.place(x=270,y=30)
    mxb1.place(x=360,y=30)
    #多个域名的CNAME
    mcn=Label(review,text="cname查询")
    mcn.pack()
    mcnen=Entry(review,bd=5)
    mcnen.pack()
    mcb=Button(review,text="选择文件路径",command=selectFile2)
    mcb.pack()
    mxb2=Button(review,text="查询",command=cnamerecord)
    mxb2.pack()
    mcn.place(x=40,y=70)
    mcnen.place(x=120,y=70)
    mcb.place(x=270,y=70)
    mxb2.place(x=360,y=70)

    text1=Label(review,text="1.多域名查询域名需要使用txt文件存放，并且一行一个域名\n")
    text1.pack()
    text2=Label(review,text="2.查询之后在该工具相同目录下会生成一个csv的文件\n")
    text2.pack()
    text3=Label(review,text="3.dns.csv的写入方式为追加，即如果存在同名的文件，会在最后一行追加写入，不会覆盖\n")
    text3.pack()
    text1.place(x=40,y=110)
    text2.place(x=40,y=130)
    text3.place(x=40,y=150)
    review.mainloop()

    

    
