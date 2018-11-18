from clases import *

'''Debido a que no se puede guardar los datos de clases con tipos de datos distintos a los del python, se tienen que 
convertir si se quieren guardar en un archivo, este archivo sirve para tal proposito, solo se emplearan tipos de datos
simples para python, el resto se deja en el de defecto'''

class saveBOX: #clase simplificada para guardar en archivo
    def __init__(self,y,x): #contiene los mismos parametros que su homologa compleja pero sin funciones
        self.ycoord = y 
        self.xcoord = x

class saveWALL: #clase simplificada para guardar
    def __init__(self,y,x):
        self.ycoord = y 
        self.xcoord = x
        
class savePLAYER: #clase simplificada
    def __init__(self,y,x,name,score,pazos,level):
        self.ycoord = y 
        self.xcoord = x 
        self.name = name
        self.score = score
        self.pazos = pazos
        self.level = level
        
class saveSTORAGE: #clase simplificada
    def __init__(self,y,x,withbox):
        self.ycoord = y 
        self.xcoord = x
        self.withbox = withbox


def convertSAVEBOX(box): #convierte la caja de unicurses a una caja simple
    savebox = saveBOX(box.ycoord,box.xcoord)
    return savebox

def convertSAVEWALL(wall): #convierte el muro de unicurses a un muro normal
    savewall = saveWALL(wall.ycoord,wall.xcoord)
    return savewall

def convertSAVEPLAYER(player): #convierte al jugador de unicurses a un jugador simple
    saveplayer = savePLAYER(player.ycoord,player.xcoord,player.name,player.score,player.pazos,player.level)
    return saveplayer

def convertSAVESTORAGE(storage): 
    savestorage = saveSTORAGE(storage.ycoord,storage.xcoord,storage.withbox)
    return savestorage

'''-------------------------------------------------------------------'''

def convertPLAYBOX(savebox):
    normalbox = box(savebox.ycoord,savebox.xcoord)
    return normalbox

def convertPLAYWALL(savewall):
    normalwall = wall(savewall.ycoord,savewall.xcoord)
    return normalwall

def convertPLAYPLAYER(saveplayer):
    normalplayer = player(saveplayer.ycoord,saveplayer.xcoord,saveplayer.name,saveplayer.score)
    normalplayer.level = saveplayer.level
    return normalplayer

def convertPLAYSTORAGE(savestorage):
    normalstorage = storage(savestorage.ycoord,savestorage.xcoord,savestorage.withbox)
    return normalstorage

#la siguiente funcion convertira todo el juego a un formato para salvarlo 

def convertALLSAVE(muros,cajas,almacenes,jugador):
    SAVEmuros = []
    SAVEcajas = []
    SAVEalmacenes = []
    for muro in muros:
        SAVEmuros.append(convertSAVEWALL(muro))
    for caja in cajas:
        SAVEcajas.append(convertSAVEBOX(caja))
    for almacen in almacenes:
        SAVEalmacenes.append(convertSAVESTORAGE(almacen))
    SAVEjugador = convertSAVEPLAYER(jugador)
    return (SAVEmuros,SAVEcajas,SAVEalmacenes,SAVEjugador) #convierte todo a un formato salvable

#la siguiente funcion convierte todo el juego salvado a un formato jugable

def convertALLPLAY(muros,cajas,almacenes,jugador):
    PLAYmuros = []
    PLAYcajas = []
    PLAYalmacenes = []
    for muro in muros:
        PLAYmuros.append(convertPLAYWALL(muro))
    for caja in cajas:
        PLAYcajas.append(convertPLAYBOX(caja))
    for almacen in almacenes:
        PLAYalmacenes.append(convertPLAYSTORAGE(almacen))
    PLAYjugador = convertPLAYPLAYER(jugador)
    PLAYjugador.pazos = jugador.pazos
    return (PLAYmuros,PLAYcajas,PLAYalmacenes,PLAYjugador) #convierte todo a un formato jugable
