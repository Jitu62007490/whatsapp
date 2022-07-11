import os
import colorama
import time
import sys
from colorama import  Fore,Style
R = Fore.RED
B = Fore.BLUE
G = Fore.GREEN
C = Fore.CYAN
Y = Fore.YELLOW
M = Fore.MAGENTA
W = Fore.WHITE
try:
	import colorama
except ModuleNotFoundError:
	print("Requests is not Installed")
	os.system("pip install colorama")
logo = f"""
{G}   ______                            __        ____      ____ 
 .' ___  |                          [  |      |_  _|    |_  _|
/ .'   \_|  _ .--.   ,--.    .--.    | |--.     \ \  /\  / /  
| |        [ `/'`\] `'_\ :  ( (`\]   | .-. |     \ \/  \/ /   
\ `.___.'\  | |     // | |,  `'.'.   | | | |      \  /\  /    
 `.____ .' [___]    \'-;__/ [\__) ) [___]|__]       \/  \/     
{R}█░█ ▄▀█  █▀▀ █▀█ ▄▀█ █▀ █░█ █▀▀ █▀█ {B}Coded By Team AxL
{M}█▀█ █▀█  █▄▄ █▀▄ █▀█ ▄█ █▀█ ██▄ █▀▄ {B}Crash Txt by @Killer 
"""
os.system('clear')
def main():
	os.system('clear')
	print(logo)
	print(G)
	number=input(f"{G}[+] Enter the Victim's Phone number with country Code\n\n{G}=> ")
	print()
	crash=int(input(f'[+] Enter the number of crashes {W}(Max 25 per 240 Min) \n\n=> '))
	link = (f"""xdg-open https://wa.me/{number}/?text=hii i am raj ,test,test""")

	for i in range (crash):
		print(f"{Y}[✓] Sending Now")
		link1 = os.system(link)
		time.sleep(5)
		if link1 == 0:
			print(f"{G} Successful")
			pass
		else:
			print(f"{G}[×] Failed  ")
		time.sleep(0.2)
	return main()
main()
    