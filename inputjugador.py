from convertidor import saveBOX,savePLAYER,saveSTORAGE,saveWALL

def cargajugador(nombre):
    level = int(nombre[-1:])
    with open(nombre+'.txt','r') as entrada:
        lineas = entrada.readlines()
        
    for linea in lineas:
        linea = linea.rstrip()
        print(linea)
            
    #muros = '*'
    #cajas = 'C'
    #player = 'J'
    #objetivo = 'O'
    
    cajas = []
    muros = []
    objetivo = []
    for y in range(len(lineas)):
        for x in range(len(lineas[y])):
            if y< 14 and x< 34: #LIMITES DE LA PANTALLA
                if lineas[y][x] in ['#','*']:
                    muro = saveWALL(y*3,x*5)
                    muros.append(muro)
                elif lineas[y][x] in ['$','C','c']:
                    caja = saveBOX(y*3,x*5)
                    cajas.append(caja)
                elif lineas[y][x] in ['@','J','j']:
                    jugador = savePLAYER(y*3,x*5,'Player',0.0,0,level)
                elif lineas[y][x] in ['.','O','o']:
                    almacen = saveSTORAGE(y*3,x*5,withbox = False)
                    objetivo.append(almacen)
                
    return muros,cajas,objetivo,jugador
