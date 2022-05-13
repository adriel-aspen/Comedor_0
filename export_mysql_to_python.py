import tkinter

import pandas as pd
from tkinter import ttk
import mysql.connector

ventana = tkinter.Tk()
ventana.geometry("800x500")
ventana.title("prueba de csv con python")




conn = mysql.connector.connect(
    host= "192.168.2.1",
    database="apson",
    user= "admin",
    password= "Monroy2020",)

def table_to_csv ():
   cursor = conn.cursor(dictionary=True)
   cursor.execute("SELECT 	c.empleado,count(c.empleado)*31.30 AS Cost,t.WEEK FROM apson.registro_comedor c JOIN dev_monche.time_dimension t ON DATE(c.fecha)=t.db_date WHERE t.YEAR=YEAR AND t.WEEK  = 16 GROUP BY c.empleado,t.WEEK ;")
   resultado = cursor.fetchall()
   df = pd.DataFrame (resultado)
   df_csv = df.to_csv("C:\\Users\\abarragan\\PycharmProjects\\sistema 06\\Comedor\\test3.csv")


boton = tkinter.Button(ventana, text = "enter", command = table_to_csv)
boton.place(x = 100, y = 100)


ventana.mainloop()
#"SELECT * FROM registro_comedor"
















