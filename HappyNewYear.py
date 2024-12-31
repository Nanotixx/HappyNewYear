import os
import time
import pyfiglet
from colorama import Fore

# Happy New Year!
while True:
	text = pyfiglet.figlet_format("Happy New Year")
	for color in range(3):
		# RED
		print(Fore.RED + text)
		time.sleep(1)
		os.system("clear")
		
		# YELLOW
		print(Fore.YELLOW + text)
		time.sleep(1)
		os.system("clear")
		
		# BLUE
		print(Fore.BLUE + text)
		time.sleep(1)
		os.system("clear")
		