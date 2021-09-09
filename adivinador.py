# Primer commit, clasico programa de adivina el numero  Ramdom entre 1-30
import random
 
secret = random.randint(1, 30)
guess = 0
tries = 0
 
print ("Adivina el Numero Secreo")
print ("El número es del 1 al 30, ¡solo tienes 6 posibilidades!")
 
print ("¿Cuál es el número que adivinaste?")
guess = input()

if int(guess) == secret:
	print ("¡Eres increíble! ¡Felicitaciones, lo has adivinado!")
else:
	print ("Has adivinado mal ¡juguemos de nuevo la próxima vez!")
	print ("Mi número secreto es:", secret)
