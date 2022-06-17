
import Banner
from Banner import logo
from Banner import info
import sys
import os
import time



def men():

	def writer(error):
		for let in error:
			sys.stdout.write(let)
			sys.stdout.flush()
			time.sleep(0.5)



	int_error = "please input number"


	options = """
\033[32m
[1].PLAY
[2].GAME STATS
[3].UPDATE
[4].CREDITS

"""

	logo()
	info()

	print(options)


	try:
		choice = input("\033[95m[+]input number(1-4): ")
	except:
		writer(int_error)


	if choice == "1":
		import game
	elif choice == "2":
		pass
	elif choice == "3":
		os.system("clear")
		print("""
This game is up to date:

next updates to be released on :

30 July 2022

stay safe

Enjoy !🔥

""")

	elif choice == "4":
		import credits
		from credits import main_creds
	else:
		pass

men()
