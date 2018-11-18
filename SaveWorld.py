import pickle


'''EL PRESENTE PROGRAMA SOLO GRABA DATOS EN ARCHIVOS, PERO NO PUEDE GRABAR DATOS QUE
NO SEAN DE USO NORMAL EN PYTHON, POR LO QUE SE REQUIERE CONVERTIR LAS CLASES CON FUNCIONES
DE NCURSES A UNAS CLASES MAS SIMPLES Y PARA ESO SE USARA EL PROGRAMA CONVERTIDOR.PY'''


def salvajuego(muros,cajas,almacenes,jugador):
    #dump es una funcion de la libreria pickle, que permite guardar un objeto o lista de objetos o cualquier tipo de dato, 
    #en este caso se guardaran los datos principales de las clases del juego
    
    with open('Salvado.skb','wb') as output:
        pickle.dump(muros, output, 4)
        pickle.dump(cajas, output, 4)
        pickle.dump(almacenes, output, 4)
        pickle.dump(jugador, output, 4)

    output.close()

def cargajuego():
    #load es una funcion que carga un objeto o lista, en este caso se carga una lista
    with open('Salvado.skb','rb') as output:
        muros = pickle.load(output)
        cajas = pickle.load(output)
        almacenes = pickle.load(output)
        jugador = pickle.load(output)
    output.close()
    
    return muros,cajas,almacenes,jugador
    
def loadscores(jugador):
    #aqui solo se guardan puntajes, aun sin ordenar
    with open('HighScores.txt','a+') as output:
        output.write('NIVEL ' + str(jugador.level) + '  ' + str(jugador.name) + '   %.3f'%jugador.score + '   ' + str(jugador.pazos)+'\n')
        

