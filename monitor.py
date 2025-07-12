import hashlib
import os
import json

DB_FILE = 'hashdb.json'

def hash_file(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        while True:
            chunk = f.read(8192)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()

def load_db():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, 'r') as f:
            return json.load(f)
    else:
        return {}

def save_db(db):
    with open(DB_FILE, 'w') as f:
        json.dump(db, f, indent=2)

def scan(paths):
    db = load_db()
    for path in paths:
        if not os.path.isfile(path):
            print(f"Warning: {path} does not exist or is not a file.")
            continue
        h = hash_file(path)
        if path in db:
            if db[path] != h:
                print(f"ALERT: {path} has been modified!")
            else:
                print(f"{path} unchanged.")
        else:
            print(f"{path} added to monitoring database.")
        db[path] = h
    save_db(db)

if __name__ == "__main__":
    # List your important files here
    files_to_monitor = ['important.txt', 'config.cfg']
    scan(files_to_monitor)
