
# File Integrity Monitoring Script

## What is it?
A Python script that monitors important files for unauthorized changes by storing and comparing their cryptographic hashes.

## Why use it?
Detecting unauthorized file changes is crucial for identifying tampering, malware infections, or accidental modifications to sensitive files.

## Features
- Monitors specified files for changes
- Stores file hashes in a local database (`hashdb.json`)
- Alerts when changes are detected

## Installation
No external dependencies required. Works with Python 3 standard library.

## Usage
1. Edit `monitor.py` and update `files_to_monitor` with your file paths.
2. Run the script:
    ```bash
    python monitor.py
    ```
3. The script checks file integrity and updates the database.

## License

MIT License
