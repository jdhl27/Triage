# -*- coding: utf-8 -*-

#ver http://www.tutorialspoint.com/python/python_files_io.htm

"""
    'r' es el modo de lectura. Curso se ubica al inicio del archivo
    'w' es un modo de escritura. En caso de existir un archivo, éste es sobreescrito. Cursor al comienzo del archivo
    'a' es un modo de escritura. En caso de existir un archivo, comienza a escribir al final de éste.
    'x' es un modo de escritura para crear un nuevo archivo. En caso de que el archivo exista se emitirá un error de tipo FileExistsError.
    '+' es un modo de escritura/lectura.
"""

def main():
    pass

if __name__ == '__main__':
    main()

import os
class Archivo:
    f="" #Se declara la variable tipo archivo
    rutaYNombre=""
    mensaje="ok"
    def __init__(self,rutaYNombre):
        self.rutaYNombre =rutaYNombre


    def abrirArchivo(self):

        try:
            if os.path.exists(self.rutaYNombre):
                self.f = open(self.rutaYNombre,'a+')#abre archivo para lectura escritura
            else:
                self.f = open(self.rutaYNombre,'a+')#crea archivo para lectura escritura

        except IOError as objIOError:
            self.mensaje= "Problemas con el archivo: Error #" + str(objIOError.errno) + " Mensaje : "+format(objIOError.strerror)
        return self.mensaje


    def abrirArchivoLectura(self):

        try:
            if os.path.exists(self.rutaYNombre):
                self.f = open(self.rutaYNombre,'r+')#abre archivo para lectura escritura
            else:
                self.f = open(self.rutaYNombre,'r+')#crea archivo para lectura escritura

        except IOError as objIOError:
            self.mensaje= "Problemas con el archivo: Error #" + str(objIOError.errno) + " Mensaje : "+format(objIOError.strerror)
        return self.mensaje

    def cerrarArchivo(self):
        self.mensaje="ok"
        try:
            self.f.close()
        except IOError as objIOError:
            self.mensaje= "Problemas con el archivo: Error #" + str(objIOError.errno) + " Mensaje : "+format(objIOError.strerror)
        return self.mensaje

    def contarNumLineasArchivo(self):
        self.mensaje="ok"
        n=0
        try:
            for LineaTexto in self.f:
                n=n+1
        except IOError as objIOError:
            self.mensaje= "Problemas con el archivo: Error #" + str(objIOError.errno) + " Mensaje : "+format(objIOError.strerror)
            return self.mensaje

        return n

    def leerUnaLinea(self):
        self.mensaje="ok"
        try:
            lineaTexto = self.f.readline()
            if lineaTexto[-1] == '\n':
                lineaTexto=lineaTexto[:-1] ##elimina el \n  #Coje la última posición
        except IOError as objIOError:
            self.mensaje= "Problemas con el archivo: Error #" + str(objIOError.errno) + " Mensaje : "+format(objIOError.strerror)
            return self.mensaje
        return lineaTexto


    def escribirUnaLineaDebajo(self,lineaTexto):
        self.mensaje="ok"
        try:
             self.f.writelines(lineaTexto+"\n")
        except IOError as objIOError:
            self.mensaje= "Problemas con el archivo: Error #" + str(objIOError.errno) + " Mensaje : "+format(objIOError.strerror)
        return self.mensaje

    def escribirUnaLineaAlFrente(self,lineaTexto):
        self.mensaje="ok"
        print(lineaTexto)
        try:
             self.f.writelines(lineaTexto)
        except IOError as objIOError:
            self.mensaje= "Problemas con el archivo: Error #" + str(objIOError.errno) + " Mensaje : "+format(objIOError.strerror)
        return self.mensaje
