'''
Ocala florida
08/21/2021
Ingeniero Roberto La Cruz
Systema de manejo de fotos para 24marine 

'''
#Importar las librerias
from tkinter.ttk import *
from tkinter import *
from os import close
from PIL import ImageTk,Image
from tkinter import filedialog
import cv2
import numpy as np


#variables
grados = 0
dibujando = False
valorx = 0
valory = 0
ruta = ""
imgrezi = ""

#Raiz del programa
raiz = Tk()
raiz.title("24Marine Systema de Analisis de Imagenes")
icon = PhotoImage(file='m24.png')
raiz.tk.call('wm', 'iconphoto', raiz._w, icon)
raiz.geometry("800x500")
def dibujar(event,x,y,etiquetas,parametros):
    global dibujando,valorx,valory,imagen, imgrezi
    if event == cv2.EVENT_LBUTTONDOWN:
        dibujando = True
        valorx = x
        valory = y
    elif event == cv2.EVENT_MOUSEMOVE:
        if dibujando:
            cv2.rectangle(imagen, (valorx,valory),(x,y), (255,0,0),4)
    elif event == cv2.EVENT_LBUTTONUP:
        dibujando = False
        cv2.rectangle(imagen, (valorx,valory),(x,y),(255,0,0), 4)
        original= cv2.imread(ruta)
        originalr= cv2.resize(original,(960,540))
        imgcrop = originalr[valory:y,valorx:x]
        cv2.imwrite('temp2.jpg',imgcrop)
        cv2.namedWindow(winname='Cortada')
        cv2.setMouseCallback('Cortada',salvarat)
        cv2.putText(imgcrop,"!Double Click!",(50,30),1,1,(0,0,255),2,cv2.LINE_AA)
        cv2.putText(imgcrop,"!para Guardar!",(50,70),1,1,(0,0,255),2,cv2.LINE_AA)
        cv2.putText(imgcrop,"!    imagen   ",(50,90),1,1,(0,0,255),2,cv2.LINE_AA)
        cv2.imshow('Cortada',imgcrop)
        
def CorteAutomatico():
    global ruta
    #leer Imagen
    imagena = cv2.imread(ruta) 
    imagena = cv2.resize(imagena,(960,540))
    copia=imagena
    #convertir a escalas de grises
    imagena = cv2.cvtColor(imagena,cv2.COLOR_BGR2GRAY)
    #desenfocar imagen
    imagena = cv2.GaussianBlur(imagena,(5,5),0)
    #detectar bordes
    imagea=cv2.Canny(imagena,50,180)
    #detectar bordes
    imagena = cv2.Canny(imagena,50,180)
    #detectar contornos
    (contornos,jerarquia)=cv2.findContours(imagena,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    #dibujar contornos
    copia= cv2.drawContours(copia,contornos,-1,(255,0,0),2)
    #mostrar imagen
    cv2.imshow('Resultado ' ,copia)
    cv2.waitKey(0)

def CorteManual():
    global dibujando,valorx,valory,ruta,imagen
    img= cv2.imread(ruta)
    imagen= cv2.resize(img,(960,540))
    dibujando = False
    valorx = 0
    valory = 0
    cv2.namedWindow(winname='Original')
    cv2.setMouseCallback('Original',dibujar)
    while True:
        cv2.imshow('Original',imagen)
        if cv2.waitKey(0):
            break
    cv2.destroyAllWindows()

def Saludos():
    print("Estamos Trabajando.....en esta opcion ")
    return None

def Limpiar():
    mi_etiqueta.destroy()
    mi_imagen_etiqueta.destroy()
    
def Salida_salva():
    global mi_imagen
    imagen1=Image.open("temp.jpg")
    archivo_nombre = filedialog.asksaveasfile()
    imagen1.save(archivo_nombre)
    raiz.quit()
    Salida()
    return None

def salvarat(event,x,y,etiquetas,parametros):
        global imgrezi
        if event == cv2.EVENT_LBUTTONDBLCLK:
            archivo_nombre = filedialog.asksaveasfile(filetypes=(("archivos jpg","*.jpg"),("todos los Archivos","*.*")))
            imgcorte = Image.open("temp2.jpg")
            imgcorte.save(archivo_nombre)
            cv2.destroyWindow('Cortada')
        return None


def Salida():
    raiz.quit()
    return None

def Abrir():
    global ruta
    global mi_etiqueta
    global mi_imagen
    global mi_imagen_etiqueta
    raiz.filename = filedialog.askopenfilename(initialdir="/Users/Roberto La Cruz/Desktop/python_files/",title="Selecciona un Archivo",filetypes=(("archivos jpg","*.jpg"),("todos los Archivos","*.*")))
    imagen_cv = cv2.imread(raiz.filename, cv2.IMREAD_COLOR)
    cv2.imwrite("temp.jpg",imagen_cv)
    mi_etiqueta = Label(text=raiz.filename)
    mi_etiqueta.pack()
    imagen1=Image.open("temp.jpg")
    imagen2 = imagen1.resize((500, 376), Image.ANTIALIAS)
    mi_imagen = ImageTk.PhotoImage(imagen2)   
    mi_imagen_etiqueta = Label(image=mi_imagen)
    mi_imagen_etiqueta.pack()      
    ruta=raiz.filename
    return(0)
    
def rotacion90():
    global mi_etiqueta
    global mi_imagen
    global mi_imagen_etiqueta
    Limpiar()
    imagen_cv = cv2.imread("temp.jpg", cv2.IMREAD_COLOR)
    imagen_cv = cv2.rotate(imagen_cv,rotateCode=0)
    cv2.imwrite("temp.jpg",imagen_cv)
    mi_etiqueta = Label(text=raiz.filename)
    mi_etiqueta.pack()
    imagen1=Image.open("temp.jpg")
    imagen2 = imagen1.resize((500, 376), Image.ANTIALIAS)
    mi_imagen = ImageTk.PhotoImage(imagen2)   
    mi_imagen_etiqueta = Label(image=mi_imagen)
    mi_imagen_etiqueta.pack()   
    return(0)

def rotacion180():
    global mi_etiqueta
    global mi_imagen
    global mi_imagen_etiqueta
    Limpiar()
    imagen_cv = cv2.imread("temp.jpg", cv2.IMREAD_COLOR)
    imagen_cv = cv2.rotate(imagen_cv,rotateCode=1)
    cv2.imwrite("temp.jpg",imagen_cv)
    mi_etiqueta = Label(text=raiz.filename)
    mi_etiqueta.pack()
    imagen1=Image.open("temp.jpg")
    imagen2 = imagen1.resize((500, 376), Image.ANTIALIAS)
    mi_imagen = ImageTk.PhotoImage(imagen2)   
    mi_imagen_etiqueta = Label(image=mi_imagen)
    mi_imagen_etiqueta.pack()   
    return(0)


def forget(widget):
    widget.forget()

def Tamano():
    return(0)

def Dividir(x):
    return(0)    

top_menu = Menu(raiz)
raiz.config(menu=top_menu)
#creando los items del menu
Archivo =Menu(top_menu, tearoff=False)
top_menu.add_cascade(menu=Archivo, label="Archivo")
Archivo.add_command(label="Abrir..............",command=Abrir)
Archivo.add_command(label="Cerrar.............",command=Saludos)
Archivo.add_command(label="Guardar............",command=Saludos)
Archivo.add_command(label="Guardar y Salir....",command=Salida_salva)
Archivo.add_command(label="Salir sin Guardar..",command=Salida)

Foto =Menu(top_menu,tearoff=False)
top_menu.add_cascade(menu=Foto, label="Foto")
Foto.add_command(label="Rotar  90 grados .......",command=rotacion90)
Foto.add_command(label="Rotar 180 grados .......",command=rotacion180)
Foto.add_command(label="Limpiar  Pantalla.......",command=Limpiar)   

Corte =Menu(top_menu,tearoff=False)
top_menu.add_cascade(menu=Corte, label="Dividir")
Corte.add_command(label="Corte Manual.",command=CorteManual)
Corte.add_command(label="Corte Automatico.",command=CorteAutomatico)

Corte.add_command(label="Corte 2x2....",command=lambda: Dividir(2))
Corte.add_command(label="Corte 3x3....",command=lambda: Dividir(3))
Corte.add_command(label="Corte 4x4....",command=lambda: Dividir(4))
Corte.add_command(label="Corte 5x5....",command=lambda: Dividir(5))

Objetos =Menu(top_menu,tearoff=False)
top_menu.add_cascade(menu=Objetos, label="Objetos")
Objetos.add_command(label="Buscar en google..........",command=Saludos)
Objetos.add_command(label="Buscar en Python..........",command=Saludos)
Objetos.add_command(label="Ver Reporte'''''''''''''''",command=Saludos)
Objetos.add_command(label="Guardar Reporte en Archivo",command=Saludos)


raiz.mainloop()
