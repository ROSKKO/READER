import json
import sys
import threading as th
import time as t
import webbrowser as web
import os
import datetime as da
import traceback as tra
import configparser as config

# LIBREBIAS PROPIAS
import helper as hel


# READER V2


class reader():

    switch = False
   

    def abrir_ini(archivo="CODS.ini", inpu:str=None):
        conf = config.ConfigParser()
        conf.read(archivo)


    def verifi(x):
        if "http" in x:
            return True
        elif "www" in x:
            return True
        else:
            return False

    def abrir() -> dict:
        try:
            file = open("CODS.txt", mode="r")
            content = file.read()
            js = json.loads(content)
            return js
        except json.decoder.JSONDecodeError:
            print("\n"+" --------- [ Algo salio mal ] --------- [ Asegurese de que este todo correcto en el archivo CODS.txt ]" )
            exit()
    
    def burbuja(pal:str=None):
        posi=[]
        len_pal = len(pal)
        posi.append(pal.upper())
        posi.append(pal.lower())
        for i in range(len_pal):
            mod_pal=""
            if i == 0:
                mod_pal = pal[i].upper() + pal[i+1:]
            if i > 0:
                mod_pal = pal[:i] + pal[i].upper() + pal[i+1:]
            posi.append(mod_pal)
        return posi
    
    def coinc_burbuja(l:list, d:dict):
        #print(l)
        keeps = d.keys()
        keeps = list(keeps)
        cont_keeps = 0
        cont = 0
        #print(keeps)
        l_len = len(l)
        keeps_len = len(keeps)
        try:
            for i in range(keeps_len):
                buscar_pal = keeps[cont_keeps]
                for r in range(l_len):
                    #print(l[cont], ">>", buscar_pal)
                    if l[cont] == buscar_pal:
                        resultado = l[cont]
                        return resultado
                    else:
                        cont = cont + 1
                cont_keeps = cont_keeps +1
        except (IndexError):
            # print(" No se ha encontrado coincidencia ")
            return 0
        
       
            # veo cual es la palabra que se busca en el diccionario
            
    def devolucion(x:list):
        try:
            js = reader.abrir()
            posi=reader.burbuja(x[0])
            coincidencia = reader.coinc_burbuja(posi, js)
        except IndexError:
            return False

        if coincidencia in js:
            print(js[coincidencia])
            reader.switch = True
            return True
        else:
            # print(" No se encontro la key")
            return False
            
    def agregar(x, js):
        if "add" in x:
            reader.switch = True
            hel.add(js, 'CODS.txt')
    
    def borrar(x, js):
        if "borrar" in x:
            reader.switch = True
            hel.borrar_iter(*x, file="CODS.txt", dicc=js)

    def reemplazar(x:list, js):
        try:
            if "reemplazar" == x[0]:
                hel.reem(js)
                reader.switch = True
                return
        except IndexError:
            return
        
    def lista(x:list, dicc:dict):
        try:
            if "lista" == x[0]:
                for key in dicc.keys():
                    print(key)
                reader.switch = True
                return
        except IndexError:
            return
        
    def comandos(x:list):
        """Muestra los comandos disponibles"""
        try:
            if "comandos" == x[0]:
                print(reader.agregar.__name__, ",", reader.borrar.__name__, ",",
                reader.lista.__name__, ",", reader.reemplazar.__name__)
                reader.switch = True
                return
        except IndexError:
            return

    def fun_reader():
        x = input("ingrese el nombre de la variable: ")
        js = reader.abrir()
        posi = reader.burbuja(x)
        # print(posi)
        t.sleep(1)
        
        if "fin" in posi:
            print(" >> adios")
            t.sleep(1.5)
            exit()
        x3 = x.split()
        lent = len(x3)
        reader.devolucion(x3)
        if reader.devolucion == False:
            return
        reader.agregar(x3, js)
        reader.borrar(x3, js)
        reader.lista(x3, dicc=js)
        reader.comandos(x3)
        print(reader.switch)
        if reader.switch == False:
            print(" No se encontro coincidencia con variable ")
            return
        # reader.nes_dick(x3)
        return
    

    def gestor(x3, agcc):
        if(x3=="agregar"):
            pass
        return

    def init():
        os.system('cls')
        os.system('title READER')
        titulo = """
########  ########    ###    ########  ######## ########
##     ## ##         ## ##   ##     ## ##       ##     ##
##     ## ##        ##   ##  ##     ## ##       ##     ##
########  ######   ##     ## ##     ## ######   ########
##   ##   ##       ######### ##     ## ##       ##   ##
##    ##  ##       ##     ## ##     ## ##       ##    ##
##     ## ######## ##     ## ########  ######## ##     ##
"""
        print(titulo)
        while True:
            reader.fun_reader()
            reader.switch = False
        
        
reader.init()