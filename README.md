# MeterLink CLI

    .::            .::                                                 :==.         -++-                =+=             
    ::::.         :::-.                :-:                             -++:                             -==.            
    :::::.       :::::.    .:::::.   .:::::::.    .:::::.     ::. .::. -=+:         .--: .--:.-===--.   ===.    :--:    
    :::.:-.     :-..::.  :-:.. ..::. ..:::....  :::.. ..:::   -::::..  -++:         :++- .+++=-::-=++-  -==   :=+=.     
    :::  :-:   :-. .::. :::.     .:-:  .::     :::.     .:::  :::.     -=+:         :+=- .===      ==+. ===.:=+=.       
    :::   :-:.::.  .::  -:::::::::::.  .::.    :::::::::::::  :::      -=+:         :++- .+=-      -++. ===++=+=:       
    :::    .--:.   .::. :::.           .::.    .-:.           :::      -=+:         :==- .+=-      -==. -==-. :++-.     
    :-:     ..     .--.  .:-::..::-.    :-:..:  .:-::..::-.   :-:      -++=------=- .++- .++=      =++. =++    .=++-    
    ...             ..      ..::..       ..::.     ..::..     ...      .::::::----:  ::.  :::      :::  :::      ::-:   

<img src="assets/MeterLinkFull.jpg" width="220" alt="MeterLink" />

A simple Python CLI app to track prepaid electricity token purchases per meter.

- Register + Login (password hashing, no salting)
- Add meters (with alias like Home / Shop)
- Import purchases from Excel (.xlsx) by pasting SMS messages
- View purchases, totals, and last 5 purchases (per selected meter)
- JSON files store data locally (no SQL database)

---

## Requirements
- Python 3.x
- openpyxl (for reading Excel)

---

## How to Run (Local / From Source)

1) Open the project folder  
cd meterlink-cli

2) Create a virtual environment  
python -m venv .venv

3) Activate the virtual environment  
Windows (PowerShell / CMD):  
.venv\Scripts\activate  

Mac / Linux:  
source .venv/bin/activate  

4) Install dependencies  
pip install -r requirements.txt

5) Run the app  
python main.py

6) Open the Excel template (choose your OS)

Windows:  
start "" "templates\meterlink_template.xlsx"

Mac:  
open "templates/meterlink_template.xlsx"

Linux (desktop):  
xdg-open "templates/meterlink_template.xlsx"

WSL (Linux terminal on Windows):  
explorer.exe "templates\meterlink_template.xlsx"

7) Exit the virtual environment  
deactivate

---

## Excel Import Template
Template file is included in the repo:
- templates/meterlink_template.xlsx

Excel columns (Row 1 headers):
- Column A: M-Pesa Message (paste full SMS)
- Column B: KPLC Message (paste full SMS)

Rows:
- Row 1 = headers
- Row 2 = template instructions (leave as-is)
- Row 3+ = real purchases (each row is ONE purchase for the selected meter)

Important:
- Import is done for ONE selected meter at a time.
- If a row contains a different meter number, the app will skip it.

---

## Examples Folder (Copy/Paste)
Use these when testing:
- examples/mpesa_examples.txt
- examples/kplc_examples.txt
- examples/paired_row_examples.txt

---

## Data Storage (JSON)
The app stores data locally in:
- data/users.json
- data/meters.json
- data/purchases.json

These files should NOT be committed to GitHub (they contain local test data).

---

## Main Menu

Before Login:
1) Register
2) Login
3) Exit

After Login:
1) Add Meter
2) List Meters
3) Choose Meter
4) Import Excel (Selected Meter)
5) View Purchases (Selected Meter)
6) Totals (Selected Meter)
7) Last 5 Purchases (Selected Meter)
8) Logout

---

## Run as Executable (No Python Needed)

1) Open the GitHub repo and go to Releases  
2) Download the latest release zip for your OS  
3) Extract the zip  
4) Run the file inside the folder

Windows:
- Double-click meterlink.exe
- OR in terminal: .\meterlink.exe

Linux / Mac:
- chmod +x meterlink
- ./meterlink

Note:
- A Windows .exe must be built on Windows.
- A Linux executable must be built on Linux (WSL builds Linux binaries).

---

## Build Executable (For Developers)

1) Install PyInstaller  
pip install pyinstaller

2) Build  
pyinstaller --onefile main.py --name meterlink

3) Output  
Your executable will be inside the dist/ folder.

---

## Quit Keys
- Ctrl+C exits cleanly (no traceback).
- Ctrl+Z does NOT exit (it suspends the app in the terminal).
