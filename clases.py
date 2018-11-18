from unicurses import *


'''Principal fuente de clases, contiene los datos de las clases utilizadas para crear el juego,
tiene tambien la iniciacion de los colores, asi como una funcion para comprobar si el juego se gano
y para dibujar todos los objetos'''

os.system("mode 650") #redefine las dimensiones de la consola al maximo tamaño
stdscr = initscr()

noecho() #hace que lo que escribas no se muestre en pantalla
keypad(stdscr, True) #permite lectura de caracteres especiales como las flechas direccionales
curs_set(0) #apaga el parpadeo del cursor en pantalla
start_color() #inicia los colores (8 por defecto)


init_color(COLOR_RED,999,999,100) #para las cajas 3
init_color(COLOR_BLACK,250,250,250) # para el fondo 2
init_color(COLOR_GREEN,50,999,100) # para los muros 7
init_color(COLOR_CYAN,100,900,999) #para el jugador 5
init_color(COLOR_MAGENTA,999,100,100) #para los contenedores 4


init_pair(0,COLOR_WHITE,COLOR_BLACK)
init_pair(1,COLOR_BLUE,COLOR_BLACK) #crea un atributo con color de texto y color del fondo en ese orden
init_pair(2,COLOR_BLACK,COLOR_BLACK)
init_pair(3,COLOR_RED,COLOR_BLACK)
init_pair(4,COLOR_MAGENTA,COLOR_BLACK)
init_pair(5,COLOR_CYAN,COLOR_BLACK)
init_pair(6,COLOR_YELLOW,COLOR_BLACK)
init_pair(7,COLOR_GREEN,COLOR_BLACK)
bkgd(' ',COLOR_PAIR(2)) #cambia el color de fondo

class box:
    def __init__(self,y,x,color = COLOR_PAIR(3)):
        self.ycoord = y #filas
        self.xcoord = x #columnas
        self.color = color #color, por defecto celeste
        
    def draw(self,storages):
        color = self.color #se empieza suponiendo que el color es el mismo de siempre
        
        for storage in storages: #chequea si esta sobre un almacen
            if (self.ycoord,self.xcoord) == (storage.ycoord,storage.xcoord): #si la caja esta sobre un almacen
                color = COLOR_PAIR(4) #cambia el color temporal de la caja a rojo
                break # no pierde tiempo en seguir buscando
        
        stdscr.addstr(self.ycoord,self.xcoord,'\u2554'+'\u2550'*3+'\u2557',color)    #╔═══╗
        stdscr.addstr(self.ycoord + 1,self.xcoord,'\u2551'+' '*3+'\u2551',color)     #║   ║
        stdscr.addstr(self.ycoord + 2,self.xcoord,'\u255A'+'\u2550'*3+'\u255D',color)#╚═══╝

    def erase(self): #se borra a si mismo (preparando el movimiento)
        stdscr.addstr(self.ycoord,self.xcoord,' '*5)
        stdscr.addstr(self.ycoord + 1,self.xcoord,' '*5)
        stdscr.addstr(self.ycoord + 2,self.xcoord,' '*5)
        
    def validmov(self,boxes,walls,direction):
        newy = self.ycoord
        newx = self.xcoord
        
        if direction == 'up':
            newy -= 3 #le resta al y 3 unidades lo que lo mueve hacia arriba
        elif direction == 'down':
            newy += 3 #le suma al y 3 unidades moviendolo abajo
        elif direction == 'left':
            newx -= 5 #le resta al x 5 unidades lo que lo mueve a la izquierda
        elif direction == 'right':
            newx += 5 #le suma al x 5 unidades moviendolo a la derecha
        
        for wall in walls: #chequea colisiones contra los muros
            if (newy,newx) == (wall.ycoord,wall.xcoord):
                return (False,)
               
        for box in boxes: #chequea si hay alguna colision con otras cajas
            if (newy,newx) == (box.ycoord,box.xcoord):
                return (False,)

        return (True,newy,newx)
    
    def move(self,direction,boxes,walls,storages):

        valido = self.validmov(boxes,walls,direction) #tupla de validacion
        
        if valido[0]: #si no es valido entonces no se mueve
            self.erase()
            #boxes.remove(self) nunca hubo necesidad de removerlo
            self.ycoord = valido[1] #al modificar las caracteristicas de la caja,
            self.xcoord = valido[2] #tambien se modifican en la lista que lo contiene
            #boxes.append(self) nunca hubo necesidad de reinsertarlo
            self.draw(storages)
            return True #si se movio
        
        return False #no se movio
            
class wall:
    def __init__(self,y,x,color = COLOR_PAIR(7)):
        self.ycoord = y
        self.xcoord = x
        self.color = color #color por defecto verde claro
        
    def draw(self):
        stdscr.addstr(self.ycoord,self.xcoord,'\u2593'*5,self.color)     #▓▓▓▓▓
        stdscr.addstr(self.ycoord + 1,self.xcoord,'\u2593'*5,self.color) #▓▓▓▓▓
        stdscr.addstr(self.ycoord + 2,self.xcoord,'\u2593'*5,self.color) #▓▓▓▓▓
    
class player:
    def __init__(self, y, x, name = 'Player', time = 0.0, color = COLOR_PAIR(5)):
        self.ycoord = y
        self.xcoord = x
        self.color = color #color por defecto naranja, 
        self.name = name #nombre del jugador, por defecto 'Player'
        self.score = time #tiempo que se usara para medir el score del jugador
        self.pazos = 0
        
        self.level = 0 
        '''AÑADIR EL LEVEL EVITA EL BUG DE SALTAR NIVELES CON CARGAR JUEGO'''

    def draw(self): #se dibuja de la forma adjunta
        stdscr.addstr(self.ycoord,self.xcoord,' '*2+'\u25B2'+' '*2,self.color)             #  ▲
        stdscr.addstr(self.ycoord + 1,self.xcoord,'\u255A'+'\u2588'*3+'\u255D',self.color) #╚███╝
        stdscr.addstr(self.ycoord + 2,self.xcoord,' \u257F'+' '+'\u257F ',self.color)      # ╿ ╿
    
    def erase(self): #se borra a si mismo (preparando el movimiento)
        stdscr.addstr(self.ycoord,self.xcoord,' '*5)
        stdscr.addstr(self.ycoord + 1,self.xcoord,' '*5)
        stdscr.addstr(self.ycoord + 2,self.xcoord,' '*5)
        
    def validmov(self,boxes,walls,direction):
        newy = self.ycoord
        newx = self.xcoord
        
        if direction == 'up':
            newy -= 3 #le resta al y 3 unidades
        elif direction == 'down':
            newy += 3 #le suma al y 3 unidades
        elif direction == 'left':
            newx -= 5 #le resta al x 5 unidades
        elif direction == 'right':
            newx += 5 #le suma al x 5 unidades
            
        #se revisa primero las cajas porque es mas probable que se las empuje, el usuario no es idiota
        #para andar contra la pared siempre
        for box in boxes: #chequea si hay alguna colision con otras cajas
            if (newy,newx) == (box.ycoord,box.xcoord):
                return (0,boxes.index(box),newy,newx) #movimiento valido a casilla con caja
        for wall in walls: #chequea colisiones contra los muros
            if (newy,newx) == (wall.ycoord,wall.xcoord):
                return (-1,) #movimiento no valido
        return (1,newy,newx) #movimiento valido a casilla vacia
    
    def move(self,direction,boxes,walls,storages):

        valido = self.validmov(boxes,walls,direction) #tupla de validacion
        # -1 indica movimiento no valido
        if valido[0]==1: #1 indica movimiento valido a casilla vacia
            self.erase() #se borra para cambiar de ubicacion
            self.ycoord = valido[1] #cambia de coordenadas
            self.xcoord = valido[2] #cambia de coordenadas
            self.draw() #se redibuja
            self.pazos += 1 #AUMENTA EL CONTADOR DE PAZOS
            
        elif valido[0]==0: #0 indica movimiento valido a casilla con caja
            if boxes[valido[1]].move(direction,boxes,walls,storages): #chequea si la caja se puede mover
                self.pazos += 1 #AUMENTA EL CONTADOR DE PAZOS
                self.erase() #lo mismo que en la primera
                self.ycoord = valido[2]
                self.xcoord = valido[3]
                self.draw()

class storage:
    def __init__(self,y,x,withbox=False,color = COLOR_PAIR(4)):
        self.ycoord = y
        self.xcoord = x
        self.color = color #color rojizo por defecto
        self.withbox = withbox #revisa si hay una caja encima

    def draw(self):
        stdscr.addstr(self.ycoord,self.xcoord,' '+ '*'*3+' ',self.color)     # ***
        stdscr.addstr(self.ycoord + 1,self.xcoord,'*'*5,self.color)          #*****
        stdscr.addstr(self.ycoord + 2,self.xcoord,' '+ '*'*3+' ',self.color) # *** 
        
    def update(self,boxes,player): #revisa y actua para cada movimiento (actualiza)
        self.withbox = False #empieza asumiendo que no hay nada encima
        for caja in boxes:
            if (self.ycoord,self.xcoord) == (caja.ycoord,caja.xcoord): #si las coordenadas son iguales
                self.withbox = True                                    #estan superpuestas
                break #no pierde tiempo en revisar las demas cajas
        #si no encuentra una caja con las mismas coordenadas, se mantiene en falso
        if not ((self.ycoord,self.xcoord) == (player.ycoord,player.xcoord) or self.withbox):
            self.draw() #si el jugador no esta sobre el almacen, dibuja el almacen

def WINGAME(storages):
    for almacen in storages: #si todos los almacenes tienen cajas encima se gana
        if not almacen.withbox: #si solo uno no tiene una caja entonces no se gano
            return False #no se gano
    return True #si gano

def drawALL(muros,cajas,almacenes,jugador): #sirve para el dibujo TOTAL, se llama con todas las listas y jugador para dibujarlos
    for muro in muros:
        muro.draw()
    for almacen in almacenes:
        almacen.draw()
    for caja in cajas:
        caja.draw(almacenes)
    jugador.draw()
        
        