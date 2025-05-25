import argparse
from pykeepass import PyKeePass

def main():
	argParser = argparse.ArgumentParser()
	argParser.add_argument("-d", "--database", type=ascii, help="Keepass database file", required=True)
	argParser.add_argument("-w", "--wordlist", type=ascii, help="Wordlist to use", required=True)
	argParser.add_argument("-l", "--log", help="log output to a file",  action="store_true")
	argParser.add_argument("-v", "--verbose", help="verbose output",  action="store_true")
	args = argParser.parse_args()

	databaseFile = args.database.replace("'", "")
	wordlistFile = args.wordlist.replace("'", "")

	print("[*] Opening wordlist")
	try:
		with open(wordlistFile, 'r', encoding='unicode_escape') as file:
			print("[*] Starting bruteforce process...")
			for line in file:
				passwordValue=line.strip()
				try:
					# load database
					kp = PyKeePass(databaseFile, password=passwordValue)
					print(f"[!] Success! Database password: {passwordValue}")
					print("[*] Stopping bruteforce process.")
					break
				except:
					continue
	except FileNotFoundError:
		print(f"[ERROR]: The file {wordlistFile} was not found.")
	except Exception as e:
		print(f"[ERROR]: An error occurred while attempting to load {wordlistFile}: {e}")
	print("[*] Done.")

if __name__ == '__main__':
	main()
