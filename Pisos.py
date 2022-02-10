
from tkinter import *
from tkinter import messagebox

from Piso1 import *
from Piso2 import *
from Piso3 import *
from Piso4 import *
from BBDDS import *


def Pisos():
    root = Toplevel()
    root.title("Registro")
    root.resizable(0,0)
    root.config(bg="#6B7787")
    root.geometry("680x470")

    myFrame = Frame(root, width=800, height=500)
    myFrame.pack(fill="none", expand=True)

    myFrame.config(bg="#37404A")

    #*-------------------Label
    Label(myFrame, text="Selecciona la opción que deseas registrar.\nAntes de elegir, asegurese que la BD este establecida.", bg="#6B7787", fg="white", width=65, height=3, font=("Calibri",15)).grid(
        row=2, column=1, padx=0, pady=29, columnspan=5)


    Label(myFrame, text="Piso 1 :", bg="#37404A").grid(row=6, column=1, sticky="e", padx=15, pady=20)
    Label(myFrame, text="Piso 2:", bg="#37404A").grid(row=8, column=1, sticky="e", padx=15, pady=20)
    Label(myFrame, text="Piso 3:", bg="#37404A").grid(row=10, column=1, sticky="e", padx=15, pady=20)
    Label(myFrame, text="Piso 4:", bg="#37404A").grid(row=12, column=1, sticky="e", padx=15, pady=20)

    def logout():
        valor = messagebox.askquestion("Logout","¿Desea cerrar sesion?")
        if valor == "yes":
            root.destroy()

    Piso1B = Button(myFrame, text="Registrar", command=Piso1)
    Piso1B.grid(row=6, column=4, sticky="w", padx=3, pady=5)

    Piso2B = Button(myFrame, text="Registrar", command=Piso2)
    Piso2B .grid(row=8, column=4, sticky="w", padx=3, pady=5)

    Piso3B  = Button(myFrame, text="Registrar", command=Piso3)
    Piso3B .grid(row=10, column=4, sticky="w", padx=3, pady=5)

    Piso4B  = Button(myFrame, text="Registrar", command=Piso4)
    Piso4B .grid(row=12, column=4, sticky="w", padx=3, pady=5)

    LogoutB = Button(myFrame, text="Cerrar Sesion", command=logout, width=10,height=2)
    LogoutB.grid(row=14, column=4, sticky="w", padx=3, pady=15, columnspan=4)

    Piso1BD = Button(myFrame, text="Conectar", command=BBDD_piso1)
    Piso1BD.grid(row=6, column=5, sticky="w", padx=20, pady=5)

    Piso2BD = Button(myFrame, text="Conectar", command=BBDD_piso2)
    Piso2BD.grid(row=8, column=5, sticky="w", padx=20, pady=5)

    Piso3BD = Button(myFrame, text="Conectar", command=BBDD_piso3)
    Piso3BD.grid(row=10, column=5, sticky="w", padx=20, pady=5)

    Piso4BD = Button(myFrame, text="Conectar", command=BBDD_piso4)
    Piso4BD.grid(row=12, column=5, sticky="w", padx=20, pady=5)

    myFrame.mainloop()


if __name__ == "__main__":
    Pisos()