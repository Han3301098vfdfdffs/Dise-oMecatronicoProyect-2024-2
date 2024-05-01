from os import *; system('clear') #Limpiar en la terminal
from tkinter import * #Bibliotecas para crear interfaces gráficas

from socket import *#Biblioteca de sockets
address = ('192.168.2.41', 5000)#Se establece la dirección IP y el puerto
s = socket(AF_INET, SOCK_DGRAM)#Objeto que usa el protocolo UPv4 y tipo de socket
s.settimeout(1)#Se establece tiempo de espera de 1 segundo

def TxArduino():#Función que envia mensaje a Arduino y recibe respuesta
    outMsg.delete('1.0', END)
    msgWR = inMsg.get()
    s.sendto(bytes(msgWR, 'utf-8'), address)
    try:
        msgRD, addr = s.recvfrom(2048)
        outMsg.insert(END, msgRD)
    except:
        outMsg.insert(END, 'TRANSMISSION ERROR')

def clrDisp(): #Función que limpia los datos de entrada y salida de la interfaz
    inMsg.delete('0', END)
    outMsg.delete('1.0', END)

win = Tk(); #Se crea una ventana de interfaz gráfica
win.title('Arduino-Python Ethernet Comm');#Se da el titulo a la interfaz gráfica
win.minsize(350, 160)#Se establece el tamaño minimo de la interfaz 

label = Label(text='Mensaje a transmitir a Arduino', font='calibri')#Se crea un label con el texto
label.pack()

inMsg = Entry(width=25, font='calibri 12 bold', fg='red')#Se crea entrada para que el usuario ingrese datos
inMsg.pack()

btn = Button(text=' Transmit ', font='calibri 12 bold', bg='#FF6666', command=TxArduino)
btn.pack()

label = Label(text='Received message from Arduino', font='calibri')
label.pack()

outMsg = Text(width=25, height=1, font='calibri 12 bold', fg='blue')
outMsg.pack()

clrBtn = Button(text=' Clear ', bg='#ADD8E6', command=clrDisp)
clrBtn.pack()
win.mainloop()