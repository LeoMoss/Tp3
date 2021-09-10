# Primer commit, clasico programa de adivina el numero  Ramdom entre 1-30
import random
 
secret = random.randint(1, 30)
guess = 0
tries = 0
 
print ("Adivina el Numero Secreo")
print ("El número es del 1 al 30, ¡solo tienes 6 posibilidades!")
 
while int(guess) != secret and tries < 6:
	print ("¿Cuál es el número que adivinaste?")
	guess = input()
	if int(guess) < secret:
		print ("¡El número es demasiado pequeño! ¡Adivina de nuevo!")
	elif int(guess) > secret:
		print ("¡El número es demasiado grande! ¡Adivina de nuevo!")
		tries = tries + 1
if int(guess) == secret:
	print ("¡Eres increíble! ¡Felicitaciones, lo has adivinado!")
else:
	print ("Has adivinado mal 6 veces, ¡juguemos de nuevo la próxima vez!")
	print ("Mi número secreto es:", secret)