from tkinter import messagebox
import sqlite3

def BBDD_piso1():
    miConexion = sqlite3.connect("Piso1")
    
    miCursor = miConexion.cursor()

    try:
        miCursor.execute('''CREATE TABLE PISO1 (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE VARCHAR(50),
            TELEFONO INTEGER(10),
            CORREO VARCHAR(50))''')
        
        messagebox.showinfo("Success", "La base de datos se creo con éxito")

    except:
        messagebox.showwarning("Atencion", "La base de datos ya existe")

def BBDD_piso2():
    miConexion = sqlite3.connect("Piso2")
    
    miCursor = miConexion.cursor()

    try:
        miCursor.execute('''CREATE TABLE PISO2 (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE VARCHAR(50),
            TELEFONO INTEGER(10),
            CORREO VARCHAR(50))''')
        
        messagebox.showinfo("Success", "La base de datos se creo con éxito")

    except:
        messagebox.showwarning("Atencion", "La base de datos ya existe")

def BBDD_piso3():
    miConexion = sqlite3.connect("Piso3")
    
    miCursor = miConexion.cursor()

    try:
        miCursor.execute('''CREATE TABLE PISO3 (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE VARCHAR(50),
            TELEFONO INTEGER(10),
            CORREO VARCHAR(50))''')
        
        messagebox.showinfo("Success", "La base de datos se creo con éxito")

    except:
        messagebox.showwarning("Atencion", "La base de datos ya existe")

def BBDD_piso4():
    miConexion = sqlite3.connect("Piso4")
    
    miCursor = miConexion.cursor()

    try:
        miCursor.execute('''CREATE TABLE PISO4 (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE VARCHAR(50),
            TELEFONO INTEGER(10),
            CORREO VARCHAR(50))''')
        
        messagebox.showinfo("Success", "La base de datos se creo con éxito")

    except:
        messagebox.showwarning("Atencion", "La base de datos ya existe")