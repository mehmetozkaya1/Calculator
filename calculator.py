from tkinter import *
import math

arayuz = Tk()

arayuz.title("Calculator")

icon = PhotoImage(file='icon-cal.png')
arayuz.iconphoto(False,icon)

canvas = Canvas(arayuz,height=665,width=380)
canvas.pack()

ust_frame = Frame(arayuz,bg="#b4dde0")
ust_frame.place(relx=0.05,rely=0.03,relwidth=0.9,relheight=0.15)

alt_frame = Frame(arayuz,bg="#b4dde0")
alt_frame.place(relx=0.05,rely=0.20,relwidth=0.9,relheight=0.77)

sonuc = ""

def yazdir(sayi): # Sayıları ve işlemleri yazdıran fonksiyon

    global sonuc # Genel sonuc değişkenimizi alıyoruz.
    sonuc = sonuc + str(sayi) # Genel sonuc değişkenimize basılan sayıları string olarak ekliyoruz.
    esitlik.set(sonuc) # esitlik değerimize sonuc değerini atıyoruz.

def esittir(): # Sonucu hesaplatan fonksiyon

    try:
 
        global sonuc # genel sonuc değişkenini alıyoruz.
        toplam = str(eval(sonuc)) # toplam değerine string sonuc içerisinden gelen değeri eval() ile hesaplatıp atıyoruz.
        esitlik.set(toplam) # esitlik ifademize toplam değerini yerleştiriyoruz.

    except:
 
        esitlik.set(" ERROR ") # Herhangi bir hatada esitlik alanına ERROR yazdırıyoruz.
        sonuc = "" # Ve tekrardan sonuc değişkenini boş hale getiriyoruz.
 
def temizle(): # Tüm içeriği temizleyen metot

    global sonuc # Genel sonuc değişkenimizi alıyoruz.
    sonuc = "" # Genel sonuc değişkenimizi 0'a eşitliyoruz. 
    esitlik.set("") # Esitlik değerimize boş değer atıyoruz.

def karekok_al():

    global sonuc

    karekok = math.sqrt(int(sonuc))
    esitlik.set(karekok)

    sonuc = ""

def logaritma_al():
    
    global sonuc

    logaritma = math.log10(int(sonuc))
    esitlik.set(logaritma)

    sonuc = ""
 

esitlik = StringVar() # Bir esitlik değeri oluşturuyoruz.
sonuc_alani = Entry(ust_frame, textvariable=esitlik,font=("Verdana",20,"bold")) # Yazdırma işlemini yapacağımız alanı oluşturuyoruz.
sonuc_alani.pack(ipadx=90,ipady=31,side=TOP) # Yerleştiriyoruz.

# Buttons

button1 = Button(alt_frame,bg="#aa86b0",text="1",height=2,width=3,font=("Verdana",20,"bold"),command=lambda: yazdir(1)) 
button1.place(x=20,y=110)

button2 = Button(alt_frame,bg="#aa86b0",text="2",height=2,width=3,font=("Verdana",20,"bold"),command=lambda: yazdir(2)) 
button2.place(x=100,y=110)

button3 = Button(alt_frame,bg="#aa86b0",text="3",height=2,width=3,font=("Verdana",20,"bold"),command=lambda: yazdir(3)) 
button3.place(x=180,y=110)

button4 = Button(alt_frame,bg="#aa86b0",text="4",height=2,width=3,font=("Verdana",20,"bold"),command=lambda: yazdir(4)) 
button4.place(x=20,y=210)

button5 = Button(alt_frame,bg="#aa86b0",text="5",height=2,width=3,font=("Verdana",20,"bold"),command=lambda: yazdir(5)) 
button5.place(x=100,y=210)

button6 = Button(alt_frame,bg="#aa86b0",text="6",height=2,width=3,font=("Verdana",20,"bold"),command=lambda: yazdir(6)) 
button6.place(x=180,y=210)

button7 = Button(alt_frame,bg="#aa86b0",text="7",height=2,width=3,font=("Verdana",20,"bold"),command=lambda: yazdir(7)) 
button7.place(x=20,y=310)

button8 = Button(alt_frame,bg="#aa86b0",text="8",height=2,width=3,font=("Verdana",20,"bold"),command=lambda: yazdir(8)) 
button8.place(x=100,y=310)

button9 = Button(alt_frame,bg="#aa86b0",text="9",height=2,width=3,font=("Verdana",20,"bold"),command=lambda: yazdir(9)) 
button9.place(x=180,y=310)

button0= Button(alt_frame,bg="#aa86b0",text="0",height=2,width=3,font=("Verdana",20,"bold"),command=lambda: yazdir(0)) 
button0.place(x=100,y=410)

button_topla= Button(alt_frame,bg="#886d8c",text="+",height=2,width=3,font=("Verdana",20,"bold"),command=lambda: yazdir("+")) 
button_topla.place(x=260,y=110)

button_cikar= Button(alt_frame,bg="#886d8c",text="-",height=2,width=3,font=("Verdana",20,"bold"),command=lambda: yazdir("-")) 
button_cikar.place(x=260,y=210)

button_carp= Button(alt_frame,bg="#886d8c",text="*",height=2,width=3,font=("Verdana",20,"bold"),command=lambda: yazdir("*")) 
button_carp.place(x=260,y=310)

button_nokta= Button(alt_frame,bg="#886d8c",text=".",height=2,width=3,font=("Verdana",20,"bold"),command=lambda: yazdir(".")) 
button_nokta.place(x=20,y=410)

button_esittir= Button(alt_frame,bg="#886d8c",text="=",height=2,width=7,font=("Verdana",20,"bold"),command=esittir) 
button_esittir.place(x=180,y=410)

button_bolme = Button(alt_frame,bg="#886d8c",text="÷",height=2,width=3,font=("Verdana",20,"bold"),command=lambda: yazdir("/")) 
button_bolme.place(x=260,y=10)

button_temizleme = Button(alt_frame,bg="#886d8c",text="C",height=2,width=3,font=("Verdana",20,"bold"),command=temizle) 
button_temizleme.place(x=20,y=10)

button_karekok= Button(alt_frame,bg="#886d8c",text="√¯",height=2,width=3,font=("Verdana",20,"bold"),command=karekok_al) 
button_karekok.place(x=100,y=10)

button_logaritma= Button(alt_frame,bg="#886d8c",text="log",height=2,width=3,font=("Verdana",20,"bold"),command=logaritma_al) 
button_logaritma.place(x=180,y=10)


arayuz.mainloop()