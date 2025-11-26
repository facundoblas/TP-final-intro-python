import json, sys, os, random
array_tkts = []

#def main():
def main():
    while True:
        os.system('cls')
        print ('''\n \n══════ Sistema de tickets ══════\n''')
        print ('Por favor, seleccione de las siguientes opciones: \n \n 1: Generar un nuevo ticket. \n 2: Leer un ticket. \n 3: Salir del sistema. \n')
        rta = input('Ingrese su número: ').lower().strip()
        
        #mensaje de error
        while True:
            if rta in ('1', '2', '3'):
                break
        
            print('Por favor, ingrese un número válido.')
            rta = input('\nIngrese su número: ').strip()
        
        #Alta ticket
        if rta == '1':
            alta_tkt()
        
        #Leer ticket
        if rta == '2':
            buscar_tkt()
        
        #Salir del programa
        if rta == '3':
            salir = salir_programa()
            if salir == 's':
                sys.exit()
                

#Opcion 1: Genera el ticket y lo guarda
def alta_tkt():
    os.system('cls')
    print('\nPerfecto, por favor ingrese:')
    nombre = input('Nombre: ')
    sector = input('Sector: ')
    asunto = input('Asunto: ')
    problema = input('Problema: ')
    num_ticket = random.randrange(1000, 9999)
    
    os.system('cls')
    print('''\n \n╔══════════════════════════════════╗
 Se ha generado el siguiente ticket 
╚══════════════════════════════════╝''')
    
    print (f'''Su nombre: {nombre.capitalize()}
N° de ticket: {num_ticket}
Sector: {sector}
Asunto: {asunto}\n
Mensaje: {problema}''')
    print ('\n* POR FAVOR NO OLVIDE SU N° DE TICKET *')

    #Guarda el ticket en el archivo json
    ticket = {
        'nombre' : nombre,
        'sector' : sector,
        'asunto' : asunto,
        'num_ticket' : num_ticket,
        'mensaje' : problema, 
        }
    
    array_tkts.append(ticket)
    guardar_tkt()
    
    #Ejecuta la pregunta de generar otro ticket
    rta_otro_tkt = generar_otro_tkt()
    if rta_otro_tkt == 's':
        alta_tkt()
    else:
        main()

#Función que guarda el ticket
def guardar_tkt():
    with open('tickets.json', 'w', encoding='utf-8') as f:
        json.dump(array_tkts, f, indent=4)

#Pregunta si genera otro ticket o vuelve al menu
def generar_otro_tkt():
    while True:
        rta_otro_tkt = input('\n¿Desea generar otro ticket? (s/n)?: ').lower().strip()
        if rta_otro_tkt in ('s', 'n'):
            return rta_otro_tkt

        print('Por favor, seleccione una de las dos opciones.')

#Opcion 2: leer el ticket
def buscar_tkt():
    tkt_num = leer_tkt()
    encontrado = False
    
    if os.path.isfile('tickets.json'):
        with open('tickets.json', 'r') as f:
            array_tkts = json.load(f)
            
        for ticket in array_tkts:
            if ticket["num_ticket"] == tkt_num:
                print(f'''\n═══ Se encontró el siguiente ticket ═══
Nombre: {ticket['nombre']}
Sector: {ticket['sector']}
Asunto: {ticket['asunto']}
Mensaje: {ticket['mensaje']}\n''')
                encontrado = True
                break
    
    if not encontrado:
        print ('\nNo se encontró ningun ticket que coincida con ese número.\n')
        
    leer_otro_tkt = leer_otros_tkt()   

#Funcion que pide el n° de ticket a leer
def leer_tkt():
    os.system('cls')
    tkt_a_leer = input ('\nPerfecto, por favor ingrese el número del ticket que quiere leer: ').strip()
    
    #Mensaje de error
    while True:
        if tkt_a_leer.isdigit() and len(tkt_a_leer) == 4:
            break
        
        print('Por favor, ingrese un número de ticket válido.')
        tkt_a_leer = input('\nIngrese el número: ').strip()
    tkt_num = int(tkt_a_leer)
    
    return tkt_num

#Pregunta si leer otro ticket
def leer_otros_tkt():
    while True:
        leer_otro_tkt = input ('¿Desea buscar otro ticket? (s/n): ').lower().strip()
        if leer_otro_tkt in ('s', 'n'):
            if leer_otro_tkt == 's':
                buscar_tkt()
            else:
                main()
        else:
            print('Por favor, seleccione una de las dos opciones.')


#Opcion 3: salir del programa
def salir_programa():
    os.system('cls')
    while True:
        salir_sist = input ('\n¿Está seguro que desea salir del programa? (s/n): ').lower().strip()
        if salir_sist in ('s', 'n'):
            return salir_sist
        else:
            print('Por favor, seleccione una de las dos opciones.')

main()
