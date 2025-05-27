# brutalkeepass
## Description
- Brute force Keepass databases
- Written in Python
- [Brute Forcing KeePass Database Passwords](https://medium.com/p/cbe2433b7beb): How to brute force KeePass database passwords with Python and wordlist
## Why?
Useful when you cannot convert the database to a format that JTR or Hashcat can use.
```
$ keepass2john recovery.kdbx 
! recovery.kdbx : File version '40000' is currently not supported!
$
```
## Usage
```
$ python bfkeepass.py 
usage: bfkeepass.py [-h] -d DATABASE -w WORDLIST [-o] [-v]
bfkeepass.py: error: the following arguments are required: -d/--database, -w/--wordlist
$ 
```
Example
```
$ python bfkeepass.py -d recovery.kdbx -w /usr/share/wordlists/rockyou.txt
[*] Opening wordlist
[*] Starting bruteforce process
[!] Success! Vault password: Toyota
[*] Stopping bf process
[*] Done.
$ 
```
Example with verbose output enabled
```
$ python bfkeepass.py -d recovery.kdbx -w /usr/share/wordlists/rockyou.txt -v
[*] Running bfkeepass
[>] Running against database: recovery.kdbx
[>] Using wordlist: /usr/share/wordlists/rockyou.txt
[>] Opening wordlist...
[>] Successfully opened wordlist.
[*] Starting bruteforce process...
[>] Testing value: (123456)
[>] Testing value: (nicole)
[>] Testing value: (111111)
[>] Testing value: (friends)
[!] Success! Database password: Toyota
[*] Stopping bruteforce process.
[*] Done.
$ 
```
Example with entry output enabled
```
$ python bfkeepass.py -d recovery.kdbx -w /usr/share/wordlists/rockyou.txt -o
[*] Running bfkeepass
[*] Starting bruteforce process...
[!] Success! Database password: Toyota
[>] Dumping entries...
--------------------
[>] Title: JAMIE WILLIAMSON
[>] Username: None
[>] Password: redacted
[>] URL: example.htb
[>] Notes: None
--------------------
[>] Title: ADAM SILVER
[>] Username: None
[>] Password: redacted
[>] URL: example.htb
[>] Notes: None
--------------------
[>] Title: ANTONY C. EDWARDS
[>] Username: None
[>] Password: redacted
[>] URL: example.htb
[>] Notes: None
--------------------
[>] Title: STEVE TUCKER
[>] Username: None
[>] Password: redacted
[>] URL: example.htb
[>] Notes: None
--------------------
[>] Title: SAMUEL BLAKE
[>] Username: None
[>] Password: redacted
[>] URL: example.htb
[>] Notes: None
--------------------
[>] Entry dump complete.
[*] Stopping bruteforce process.
[*] Done.
$
```
## Dependencies
- [pykeepass](https://github.com/libkeepass/pykeepass): Python library to interact with Keepass databases
