# Checksum Checker

A simple Python desktop app that calculates and verifies file checksums (**MD5**, **SHA256**, **SHA512**).  
Built with Tkinter. Great for verifying file integrity or checking downloaded files.

---

## How to Run (with Python)

No setup required — the app only uses built-in Python libraries.

### Steps:

1. Make sure you have **Python 3.7 or newer** installed.
2. Download the file `sum_checker.py`.
3. Run it using:
   ```bash
   python sum_checker.py

## How to build a .exe (Windows)

If you want to build a standalone Windows .exe file from the Python script:

 ### Steps:

1. Make sure Python is installed
   You need Pytho 3.7 or newer.
2. Create a virtual environment (optional)
   python -m venv env_name
3. Activate the env
  source env_name\Scripts\Activate
4. Install requirements
   pip install -r requirements.txt
5. Build the executable
   pyinstaller --onefile --windowed sum_checker.py
6. Find the output
   The executable can be found under the /dist section

NOTE: If you have an antivirus, it is possible that it detects the .exe as a threat.
      This is totally normal. Just make an exception to that file.


## Download the Ready-to-Use .exe

If you don't want to install Python or build anything:
    - Go to the Releases tab to download the zipped file.

NOTE: If you have an antivirus, it is possible that it detects the .exe as a threat.
      This is totally normal. Just make an exception to that file.

## Questions or Feedback?

Feel free to open an issue or submit suggestions at: https://github.com/AlexPsr/checksum-checker
