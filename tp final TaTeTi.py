import os

tablero = {
'1': '1', '2': '2', '3': '3',
'4': '4', '5': '5', '6': '6',
'7': '7', '8': '8', '9': '9'
}

#inciciar juego
def main():
    os.system('cls')
    print ('''\n \n══════ Nueva partida ══════
         Ta Te Ti''')
    
    tablero_act()
    
    while True:
        actualizar_tablero1()
        resultado = checkar_resultado()
        if resultado == 'si':
            print ('''\nPartida finalizada\nEl jugador 1 ha ganado.''')
            break
        
        if tablero_lleno():
            print ('Tablero lleno, la partida termina en empate.')
            break
        
        actualizar_tablero2()
        
        resultado = checkar_resultado()
        if resultado == 'si':
            print ('''\nPartida finalizada\nEl jugador 2 ha ganado.''')
            break
        
        if tablero_lleno():
            print ('Tablero lleno, la partida finaliza en empate.')
            break

#jugador 1 elige su posición
def jugador1_pos():
    
    while True:
        elección_p1_ = input('\nJugador 1, escriba su posición: ')
        
        elección_p1 = elección_p1_.strip()
        
        if elección_p1 not in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
            print ('Seleccione una posición válida.')
            continue
        elif tablero[elección_p1] == 'X' or tablero[elección_p1] == 'O':
            print ('Esa posición está ocupada, seleccione otra.')
            continue
        else:
            break
    
    return elección_p1

#jugador 2 elige su posición
def jugador2_pos():
    
    while True:
        elección_p2_ = input('\nJugador 2, escriba su posición: ')
        
        elección_p2 = elección_p2_.strip()
        
        if elección_p2.strip() not in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
            print ('Seleccione una posición válida.')
            continue
        elif tablero[elección_p2] == 'X' or tablero[elección_p2] == 'O':
            print ('Esa posición está ocupada, seleccione otra.')
            continue
        else:
            break
    
    return elección_p2

#Imprime el tablero
def tablero_act():
    
    print (f'''\n        |       |       
    {tablero['1']}   |   {tablero['2']}   |   {tablero['3']}   
        |       |
--------+-------+-------
        |       |
    {tablero['4']}   |   {tablero['5']}   |   {tablero['6']}
        |       |       
--------+-------+-------
        |       |
    {tablero['7']}   |   {tablero['8']}   |   {tablero['9']}
        |       |       
''')
    
def actualizar_tablero1():
    elección_p1 = jugador1_pos()
    os.system('cls')
    tablero[elección_p1] = 'X'
    tablero_act()
    
def actualizar_tablero2():
    elección_p2 = jugador2_pos()
    os.system('cls')
    tablero[elección_p2] = 'O'
    tablero_act()
    
#Evalúa si ganó alguno
def tres_en_linea():
    combinaciones = {
        #Combinaciones horizontales
        ('1','2','3'),
        ('4','5','6'),
        ('7','8','9'),
        
        #Combinaciones verticales
        ('1','4','7'),
        ('2','5','8'),
        ('3','6','9'),
        
        #Combinaciones diagonales
        ('1','5','9'),
        ('3','5','7')
    }
    
    for a, b, c in combinaciones:
        if tablero[a] == tablero[b] == tablero[c]:
            return 'hay_ganador'
        
    return 'no_hay_ganador'
        
def checkar_resultado():
    resultado = tres_en_linea()
    
    while True:
        if resultado == 'hay_ganador':
            return 'si'
        else:
            return 'no'

def tablero_lleno():
    return all(valor in ('X', 'O') for valor in tablero.values())

main()
