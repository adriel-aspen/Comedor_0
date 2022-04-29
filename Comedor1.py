"""Este programa se usa para borrar archivos en una carpeta y abrir otros"""


import os
import tkinter
from tkinter import ttk
from tkinter import messagebox
import os
import tkinter
from tkinter import ttk
from tkinter import messagebox

ventana = tkinter.Tk()
ventana.geometry("500x400")
ventana.title("Prueba de borrado")

#labes
label_1 = tkinter.Label(ventana, text = "Que semana desea actualizar?")
label_1.place(x = 50, y = 50)

#combobox
combo = ttk.Combobox(ventana,  state = "readonly")
combo["values"] =('01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30',
                  '31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52',)
combo.place(x = 215, y = 52, width = 50, height = 25)
combo = True


def docs ():
    try:
        file = 'old.xlsx'
        file_2 = 'old.txt'
        file_3 = 'new.xlsx'
        file_4 = 'new.txt'
        location = "C:\\Users\\abarragan\\OneDrive - Aspen Surgical Products Inc\\Documents\\ADRIEL\\sistema 06\\Comedor"
        location_2 = "C:\\Users\\abarragan\\OneDrive - Aspen Surgical Products Inc\\Documents\\ADRIEL\\sistema 06\\Comedor"
        location_3 = "C:\\Users\\abarragan\\OneDrive - Aspen Surgical Products Inc\\Documents\\ADRIEL\\sistema 06\\Comedor"
        location_4 = "C:\\Users\\abarragan\\OneDrive - Aspen Surgical Products Inc\\Documents\\ADRIEL\\sistema 06\\Comedor"
        path = os.path.join(location, file)
        path_2 = os.path.join(location_2, file_2)
        path_3 = os.path.join(location_3, file_3)
        path_4 = os.path.join(location_4, file_4)
        os.remove(path)
        os.remove(path_2)
        os.mkdir(path_3)
        os.mkdir(path_4)

        messagebox.showinfo(ventana,"Se borro exitosamente y se actualizaron los datos")
    except:
        messagebox.showerror(ventana,"No se borraron los archivos \n   o no existen")

boton = tkinter.Button(ventana, text = "actualizar", command = docs)
boton.place(x = 100, y = 100)

ventana.mainloop()