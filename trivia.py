#Se importa modulo random y time
import random as rd
import time

puntaje = rd.randint(0,6)

#Colores
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

#Ingreso a la trivia 
print(f"""{MAGENTA}\tBienvenido a nuestra trivia sobre Python{RESET}
\nHoy pondremos a prueba tus conocimientos sobre este lenguaje de programación.""")
time.sleep(3)
name= input('\n> Para empezar, por favor ingresa tu nombre: ')
print(f'Genial {name}! Are you ready? \n\nEmpiezas con...\nCalculando al azar... \n')
time.sleep(5)
print(f'{GREEN}{puntaje} puntos.{RESET}\n')

#Listado de preguntas
question_1 = f'{BLUE}> Pregunta 1. ¿Cuál es el origen del nombre \'Python\' ?{RESET}\n'
question_2 = f'{BLUE}> Pregunta 2. ¿Quien es el creador de este lenguaje de programación?{RESET}\n'
question_3 = f'{BLUE}> Pregunta 3. Python es considerado un lenguaje de ¿bajo o alto nivel? ¿Por qué?{RESET}\n'
question_4 = f'{BLUE}> Pregunta 4. ¿Es un lenguaje compilado o un lenguaje interpretado?{RESET}\n'
question_5 = f'{BLUE}> Pregunta 5. ¿Cual de estos frameworks pertenecen a Python?'

# Tipo de respuesta
right_answer = f'Respuesta correcta {name} ganaste 5 puntos. Tu nuevo puntaje es '
wrong_answer = f'Respuesta incorrecta {name}. Pierdes 2 puntos, tu nuevo puntaje es '


# 

#Pregunta 1
print(question_1)
print("""a) Esto es debido a que el creador del lenguaje es amante de las serpientes.
b) Es el nombre de la ciudad donde nació el creador de este lenguaje.
c) Según su creador, el nombre se deriva de la serie de comedia británica Monty Python, de la cual es gran fan. 
\n Responde escribiendo a, b, c según la opción que elijas. """)
answer_1=input('> ')
while answer_1 not in ('a','b','c'):
    answer_1 = input('Debes escribir a, b o c según corresponda: ')

if answer_1 == 'c':
    puntaje+=5
    print(f'{GREEN}{right_answer}{puntaje}{RESET}\n')
else:
    puntaje-=2
    print(f'{RED}{wrong_answer}{puntaje}\n') 

#Pregunta 2
print(question_2)
print("""a) El creador es Bill Gates.
b) El nombre de su creador es Guido Van Rossum.
c) Fue creado por un equipo de ingenieros de Google. 
d) Su creador fue Brendan Eich.
\n Responde escribiendo a, b, c, d según la opción que elijas. """)
answer_2=input('> ')
while answer_2 not in ('a','b','c','d'):
    answer_2 = input('Debes escribir a, b, c o d según corresponda: ')

if answer_2 == 'b':
    puntaje+=5
    print(f'{GREEN}{right_answer}{puntaje}{RESET}\n')
else:
    puntaje-=2
    print(f'{RED}{wrong_answer}{puntaje}\n') 

#Pregunta 3
print(question_3)
print("""a) Se considera como lenguaje de bajo nivel porque está cerca al código máquina.
b) Se considera de alto nivel porque se acerca al lenguaje humano.
c) Se considera como lenguaje de bajo nivel porque se acerca al lenguaje humano. 
d) Se considera de alto nivel porque se acerca al lenguaje máquina.
\n Responde escribiendo a, b, c, d según la opción que elijas. """)
answer_3=input('> ')
while answer_3 not in ('a','b','c','d'):
    answer_3 = input('Debes escribir a, b, c o d según corresponda: ')

if answer_3 == 'b':
    puntaje+=5
    print(f'{GREEN}{right_answer}{puntaje}{RESET}\n')
else:
    puntaje-=2
    print(f'{RED}{wrong_answer}{puntaje}\n') 

#Pregunta 4 
print(question_4)
print("""a) Python usa un compilador, por lo que decimos que es un lenguaje compilado.
b) A diferencia de otros lenguajes de programación Python no necesita de compilador ni de interprete. Se ejecuta facilmente en los ordenadores.
c) Python es un lenguaje interpretado 
\n Responde escribiendo a, b, c según la opción que elijas. """)
answer_4=input('> ')
while answer_4 not in ('a','b','c'):
    answer_4 = input('Debes escribir a, b o c según corresponda: ')

if answer_4 == 'c':
    puntaje+=5
    print(f'{GREEN}{right_answer}{puntaje}{RESET}\n')
else:
    puntaje-=2
    print(f'{RED}{wrong_answer}{puntaje}\n') 


# Pregunta 5 
print(question_5)
print("""a) Laravel
b) Django
c) Angular 
\n Responde escribiendo a, b, c según la opción que elijas. """)
answer_5=input('> ')
while answer_5 not in ('a','b','c'):
    answer_5 = input('Debes escribir a, b o c según corresponda: ')

if answer_5 == 'b':
    puntaje+=5
    print(f'{GREEN}{right_answer}{puntaje}{RESET}\n')
else:
    puntaje-=2
    print(f'{RED}{wrong_answer}{puntaje}\n') 
    
#Fin del juego
if puntaje>0:
        print(f'\n{GREEN}Felicidades {name}, has llegado al fin de la trivia, tu puntaje final es {puntaje}.{RESET}')
else:
    print(f'{RED}Lo sentimos! Perdiste la trivia {name}, tu puntaje final es de {puntaje}. Sigue estudiando y vuelve a intentarlo :) {RESET}')
