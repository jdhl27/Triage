#-------------------------------------------------------------------------------
# Author:      Juan David Hdez
#
# Proyecto:    frunciones Triage
# Created:     26/10/2019
# Copyright:   (c) Juan 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------


from Archivo import *
from datetime import datetime


class Nodo:
    def __init__(self, cedula, nombre, gravedad, fechaEntrada, horaEntrada, anterior, siguiente):
        self.cedula = cedula
        self.nombre = nombre
        self.gravedad = gravedad
        self.fechaEntrada = fechaEntrada
        self.horaEntrada = horaEntrada
        self.siguiente = siguiente
        self.anterior = anterior

class Triage:

    def __init__(self):
        self.cabeza = None

    def cedulaRepetida(self, cedula):
        actual = self.cabeza
        sw = False
        while actual != None:
            if actual.cedula == cedula:
                sw = True
                break
            actual = actual.siguiente
        return sw

    def contadorPacientes(self):
        actual = self.cabeza
        contador = 0
        while actual is not None:
            actual = actual.siguiente
            contador += 1
        return contador

    def agregarPaciente(self, cedula, nombre, gravedad, fechaEntrada, horaEntrada):
        if self.cabeza == None:
            self.cabeza = Nodo(cedula, nombre,gravedad,fechaEntrada,horaEntrada, None, None)
        else:
            actual = self.cabeza
            anterior = actual
            if gravedad >= actual.gravedad:         ## Valida si el dato ingresado es mayor o igual al dato de la cabeza
                while gravedad >= actual.gravedad:  ## Camina hasta que el dato ingresado no sea mayor o igual a los datos de los nodos
                    anterior = actual
                    actual = actual.siguiente
                    if actual is None:         ## Valida si llegó a la última posición y se sale del ciclo
                        break
                nuevoNodo = Nodo(cedula, nombre,gravedad,fechaEntrada,horaEntrada,anterior,actual)     ## Crea el nodo
                anterior.siguiente = nuevoNodo      ## Al nodo anterior, en (siguiente) le asigna la dirección del nodo nuevo
                if actual is not None:      ## Valida si delante del nodo nuevo hay un nodo
                    actual.anterior = nuevoNodo     ## Al nodo siguiente, en (anterior) le asigna la dirección del nodo nuevo
            else:
                actual = self.cabeza         ## Crea el nodo
                self.cabeza = Nodo(cedula, nombre,gravedad, fechaEntrada, horaEntrada, None, actual)       ## Como el dato es menor que la cabeza actual, crea el nodo y se le asigna a la cabeza
                actual.anterior = self.cabeza       ## Al dato siguiente, osea a la cabeza que había anteriormente se le asigna el nuevo nodo

    def atenderPaciente(self):

        fecha = datetime.now()
        actual = self.cabeza

        objArchivo = Archivo("contadorPacientesAtendidos.txt")
        objArchivo.abrirArchivo()
        objArchivo.escribirUnaLineaDebajo("paciente")
        objArchivo.cerrarArchivo()
        objArchivo.abrirArchivoLectura()
        contador = objArchivo.contarNumLineasArchivo()
        objArchivo.cerrarArchivo()

        objArchivo = Archivo("HistorialPacientes.txt")
        objArchivo.abrirArchivo()
        objArchivo.escribirUnaLineaDebajo("-----------------------------")
        objArchivo.escribirUnaLineaDebajo("            PACIENTE #" + str(contador))
        objArchivo.escribirUnaLineaDebajo("-----------------------------")
        objArchivo.escribirUnaLineaDebajo("Nombre: " + actual.nombre)
        objArchivo.escribirUnaLineaDebajo("Cédula: " + actual.cedula)
        objArchivo.escribirUnaLineaDebajo("Gravedad: " + str(actual.gravedad))
        objArchivo.escribirUnaLineaDebajo("Fecha de entrada: " + str(actual.fechaEntrada))
        objArchivo.escribirUnaLineaDebajo("Hora de entrada: " + str(actual.horaEntrada))
        objArchivo.escribirUnaLineaDebajo("Hora de atención: " + str(fecha.hour) + ":" + str(fecha.minute) + ":" + str(fecha.second))
        objArchivo.cerrarArchivo()

        self.cabeza = actual.siguiente  ## Desenlazando primer dato

    def listar(self):
        mat = []
        n = self.contadorPacientes()
        actual = self.cabeza
        for i in range(n):
            mat.append([])
            mat[i].append(actual.cedula)
            mat[i].append(actual.nombre)
            mat[i].append(actual.gravedad)
            actual = actual.siguiente
        return mat