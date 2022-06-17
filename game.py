#modules

import os
import sys
import time
import curses

#tic tac toe

#colors

black='\033[30m'
red='\033[31m'
green='\033[32m'
orange='\033[33m'
blue='\033[34m'
purple='\033[35m'
cyan='\033[36m'
lightgrey='\033[37m'
darkgrey='\033[90m'
lightred='\033[91m'
lightgreen='\033[92m'
yellow='\033[93m'
lightblue='\033[94m'
pink='\033[95m'
lightcyan='\033[96m'


max_spaces = 10
space = [' ' for i in range(max_spaces)]

last_player = ["\x1b[34mx"]
win_player = ["\x1b[95mo"]
run = True
count = 0
player_x = "\x1b[34mx"
player_o = "\x1b[95mo"

max = 9

available = " "

accept ,deny = "yes" ,"no"

#errors

invalid_num = "error please enter number between(0_10)"

occupied = red + "position already chosen please re-chose"

non_int = "please enter an integer"

#type writer


def write(error):
	for let in error:
		sys.stdout.write(let)
		sys.stdout.flush()
		time.sleep(0.09)

# win conditions

def board(space):
	print(yellow + " " + space[1] + yellow + " | " + space[2] + yellow + " | " + space[3])
	print(yellow + "-----------")
	print(yellow + " " + space[4] + yellow +  " | " + space[5] + yellow + " | " + space[6])
	print(yellow + "-----------")
	print(yellow + " " + space[7] + yellow + " | " + space[8] + yellow + " | " + space[9])
	spaces()
	print("[$]type 99 to exit")

def insert(space, player_o, place, player_x):

	if last_player[0] == "\x1b[34mx":
		space[place] = player_x
		last_player.remove(player_x)
		last_player.append(player_o)
		win_player.remove(player_o)
		win_player.append(player_x)

	else:
		space[place] = player_o
		last_player.remove(player_o)
		last_player.append(player_x)
		win_player.remove(player_x)
		win_player.append(player_o)
def spaces():
	print("")

def clear():
	os.system("clear")

def check_win():
	return (space[1] == win_player[0] and space[2] == win_player[0] and space[3] == win_player[0]) or (space[4] == last_player[0] and space[5] == last_player[0] and space[6] == last_player[0]) or (space[7] == last_player[0] and space[8] == last_player[0] and space[9] == last_player[0]) or (space[1] == last_player[0] and space[4] == last_player[0] and space[7] == last_player[0]) or (space[2] == last_player[0] and space[5] == last_player[0] and space[8] == last_player[0]) or (space[3] == last_player[0] and space[6] == last_player[0] and space[9] == last_player[0]) or (space[1] == last_player[0] and space[5] == last_player[0] and space[9] == last_player[0]) or (space[3] == last_player[0] and space[5] == last_player[0] and space[7] == last_player[0])


def restart():
	say = input("Do you want to restart?(Yes/No): ")
	if say == accept.lower():
		re_start()
	else:
		re_start()

def check_open(space,place,available):
	return(space[place] == available)


def re_start():
	for i in space:
		if i == player_x or player_o:
			space.remove(i)
			space.append(available)




def main(count):

	while run:

		if check_win():
			clear()
			board(space)
			print(f"{win_player[0]} wins")
			spaces()
			restart()


		if count != max:
			clear()
			pass
		else:
			pass
		board(space)

		try:
			place = int(input(f"{green}chose position(1-9): " + pink))
			if place == "99":
				break


		except:
			write(non_int)


		if place > 0 and place < 10:
			if  check_open(space,place,available):

				if place > 0 and place < 10:
					insert(space, player_o ,place,player_x)


			else:
				write(occupied)
				time.sleep(0.5)
				continue

		elif place == 99:
			clear()
			import main


		count += 1
		if count == max:
			os.system("clear")
			board(space)
			print("")
			print("its a draw")
			break

main(count)
