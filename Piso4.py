import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

def Piso4():
    global miId
    global miName
    global miTelefono
    global miCorreo
    
    global miFrame

    miFrame = Toplevel()
    miFrame.title("Piso4")
    miFrame.config(bg="blue")
    miFrame.geometry("400x550")
    #-------------Etiquetas

    Label(miFrame, text="ID: ", bg="blue").place(x=20, y=20, relx=0.10, rely=0.10)
    Label(miFrame, text="Nombre: ", bg="blue").place(x=20, y=40, relx=0.10, rely=0.20)
    Label(miFrame, text="Telefono: ", bg="blue").place(x=20, y=60, relx=0.10, rely=0.30)
    Label(miFrame, text="Correo: ", bg="blue").place(x=20, y=80, relx=0.10, rely=0.40)

    #------------Cuadros de Texto
    miId = StringVar()
    miName = StringVar()
    miTelefono = StringVar()
    miCorreo = StringVar()

    cId = Entry(miFrame, textvariable=miId)
    cId.insert(0, "Read Only for Create...")
    cId.place(x=120 , y=20, relx=0.10, rely=0.10)
    cName = Entry(miFrame, textvariable=miName)
    cName.place(x=120, y=40, relx=0.10, rely=0.20) 
    cTelefono = Entry(miFrame, textvariable=miTelefono)
    cTelefono.place(x=120, y=60, relx=0.10, rely=0.30)
    cCorreo = Entry(miFrame, textvariable=miCorreo)
    cCorreo.place(x=120, y=80, relx=0.10, rely=0.40)

    #--------------Botones

    bCreate = Button(miFrame, text="Create", command=Create)
    bCreate.place(x=30, y=80, rely=0.60, relx=0.20) 
    bRead = Button(miFrame, text="Read", command=Read)
    bRead.place(x=30, y=100, rely=0.70, relx=.20)
    bUpdate = Button(miFrame, text="Update", command=Update)
    bUpdate.place(x=60, y=80, rely=0.60, relx=0.40)
    bDelete = Button(miFrame, text="Delete", command=Delete)
    bDelete.place(x=60, y=100, rely=0.70, relx=0.40)
    bBorrar = Button(miFrame, text="Borrar Campos", command=Borrar_campos)
    bBorrar.place(x=45, y=90, rely=0.50, relx=0.25 )

    #-----------TreeView

    ListarM()
    lista.reverse()
    
    pantalla = ttk.Treeview(miFrame, height=14, columns = ("NOMBRE", "TELEFONO","CORREO"))
    pantalla.place(x=140, y=20, relx=0.50)
    
    pantalla.heading("#0", text="ID", anchor=N)
    pantalla.column("#0", minwidth=0, stretch=YES, width=30)
    pantalla.heading("#1", text="NOMBRE")
    pantalla.column("#1", minwidth=0, stretch=YES, width=140)
    pantalla.heading("#2", text="TELEFONO")
    pantalla.column("#2", minwidth=0, stretch=YES, width=150)
    pantalla.heading("#3", text="CORREO")
    pantalla.column("#3", minwidth=0, stretch=YES, width=100)
    
    for j in lista:
        pantalla.insert("", 0, text=j[0],
        values = (j[1], j[2], j[3]))

#-----------Base de datos

def Create():
    miConexion = sqlite3.connect("Piso4")
    miCursor = miConexion.cursor()
    miCursor.execute("INSERT INTO PISO4 VALUES(NULL,'" + miName.get()+ 
    "','" + miTelefono.get() +
    "','" + miCorreo.get() + "')")

    miConexion.commit()
    messagebox.showinfo("BBDD", "Registro creado con éxito.")

def Read():
    miConexion = sqlite3.connect("Piso4")
    miCursor = miConexion.cursor()
    miCursor.execute("SELECT * FROM PISO4 WHERE ID=" + miId.get())
    elEmpleado = miCursor.fetchall()

    for empleado in elEmpleado:
        miId.set(empleado[0])
        miName.set(empleado[1])
        miTelefono.set(empleado[2])
        miCorreo.set(empleado[3])

    miConexion.commit()

def Update():
    miConexion = sqlite3.connect("Piso4")
    miCursor = miConexion.cursor()
    miCursor.execute("UPDATE PISO4 SET NOMBRE= '" + miName.get()+ 
    "', TELEFONO='" + miTelefono.get() + 
    "', CORREO='" + miCorreo.get() +
    "'WHERE ID=" + miId.get())

    miConexion.commit()
    messagebox.showinfo("BBDD", "Registro actualizado con éxito.")

def Delete():
    miConexion = sqlite3.connect("Piso4")
    miCursor = miConexion.cursor()
    miCursor.execute("DELETE FROM PISO4 WHERE ID=" + miId.get())

    miConexion.commit()
    messagebox.showinfo("BBDD","Registro borrado satisfactoriamente")

def Borrar_campos():
    miId.set("")
    miName.set("")
    miTelefono.set("")
    miCorreo.set("")

def ListarM():
    global lista
    miConexion = sqlite3.connect("Piso4")
    miCursor = miConexion.cursor()
    miCursor.execute("SELECT * FROM PISO4")
    lista = []
    lista = miCursor.fetchall()
    miConexion.commit()
    miConexion.close()
    return lista