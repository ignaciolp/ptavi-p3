#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler
import sys
import json
import urllib

def imprimir(lista):
    for linea in lista:
        atributo = ""
        if isinstance(linea, dict):
            for valor_att in linea:
                atributo = atributo + valor_att + "=" + linea[valor_att] + "\t"
            print(etiqueta + "\t" + atributo)

        else:
            etiqueta =  linea

def busca_url(lista):
        list_url = []
        #print(lista)
        for linea in lista:
            if isinstance(linea, dict):
                if 'src' in linea:
                    list_url.append(linea['src'])
                    #print(list_url)
        return(list_url)

def archivo_url(lista_url):
    for linea in lista_url:
        archivo = linea.split('/')[-1]
        try:
            urllib.request.urlretrieve(linea, archivo)
        except ValueError:
            sys.exit("Not a URL")
        
    
   

  

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

    #imprimir(cHandler.get_tags())
    fch = open('karaoke.json', 'w')
    json.dump(cHandler.get_tags(), fch, sort_keys=True, indent=4, separators=(',',':'))
    fch.close()
    
    url_lista = busca_url(cHandler.get_tags())
    archivo_url(url_lista)
