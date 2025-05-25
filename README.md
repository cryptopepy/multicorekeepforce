# brutalkeepass
## Description
Brute force Keepass databases  
Written in Python  
## Why?
Useful when you cannot convert the database to a format that JTR or Hashcat can use:
```
$ keepass2john recovery.kdbx 
! recovery.kdbx : File version '40000' is currently not supported!
$
```
## Usage
```
$ python bfkeepass.py 
usage: bfkeepass.py [-h] -d DATABASE -w WORDLIST [-l] [-v]
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
## Dependencies
- [pykeepass](https://github.com/libkeepass/pykeepass): Python library to interact with Keepass databases
