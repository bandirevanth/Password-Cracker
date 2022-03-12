import random
import pyautogui
import string

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!$%&'()*+,-./:;<=>?@[\]^_`{|}~"
chars_list = list(chars)

print("Password Cracker by Bandi Revanth")
print()
print("EDUCATIONAL PURPOSES ONLY!!!")

print()

password = pyautogui.password("Enter Password: ")
guess_password = ""

while(guess_password != password):
	guess_password = random.choices(chars_list, k=len(password))
	print("<============"+ str(guess_password) +"============>")

	if(guess_password == list(password)):
		print("Cracked Password: " + "".join(guess_password))
		input()
		break
