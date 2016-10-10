#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler
import sys
import json
import urllib

class Karaokelocal(SmallSMILHandler):

    def __init__(self, fichero):
        parser = make_parser()
        self.cHandler = SmallSMILHandler()
        parser.setContentHandler(self.cHandler)
        parser.parse(open(fichero)) 

    def __str__(self):
        atributo = ""
        for linea in self.cHandler.get_tags():
            if isinstance(linea, dict):
                for valor_att in linea:
                    atributo = atributo + valor_att + "=" + linea[valor_att] + "\t"
                print(etiqueta + "\t" + atributo)

            else:
                etiqueta =  linea
        return(atributo) 

    def to_json(self, fichero):

        if new_fichero == "":
            nuevo_fichero = fich[:fich.find('.')]
        else:
            nuevofichero = new_fich
            fich_json = open(nuevoficherof + '.json', 'w')
            json.dump(self.cHandler.get_tags(), fich_json, sort_keys=True, indent=4, separators=(',', ':'))
            fich_json.close()

    def do_local(self):
        for linea in self.cHandler.get_tags():
            if isinstance(linea, dict):
                if 'src' in linea:
                    if linea['scr'] == 'http':
                        local = linea['src'].split('/')[-1]
                        urllib.request.urlretrieve(linea['scr'], local)
                           

    
    

if __name__ == "__main__":
    try:
        fichero = sys.argv[1]
    except IndexError:
        sys.exit("Usage: python3 karaoke.py file.smil")

    try:
        karaoke = Karaokelocal(fichero)
    except FileNotFoundError:
        sys.exit("Error: File not found")

    print(karaoke)
    karaoke.to_json(fichero)
    karaoke.do_local()
    karaoke.to_json(fichero, 'local')
    print(karaoke)
    
   
   
