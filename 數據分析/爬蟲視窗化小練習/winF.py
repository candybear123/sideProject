from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import tkinter.ttk as tt
root=Tk()
root.title('大樂透數字機率查詢')

#按鈕執行
def Fig1():
    canvas1=Canvas(root, width=1000,height=300,bd=0, highlightthickness=0,bg="gray")
    imgpath1="p1.png"
    img1 = Image.open(imgpath1)
    img1=img1.resize((650,300),Image.ANTIALIAS)
    photo1 = ImageTk.PhotoImage(img1)
    pic1=canvas1.create_image(500,150, image=photo1)
    canvas1.pack()
    btn_close=Button(root,text="關閉圖表",command=canvas1.destroy)
    btn_close.pack()
    canvas1.create_window(window=pic1)
    quit()
def Fig2():
    canvas3=Canvas(root, width=1000,height=300,bd=0, highlightthickness=0,bg="gray")
    imgpath3="s1.png"
    img3= Image.open(imgpath3)
    img3=img3.resize((450,300),Image.ANTIALIAS)
    photo3 = ImageTk.PhotoImage(img3)
    pic3=canvas3.create_image(500,150, image=photo3)
    canvas3.pack()
    btn_close=Button(root,text="關閉圖表",command=canvas3.destroy)
    btn_close.pack()
    canvas1.create_window(window=pic3)
    quit()
def choice():
    if com1.get()=='103':
        Fig3()
    elif com1.get()=='104':
        Fig4()
    elif com1.get()=='105':
        Fig5()
    elif com1.get()=='106':
        Fig6()
    elif com1.get()=='107':
        Fig7()
    elif com1.get()=='108':
        Fig8()
        
def choice1():
    if com.get()=='103':
        Fig9()
    elif com.get()=='104':
        Fig10()
    elif com.get()=='105':
        Fig11()
    elif com.get()=='106':
        Fig12()
    elif com.get()=='107':
        Fig13()
    elif com.get()=='108':
        Fig14()

def choice2():
    num=com2.get()
    canvas4=Canvas(root, width=1000,height=300,bd=0, highlightthickness=0,bg="gray")
    imgpath4="t{}.png".format(num)
    img4= Image.open(imgpath4)
    img4=img4.resize((450,300),Image.ANTIALIAS)
    photo4= ImageTk.PhotoImage(img4)
    pic4=canvas4.create_image(500,150, image=photo4)
    canvas4.pack()
    btn_close=Button(root,text="關閉圖表",command=canvas4.destroy)
    btn_close.pack()
    canvas1.create_window(window=pic4)    
    

def Fig3():
    canvas4=Canvas(root, width=1000,height=300,bd=0, highlightthickness=0,bg="gray")
    imgpath4="p3.png"
    img4= Image.open(imgpath4)
    img4=img4.resize((450,300),Image.ANTIALIAS)
    photo4= ImageTk.PhotoImage(img4)
    pic4=canvas4.create_image(500,150, image=photo4)
    canvas4.pack()
    btn_close=Button(root,text="關閉圖表",command=canvas4.destroy)
    btn_close.pack()
    canvas1.create_window(window=pic4)
    
def Fig4():
    canvas4=Canvas(root, width=1000,height=300,bd=0, highlightthickness=0,bg="gray")
    imgpath4="p4.png"
    img4= Image.open(imgpath4)
    img4=img4.resize((450,300),Image.ANTIALIAS)
    photo4= ImageTk.PhotoImage(img4)
    pic4=canvas4.create_image(500,150, image=photo4)
    canvas4.pack()
    btn_close=Button(root,text="關閉圖表",command=canvas4.destroy)
    btn_close.pack()
    canvas1.create_window(window=pic4)
    
def Fig5():
    canvas4=Canvas(root, width=1000,height=300,bd=0, highlightthickness=0,bg="gray")
    imgpath4="p5.png"
    img4= Image.open(imgpath4)
    img4=img4.resize((450,300),Image.ANTIALIAS)
    photo4= ImageTk.PhotoImage(img4)
    pic4=canvas4.create_image(500,150, image=photo4)
    canvas4.pack()
    btn_close=Button(root,text="關閉圖表",command=canvas4.destroy)
    btn_close.pack()
    canvas1.create_window(window=pic4)
    
def Fig6():
    canvas4=Canvas(root, width=1000,height=300,bd=0, highlightthickness=0,bg="gray")
    imgpath4="p6.png"
    img4= Image.open(imgpath4)
    img4=img4.resize((450,300),Image.ANTIALIAS)
    photo4= ImageTk.PhotoImage(img4)
    pic4=canvas4.create_image(500,150, image=photo4)
    canvas4.pack()
    btn_close=Button(root,text="關閉圖表",command=canvas4.destroy)
    btn_close.pack()
    canvas1.create_window(window=pic4)
    
def Fig7():
    canvas4=Canvas(root, width=1000,height=300,bd=0, highlightthickness=0,bg="gray")
    imgpath4="p7.png"
    img4= Image.open(imgpath4)
    img4=img4.resize((450,300),Image.ANTIALIAS)
    photo4= ImageTk.PhotoImage(img4)
    pic4=canvas4.create_image(500,150, image=photo4)
    canvas4.pack()
    btn_close=Button(root,text="關閉圖表",command=canvas4.destroy)
    btn_close.pack()
    canvas1.create_window(window=pic4)
    
def Fig8():
    canvas4=Canvas(root, width=1000,height=300,bd=0, highlightthickness=0,bg="gray")
    imgpath4="p8.png"
    img4= Image.open(imgpath4)
    img4=img4.resize((450,300),Image.ANTIALIAS)
    photo4= ImageTk.PhotoImage(img4)
    pic4=canvas4.create_image(500,150, image=photo4)
    canvas4.pack()
    btn_close=Button(root,text="關閉圖表",command=canvas4.destroy)
    btn_close.pack()
    canvas1.create_window(window=pic4)
    
def Fig9():
    canvas4=Canvas(root, width=1000,height=300,bd=0, highlightthickness=0,bg="gray")
    imgpath4="s3.png"
    img4= Image.open(imgpath4)
    img4=img4.resize((450,300),Image.ANTIALIAS)
    photo4= ImageTk.PhotoImage(img4)
    pic4=canvas4.create_image(500,150, image=photo4)
    canvas4.pack()
    btn_close=Button(root,text="關閉圖表",command=canvas4.destroy)
    btn_close.pack()
    canvas1.create_window(window=pic4)
    
def Fig10():
    canvas4=Canvas(root, width=1000,height=300,bd=0, highlightthickness=0,bg="gray")
    imgpath4="s4.png"
    img4= Image.open(imgpath4)
    img4=img4.resize((450,300),Image.ANTIALIAS)
    photo4= ImageTk.PhotoImage(img4)
    pic4=canvas4.create_image(500,150, image=photo4)
    canvas4.pack()
    btn_close=Button(root,text="關閉圖表",command=canvas4.destroy)
    btn_close.pack()
    canvas1.create_window(window=pic4)
    
def Fig11():
    canvas4=Canvas(root, width=1000,height=300,bd=0, highlightthickness=0,bg="gray")
    imgpath4="s5.png"
    img4= Image.open(imgpath4)
    img4=img4.resize((450,300),Image.ANTIALIAS)
    photo4= ImageTk.PhotoImage(img4)
    pic4=canvas4.create_image(500,150, image=photo4)
    canvas4.pack()
    btn_close=Button(root,text="關閉圖表",command=canvas4.destroy)
    btn_close.pack()
    canvas1.create_window(window=pic4)
    
def Fig12():
    canvas4=Canvas(root, width=1000,height=300,bd=0, highlightthickness=0,bg="gray")
    imgpath4="s6.png"
    img4= Image.open(imgpath4)
    img4=img4.resize((450,300),Image.ANTIALIAS)
    photo4= ImageTk.PhotoImage(img4)
    pic4=canvas4.create_image(500,150, image=photo4)
    canvas4.pack()
    btn_close=Button(root,text="關閉圖表",command=canvas4.destroy)
    btn_close.pack()
    canvas1.create_window(window=pic4)
    
def Fig13():
    canvas4=Canvas(root, width=1000,height=300,bd=0, highlightthickness=0,bg="gray")
    imgpath4="s7.png"
    img4= Image.open(imgpath4)
    img4=img4.resize((450,300),Image.ANTIALIAS)
    photo4= ImageTk.PhotoImage(img4)
    pic4=canvas4.create_image(500,150, image=photo4)
    canvas4.pack()
    btn_close=Button(root,text="關閉圖表",command=canvas4.destroy)
    btn_close.pack()
    canvas1.create_window(window=pic4)
    
def Fig14():
    canvas4=Canvas(root, width=1000,height=300,bd=0, highlightthickness=0,bg="gray")
    imgpath4="s8.png"
    img4= Image.open(imgpath4)
    img4=img4.resize((450,300),Image.ANTIALIAS)
    photo4= ImageTk.PhotoImage(img4)
    pic4=canvas4.create_image(500,150, image=photo4)
    canvas4.pack()
    btn_close=Button(root,text="關閉圖表",command=canvas4.destroy)
    btn_close.pack()
    canvas1.create_window(window=pic4)
    
#按鈕
Button(root,text="103~108年前6碼比率",width=25,height=2,command=Fig1).pack()
Label(root,text='各年度前 6 碼比率',justify=RIGHT,width=25,height=2).pack()
stdYear1 = ('103','104','105','106','107','108')
com1 = tt.Combobox(root, width=25, values=stdYear1)
com1.pack()
Button(root,text='查詢',command=choice).pack()
Button(root,text="103~108年度特別號比率",width=25,height=2,command=Fig2).pack()
Label(root,text='各年度特別號比率',justify=RIGHT,width=25,height=2).pack()
stdYear = ('103','104','105','106','107','108')
com = tt.Combobox(root, width=25, values=stdYear)
com.pack()
Button(root,text='查詢',command=choice1).pack()
Label(root,text='各號碼出現在前6碼比率',justify=RIGHT,width=25,height=2).pack()
stdNum = ('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16',\
          '17','18','19','20','21','22','23','24','25','26','27','28','29','30',\
          '31','32','33','34')
stdNum1=[]
for i in range(1,50):
    stdNum1.append(str(i))
com2 = tt.Combobox(root, width=25, values=stdNum1)
com2.pack()
Button(root,text='查詢',command=choice2).pack()

root.mainloop()
