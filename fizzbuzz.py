from time import sleep
from os import system
import winsound

winsound.Beep(17000, 100)
exit()

i = 1
while i < 20:
	print(i)
	if i % 15 == 0: system("say fizzbuzz")
	elif i % 3 == 0: system("say fizz")
	elif i % 5 == 0: system("say buzz")
	else: system("tput bel")
	sleep(10)
	i = i + 1