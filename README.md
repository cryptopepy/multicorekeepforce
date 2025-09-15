# multicorekeepforce
## Description
- Fork of toneillcodes brutalkeepass
- Brute force Keepass databases
- Adds support for keyfiles, multicore processing, and a progress bar
- Written in Python
- [Brute Forcing KeePass Database Passwords](https://medium.com/p/cbe2433b7beb): How to brute force KeePass database passwords with Python and wordlist

## Dependencies
- [pykeepass](https://github.com/libkeepass/pykeepass): Python library to interact with Keepass databases
- [tqdm](https://github.com/tqdm/tqdm): Python library for status bar

Install dependencies using the `requirements.txt` file:
```
pip install -r requirements.txt
```

## Why?
Useful when you cannot convert the database to a format that JTR or Hashcat can use.
```
$ keepass2john recovery.kdbx 
! recovery.kdbx : File version '40000' is currently not supported!
$
```

## Usage
```
$ python bfkeepforce.py 
usage: bfkeepforce.py [-h] -d DATABASE -w WORDLIST [-k KEYFILE] [-c CORES] [-o]

options:
  -h, --help            show this help message and exit
  -d DATABASE, --database DATABASE
                        KeePass database file (.kdbx)
  -w WORDLIST, --wordlist WORDLIST
                        Wordlist to use
  -k KEYFILE, --keyfile KEYFILE
                        Key file to use with the database
  -c CORES, --cores CORES
                        Number of CPU cores to use (default: all available)
  -o, --output          Output entries on success
```

##Example Usage
```
python bfkeepforce.py -d db.kdbx -w /usr/share/wordlists/rockyou.txt
 
[*] bfkeepass multi-core script initialized.
[>] Target Database: db.kdbx
[>] Wordlist File: /usr/share/wordlists/rockyou.txt
[>] Reading wordlist into memory...
[>] 14344392 passwords loaded.
[*] Using all 16 available CPU cores by default.
[*] Starting the cracking process...
Testing Passwords:   2%|▏         | 254823/14344392 [00:05<04:51, 48391.45pw/s]
```

###Example with a keyfile in addition to a password
Use --keyfile or -k to specify a keyfile. 

```
python bfkeepforce.py -d db.kdbx -w passwords.txt -k my_database.key
```

###Specify core count 
Use --cores or the -c flag to specify how many CPU cores to use.

```
python bfkeepforce.py -d db.kdbx -w passwords.txt -c 8
```

###Outputting Entries on Success
Use the -o flag to dump all database entries after finding the correct password.

```
python bfkeepforce.py -d db.kdbx -w passwords.txt -o
```


##Good luck!

Thank you to toneillcodes for the ideas & original code!
Leave any feedback in Issues
