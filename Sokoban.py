from clases import * 
import SaveWorld
from convertidor import convertALLPLAY
import time
import inputjugador
from random import randint


'''LISTA DE ARCHIVOS PARA VER EN ORDEN:
-CLASES.PY
-CONVERTIDOR.PY
-SAVEWORLD.PY
-LEVEL?.PY'''

def menu(y = 10 , x = 70):
    init_color(COLOR_YELLOW,999,999,0)
    stdscr.clear()
    stdscr.addstr(y,x-10,'-'*20 + 'MENU DEL JUEGO' + '-'*20, color_pair(6))
    stdscr.addstr(y + 5,x,'1. Nueva partida (clasico)', color_pair(6))
    stdscr.addstr(y + 7,x,'2. Cargar partida', color_pair(6))
    stdscr.addstr(y + 9,x,'3. Jugar nivel creado', color_pair(6))
    stdscr.addstr(y + 11,x,'4. Instrucciones de juego', color_pair(6))
    stdscr.addstr(y + 13,x,'5. Instrucciones del creador de mundos', color_pair(6))
    stdscr.addstr(y + 15,x,'6. Creditos', color_pair(6))
    stdscr.addstr(y + 17,x,'Ingrese un numero para continuar: ', color_pair(6))
    curs_set(1)
    entrada = stdscr.getch()
    stdscr.addch(str(chr(entrada)), color_pair(6))
    stdscr.refresh()
    napms(250)
    curs_set(0)
    
    return chr(entrada)

def MAIN(level = 0,reset = False, saved = False, newgame = False): #funcion principal, ejecuta el juego en el nivel seleccionado
    flag = True
    niveles = {1:'Nivel1',2:'Nivel2',3:'Nivel3',4:'Nivel4',5:'Nivel5',0:'Nivel0'}   
     
    movimientos = {KEY_UP:'up',KEY_DOWN:'down',KEY_RIGHT:'right',KEY_LEFT:'left'}
    stdscr.clear()
    

    muros,cajas,almacenes,jugador = inputjugador.cargajugador(niveles[level])
    muros,cajas,almacenes,jugador = convertALLPLAY(muros, cajas, almacenes, jugador)
    
    if newgame:
        SaveWorld.salvajuego(muros, cajas, almacenes, jugador)

    #level = jugador.level
    
    '''if level == 0:
        stdscr.clear() 
        muros,cajas,almacenes,jugador = SaveWorld.cargajuego()
        muros,cajas,almacenes,jugador = convertALLPLAY(muros, cajas, almacenes, jugador)
        level = jugador.level
    elif level == 1:
        muros,cajas,almacenes,jugador = level1()
    elif level == 2:
        muros,cajas,almacenes,jugador = level2()
    elif level == -1:
        muros,cajas,almacenes,jugador = cargajugador()
        muros,cajas,almacenes,jugador = convertALLPLAY(muros, cajas, almacenes, jugador)
        level = jugador.level'''
    
    ahora = time.time()
    
    while flag:
        if reset:
            stdscr.clear()
            muros,cajas,almacenes,jugador = inputjugador.cargajugador(niveles[level])
            muros,cajas,almacenes,jugador = convertALLPLAY(muros, cajas, almacenes, jugador)
            #level = jugador.level
            '''if level == 1:
                muros,cajas,almacenes,jugador = level1()
            elif level == 2:
                muros,cajas,almacenes,jugador = level2()
            elif level ==-1:
                muros,cajas,almacenes,jugador = cargajugador()
                muros,cajas,almacenes,jugador = convertALLPLAY(muros, cajas, almacenes, jugador)'''
                
            #muros,cajas,almacenes,jugador = level
            ahora = time.time()
            reset = False
            
            
        if saved and jugador.level == level:

            ahora = time.time()
            stdscr.clear() 
            muros,cajas,almacenes,jugador = SaveWorld.cargajuego()
            muros,cajas,almacenes,jugador = convertALLPLAY(muros, cajas, almacenes, jugador)
            saved = False
            
        drawALL(muros,cajas,almacenes,jugador)
         
        while not WINGAME(almacenes):
            entrada = stdscr.getch()
        
            if entrada in movimientos:
                jugador.move(movimientos[entrada],cajas,muros,almacenes)
                #stdscr.addstr(str(jugador.level),color_pair(5))
                #stdscr.addstr(str(jugador.pazos), color_pair(5))
    
            for almacen in almacenes:
                almacen.update(cajas,jugador)
                
            if chr(entrada) in ['r','R']:
                stdscr.clear()
                reset = True
                break
            elif chr(entrada) in ['s','S']:
                jugador.score += time.time() - ahora
                #Smuros, Scajas, Salmacenes, Sjugador = convertALLPLAY(muros, cajas, almacenes, jugador)
                SaveWorld.salvajuego(muros, cajas, almacenes, jugador)
            elif chr(entrada) in ['c','C']:   
                saved = True
                break
            
        flag = reset or saved
    
    jugador.score += time.time() - ahora
    SaveWorld.loadscores(jugador)
    stdscr.addstr('GANASTE!!', color_pair(5))
    stdscr.addstr('Presiona una tecla para continuar...',color_pair(3))
    stdscr.refresh()
    stdscr.getch()
    
def creditos(y = 45,ymin = 10,x=90):
    
    for i in range(y-ymin):
        stdscr.clear()
        
        init_color(COLOR_RED,randint(0,999),randint(0,999),randint(0,999))
        stdscr.addstr(y-i,x,'CREADO POR: ',color_pair(3))
        
        init_color(COLOR_GREEN,randint(0,999),randint(0,999),randint(0,999))
        stdscr.addstr(y+2-i,x,'SANDRA CAMACHO PESCORAN 20174108F',color_pair(7))
        
        init_color(COLOR_CYAN,randint(0,999),randint(0,999),randint(0,999))
        stdscr.addstr(y+4-i,x,'MARCO ANTONIO VELA RODRIGUEZ 20174140G',color_pair(5))
        
        init_color(COLOR_MAGENTA,randint(0,999),randint(0,999),randint(0,999))
        stdscr.addstr(y+8-i,x,'UNIVERSIDAD NACIONAL DE INGENIERIA ',color_pair(4))
        
        init_color(COLOR_YELLOW,randint(0,999),randint(0,999),randint(0,999))
        stdscr.addstr(y+10-i,x,'LENGUAJES DE PROGRAMACION ESTRUCTURADO ',color_pair(6))
        
        init_color(COLOR_BLUE,randint(0,999),randint(0,999),randint(0,999))
        stdscr.addstr(y+12-i,x+15,'2018-II ',color_pair(1))
        stdscr.refresh()
        napms((y - ymin)*21 //10)
    
    init_color(COLOR_RED,999,999,999) #para las cajas 3
    init_color(COLOR_BLACK,250,250,250) # para el fondo 2
    init_color(COLOR_GREEN,50,999,100) # para los muros 7
    init_color(COLOR_CYAN,100,900,999) #para el jugador 5
    init_color(COLOR_MAGENTA,999,100,100) #para los contenedores 4
    

    stdscr.addstr(y-i,x,'CREADO POR: ',color_pair(3))

    stdscr.addstr(y+2-i,x,'SANDRA CAMACHO PESCORAN 20174108F',color_pair(3))

    stdscr.addstr(y+4-i,x,'MARCO ANTONIO VELA RODRIGUEZ 20174140G',color_pair(3))

    stdscr.addstr(y+8-i,x,'UNIVERSIDAD NACIONAL DE INGENIERIA ',color_pair(3))
    
    stdscr.addstr(y+10-i,x,'LENGUAJES DE PROGRAMACION ESTRUCTURADO ',color_pair(3))
    
    stdscr.addstr(y+12-i,x+15,'2018-II ',color_pair(3))
    
    stdscr.addstr(y+15-i,x-30,'Presiona una tecla para continuar...',color_pair(3))
    stdscr.refresh()
    stdscr.getch()
    init_color(COLOR_RED,999,999,100)
    init_color(COLOR_YELLOW,999,999,0)

def instrucciones(y,x):
    stdscr.clear()
    stdscr.refresh()
    init_color(COLOR_RED,999,999,999)
    stdscr.addstr(y,x+10,'SOKOBAN:',color_pair(3))
    stdscr.refresh()
    napms(1000)
    
    stdscr.addstr(y+2,x,'El juego consiste en empujar cajas para ubicarlas en ciertos objetivos.',color_pair(3))
    stdscr.refresh()
    napms(2000) 
    
    objprueba = storage(23,x+100,color = color_pair(3))
    stdscr.addstr(y+4,x,'Los objetivos tienen la siguiente forma: ',color_pair(3))
    objprueba.draw()
    stdscr.refresh()
    napms(3500)
    
    cajaprueba = box(20,x+100)
    stdscr.addstr(y+6,x,'Las cajas tienen la siguiente forma: ',color_pair(3))
    cajaprueba.draw([objprueba])
    stdscr.refresh()
    napms(3500)
    
    muroprueba = wall(20,x+105,color = color_pair(3))
    stdscr.addstr(y+8,x,'Los muros tienen la siguiente forma: ',color_pair(3))
    muroprueba.draw()
    stdscr.refresh()
    napms(3500)
    
    personajeprueba = player(17,x+100,color = color_pair(3))
    stdscr.addstr(y+10,x,'El personaje tiene la siguiente forma: ',color_pair(3))
    personajeprueba.draw()
    stdscr.refresh()
    napms(3500)
    
    stdscr.addstr(y+12,x,'El personaje se mueve con las flechas direccionales',color_pair(3))
    stdscr.refresh()
    napms(1500)
    stdscr.addstr(y+13,x,'Derecha ',color_pair(3))
    personajeprueba.move('right',[cajaprueba],[muroprueba],[objprueba])
    stdscr.refresh()
    napms(1500)
    stdscr.addstr(y+14,x,'Izquierda ',color_pair(3))
    personajeprueba.move('left',[cajaprueba],[muroprueba],[objprueba])
    stdscr.refresh()
    napms(1500)
    stdscr.addstr(y+15,x,'Abajo ',color_pair(3))
    personajeprueba.move('down',[cajaprueba],[muroprueba],[objprueba])
    stdscr.refresh()
    napms(1500)
    stdscr.addstr(y+16,x,'Arriba ',color_pair(3))
    personajeprueba.move('up',[cajaprueba],[muroprueba],[objprueba])
    stdscr.refresh()
    napms(2000)
    stdscr.addstr(y+18,x,'Puedes reiniciar el nivel que juegues presionando la tecla "R" ',color_pair(3))
    stdscr.refresh()
    napms(2000)
    stdscr.addstr(y+19,x,'Con la tecla "S" salvas el juego en su estado actual, y con la tecla "C" lo cargas',color_pair(3))
    stdscr.refresh()
    napms(2000)
    stdscr.addstr(y+20,x,'desde la ultima vez que lo salvaste o desde el comienzo de un nuevo nivel',color_pair(3))
    stdscr.refresh()
    napms(2000)
    stdscr.addstr(y+21,x,'Presiona una tecla para continuar...',color_pair(3))
    stdscr.refresh()
    stdscr.getch()
    init_color(COLOR_RED,999,999,100)

def instrCreador(y,x):
    stdscr.clear()
    stdscr.refresh()
    init_color(COLOR_RED,999,999,999)
    stdscr.addstr(y,x+10,'BIENVENIDO AL CREADOR DE NIVELES',color_pair(3))
    stdscr.refresh()
    napms(1000)
    stdscr.addstr(y+2,x,'Los archivos de niveles estan creados por defecto con 5 niveles numerados del 1 al 5, el programa',color_pair(3))
    stdscr.refresh()
    napms(3000)
    stdscr.addstr(y+3,x,'NO reconocera otros archivos, puedes modificar los niveles clasicos o crear un nivel extra para una partida corta,',color_pair(3))
    stdscr.refresh()
    napms(3000)
    stdscr.addstr(y+4,x,'los niveles clasicos tienen por nombre Nivel 1,2,3,4,5 mientras que el nivel extra tiene por nombre Nivel0',color_pair(3))
    stdscr.refresh()
    napms(3000)
    stdscr.addstr(y+5,x,'La notacion es la siguiente',color_pair(3))
    stdscr.refresh()
    napms(1000)
    stdscr.addstr(y+6,x,'Jugador : "@" o "J" o "j" ',color_pair(3))
    stdscr.refresh()
    napms(3000)
    stdscr.addstr(y+7,x,'Caja    : "$" o "C" o "c" ',color_pair(3))
    stdscr.refresh()
    napms(3000)
    stdscr.addstr(y+8,x,'Muro    : "#" o "*" ',color_pair(3))
    stdscr.refresh()
    napms(3000)
    stdscr.addstr(y+9,x,'Objetivo: "." u "O" u "o"',color_pair(3))
    stdscr.refresh()
    napms(1000)
    stdscr.addstr(y+11,x,'Cuentas con 14 columnas y 34 filas para crear un nivel (SUJETO A TAMAÑO DE PANTALLA)',color_pair(3))
    stdscr.refresh()
    napms(3000)
    stdscr.addstr(y+12,x,'Presiona una tecla para continuar...',color_pair(3))
    stdscr.refresh()
    stdscr.getch()
    
    init_color(COLOR_RED,999,999,100)
    
def mainloop():
    maxy,maxx = stdscr.getmaxyx()
    entrada = menu(y = int(maxy/3), x=int(maxx/2.5))
    if entrada == '1':
        for i in range(1,6):
            MAIN(i,newgame = True)
        creditos(maxy-15,10,int(maxx/2.5))
    elif entrada == '2':
        muros,cajas,almacenes,jugador = SaveWorld.cargajuego()
        lvl = jugador.level
        MAIN(lvl, saved = True)
        if lvl != 0:
            
            for i in range(lvl+1,6):
                MAIN(i,newgame = True)
            
        creditos(maxy-15,10,int(maxx/2.5))
    elif entrada == '3':
        MAIN(newgame = True)
        creditos(maxy-15,10,int(maxx/2.5))
        mainloop()
    elif entrada == '4':
        instrucciones(maxy//5,maxx//4)
        mainloop()
    elif entrada == '5':
        instrCreador(maxy//5,maxx//4)
        mainloop()
    elif entrada == '6':
        creditos(maxy-15,10,int(maxx/2.5))
        mainloop()

        
mainloop()
init_color(COLOR_RED,999,999,999)
stdscr.addstr(35,40, 'FIN DEL PROGRAMA! ESPERAMOS QUE LO HAYAS DISFRUTADO :)',color_pair(3))
stdscr.refresh()
napms(750)
stdscr.addstr(37,40, 'PRESIONA UNA TECLA PARA FINALIZAR EL PROGRAMA',color_pair(3))
stdscr.refresh()
stdscr.getch()


