#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler
import sys

def imprimir(lista):
    for linea in lista:
        atributo = ""
        if isinstance(linea, dict):
            for valor_att in linea:
                atributo = atributo + valor_att + "=" + linea[valor_att] + "\t"
            print(etiqueta + "\t" + atributo)

        else:
            etiqueta =  linea        

  

if __name__ == "__main__":
    try:
        File = sys.argv[1]
    except IndexError:
        sys.exit("Usage: python3 karaoke.py file.smil")

    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open(sys.argv[1]))
    #print(cHandler.get_tags())

    imprimir(cHandler.get_tags())
