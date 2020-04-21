#-------------------------------------------------------------------------------
# Author:      Juan David Hdez
#
# Proyecto:    Vista Triage
# Created:     26/10/2019
# Copyright:   (c) Juan 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from tkinter.tix import *

from triage import *

##-----------------------------GRAFICA------------------------------------------

objTriage = Triage()
gravedad = 0

def gravedad1():
    global gravedad
    gravedad = 1
    btnGravedad1.config(text="X")
    btnGravedad2.config(text="")
    btnGravedad3.config(text="")
    btnGravedad4.config(text="")
    btnGravedad5.config(text="")
    btnGravedad6.config(text="")

def gravedad2():
    global gravedad
    gravedad = 2
    btnGravedad1.config(text="")
    btnGravedad2.config(text="X")
    btnGravedad3.config(text="")
    btnGravedad4.config(text="")
    btnGravedad5.config(text="")
    btnGravedad6.config(text="")

def gravedad3():
    global gravedad
    gravedad = 3
    btnGravedad1.config(text="")
    btnGravedad2.config(text="")
    btnGravedad3.config(text="X")
    btnGravedad4.config(text="")
    btnGravedad5.config(text="")
    btnGravedad6.config(text="")

def gravedad4():
    global gravedad
    gravedad = 4
    btnGravedad1.config(text="")
    btnGravedad2.config(text="")
    btnGravedad3.config(text="")
    btnGravedad4.config(text="X")
    btnGravedad5.config(text="")
    btnGravedad6.config(text="")

def gravedad5():
    global gravedad
    gravedad = 5
    btnGravedad1.config(text="")
    btnGravedad2.config(text="")
    btnGravedad3.config(text="")
    btnGravedad4.config(text="")
    btnGravedad5.config(text="X")
    btnGravedad6.config(text="")

def gravedad6():
    global gravedad
    gravedad = 6
    btnGravedad1.config(text="")
    btnGravedad2.config(text="")
    btnGravedad3.config(text="")
    btnGravedad4.config(text="")
    btnGravedad5.config(text="")
    btnGravedad6.config(text="X")

def registarPaciente():
    cedula = txtCedula.get()
    nombre = txtNombre.get()
    global gravedad

    sw = objTriage.cedulaRepetida(cedula)

    if cedula != "" and nombre != "" and gravedad != 0:
        if (cedula.isnumeric()):
            if sw == False:
                txtCedula.config(bg="#0b2239")
                txtNombre.config(bg="#0b2239")
                btnGravedad1.config(text="")
                btnGravedad2.config(text="")
                btnGravedad3.config(text="")
                btnGravedad4.config(text="")
                btnGravedad5.config(text="")
                btnGravedad6.config(text="")
                lblImageError.config(image="")

                fecha = datetime.now()
                meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
                mes = meses[fecha.month - 1]
                fechaEntrada = str(fecha.day) + " de " + str(mes) + " del " + str(fecha.year)
                horaEntrada = str(fecha.hour) + ":" + str(fecha.minute) + ":" + str(fecha.second)

                objTriage.agregarPaciente(cedula,nombre,gravedad,fechaEntrada,horaEntrada)
                txtCedula.delete(0, 'end')
                txtNombre.delete(0, 'end')

                gravedad = 0

                txtCedula.focus()
                lblMensaje.config(text="Paciente regitrado" , bg="Green", fg="White")
                lblMensaje.place(x=160, y=260)

                arr = objTriage.listar()
                item.config(state=NORMAL)
                item.delete(1.0, 'end')
                for i in range(len(arr)):
                    item.insert(INSERT, "          " + str(arr[i][0]) + "	                     " + str(
                        arr[i][1]) + "                          " + str(arr[i][2]) + "\n")
                    item.insert(INSERT, "______________________________________________________")
                item.config(state=DISABLED)

                lblImageNotificacion.config(image=imageRegistro)
                lblImageNotificacion.place(x=160, y=300)

                lblDatosPacientes.config(state=NORMAL)
                btnAtender.config(state=NORMAL, cursor='hand2')
                lblCedulaPacientes.config(state=NORMAL)
                lblNombrePacientes.config(state=NORMAL)
                lblGravedadPacientes.config(state=NORMAL)

                lblImageQuirofano.config(image="")
            else:
                lblMensaje.config(text="Cédula ya registrada", bg="Red", fg="White")
                lblMensaje.place(x=145, y=260)

                txtCedula.config(bg="#f35040")
                txtCedula.focus()

                txtNombre.config(bg="#0b2239")

                lblImageNotificacion.config(image=imageLlenarCampos)
                lblImageNotificacion.place(x=160, y=300)

                lblImageQuirofano.config(image="")
        else:
            lblMensaje.config(text="Cédula Incorrecta", bg="Red", fg="White")
            lblMensaje.place(x=165, y=260)

            lblImageError.config(image=imageError)
            lblImageError.place(x=320, y=70)
            txtCedula.focus()

            txtNombre.config(bg="#0b2239")

            lblImageNotificacion.config(image=imageLlenarCampos)
            lblImageNotificacion.place(x=160, y=300)

            lblImageQuirofano.config(image="")


    else:
        lblMensaje.config(text="Llene todos los campos", bg="Red", fg="White")
        lblMensaje.place(x=145, y=260)

        lblImageNotificacion.config(image=imageLlenarCampos)
        lblImageNotificacion.place(x=160, y=300)

        lblImageQuirofano.config(image="")

        if cedula == "":
            txtCedula.config(bg="#f35040")
            txtNombre.config(bg="#0b2239")
            lblImageError.config(image="")
            txtCedula.focus()
        elif nombre == "":
            txtCedula.config(bg="#0b2239")
            txtNombre.config(bg="#f35040")
            lblImageError.config(image="")
            txtNombre.focus()
        elif gravedad == 0:
            txtCedula.config(bg="#0b2239")
            txtNombre.config(bg="#0b2239")
            lblImageError.config(image=imageError)
            lblImageError.place(x=370, y=145)



def atenderPaciente():
    cantidad = objTriage.contadorPacientes()
    if cantidad != 0:
        objTriage.atenderPaciente()
        lblMensaje.config(text="Paciente Atendido", bg="Green", fg="White")
        lblMensaje.place(x=160, y=260)

        arr = objTriage.listar()
        item.config(state=NORMAL)
        item.delete(1.0, 'end')
        for i in range(len(arr)):
            item.insert(INSERT, "          " + str(arr[i][0]) + "	                     " + str(
                arr[i][1]) + "                          " + str(arr[i][2]) + "\n")
            item.insert(INSERT, "______________________________________________________")
        item.config(state=DISABLED)

        lblImageNotificacion.config(image=imageAtender)
        lblImageNotificacion.place(x=200, y=300)

        lblImageQuirofano.config(image=imageQuirofano)
    else:
        lblMensaje.config(text="No hay pacientes", bg="Red", fg="White")
        lblMensaje.place(x=160, y=260)

        lblImageNotificacion.config(image=imageNoPacientes)
        lblImageNotificacion.place(x=160, y=300)

        lblImageQuirofano.config(image="")

        btnAtender.config(state=DISABLED, cursor='')
        lblDatosPacientes.config(state=DISABLED)
        lblNombrePacientes.config(state=DISABLED)
        lblCedulaPacientes.config(state=DISABLED)
        lblGravedadPacientes.config(state=DISABLED)


window = Tk()
window.tk.call('wm', 'resizable', window._w, False, False)
window.title("  Hospital")
window.iconbitmap('cruzar.ico')
window.configure(background="#d5efe3")
window.geometry('730x490+350+80') ##(ancho x altura + EjeX + EjeY)



imageRegistro = PhotoImage(file=("pacienteRegistro.png"))
imageAtender = PhotoImage(file=("pacienteAtendido.png"))
imageNoPacientes = PhotoImage(file=("historial.png"))
imageInforme = PhotoImage(file=("informe.png"))
imageLlenarCampos = PhotoImage(file=("llenar.png"))
imageQuirofano = PhotoImage(file=("quirofano.png"))
imageError = PhotoImage(file=("error.png"))

lblImageNotificacion = Label(window, bg="#d5efe3", image=imageInforme)
lblImageNotificacion.place(x=160, y=300)

lblImageQuirofano = Label(window, bg="#d5efe3", image=None)
lblImageQuirofano.place(x=70, y=300)

lblImageError = Label(window, bg="#d5efe3", image=None)

lblTitulo = Label(window, text="HOSPITAL", font=("Bahnschrift SemiBold Condensed", 40),  fg="#3257a8",bg="#d5efe3")
lblTitulo.grid(row=0, column=1)

## CEDULA(lbl, txt)
lblCedula = Label(window, text=" CÉDULA:     " ,font=("Bahnschrift Light Condensed", 18), fg="black", bg="#d5efe3")
lblCedula.grid(row=1, column=0)

txtCedula = Entry(window,width=25, bg="#0b2239",borderwidth = 2, fg="white",font=("Bahnschrift Light Condensed", 13))
txtCedula.grid(row=1, column=1)
txtCedula.focus()

## NOMBRE(lbl, txt)
lblNombre = Label(window, text=" NOMBRE:     ", font=("Bahnschrift Light Condensed", 18), fg="black", bg="#d5efe3", anchor="center")
lblNombre.grid(row=2, column=0)

txtNombre = Entry(window,width=25,bg="#0b2239",borderwidth = 2,fg="white", font=("Bahnschrift Light Condensed", 13))
txtNombre.grid(row=2, column=1)

## GRAVEDAD(lbl, txt)
lblGravedad = Label(window, text="    GRAVEDAD:     ", font=("Bahnschrift Light Condensed", 18), fg="black", bg="#d5efe3", anchor="center")
lblGravedad.grid(row=3, column=0)

btnGravedad1 = Button(window, text="", width=4, border=2, bg="red", fg="black", font=("Bahnschrift SemiBold Condensed", 12), relief=GROOVE, cursor="hand2", command=gravedad1)
btnGravedad1.place(x=135 , y=150 )
btnGravedad2 = Button(window, text="", width=4, border=2, bg="orange", fg="black", font=("Bahnschrift SemiBold Condensed", 12), relief=GROOVE, cursor="hand2", command=gravedad2)
btnGravedad2.place(x=175 , y=150 )
btnGravedad3 = Button(window, text="", width=4, border=2, bg="yellow", fg="black", font=("Bahnschrift SemiBold Condensed", 12), relief=GROOVE, cursor="hand2", command=gravedad3)
btnGravedad3.place(x=215 , y=150 )
btnGravedad4 = Button(window, text="", width=4, border=2, bg="green", fg="black", font=("Bahnschrift SemiBold Condensed", 12), relief=GROOVE, cursor="hand2", command=gravedad4)
btnGravedad4.place(x=255 , y=150 )
btnGravedad5 = Button(window, text="", width=4, border=2, bg="blue", fg="black", font=("Bahnschrift SemiBold Condensed", 12), relief=GROOVE, cursor="hand2", command=gravedad5)
btnGravedad5.place(x=295 , y=150 )
btnGravedad6 = Button(window, text="", width=4, border=2, bg="white", fg="black", font=("Bahnschrift SemiBold Condensed", 12), relief=GROOVE, cursor="hand2", command=gravedad6)
btnGravedad6.place(x=335 , y=150 )

## ESPACIO
lblEspacio = Label(window, text="", bg="#d5efe3")
lblEspacio.grid(row=4, column=0)

## ESPACIO
lblEspacio = Label(window, text="", bg="#d5efe3")
lblEspacio.grid(row=5, column=0)

## BOTON REGISTRAR
btnRegistrar = Button(window, text="Registrar", activebackground="green", font=("Bahnschrift Light Condensed", 12), bg="#8dfa6a", fg="white", cursor="hand2", relief=GROOVE, command=registarPaciente)
btnRegistrar.grid(row=6, column=1)


## MENSAJES(lbl, txt)
lblMensaje = Label(window, text="", font=("Bahnschrift Light Condensed", 14), fg="#ff9349",bg="#d5efe3")

## TITULO PACIENTES
lblDatosPacientes = Label(window, text="PACIENTES", font=("Bahnschrift SemiBold Condensed", 18),fg="#3257a8",bg="#d5efe3")
lblDatosPacientes.place(x=505, y=20)

## BOTON ATENDER
btnAtender = Button(window, text="Atender", bg="#3257a8", activebackground="#f93535", fg="white", relief=GROOVE, state=DISABLED,command=atenderPaciente)
btnAtender.place(x=605, y=25)

## TITULO CEDULA PACIENTES
lblCedulaPacientes= Label(window, text="CÉDULA", font=("Bahnschrift Light Condensed", 15),fg="black",bg="#d5efe3")
lblCedulaPacientes.place(x=430, y=55)

## TITULO NOMBRE PACIENTES
lblNombrePacientes = Label(window, text="NOMBRE", font=("Bahnschrift Light Condensed", 15),fg="black",bg="#d5efe3")
lblNombrePacientes.place(x=520, y=55)

## TITULO GRAVEDAD DATOS
lblGravedadPacientes= Label(window, text="GRAVEDAD", font=("Bahnschrift Light Condensed", 15),fg="black",bg="#d5efe3")
lblGravedadPacientes.place(x=610, y=55)


item = Text(window, width=40, height=15, border=5, bg="#0b2239", font=("Bahnschrift Light Condensed", 13), fg="white", cursor='', state=DISABLED)
item.place(x=410, y=90)

scrollBarText = Scrollbar(window, orient="vertical", command= item.yview)
scrollBarText.place(x=690, y=90, height=330)

item.configure(yscroll=scrollBarText.set)





## MOSTRAR LA VENTANA

window.mainloop()