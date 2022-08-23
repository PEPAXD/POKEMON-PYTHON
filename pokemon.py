#HACER UN PROGRAMA SIMPLE QUE SIMULE UN COMBATE POKEMON ENTRE UN PIKACHU Y UN SQUIRTLE USANDO WHILE

#LIBRERIAS
import os
from random import randint

#VARIABLES
text = "░░░░░░░░░▀████▀▄▄░░░░░░░░░░░░░░▄█░                                       "
turno_number = 0
pokemon_1_vida = 0
pokemon_2_vida = 0

#COLOR
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

#STATS PIKACHU LVL50 IA
pikachu_number_25 = "PIKACHU"
pikachu_vida = 126
pikachu_speed =	63

pikachu_attack_1 = "ONDA VOLTIO"
pikachu_attack_2 = "IMPACTRUENO"
pikachu_attack_3 = "ATAQUE RAPIDO"
pikachu_attack_4 = "COLA FERREA"

pikachu_onda_voltio = 42
pikachu_impactrueno = 47
pikachu_ataque_rapido = 21
pikachu_cola_ferrea = 8

pikachu_names_attacks_array = [pikachu_attack_1, pikachu_attack_2, pikachu_attack_3, pikachu_attack_4]
pikachu_attacks_array = [pikachu_onda_voltio, pikachu_impactrueno, pikachu_ataque_rapido, pikachu_cola_ferrea]

#STATS SQUIRTLE LVL50 PLAYER
squirtle_number_7 = "SQUIRTLE"
squirtle_vida = 135
squirtle_speed = 39

squirtle_attack_1 = "HIDROBOMBA"
squirtle_attack_2 = "PISTOLA AGUA"
squirtle_attack_3 = "PLACAJE"
squirtle_attack_4 = "GOLPE ROCA"

squirtle_hidrobomba = 12
squirtle_pistola_agua = 8
squirtle_placaje = 25
squirtle_golpe_roca = 58

squirtle_names_attacks_array = [squirtle_attack_1, squirtle_attack_2, squirtle_attack_3, squirtle_attack_4]
squirtle_attacks_array = [squirtle_hidrobomba, squirtle_pistola_agua, squirtle_placaje, squirtle_golpe_roca]

#UN POKEMON SALVAJE HA APARECIDO
print("\n"+"-"*len(text)+"\n"+RED+"UN "+pikachu_number_25+" SALVAJE HA APARECIDO!\n"+RESET+"-"*len(text))

#TEXT ART PIKACHU
print("░░░░░░░░░▀████▀▄▄░░░░░░░░░░░░░░▄█░")
print("░░░░░░░░░░░█▀░░░░▀▀▄▄▄▄▄░░░░▄▄▀▀█░")
print("░░░▄░░░░░░░░█░░░░░░░░░░▀▀▀▀▄░░▄▀░░")
print("░░▄▀░▀▄░░░░░░▀▄░░░░░░░░░░░░░░▀▄▀░░")
print("░▄▀░░░░█░░░░░█▀░░░▄█▀▄░░░░░░▄█░░░░")
print("░▀▄░░░░░▀▄░░█░░░░░▀██▀░░░░░██▄█░░░")
print("░░▀▄░░░░▄▀░█░░░▄██▄░░░▄░░▄░░▀▀░█░░")
print("░░░█░░▄▀░░█░░░░▀██▀░░░░▀▀░▀▀░░▄▀░░")
print("░░█░░░█░░█░░░░░░▄▄░░░░░░░░░░░▄▀░░░")

#PELEAR / HUIR
pelear_huir = int(input("-"*len(text)+"\n"+MAGENTA+"1) PELEAR / 2) HUIR "+RESET))

while pelear_huir != 1 and pelear_huir !=2:
    pelear_huir = int(input("-" * len(text) + "\n" + MAGENTA + "1) PELEAR / 2) HUIR " + RESET))

if(pelear_huir == 2):

    # HUIR
    print("-" * len(text) + "\n" + RESET + "HAS HUIDO DEL COMBATE" +"\n" + RESET + "-" * len(text))
    exit()

if(pelear_huir == 1):
    # PELEAR
    print("-" * len(text) + "\n" + CYAN + "VAMOS "+squirtle_number_7 +" YO TE INVOCO, PELEA!!!\n" + RESET + "-" * len(text))

# CONTADORES VIDA
    pokemon_1_vida = pikachu_vida
    pokemon_2_vida = squirtle_vida

print()
print(pikachu_number_25 + "  HP [" + GREEN + "##########" + RESET + "] {}".format(pokemon_1_vida) + " / {}".format(pikachu_vida))
print(squirtle_number_7 + " HP [" + GREEN + "##########" + RESET + "] {}".format(pokemon_2_vida) + " / {}".format(squirtle_vida))

input("-" * len(text) + "\n"+MAGENTA+"PRESS ENTER TO START BATTLE ")
print(RESET + "-" * len(text))

# PRIMERO EN PEGAR
if(pikachu_speed > squirtle_speed):

    # INICIO COMBATE PIKACHU ATACA PRIMERO
    while pokemon_1_vida > 0 and pokemon_2_vida > 0:

        #CONTADOR TURNO
        turno_number += 1
        print("TURNO {}".format(turno_number)+"\n")

        #SELECTOR ATAQUE IA
        attack = randint(0, 3)
        pokemon_2_vida -= pikachu_attacks_array[attack]
        print(pikachu_number_25+" USA "+pikachu_names_attacks_array[attack]+" [{}]".format(pikachu_attacks_array[attack]))

        if(pikachu_attacks_array[attack]>40):
            print(RED+"EL ATAQUE ES MUY EFECTIVO!!!"+RESET)
        elif(pikachu_attacks_array[attack]<20):
            print(RED + "EL ATAQUE NO ES MUY EFECTIVO!!!" + RESET)

        #IMPRIMO GANADOR
        if(pokemon_2_vida <= 0):
            print("-" * len(text)+"\n"+RED+squirtle_number_7+" HA MUERTO EN BATALLA EL GANADOR ES: "+pikachu_number_25+"!!!"+RESET+"\n"+"-" * len(text))
            exit()

        #PORCENTAJE DE VIDA
        barra_vida_pikachu = int(pokemon_1_vida *10 / pikachu_vida)
        barra_vida_squirtle = int(pokemon_2_vida *10 / squirtle_vida)

        #BARRAS DE VIDA CON PORCENTAJE Y COLORES
        print()

        if(barra_vida_pikachu>5):
            print(pikachu_number_25 + "  HP "+GREEN+"[{}{}] {} / {}".format("#" * barra_vida_pikachu, " " * (10 - barra_vida_pikachu), pokemon_1_vida, pikachu_vida)+RESET)

        elif(barra_vida_pikachu>3):
            print(pikachu_number_25 + "  HP " + YELLOW + "[{}{}] {} / {}".format("#" * barra_vida_pikachu, " " * (10 - barra_vida_pikachu), pokemon_1_vida, pikachu_vida) + RESET)

        elif(barra_vida_pikachu>-1):
            print(pikachu_number_25 + "  HP " + RED + "[{}{}] {} / {}".format("#" * barra_vida_pikachu, " " * (10 - barra_vida_pikachu), pokemon_1_vida, pikachu_vida) + RESET)

        if (barra_vida_squirtle > 5):
            print(squirtle_number_7 + " HP " + GREEN + "[{}{}] {} / {}".format("#" * barra_vida_squirtle, " " * (10 - barra_vida_squirtle), pokemon_2_vida, squirtle_vida) + RESET)

        elif (barra_vida_squirtle > 3):
            print(squirtle_number_7 + " HP " + YELLOW + "[{}{}] {} / {}".format("#" * barra_vida_squirtle, " " * (10 - barra_vida_squirtle), pokemon_2_vida, squirtle_vida) + RESET)

        elif (barra_vida_squirtle >-1):
            print(squirtle_number_7 + " HP " + RED + "[{}{}] {} / {}".format("#" * barra_vida_squirtle, " " * (10 - barra_vida_squirtle), pokemon_2_vida, squirtle_vida) + RESET)

        #TURNO SQUIRTLE
        print("-"*len(text)+"\n"+MAGENTA + squirtle_number_7+" SE PREPARA PARA ATACAR!!!")
        attack = int(input("1) "+squirtle_names_attacks_array[0]+" / 2) "+squirtle_names_attacks_array[1]+" / 3) "+squirtle_names_attacks_array[2]+" / 4) "+squirtle_names_attacks_array[3] + " "+" / 5) HUIR "))
        print(RESET+"-"*len(text))

        if(attack==5):
            # HUIR
            print("-" * len(text) + "\n" + RESET + "HAS HUIDO DEL COMBATE" + "\n" + RESET + "-" * len(text))
            exit()

        #SELECTOR ATAQUE USUARIO
        attack -= 1
        pokemon_1_vida -= squirtle_attacks_array[attack]
        print(squirtle_number_7+" USA "+squirtle_names_attacks_array[attack]+" [{}]".format(squirtle_attacks_array[attack]))

        if (squirtle_attacks_array[attack] > 30):
            print(RED + "EL ATAQUE ES MUY EFECTIVO!!!" + RESET)
        elif (squirtle_attacks_array[attack] < 15):
            print(RED + "EL ATAQUE NO ES MUY EFECTIVO!!!" + RESET)

        #IMPRIMO GANADOR
        if(pokemon_1_vida <= 0):
            print("-" * len(text)+"\n"+RED+pikachu_number_25+" HA MUERTO EN BATALLA EL GANADOR ES: "+squirtle_number_7+"!!!"+RESET+"\n"+"-" * len(text))
            exit()

        # BARRAS DE VIDA CON PORCENTAJE Y COLORES
        print()

        if (barra_vida_pikachu > 5):
            print(pikachu_number_25 + "  HP " + GREEN + "[{}{}] {} / {}".format("#" * barra_vida_pikachu, " " * (10 - barra_vida_pikachu), pokemon_1_vida, pikachu_vida) + RESET)

        elif (barra_vida_pikachu > 3):
            print(pikachu_number_25 + "  HP " + YELLOW + "[{}{}] {} / {}".format("#" * barra_vida_pikachu, " " * (10 - barra_vida_pikachu), pokemon_1_vida, pikachu_vida) + RESET)

        elif (barra_vida_pikachu > -1):
            print(pikachu_number_25 + "  HP " + RED + "[{}{}] {} / {}".format("#" * barra_vida_pikachu, " " * (10 - barra_vida_pikachu), pokemon_1_vida, pikachu_vida) + RESET)

        if (barra_vida_squirtle > 5):
            print(squirtle_number_7 + " HP " + GREEN + "[{}{}] {} / {}".format("#" * barra_vida_squirtle, " " * (10 - barra_vida_squirtle), pokemon_2_vida, squirtle_vida) + RESET)

        elif (barra_vida_squirtle > 3):
            print(squirtle_number_7 + " HP " + YELLOW + "[{}{}] {} / {}".format("#" * barra_vida_squirtle, " " * (10 - barra_vida_squirtle), pokemon_2_vida, squirtle_vida) + RESET)

        elif (barra_vida_squirtle > -1):
            print(squirtle_number_7 + " HP " + RED + "[{}{}] {} / {}".format("#" * barra_vida_squirtle, " " * (10 - barra_vida_squirtle), pokemon_2_vida, squirtle_vida) + RESET)

    print("-" * len(text))
