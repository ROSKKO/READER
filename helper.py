import json
import sys
import platform as pla
import socket
import http.server
import os
import subprocess as sub
import datetime as da
import traceback as tra
import pyautogui as auto
import time as t
import webbrowser as web

def verifi(x):
    if "http" in x:
        return True
    elif "www" in x:
        return True
    else:
        return False

def argumentos(*argumentos, dicc:dict):
    try:
        if "/o" == argumentos[1]:
            ind = argumentos[0]
            try:
                pag= dicc[ind]
                ver_= verifi(pag)
                if ver_== True:
                    print(" [ ABRIENDO ] ")
                    web.open(pag)
                    return
                else:
                    print("<< Asegurese de que el valor pueda abrirse en el explorador >>")
                    return
            except (KeyError, Exception):
                print(f" < {argumentos[0]} > no se pudo encontrar")
                return
        if "/c" == argumentos[1]:
            ind = argumentos[0]
            try:
                pag = dicc[ind]
                rcop(pag)
                print(" [ COPIADO ] ")
                return
            except Exception:
                print(f" < {argumentos[0]} > no se pudo copiar")
                return
    except (Exception) as e:
        with open("ERRORS.txt", 'a+') as f:
                f.write(__file__)
                tra.print_exception(e, file=f)

    return

    


def fecha():
    fecha = da.datetime.now()
    fecha1 = fecha.strftime('%w') + "-" + fecha.strftime('%d') + "-" + fecha.strftime('%Y') + ' >> ' + fecha.strftime('%X') + '\n'
    return fecha1

def burbuja(pal=None):
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



def chek(valor_a_chekear, dict):
    """ verifica que exista le key en el diccionario que se pasa"""
    try:
        g = dict[valor_a_chekear]
    except Exception as e:
        return False
    else:
        return True

def reemplazar(dicc=None): # EN USO
    """ comando: reem """
    preg = input("Quiere ver el diccionario? [Y/N] ")
    if preg == 'Y' or preg=='y':
        dicc1_0 = json.dumps(dicc, indent=1)
        print(dicc1_0)
    else:
        pass
    x = input("[ KEY / VALUE ] ")
    # [!] Opcion 1 -> si x == key
    if x == "key" or x == "KEY":

        x1 = input("Key actual: ")
        chek_x1 = chek(x1, dicc) # CHEKEA QUE EXISTA LA KEY
        if chek_x1 == False:
            print(" [!] La Key ingresada no existe ")
            return False
        if chek_x1 == True:
            pass
        x2 = input("Por lo que quiere reemplazar: ")
        obt_value = dicc[x1]
        dicc.pop(x1)
        dicc.update({x2:obt_value})
        jsn = json.dumps(dicc, indent=1)

    # [!] Opcion 2 -> si x == value
    if x == "value" or x == "VALUE":
        obt_key = input("Key del value: ")
        chek_x1 = chek(obt_key, dicc) # CHEKEA QUE EXISTA LA KEY
        if chek_x1 == False:
            print(" [!] La Key ingresada no existe ")
            return False
        if chek_x1 == True:
            pass
        obt_value1 = dicc.get(obt_key)
        nuevo = input("Valor nuevo: ")
        dicc.pop(obt_key)

        dicc.update({obt_key:nuevo})

        jsn = json.dumps(dicc, indent=1)

    return jsn


def add(dicc=None, file=None, key=None, value=None, n=1): # EN USO
    """ comando: add """
    if n == 1:
        if key == None:
            key=input("Key >> ")
        if value == None:
            value=input("Value >> ")

        dicc.update({key:value})
        try:
            jsn = json.dumps(dicc, indent=1)
            op0= open(file,'w')
            op0.writelines(jsn)
            op0.close()
            print("[ LISTO ]")
        except Exception as e:
            print(f"ALGO SALIO MAL {Exception}")
            with open("ERRORS.txt", 'a+') as f:
                f.write(__file__)
                tra.print_exception(e, file=f)


def borrar_iter(*args, file, dicc=None): # EN USO
    """Para borrar una determinada cantidad de veces
    comando: borrar <num de cantidad de veces que vas a borrar>"""
    try:
        num_iter = int(args[1]) # numero de iteraciones
    except Exception as e:
        with open('ERRORS.txt', 'a+') as f:
            f.write(fecha())
            tra.print_exception(e, file=f)
        num_iter=1
    for n in range(num_iter): 
        inp = input(" Linea a borrar >> ")
        chek_ = chek(valor_a_chekear=inp, dict=dicc)
        if chek_ == True:
            try:
                with open(file, 'r') as fi:
                    content = fi.read()
                    js = json.loads(content)
                    js.pop(str(inp))
                    jsn=json.dumps(js, indent=1)
                with open(file, 'w') as fi1:
                    fi1.writelines(jsn)
                    fi1.close()
                print("[ LISTO ]")
            except Exception as e:
                with open("ERRORS.txt", 'a+') as f:
                    fe = fecha()
                    f.write(fe)
                    tra.print_exception(e, file=f)
                    print(" [!] No se pudo borrar")
                pass

def busq(ext_file=None): # EN USO
    dirarchs = os.listdir()
    print('\n')
    print(f"> ARCHIVOS DE EXTENSION {ext_file} <")
    for words in dirarchs:
        if words.endswith(ext_file):
            print(words)

def most_arch():
    dirarchs = os.listdir()
    #print(json.dumps(os.listdir(), indent=1))
    print('\n')
    print("> ARCHIVOS PYTHON <")
    for words in dirarchs:
        if words.endswith(".py"):
            print(words)

    print('\n')
    print("> ARCHIVOS DE TEXTO <")
    for word in dirarchs:
        if word.endswith(".txt"):
            print(word)


def rcop(string): # EN USO
    cmd = 'echo ' + string + '|clip'
    return sub.check_call(cmd, shell=True)

def columnas(l=None): # EN USO COMO FUNCION IMPORTANTE
    if len(l)%2 !=0:
        l.append(" ")
    splita = round(len(l)/2)
    l1 = l[0:splita]
    l2 = l[splita:]
    for key,value in zip(l1,l2):
        print( "{}           {}".format(key, value))


def stri_color(string_a_imprimir, color):
    colores = {
    'violeta' : '\033[1;35m',
    'rojo' : '\033[1;31m',
    'verde' : '\033[1;32m',
    'beish' : '\033[1;33m',
    'azul' : '\033[1;34m',
    'celeste' : '\033[1;36m'
    }
    print(colores[color]+string_a_imprimir+'\033[1;m')


def subrayar(string):
    nuevo_string = '\033[1;4m'+string+'\033[1;m'
    return nuevo_string

def nested_dicks(com,*arguments,archivo): # EN IMPLEMENTACION
    if "dict" == arguments[0]:
        with open(archivo, 'r') as archivo:
            archivo_read = archivo.read()
            archivo_load = json.loads(archivo_read)
            if arguments[1] == "todo":
                print(archivo_load[com])
            try:

                print(arguments[1]+" >> es >> "+archivo_load[com][arguments[1]])

            except (IndexError,KeyError) as Error:
                print("[!] El comando dict es <key_de_variable> dict <key_de_segunda_variable> ")
                print(" No se ha encontrado una segunda key llamada >> "+ str(Error)) 
                # La segunda Key es la key que se encuentra dentro de la Key principal 
            try:
                print(arguments[2]+" >> es >> "+archivo_load[com][arguments[2]])
            except (IndexError,KeyError):
                pass




# def exxit():
#     exit()
#
#
# def manj_threads(th1, th_final):
