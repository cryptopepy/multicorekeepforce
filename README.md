# brutalkeepass
Brute force tool for Keepass written in Python
```
$ keepass2john recovery.kdbx 
! recovery.kdbx : File version '40000' is currently not supported!
$
```
Example
```
$ python bfkeepass.py 
[*] Opening wordlist
[*] Starting bruteforce process
[!] Success! Vault password: Toyota
[*] Stopping bf process
[*] Done.
$ 
```
## Dependencies
- [pykeepass](https://github.com/libkeepass/pykeepass): Python library to interact with Keepass databases
